 print "Ultrasonic Measurement"
 
 try:
   count=0
   lid_status=True

         pir_Input=GPIO.input(11)

        if pir_Input==1 and pirStat:
            print "Life Detected ",count              #When output from motion sensor is HIGH
        else:
            print "No Any Life Detected",count
 
        time.sleep(2)
        count=count+1
 
 except KeyboardInterrupt:
   GPIO.cleanup()