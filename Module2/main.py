import serial
import time
import pygame

ser = serial.Serial()
ser.port = '/dev/ttyUSB0' #rasppi
#ser.port = '/dev/cu.SLAB_USBtoUART' #mac

pygame.init()
pygame.mixer.init()

backgroundch = pygame.mixer.Channel(0) #create channels for simultaneous playback
footstepsch = pygame.mixer.Channel(1)
birdsch = pygame.mixer.Channel(2)

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
			#print('JOYSTICK PRESSED')

	if (device == 4): #button
		if (int(decoded_line) == 0):
			#print('BUTTON PRESSED')
			if (prevButtonPressed == 0):
				if (state == 2):
					#initialize to snow
					state = 0
					footsteps = pygame.mixer.Sound('/home/pi/cpsc334/Module2/OggSounds/SnowFootsteps.ogg')
					footstepsch.play(footsteps, loops = -1)
					footstepsch.pause()
					birds = pygame.mixer.Sound('/home/pi/cpsc334/Module2/OggSounds/SnowOwl.ogg')
					birdsch.play(birds, loops = -1)
					birdsch.pause()
					background = pygame.mixer.Sound("/home/pi/cpsc334/Module2/OggSounds/SnowBackground.ogg")
					backgroundch.play(background, loops = -1)
					print('SNOW')
				elif (state == 1):
					state = 2
					#initialize to fall
					footsteps = pygame.mixer.Sound('/home/pi/cpsc334/Module2/OggSounds/ForestFootsteps.ogg')
					footstepsch.play(footsteps, loops = -1)
					footstepsch.pause()
					birds = pygame.mixer.Sound('/home/pi/cpsc334/Module2/OggSounds/ForestBirds.ogg')
					birdsch.play(birds, loops = -1)
					birdsch.pause()
					background = pygame.mixer.Sound("/home/pi/cpsc334/Module2/OggSounds/ForestBackground.ogg")
					backgroundch.set_volume(0.7)
					backgroundch.play(background, loops = -1)
					print('FOREST')
				else:
					state = 1
					#initialize to beach
					footsteps = pygame.mixer.Sound('/home/pi/cpsc334/Module2/OggSounds/BeachFootsteps.ogg')
					footstepsch.play(footsteps, loops = -1)
					footstepsch.pause()
					birds = pygame.mixer.Sound('/home/pi/cpsc334/Module2/OggSounds/BeachSeagulls.ogg')
					birdsch.play(birds, loops = -1)
					birdsch.pause()
					background = pygame.mixer.Sound("/home/pi/cpsc334/Module2/OggSounds/BeachBackground.ogg")
					backgroundch.set_volume(0.7)
					backgroundch.play(background, loops = -1)
					print('BEACH')

				#start playing background
				#backgroundch.play(background, loops = -1)

			#print('STATE: ' + str(state))
			prevButtonPressed = 1
		else:
			prevButtonPressed = 0

	if (device == 5): #switch
		if (int(decoded_line) == 0):
			#print('SWITCH PRESSED')
			birdsch.unpause()
		else:
			birdsch.pause()

	if ((joystickY == 0) or (joystickX == 0) or (joystickY == 4095) or (joystickX == 4095)):
		#print('RUNNING')
		footstepsch.unpause()
	elif ((joystickY < 1940) or (joystickY > 2000) or (joystickX < 1860) or (joystickX > 1920)):
		#print('WALKING')
		footstepsch.unpause()
	else:
		footstepsch.pause()


	device = device+1






