# Crie um programa que leia vários números inteiros pelo teclado.
# No final da execução, mostre a média entre todos os valores e qual foi o maior e o menor valores lidos
# O programa deve perguntar ao usuário se ele quer ou não continuar a digitar valores.
num = int(input("Digite um número inteiro: "))
cont = 1
maior = menor = soma = num

while True:
    continuar = input("Quer continuar [S/N]? ").upper().strip()

    if continuar == "N":
        break

    num = int(input("Digite um número inteiro: "))
    soma += num
    cont += 1
    
    if num > maior:
        maior = num
    if num < menor:
        menor = num
media = soma / cont

print(f"Média: {media:.2f} \nMaior número: {maior} \nMenor número: {menor}")