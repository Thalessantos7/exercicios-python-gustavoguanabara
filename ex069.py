""" Crie um programa que leia a idade e o sexo de várias pessoas.
A cada pessoa cadastrada, o programa deverá perguntar se o usuário quer ou não continuar. No final, mostre:
A) quantas pessoas tem mais de 18 anos.
B) quantos homens foram cadastrados.
C) quantas mulheres tem menos de 20 anos. """
contMais18 = contHomem = contMulher = 0

while True:
    print(f"{'-=-' * 10}\nCADASTRO DE PESSOA\n{'-=-' * 10}")

    idade = int(input("Idade: "))
    sexo = input("Sexo [M/F]: ").upper().strip()

    print(f"{'-=-' * 10}")
    
    if idade > 18:
        contMais18 += 1
    if sexo == "M":
        contHomem += 1
    elif sexo == "F" and idade < 20:
        contMulher += 1
    
    continuar = input("Quer continuar [S/N]? ").upper().strip()

    if continuar == "N":
        break

print(f"Pessoas com mais de 18 anos: {contMais18} \nHomems cadastrados: {contHomem} \nMulheres com menos de 20 anos: {contMulher}")