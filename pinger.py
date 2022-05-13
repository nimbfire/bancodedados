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

    while True:
        entrada = input("Digite a url para pingar OU fim para finalizar o programa: ")
        if entrada == 'fim':
            print("Finalizando")
            print("Obrigado pela preferencia")
            break
        else:
            try:
                _ping(entrada)
            except ValueError:
                print("Erro ao pingar a url :/")
                print("Por favor entre em contato com o admin")

def _ping(url):
    comando = "ping -c 5 " + url
    print("------------ Pingando URL: www.google.com ")
    execute(comando)

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

