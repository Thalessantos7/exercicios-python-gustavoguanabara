""" Crie um programa que simule o funcionamento de um caixa eletrônico.
No início, pergunte ao usuário qual será o valor a ser sacado (número inteiro)
e o programa vai informar quantas cédulas de cada valor serão entregues.
OBS: considere que o caixa possui cédulas de R$50, R$20, R$10 e R$1. """
valor = int(input("Qual valor você quer sacar? R$"))
cedulas = [50, 20, 10, 1]
total = []
cont = 0

while cont < 4:
    total.append(int(valor / cedulas[cont]))

    if total[cont] != 0:
        print(f"Total de {total[cont]} cédulas de R${cedulas[cont]}")
        
    valor = valor % cedulas[cont]
    cont += 1