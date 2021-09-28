import RPi.GPIO as GPIO # Import Raspberry Pi GPIO library
import time

GPIO.setwarnings(False) # Ignore warning for now
GPIO.setmode(GPIO.BOARD) # Use physical pin numbering
#GPIO.setup(10, GPIO.IN, pull_up_down=GPIO.PUD_DOWN) # Set pin 10 to be an input pin and set initial value to be pulled low (off)
GPIO.setup(18, GPIO.IN, pull_up_down=GPIO.PUD_UP) #button
GPIO.setup(22, GPIO.IN) #switch
GPIO.setup(15, GPIO.IN, pull_up_down=GPIO.PUD_UP) #joystick x
GPIO.setup(13, GPIO.IN, pull_up_down=GPIO.PUD_UP) #joystick y
GPIO.setup(11, GPIO.IN, pull_up_down=GPIO.PUD_UP) #joystick switch

#try:
while True: # Run forever
	if GPIO.input(18) == False:
		print("Button was pushed")
		time.sleep(0.5)

	if GPIO.input(22):
		print("Switch is high")

	if GPIO.input(15) == False:
		print("Joystick x")
	if GPIO.input(13) == False:
		print(GPIO.input(13))
	if GPIO.input(11) == False: 
		print("Joystick switch")
		time.sleep(0.5)

#finally:
	#GPIO.cleanup()
