#------------------------
  import RPi.GPIO as GPIO
#------------------------
  
 def measure():
   # This function measures a distance
   GPIO.output(GPIO_TRIGGER, True)
   time.sleep(0.0001)
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
 
 GPIO_TRIGGER = 16
 GPIO_ECHO    = 18
 GPIO_PIR     = 11
 
 Try :  
    print "Ultrasonic Measurement"
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
       distance = measure()
    else:
       print "No Any Life Detected",count
  
    time.sleep(2)
    count=count+1

  except KeyboardInterrupt:
    GPIO.cleanup()