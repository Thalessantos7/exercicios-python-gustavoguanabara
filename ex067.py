# Faça um programa que mostre a tabuada de vários números, um de cada vez, para cada valor digitado pelo usuário.
# O programa será interrompido quando o número solicitado for negativo.
while True:
    print(f"{'-' * 40}")
    num = int(input("Digite um número para ver sua tabuada: "))
    print(f"{'-' * 40}")

    if num < 0:
        print("PROGRAMA ENCERRADO!")
        break

    cont = 1
    while cont <= 10:
        print(f"{num} x {cont} = {num * cont}")
        cont += 1