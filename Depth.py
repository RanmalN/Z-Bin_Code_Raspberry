
# -----------------------
  import time
  import RPi.GPIO as GPIO
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

  return distance
  #This function measure a average.to improve the accuracy

def measure_average(): 
 try:
  count=0
  distance=0;
  while (count<3):
	distance1=measure()
	time.sleep(.0005)
	distance=distance+distance1
	count=count+1
   except:
	print "Exception"
 
  distance=distance/3
  return distance


# -----------------------
# Main Script
# -----------------------

# Use BCM GPIO references
# instead of physical pin numbers
# instead of physical pin numbers
# instead of physical pin numbers

GPIO.setmode(GPIO.BCM)

#defining the GPIO pin for the trigger and echo
TRIGGER_PIN = 33
ECHO_PIN    = 35
  try:
	GPIO.setup(TRIGGER_PIN,GPIO.OUT)  # Trigger
	GPIO.setup(ECHO_PIN,GPIO.IN)      # Echo
	GPIO.output(TRIGGER_PIN, False)
   except:
	print "Exception"
try:

  while True:

    distance = measure_average()
   
    time.sleep(1)

except KeyboardInterrupt:
  GPIO.cleanup()
