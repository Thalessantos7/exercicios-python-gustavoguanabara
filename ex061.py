# Refaça o DESAFIO 51, lendo o primeiro termo e a razão de uma PA, mostrando os 
# 10 primeiros termos da progressão usando a estrutura while.
termo1 = int(input("Primeiro termo da PA: "))
razao = int(input("Razão da PA: "))
termo10 = termo1 + (10 - 1) * razao

while termo1 < termo10 + razao:
    print(termo1, end=" -> ")
    termo1 += razao
print("ACABOU")