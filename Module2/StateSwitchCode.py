import RPi.GPIO as GPIO # Import Raspberry Pi GPIO library

GPIO.setwarnings(False) # Ignore warning for now
GPIO.setmode(GPIO.BOARD) # Use physical pin numbering
#GPIO.setup(10, GPIO.IN, pull_up_down=GPIO.PUD_DOWN) # Set pin 10 to be an input pin and set initial value to be pulled low (off)
GPIO.setup(10, GPIO.IN)
GPIO.setup(2, GPIO.IN)
GPIO.setup(3, GPIO.IN)
GPIO.setup(3, GPIO.IN)
GPIO.setup(3, GPIO.IN)

try:
	while True: # Run forever
		button_input = GPIO.input(10)
    	if button_input == GPIO.HIGH:
       		print("Button was pushed")

    	switch_input = GPIO.input(2)
    	if switch_input == GPIO.HIGH:
        	print("Switch is high")

        joystick_input_x = GPIO.input(3)
        joystick_input_y = GPIO.input(4)
        joystick_input_sw = GPIO.input(5)

        if joystick_input_x != GPIO.LOW:
        	print("Joystick x")
        if joystick_input_y != GPIO.LOW:
        	print("Joystick y")
        if joystick_input_sw != GPIO.HIGH:
        	print("Joystick switch")

finally:
	GPIO.cleanup()