import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

s.bind(("172.29.17.214", 7000))

s.listen(0)

while True:
	client, addr = s.accept()
	while True:
		content = client.recv(2048)
		print(len(content))
		print(content)
		content = 0
	clinet.close()