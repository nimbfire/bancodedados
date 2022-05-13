import sys

from subprocess import call, check_output, CalledProcessError, STDOUT

def execute(comando):
    return call(comando.split())

def check (comando):
    return call(comando.split()) == 0

def get(comando):
    try:
        return 0, check_output(comando.split(), stderr=STDOUT)
    except CalledProcessError as e:
        return e.returncode, e.check_output

#comando = "ping globo.com"
#execute(comando)
#print(check(comando))
#get(comando)

continua = "s"

while (continua == "s"):
    url = input("Digite uma URL: ")
    url = url.lower()
    comando = "ping -c 5 " + url
    #print(comando)
    print("\n ---------------------- PINGANDO ----------------------")
    if (execute(comando) == 0):

        resultadoPing = get(comando)
    #print(resultadoPing)
        p = resultadoPing[1]
        #print(p)
        lista = []
        lista = p.split()
        ip = lista[2].decode('ascii')
        print("\n -------------- URL | IP ------------------")
        print("    " + url + "  | " + ip[1:-1])
    else:
        print(" # IP NAO ENCONTRADO #")

    continua = input("\n Deseja Continuar? [S]im [N]ao ")
    continua.lower()

    print("\n #################### FIM DE PROGRAMA ####################")


#--------------------------
#for i in lista:
#    print(i)
#ip = lista[2]
#print(ip[2:-1])
#for i in p:
    #print(p[2])


#for i in resultadoPing:
    #partes = i.split()
 #   print(i.split(" "))
    #print(i.split())
'''
for line  in f:
    t = line.split()
    if ('QP' in line):
      if ('QP' in t[0]):
        temp += t[2][:-3] + "\t"
'''
#subprocess.call(["dir"])
#subprocess.check_call(["dir"])


#ipconfig = get("ipconfig")
#print(ipconfig[1])
'''import os, platform

def ping(host):
    if (platform.system().lower()=="windows"):
        ping_str = "-n 1"
    else:
        ping_str = "-c 1"

    resposta = os.system("ping " + ping_str + " " + host)
    return resposta

host = input("Digite o IP ou Endereco: ")
print("\n ----- Pingando: ", host)
resposta = 0
reposta = ping(host)
if (resposta == 0):
    print("UP")
else:
    print("Down")
'''
