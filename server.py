import socket



HOST = '127.0.0.1'  # Standard loopback interface address (localhost)
PORT = 8080        # Port to listen on (non-privileged ports are > 1023)
def start():
	# create an INET, STREAMing socket
	serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	# bind the socket to a public host, and a well-known port
	serversocket.bind((HOST, PORT))
	# become a server socket
	serversocket.listen(5)
	(serversocket, address) = serversocket.accept()
	print("conectou")
	while True:
		# accept connections from outside
		# now do something with the clientsocket
		# in this case, we'll pretend this is a threaded server
		data = serversocket.recv(1024)
		if not data: # quando acabar a conexão
			print('sem conexão')
			serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
			# bind the socket to a public host, and a well-known port
			serversocket.bind((HOST, PORT))
			# become a server socket
			serversocket.listen(5)
			(serversocket, address) = serversocket.accept()
		serversocket.sendall(data) # mandar mensagem


# funções separadas para erro

# 