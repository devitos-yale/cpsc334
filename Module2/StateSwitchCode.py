import RPi.GPIO as GPIO # Import Raspberry Pi GPIO library
import time

GPIO.setwarnings(False) # Ignore warning for now
GPIO.setmode(GPIO.BOARD) # Use physical pin numbering
#GPIO.setup(10, GPIO.IN, pull_up_down=GPIO.PUD_DOWN) # Set pin 10 to be an input pin and set initial value to be pulled low (off)
GPIO.setup(18, GPIO.IN, pull_up_down=GPIO.PUD_DOWN) #button
GPIO.setup(22, GPIO.IN, pull_up_down=GPIO.PUD_DOWN) #switch
GPIO.setup(15, GPIO.IN) #joystick x
GPIO.setup(13, GPIO.IN) #joystick y
GPIO.setup(11, GPIO.IN) #joystick switch

#try:
while True: # Run forever
	if GPIO.input(18) == True:
		print("Button was pushed")
		time.sleep(0.2)

	if GPIO.input(22) == True:
		print("Switch is high")

	#if GPIO.input(15) == GPIO.HIGH:
		#print("Joystick x")
	#if GPIO.input(13) == GPIO.HIGH:
		#print("Joystick y")
	#if GPIO.input(11) == GPIO.HIGH:
		#print("Joystick switch")

#finally:
	#GPIO.cleanup()