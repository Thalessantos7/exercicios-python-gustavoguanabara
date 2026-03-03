""" Escreva um programa que faça o computador “pensar” em um número inteiro entre 0 e 5
e peça para o usuário tentar descobrir qual foi o número escolhido pelo computador.
O programa deverá escrever na tela se o usuário venceu ou perdeu. """
from random import randrange
from time import sleep

print(f"""{"-=-" * 25}
Pensarei em um número entre 0 e 5. Tente adivinhar qual número eu pensei...
{"-=-" * 25}""")

numMagico = randrange(6)
tentativa = int(input("Qual número eu pensei? "))

print("PROCESSANDO...")
sleep(1)

print(f"PARABÉNS! Você conseguiu acertar." if tentativa == numMagico else f"GANHEI! Eu pensei no número {numMagico} e não no {tentativa}.")