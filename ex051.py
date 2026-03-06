# Desenvolva um programa que leia o primeiro termo e a razão de uma PA. No final, mostre os 10 primeiros termos dessa progressão.
termo1 = int(input("Primeiro termo da PA: "))
razao = int(input("Razão da PA: "))
termo10 = termo1 + (10 - 1) * razao

for i in range(termo1, termo10 + razao, razao):
    print(i, end=" -> ")
print("ACABOU")