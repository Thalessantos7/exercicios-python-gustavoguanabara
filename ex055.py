# Faça um programa que leia o peso de cinco pessoas. No final, mostre qual foi o maior e o menor peso lidos.
pesos = []

for i in range(1, 6):
    peso = float(input(f"Peso da {i}ª pessoa: "))
    pesos.append(peso)
print(f"Maior peso: {max(pesos)}Kg \nMenor peso: {min(pesos)}Kg")