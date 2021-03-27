import socket

HOST = '127.0.0.1'  # The server's hostname or IP address
PORT = 8008        # The port used by the server

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((HOST, PORT))
while True:
	x = input("C: ")
	s.sendall(x.encode('utf-8')) # manda a mensagem
	data = s.recv(1024) # le a resposta
	if(data.decode('utf-8')!="X"):
		print('S:', data.decode('utf-8'))
