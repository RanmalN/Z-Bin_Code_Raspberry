# -----------------------
import time
import RPi.GPIO as GPIO
#------------------------
 
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
        GPIO.setup(GPIO_PIR, GPIO.IN)      # Read output from PIR motion sensor

        pir_Input=GPIO.input(11)

        print pir_Input              #When output from motion sensor is HIGH


except KeyboardInterrupt:
  GPIO.cleanup()