# Faça um programa que leia um ano qualquer e mostre se ele é bissexto.
ano = int(input("Digite um ano qualquer: "))

print(f"O ano de {ano} é bissexto." if ano % 4 == 0 else f"O ano de {ano} não é bissexto.")