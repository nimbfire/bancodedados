'''
Escreva um programa em Python que:
- Recebe uma URL digitada via teclado
- Realiza um ping da respectiva URL
- Retorna o ip (se houver) da URL digitada
- Considere o exemplo de execução apresentado abaixo:


Critérios de Avaliação:
- Conceito C
- Entrada:
- URL’s para serem pingadas devem entrar via teclado
- Saída:
- Resultado de cada ping mostrado na tela, conforme exemplo acima
- Ao final do execução de cada ping, o programa deve mostrar na tela uma Tabela de Resultados
- A Tabela de Resultados deve conter os campos: URL e IP, formatados da seguinte
maneira (veja imagem abaixo e/ou acima):

- Conceito B
- Entrada:
- URL’s para serem pingadas devem entrar via teclado
- Saída:
- Resultado de cada ping mostrado na tela, conforme exemplo acima.
- Ao final do execução do programa, isto é, quando o usuário indicar que não deseja continuar,
o programa deve mostrar na tela uma única Tabela de Resultados contendo os dados de todos
os pings realizado durante a execução.
- A Tabela de Resultados deve conter os campos:
URL, IP, Status (Ativo ou Inativo), Data e Hora, formatados da seguinte maneira
(veja imagem abaixo):

- Conceito A, indo além:
- Entrada:
- URL’s para serem pingadas a partir de um arquivo .txt

- Os pings devem ser disparados automaticamente (uma URL por vez) e uma mensagem deve
ser informada na tela para o usuário:
'''

import os
import sys
from subprocess import call, check_output, CalledProcessError, STDOUT
from datetime import datetime


MODE_INTERACTIVE = "interactive"
MODE_AUTOMATIC = "automatic"
MODE_UNDEFINED = "undefined"

running_mode = "undefined"
flag_help = False
flag_interactive = False
flag_automatic = False
flag_output = False
flag_debug = False
file_input = "entrada.txt"
file_output = "saida.txt"

def _get_running_mode(args_list):
    mode = MODE_UNDEFINED
    for arg in args_list:
        if arg == '-h' or arg == '--help':
            global flag_help
            flag_help = True
        if arg == "-i" or arg == "--interactive":
            mode = MODE_INTERACTIVE
        if arg == "-a" or arg == "--automatic":
            mode = MODE_AUTOMATIC
        if arg[0:3] == '-f=':
            mode = MODE_AUTOMATIC
            file_input = arg[3:]
            print("Arquivo escolhido para importar:{}".format(file_input))
        if arg[0:3] == '-o=':
            mode = MODE_AUTOMATIC
            file_output = arg[3:]
            print("Arquivo escolhido para exportar:{}".format(file_output))
        if arg == '-d':
            flag_debug = True;
    return mode

def _show_help():
    print('help')
    message = """Pinger!

    O programa tem 2 modos principais
    de funcionamento!

    1) O usuário digita as urls que ele quer
    testar o ping manualmente
    2) O usuário importa de um arquivo txt
    as urls que devem ser testadas

    Além disso, aceitamos:
    -h ou --help pra mostrar um texto de ajuda
    -i ou --interactive para preenchimento manual
    -a ou --automatic para leitura automatica
    de um arquivo txt
    -f=file para definir o arquivo
    de leitura que o modo automatico usará para
    importar as urls (se não ele vai tentar importar
    do arquivo entrada.txt)
    -o=file para definir o arquivo de
    output quando usando a metodologia automatica (
    se não ele vai salvar no arquivo saida.txt)
    """
    print(message)

def main() -> int:
    """Pinger!

    O programa tem 2 modos principais
    de funcionamento!

    1) O usuário digita as urls que ele quer
    testar o ping manualmente
    2) O usuário importa de um arquivo txt
    as urls que devem ser testadas

    Além disso, aceitamos:
    -h ou --help pra mostrar um texto de ajuda
    -i ou --interactive para preenchimento manual
    -a ou --automatic para leitura automatica
    de um arquivo txt

    -o ou --output para definir o arquivo de
    output quando usando a metodologia automatica

    """
    print(sys.argv)
    global flag_help
    running_mode = _get_running_mode(sys.argv)

    print("Running mode:{}".format(running_mode))
    if flag_help or running_mode == MODE_UNDEFINED:
        _show_help()
        return 0

    if running_mode == MODE_INTERACTIVE:
        _interactive_loop()
    return 0

def _interactive_loop():
    resultados = []
    while True:
        entrada = input("Digite a url para pingar OU fim para finalizar o programa: ")
        if entrada == 'fim':
            print("Finalizando")
            print("Obrigado pela preferencia")
            print(resultados)
            break
        else:
            try:
                resultado = _ping(entrada)
                if resultado:
                    resultados.append(_parse_resultados(resultado, entrada))
                else:
                    resultados.append(_resultado_inativo(entrada))
            except ValueError:
                print("Erro ao pingar a url :/")
                print("Por favor entre em contato com o admin")

def _ping(url):
    comando = "ping -c 5 " + url
    print("------------ Pingando URL: www.google.com ")

    if (execute(comando) == 0):
        resultado = get(comando)
        return resultado

    else:
        print("Url não encontrada!")
        return False

def _parse_resultados(resultado, url):
    # Exemplo de resultado esperado:
    # (0, b'PING www.google.com (142.251.128.132) 56(84) bytes of data.\n64 bytes from gru06s71-in-f4.1e100.net (142.251.128.132): icmp_seq=1 ttl=55 time=166 ms\n64 bytes from gru06s71-in-f4.1e100.net (142.251.128.132): icmp_seq=2 ttl=55 time=145 ms\n64 bytes from gru06s71-in-f4.1e100.net (142.251.128.132): icmp_seq=3 ttl=55 time=33.7 ms\n64 bytes from gru06s71-in-f4.1e100.net (142.251.128.132): icmp_seq=4 ttl=55 time=45.2 ms\n64 bytes from gru06s71-in-f4.1e100.net (142.251.128.132): icmp_seq=5 ttl=55 time=22.0 ms\n\n--- www.google.com ping statistics ---\n5 packets transmitted, 5 received, 0% packet loss, time 4004ms\nrtt min/avg/max/mdev = 22.046/82.354/165.625/60.437 ms\n')
    resultado_array = resultado[1].split()

    return {
        "url":url,
        "ip": resultado_array[2].decode('ascii'),
        "ativo":"Ativo",
        "data": datetime.today().strftime('%Y/%m/%d'),
        "hora": datetime.today().strftime('%H:%M:%S')
    }

def _resultado_inativo(url):
    return {
        "url":url,
        "ip": "----",
        "ativo":"Inativo",
        "data": datetime.today().strftime('%Y/%m/%d'),
        "hora": datetime.today().strftime('%H:%M:%S')
    }

def execute(comando):
    return call(comando.split())

def check (comando):
    return call(comando.split()) == 0

def get(comando):
    try:
        return 0, check_output(comando.split(), stderr=STDOUT)
    except CalledProcessError as e:
        return e.returncode, e.check_output

if __name__ == '__main__':
    sys.exit(main())  # Pelo visto é o jeito certo neh

