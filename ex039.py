""" Faça um programa que leia o ano de nascimento de um jovem e informe, de acordo com a sua idade, se ele ainda
vai se alistar ao serviço militar, se é a hora exata de se alistar ou se já passou do tempo do alistamento.
Seu programa também deverá mostrar o tempo que falta ou que passou do prazo. """
from datetime import date

anoNascimento = int(input("Ano de nascimento: "))
dataAtual = date.today()
idade = dataAtual.year - anoNascimento

if idade < 18:
    print(f"Você tem {idade} anos, faltam {18 - idade} anos para você se alistar!")
elif idade == 18:
    print(f"Você tem {idade} anos, está na idade exata para se alistar!")
else:
    print(f"Você tem {idade} anos, faz {idade - 18} anos que já deveria ter se alistado!")