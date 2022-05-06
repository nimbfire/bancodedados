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
    return 0

if __name__ == '__main__':
    sys.exit(main())  # Pelo visto é o jeito certo neh

