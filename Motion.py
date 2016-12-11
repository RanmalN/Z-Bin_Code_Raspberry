
# -----------------------
import time
import RPi.GPIO as GPIO
#------------------------

def measure():
  # This function measures a distance
  GPIO.output(GPIO_TRIGGER, True)
  time.sleep(0.00001)
  GPIO.output(GPIO_TRIGGER, False)
  start = time.time()
  stop = 0
  while GPIO.input(GPIO_ECHO)==0:
    start = time.time()

  while GPIO.input(GPIO_ECHO)==1:
    stop = time.time()

  elapsed = stop-start
  distance = (elapsed * 34300)/2

  return distance

def measure_average():
  # This function measures a average distance
    distance1=measure()
    time.sleep(.25)
    distance2=measure()
    time.sleep(.25)
    distance3=measure()
    time.sleep(.35)
    distance4=measure()
    time.sleep(.25)
    distance5=measure()
    time.sleep(.25)
    distance6=measure()
    time.sleep(.35)
    distance=distance1+distance2+distance3+distance4+distance5+distance6
    print distance
    distance=distance/6
    return distance


GPIO_TRIGGER = 16
GPIO_ECHO    = 18
GPIO_PIR     = 11

print "Ultrasonic Measurement"




try:
  count=0
  lid_status=True
  while True:
        GPIO.cleanup()
        # Define GPIO to use on Pi
        GPIO.setmode(GPIO.BOARD)
      	# Set pins as output and input
        GPIO.setup(GPIO_TRIGGER,GPIO.OUT)  # Trigger
        GPIO.setup(GPIO_ECHO,GPIO.IN)      # Echo
        GPIO.setup(GPIO_PIR, GPIO.IN)      # Read output from PIR motion sensor

        # Set trigger to False (Low)
        GPIO.output(GPIO_TRIGGER, False)
        pir_Input=GPIO.input(11)

        if pir_Input==1 and pirStat:
            print "Life Detected ",count              #When output from motion sensor is HIGH
            distance = measure_average()
        else:

        time.sleep(2)
        count=count+1
except KeyboardInterrupt:
  GPIO.cleanup()