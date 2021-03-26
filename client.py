import socket
import base64

HOST = '127.0.0.1'  # The server's hostname or IP address
PORT = 8080        # The port used by the server

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((HOST, PORT))

while True:
	x = input("Digite alguma coisa")
	x = base64.b64encode(bytes(str(x), 'utf-8'))
	s.sendall(str(x).encode('ascii')) # manda a mensagem
	data = s.recv(1024) # le a resposta
	print('Received', data)