""" Crie um programa que leia o nome e o preço de vários produtos.
O programa deverá perguntar se o usuário vai continuar ou não. No final, mostre:
A) qual é o total gasto na compra.
B) quantos produtos custam mais de R$1000.
C) qual é o nome do produto mais barato. """
nome = input("Nome do produto: ")
preco = float(input("Preço do produto: R$"))
total = preco
contMais1000 = 0
nomeMaisBrato = nome
precoMaisBarato = preco

if preco > 1000:
    contMais1000 += 1

while True:
    continuar = input("Quer continuar [S/N]? ").upper().strip()

    if continuar == "N":
        print("-----FIM DO PROGRAMA-----")
        break

    nome = input("Nome do produto: ")
    preco = float(input("Preço do produto: R$"))

    total += preco

    if preco > 1000:
        contMais1000 += 1
    if preco < precoMaisBarato:
        precoMaisBarato = preco
        nomeMaisBrato = nome

print(f"""Total gasto na compra: R${total:.2f}
Produtos que custam mais de R$1000.00: {contMais1000}
O produto mais barato foi {nomeMaisBrato} que custa R${precoMaisBarato:.2f}""")