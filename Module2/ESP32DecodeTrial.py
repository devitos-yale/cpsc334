import serial
import time
import pygame

ser = serial.Serial()
#ser.port = '/dev/ttyUSB0' #rasppi
ser.port = '/dev/cu.SLAB_USBtoUART' #mac

pygame.mixer.init()
background = pygame.mixer.Channel(0) #create channels for simultaneous playback
footsteps = pygame.mixer.Channel(1)
birds = pygame.mixer.Channel(2)

pygame.mixer.footsteps.play("SoundFiles/SnowFootsteps.mp3", loops = -1)
pygame.mixer.birds.play("SoundFiles/SnowOwl.mp3", loops = -1)
pygame.mixer.footsteps.pause()
pygame.mixer.birds.pause()

ser.open()
device = 0;
state = 1;
prevButtonPressed = 0; #was button pressed on last iteration
joystickY = 1958; #neutral Y position
joystickX = 1873; #neutral X position

while True:
	line = ser.readline()
	decoded_line = (line[0:len(line)-2].decode("utf-8"))
	#print(str(device) + ", " + str(decoded_line))

	if (decoded_line == ''): #handles case if line is NULL
		continue

	if (int(decoded_line) == 5000): #recognizes start key and resets device
		#print("RESTART")
		device = 0

	if (device == 1): #joystick Y
		joystickY = int(decoded_line)

	if (device == 2): #joystick X
		joystickX = int(decoded_line)

	if (device == 3): #joystick switch
		if (int(decoded_line) == 0):
			print('JOYSTICK PRESSED')

	if (device == 4): #button
		if (int(decoded_line) == 0):
			print('BUTTON PRESSED')
			if (prevButtonPressed == 0):
				if (state == 2):
					state = 0
				else:
					state = state+1
				#start playing background
				pygame.mixer.background.play("SoundFiles/SnowBackground.mp3", loops = -1)

			#time.sleep(0.5) #avoid bouncing
			print('STATE: ' + str(state))
			prevButtonPressed = 1
		else:
			prevButtonPressed = 0

	if (device == 5): #switch
		if (int(decoded_line) == 0):
			print('SWITCH PRESSED')
			pygame.mixer.birds.unpause("SoundFiles/SnowOwl.mp3")
		else:
			pygame.mixer.birds.pause("SoundFiles/SnowOwl.mp3")

	#if (device == 5):
	#	device = 1
	#else:
	#	device = device+1

	if ((joystickY == 0) or (joystickX == 0) or (joystickY == 4095) or (joystickX == 4095)):
		print('RUNNING')
		pygame.mixer.footsteps.unpause("SoundFiles/SnowFootsteps.mp3")
	elif ((joystickY < 1940) or (joystickY > 2000) or (joystickX < 1860) or (joystickX > 1920)):
		print('WALKING')
		pygame.mixer.footsteps.unpause("SoundFiles/SnowFootsteps.mp3")
	else:
		pygame.mixer.footsteps.pause("SoundFiles/SnowFootsteps.mp3")


	device = device+1






