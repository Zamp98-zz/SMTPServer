import errno
import sys
import runpy
import user
import input_output
import os
import time

def checkUsers():
    r = input_output.loadUsers("users.txt")
    print("Diretorio corrente:",os.getcwd())
    for i in r:
        i.print() #cria o arquivo com o nome i
        try:#tenta verificar se a caixa do usuário existe
            f = open(os.path.join(os.getcwd()+'/data', i.getLogin()+ 'Inbox.txt'), 'r')
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
            f = open(os.path.join(os.getcwd()+'/data', i.getLogin()+ 'Inbox.txt'), 'w')
            f.close()
    print("Número de usuários cadastrados:",len(r))

def main():
    checkUsers()
    #print(sys.platform)
    #runpy.run_module(mod_name='server')
    #print("Iniciando servidor...")
    #time.sleep(1)
    #print("Iniciando cliente...")
    #runpy.run_module(mod_name='client')

