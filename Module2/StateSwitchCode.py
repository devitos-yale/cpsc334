import RPi.GPIO as GPIO # Import Raspberry Pi GPIO library

GPIO.setwarnings(False) # Ignore warning for now
GPIO.setmode(GPIO.BOARD) # Use physical pin numbering
#GPIO.setup(10, GPIO.IN, pull_up_down=GPIO.PUD_DOWN) # Set pin 10 to be an input pin and set initial value to be pulled low (off)
GPIO.setup(18, GPIO.IN) #button
GPIO.setup(22, GPIO.IN) #switch
GPIO.setup(15, GPIO.IN) #joystick x
GPIO.setup(13, GPIO.IN) #joystick y
GPIO.setup(11, GPIO.IN) #joystick switch

try:
	while True: # Run forever
		#button_input = GPIO.input(18)
    	if GPIO.input(18) == GPIO.HIGH:
       		print("Button was pushed")

    	#switch_input = GPIO.input(22)
    	if GPIO.input(22) == GPIO.HIGH:
        	print("Switch is high")

        #joystick_input_x = GPIO.input(15)
        #joystick_input_y = GPIO.input(13)
        #joystick_input_sw = GPIO.input(11)

        if GPIO.input(15) != GPIO.LOW:
        	print("Joystick x")
        if GPIO.input(13) != GPIO.LOW:
        	print("Joystick y")
        if GPIO.input(11) != GPIO.HIGH:
        	print("Joystick switch")

finally:
	GPIO.cleanup()