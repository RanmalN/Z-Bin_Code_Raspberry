
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
    distance=distance1+distance2+distance3
    distance=distance/3
    return distance
  
def lid_open():
# This function open the lid
  print "Lid is Opening"
  count =0
    while count<50:
			GPIO.output(7,1)
			time.sleep(0.0005)
			GPIO.output(7,0)
			time.sleep(0.0020)
			count = count + 1


def lid_close():
# This function close the lid
  print "Lid is Opening"
  counter =0
      while counter<50:
                        GPIO.output(7,1)
                        time.sleep(.0015)
                        GPIO.output(7,0)
                        time.sleep(.0020)
                        counter=counter+1
			GPIO.cleanup()

# Define the distance for sensing
maxDistance   = 20

# Define whether the pir sensor is needed.
pirStat = True


GPIO_TRIGGER = 16
GPIO_ECHO    = 18
GPIO_MOTOR   = 7
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
        GPIO.setup(GPIO_MOTOR,GPIO.OUT)    # Motor
        GPIO.setup(GPIO_PIR, GPIO.IN)      # Read output from PIR motion sensor

        # Set trigger to False (Low)
        GPIO.output(GPIO_TRIGGER, False)
        pir_Input=GPIO.input(11)
        
        if pir_Input==1 and pirStat: 
            print "Life Detected ",count              #When output from motion sensor is HIGH
            distance = measure()
            print distance
            if distance<maxDistance and distance>0:
                if lid_status:
                    lid_open()
                    print "opening @",count
                    time.sleep(2)
                    lid_status=False
                else:
                     print "LID is Already Open ",count
            else:
                if lid_status==False:
                    lid_close()
                    print "closing @",count
                    lid_status=True
                else:
                     print "Swipe to Open the lid",count
        else:
            print "No Any Life Detected",count
        
        time.sleep(2)
        count=count+1
except KeyboardInterrupt:
  GPIO.cleanup()
