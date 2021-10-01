import serial

ser = serial.Serial()
ser.port = '/dev/cu.SLAB_USBtoUART'

#ser.baudrate = 115200
#ser.setDTR(False)
#ser.setRTS(False)

ser.open()
device = 1;

while True:
	line = ser.readline()
	decoded_line = (line[0:len(line)-2].decode("utf-8"))
	#print(str(device) + ", " + str(decoded_line))

	#if (str(decoded_line) == 'NEW'):
		#device = 1

	#if (device == 1): #joystick Y

	#if (device == 2): #joystick X

	if (device == 3): #joystick switch
		if (int(decoded_line) == 0):
			print('JOYSTICK PRESSED')

	if (device == 4): #button
		if (int(decoded_line) == 0):
			print('BUTTON PRESSED')

	if (device == 5): #switch
		if (int(decoded_line) == 0):
			print('SWITCH PRESSED')

	if (device == 5):
		device = 1
	else:
		device = device+1