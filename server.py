import socket
import os
import user
import init

def erroDestinatario(destinatario):
	try:
		f = open(os.path.join(os.getcwd()+'/data', destinatario + 'Inbox.txt'), 'r')
		return [False, destinatario]
	except:
		return [True, "550 Address Unknown"]

def erroComando(comando):
	# comando = "RCPT TO: email.com>"
	if ( comando.startswith("RCP TO:")):
		start = comando.find('<') + 1
		end = comando.find('>', start)
		if (start!= -1 and end != -1):
			destinario = comando[start:end]
			return erroDestinatario(destinario)
	elif(comando == "DATA"):
		return [False, "DATA"]

	return [True, "500 Syntax error, command unrecognized"]

# def input(serversocket):
# 	data = ""
# 	serversocket.sendall("Digite sua mensagem:".encode('utf-8'))
# 	while True:
# 		x = serversocket.recv(1024).decode('utf-8')
# 		data += x
# 		if(x == "."):
# 			return data
# 		serversocket.sendall("".encode('utf-8'))

def enviaEmail(mensagem, destinatario):
	f = open(os.path.join(os.getcwd()+'/data', destinatario + 'Inbox.txt'), 'a')
	f.write(mensagem+"\n")
	f.close()


HOST = '127.0.0.1'  # Standard loopback interface address (localhost)
PORT = 8008        # Port to listen on (non-privileged ports are > 1023)
def start():
	# create an INET, STREAMing socket
	serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	# bind the socket to a public host, and a well-known port
	serversocket.bind((HOST, PORT))
	# become a server socket
	serversocket.listen(5)
	(serversocket, address) = serversocket.accept()
	print("conectou")
	destinatario = None
	recebendoEmail = False
	email = ""
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
		
		if (not recebendoEmail):
			codigo = erroComando(data.decode('utf-8'))
			if(codigo[0]):
				data = codigo[1]
			else:
				if(codigo[1] == "DATA"):
					if(not destinatario):
						data = "550 Address Unknown"
					else:
						recebendoEmail = True	
						data = "Escreve sua mensagem"	
				else:
					destinatario = codigo[1]
					data = "Destinatário aceito"
		else:
			if(data.decode('utf-8')=="."):
				enviaEmail(email, destinatario)
				destinatario = None
				data = "Mensagem enviada com sucesso"
				recebendoEmail= False
				email = ""
			else:
				email += data.decode('utf-8')
				data = "X"
		serversocket.sendall(data.encode('utf-8')) # mandar mensagem
init.main()
start()

# funções separadas para erro

# 