# Crie um programa onde o usuário possa digitar sete valores numéricos e cadastre-os
# em uma lista única que mantenha separados os valores pares e ímpares.No final, mostre os valores pares e ímpares em ordem crescente.
pares = []
impares = []

for i in range(1, 8):
    valor = int(input(f"{i}o. valor: "))

    if valor % 2 == 0: pares.append(valor)
    else: impares.append(valor)

pares.sort()
impares.sort()

print(f"\nOs valores pares digitados foram: {pares}\nOs valores impares digitados foram: {impares}")