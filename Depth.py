
# -----------------------
  import time
  import RPi.GPIO as GPIO
  import httplib, urllib
  from firebase import firebase
# -----------------------

def measure():
  # This function measures a distance
  GPIO.output(TRIGGER_PIN, True)
  time.sleep(0.00001)
  GPIO.output(TRIGGER_PIN, False)
  start = time.time()

  while GPIO.input(ECHO_PIN)==0:
    start = time.time()

  while GPIO.input(ECHO_PIN)==1:
    stop = time.time()

  elapsed = stop-start

  distance = (elapsed * 34300)/2

  return distance
  
#This function measure a average.to improve the accuracy

def measure_average(): 
  count=0
  distance=0;
  while (count<3):
	distance1=measure()
	time.sleep(.01)
	distance=distance+distance1
	count=count+1
 
  distance=distance/3
  return distance

# -----------------------
# Main Script
# -----------------------

# Use BCM GPIO references
# instead of physical pin numbers
GPIO.setmode(GPIO.BCM)

#defining the GPIO pin for the trigger and echo
TRIGGER_PIN = 23
ECHO_PIN    = 24

print "Ultrasonic Measurement"

GPIO.setup(TRIGGER_PIN,GPIO.OUT)  # Trigger
GPIO.setup(ECHO_PIN,GPIO.IN)      # Echo
GPIO.output(TRIGGER_PIN, False)


#Firebase Configuration
fire = firebase.FirebaseApplication('https://zbin-6eb81.firebaseio.com/')

try:

  while True:

    distance = measure_average()
    print "Distance : %.1f" % distance
    stringDistance = str(distance)
    try:
           result = fire.put('level','currentLevel',stringDistance)
    except:
           print "connection failed"

    time.sleep(1)

except KeyboardInterrupt:
  GPIO.cleanup()
