
# -----------------------
  import time
  import RPi.GPIO as GPIO
# -----------------------

def measure():
  # This function measures a distance
  GPIO.output(TRIGGER_PIN, True)
  time.sleep(0.0001)
  GPIO.output(TRIGGER_PIN, False)
  start = time.time()

  while GPIO.input(ECHO_PIN)==0:
    start = time.time()

  while GPIO.input(ECHO_PIN)==1:
    stop = time.time()

  elapsed = stop-start

  distance = (elapsed * 34300)/2

  return distance
  

# -----------------------
# Main Script
# -----------------------

# Use BCM GPIO references
# instead of physical pin numbers
GPIO.setmode(GPIO.BCM)

#defining the GPIO pin for the trigger and echo
TRIGGER_PIN = 33
ECHO_PIN    = 35

print "Ultrasonic Measurement"

GPIO.setup(TRIGGER_PIN,GPIO.OUT)  # Trigger
GPIO.setup(ECHO_PIN,GPIO.IN)      # Echo
GPIO.output(TRIGGER_PIN, False)

try:

  while True:

    distance = measure_average()
   
    time.sleep(1)

except KeyboardInterrupt:
  GPIO.cleanup()
