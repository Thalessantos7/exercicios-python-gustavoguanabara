# Crie um programa que vai gerar cinco números aleatórios e colocar em uma tupla.
# Depois disso, mostre a listagem de números gerados e também indique o menor e o maior valor que estão na tupla
from random import randrange

numeros = (randrange(11), randrange(11), randrange(11), randrange(11), randrange(11))

print("Os números sorteados foram:", end=" ")

for num in numeros:
    print(num, end=" ")

print(f"\nMaior número sorteado: {max(numeros)} \nMenor número sorteado: {min(numeros)}")