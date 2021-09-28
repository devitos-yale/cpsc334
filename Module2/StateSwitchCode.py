import RPi.GPIO as GPIO # Import Raspberry Pi GPIO library
import time
import pygame

GPIO.setwarnings(False) # Ignore warning for now
GPIO.setmode(GPIO.BOARD) # Use physical pin numbering
GPIO.setup(18, GPIO.IN, pull_up_down=GPIO.PUD_UP) #button
GPIO.setup(22, GPIO.IN) #switch
GPIO.setup(15, GPIO.IN, pull_up_down=GPIO.PUD_UP) #joystick x
GPIO.setup(13, GPIO.IN, pull_up_down=GPIO.PUD_UP) #joystick y
GPIO.setup(11, GPIO.IN, pull_up_down=GPIO.PUD_UP) #joystick switch

stage=1
print("Stage " + str(stage))
playing = False #whether music is currently playing

pygame.mixer.init()
pygame.mixer.music.load("RockGuitar.mp3")
pygame.mixer.music.play(loops=-1) #loops mp3
pygame.mixer.music.pause()

while True: # Run forever
	if GPIO.input(18) == False:
		if (stage != 3): #increment stages with button press
			stage = stage+1
		else:
			stage = 1
		print("Stage " + str(stage))
		time.sleep(0.5) #avoid bouncing

	if GPIO.input(22):
		print("Switch is high")
		if (stage == 1): #pause on button press in stage 1
			pygame.mixer.music.unpause()
			playing = True
		time.sleep(0.2)
	elif (stage == 1): #pause on button press in stage 1
		pygame.mixer.music.pause()
		playing = False

	if GPIO.input(15) == False:
		print("Joystick x")
		if (stage == 3): #play when joystick in moved down in stage 3
			if (playing == False):
                        	pygame.mixer.music.unpause()
                        	playing = True
	if GPIO.input(13) == False:
		print("Joystick y")
		if (stage == 3): #pause when joystick is moved left in stage 3
			if (playing == True):
				pygame.mixer.music.pause()
				playing = False
	if GPIO.input(11) == False:
		print("Joystick switch")
		if (stage == 2): #play/pause on joystick switch press in stage 2
			if playing:
				pygame.mixer.music.pause()
				playing = False
			else:
				pygame.mixer.music.unpause()
				playing = True
		time.sleep(0.5)
