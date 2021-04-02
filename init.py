import errno
import sys
import runpy
import input_output
import os
import time

def checkUsers():
	r = input_output.loadUsers("users.txt")
	path = os.getcwd() + "/data"
	os.mkdir(path)

	print("Diretorio corrente:",os.getcwd())
	# r = são os caixas de user
	# c = caixas que existem
	# c - r
	c = os.listdir(path)
	for i in r:
		print(i) #cria o arquivo com o nome i
		try:#tenta verificar se a caixa do usuário existe
			c.remove(i)
			f = open(os.path.join(os.getcwd()+'/data', i), 'r')
			print("caixa existente")
			f.close()
		except:
			print("caixa criada")
			if not os.path.exists(os.getcwd()+'/data'):
				try:
					os.makedirs(os.getcwd()+'/data')
				except OSError as exc: # Guard against race condition
					if exc.errno != errno.EEXIST:
						raise
			f = open(os.path.join(os.getcwd()+'/data', i), 'w')
			f.close()
	for i in c:
		os.remove(path + "/" + i)
	print("Número de usuários cadastrados:",len(r))

def main():
	checkUsers()
	#print(sys.platform)
	#runpy.run_module(mod_name='server')
	#print("Iniciando servidor...")
	#time.sleep(1)
	#print("Iniciando cliente...")
	#runpy.run_module(mod_name='client')

