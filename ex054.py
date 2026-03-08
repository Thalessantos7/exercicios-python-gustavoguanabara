# Crie um programa que leia o ano de nascimento de sete pessoas. 
# No final, mostre quantas pessoas ainda não atingiram a maioridade e quantas já são maiores.
from datetime import date

idade = contMaior = contMenor = 0
anoAtual = date.today().year

for i in range(1, 8):
    anoDeNascimento = int(input(f"Em que ano a {i}ª pessoa nasceu? "))
    idade = anoAtual - anoDeNascimento

    if idade >= 18:
        contMaior += 1
    else:
        contMenor += 1
print(f"{contMenor} pessoas ainda são menores de idade. \n{contMaior} pessoas já são maiores de idade.")