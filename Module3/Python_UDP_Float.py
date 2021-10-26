import socket
from pythonosc import udp_client
from pydub import AudioSegment

#audio segment
#filename = 'input.wav'
#sound = AudioSegment.from_file(filename, format="wav")

UDP_IP = "172.29.17.214"
UDP_PORT = 8092

sock = socket.socket(socket.AF_INET, # Internet
                     socket.SOCK_DGRAM) # UDP
sock.bind((UDP_IP, UDP_PORT))

sc_client = udp_client.SimpleUDPClient("127.0.0.1", 57120) # Default ip and port for SC
#sc_client.send_message('/print', value)

n = 0 #packet data
sensor = 0 #which sensor is being read

while True:

	value = 3
	#sc_client.send_message("/print", value)

	data, addr = sock.recvfrom(1024)
	n = data.decode("ASCII")
	print("Message: ", n)
    #print("sensor: ", sensor)

	if (int(n) == 5000): #start key
    	#print('KEY');
		sensor = 1;

	elif (sensor == 1): #BUTTON 1
		string = str(int(n)*100)
		#sc_client.send_message("/print", string)
		if (int(n) == 0):
			print('BUTTON 1 PRESSED')
		sensor = 2

	elif (sensor == 2): #BUTTON 2
		if (int(n) == 0):
			print('BUTTON 2 PRESSED')
		sensor = 3

	elif (sensor == 3): #PHOTORESISTOR 1
		sc_client.send_message("/print", n)
		sensor = 4

	elif (sensor == 4): #PHOTORESISTOR 2
		sc_client.send_message("/p2", n)
		sensor = 5

	elif (sensor == 5): #PHOTORESISTOR 3
		sensor = 6

	elif (sensor == 6): #PIEZO
		sensor = 0









