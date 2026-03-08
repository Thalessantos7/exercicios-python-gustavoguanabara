# Faça um programa que jogue par ou ímpar com o computador.
# O jogo só será interrompido quando o jogador perder, mostrando o total de vitórias consecutivas
# que ele conquistou no final do jogo.
from random import randrange

print(f"{'-=-' * 10} \nPAR OU ÍMPAR \n{'-=-' * 10}")
vitorias = 0

while True:
    valor = int(input("Digite um valor: "))
    parImpar = input("Par ou ímpar [P/I]? ").upper().strip()
    print(f"{'-=-' * 10}")
    valorComp = randrange(11)
    total = valor + valorComp

    if parImpar == "P" and total % 2 != 0:
        print(f"Você jogou {valor} e o computador {valorComp}. Total de {total} DEU ÍMPAR")
        print("Você PERDEU!")
        break
    if parImpar == "I" and total % 2 == 0:
        print(f"Você jogou {valor} e o computador {valorComp}. Total de {total} DEU PAR")
        print("Você PERDEU!")
        break
    elif parImpar == "P" and total % 2 == 0:
        vitorias += 1
        print(f"Você jogou {valor} e o computador {valorComp}. Total de {total} DEU PAR")
        print("Você VENCEU! \nVamos jogar novamente...")
    else:
        vitorias += 1
        print(f"Você jogou {valor} e o computador {valorComp}. Total de {total} DEU ÍMPAR")
        print("Você VENCEU! \nVamos jogar novamente...")
    print(f"{'-=-' * 10}")

print(f"{'-=-' * 10} \nGAME OVER! Você venceu {vitorias} vezes.")