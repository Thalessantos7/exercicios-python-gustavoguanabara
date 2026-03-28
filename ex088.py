# Faça um programa que ajude um jogador da MEGA SENA a criar palpites.
# O programa vai perguntar quantos jogos serão gerados e vai sortear 6 números entre 1 e 60 para cada jogo, cadastrando tudo em uma lista composta.
from random import randint

jogos = int(input("Quantos jogos quer sortear? "))
lista = []

for i in range(1, jogos + 1):
    for j in range(6):
        lista.append(randint(1, 60))
    print(f"Jogo {i}: {lista}")
    lista.clear()