""" Crie um programa que leia dois valores e mostre um menu na tela:
[ 1 ] somar
[ 2 ] multiplicar
[ 3 ] maior
[ 4 ] novos números
[ 5 ] sair do programa
Seu programa deverá realizar a operação solicitada em cada caso. """
from time import sleep

valor1 = int(input("Primeiro valor: "))
valor2 = int(input("Segundo valor: "))

while True:
    menu = int(input("""[ 1 ] somar
[ 2 ] multiplicar
[ 3 ] maior
[ 4 ] novos números
[ 5 ] sair do programa
Sua opção: """))
    
    if menu == 5:
        print("Obrigado por usar o programa!")
        print("FINALIZANDO...")
        sleep(1)
        break
    elif menu == 1:
        print(f"{valor1} + {valor2} = {valor1 + valor2}")
    elif menu == 2:
        print(f"{valor1} x {valor2} = {valor1 * valor2}")
    elif menu == 3:
        print(f"O número {max(valor1, valor2)} é maior que o número {min(valor1, valor2)}.")
    elif menu == 4:
        print("Digite os números novamente.")
        valor1 = int(input("Primeiro valor: "))
        valor2 = int(input("Segundo valor: "))
    else:
        print("Opção inválida. Tente novamente.")
    
    print(f"{'-=-' * 10}")