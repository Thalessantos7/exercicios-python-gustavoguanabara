# Desenvolva um programa que leia o nome, idade e sexo de 4 pessoas.
# No final do programa, mostre: a média de idade do grupo, qual é o nome do homem mais velho e quantas mulheres têm menos de 20 anos.
somaIdade = idadeMaisVelho = contMulher = nomeMaisVelho = 0

for i in range(1, 5):
    print(f"----- {i}ª PESSOA -----")
    nome = input("Nome: ").strip().title()
    idade = int(input("Idade: "))
    sexo = input("Sexo [M/F]: ").strip().upper()

    somaIdade += idade

    if sexo == "M" and idade > idadeMaisVelho:
        idadeMaisVelho = idade
        nomeMaisVelho = nome
    if sexo == "F" and idade < 20:
        contMulher += 1
mediaIdade = somaIdade / 4

print(f"Média de idade do grupo: {mediaIdade:.1f} anos. \nNome do homem mais velho: {nomeMaisVelho} e tem {idadeMaisVelho} anos. \n{contMulher} mulheres tem menos de 20 anos.")