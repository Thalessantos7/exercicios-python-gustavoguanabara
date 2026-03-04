# Crie um programa que faça o computador jogar Jokenpô com você.
from time import sleep
from random import randrange

print(f"{'-=-' * 8}\nPEDRA, PAPEL E TESOURA\n{'-=-' * 8}")

jogadas = ["Pedra", "Papel", "Tesoura"]

jogada = int(input("""Suas opções:
[ 0 ] PEDRA
[ 1 ] PAPEL
[ 2 ] TESOURA
Sua jogada: """))
jogadaComp = randrange(3)

print("JO")
sleep(1)
print("KEN")
sleep(1)
print("PO!")

print(f"""{'-=-' * 8}
Computador jogou {jogadas[jogadaComp]}
Jogador jogou {jogadas[jogada]}
{'-=-' * 8}""")

if jogada == 0:
    if jogadaComp == 0:
        print("EMPATE!")
    elif jogadaComp == 1:
        print("COMPUTADOR VENCEU!")
    else:
        print("JOGADOR VENCEU!")
elif jogada == 1:
    if jogadaComp == 0:
        print("JOGADOR VENCEU!")
    elif jogadaComp == 1:
        print("EMPATE!")
    else:
        print("COMPUTADOR VENCEU!")
else:
    if jogadaComp == 0:
        print("COMPUTADOR VENCEU!")
    elif jogadaComp == 1:
        print("JOGADOR VENCEU!")
    else:
        print("EMPATE!")