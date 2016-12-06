 print "Ultrasonic Measurement"
 
 try:
   lid_status=True

         pir_Input=GPIO.input(11)
 
        if pir_Input==1 and pirStat:
            print "Life Detected "            
        else:
            print "No Any Life Detected"
 
        time.sleep(2)
 
 except KeyboardInterrupt:
   GPIO.cleanup()