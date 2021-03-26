import sys
import runpy
import user
import input_output
import server
import os
import time

def checkUsers():
    r = input_output.loadUsers("users.txt")
    for i in r:
        i.print() #cria o arquivo com o nome i
        try:#tenta verificar se a caixa do usuário existe
            f = open(i.getLogin()+'Inbox.txt', 'r')
            print("caixa existente")
            f.close()
        except:
            print("caixa criada")
            f = open(i.getLogin()+'Inbox.txt', 'w')
            f.close()


def main():
    checkUsers()
    print(sys.platform)
    runpy.run_module(mod_name='server')
    print("Iniciando servidor...")
    time.sleep(1)
    print("Iniciando cliente...")
    runpy.run_module(mod_name='client')
main()
