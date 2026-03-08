# Faça um programa que leia 5 valores numéricos e guarde-os em uma lista.
# No final, mostre qual foi o maior e o menor valor digitado e as suas respectivas posições na lista.
numeros = []

for i in range(5):
    num = int(input(f"Digite um valor para a posição {i}: "))
    numeros.append(num)

print(f"O maior valor digitado foi {max(numeros)} nas posições", end=" ")
for i, v in enumerate(numeros):
    if v == max(numeros):
        print(i, end="... ")

print(f"\nO menor valor digitado foi {min(numeros)} nas posições", end=" ")
for i, v in enumerate(numeros):
    if v == min(numeros):
        print(i, end="... ")