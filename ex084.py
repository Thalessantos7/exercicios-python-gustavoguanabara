""" Faça um programa que leia nome e peso de várias pessoas, guardando tudo em uma lista. No final, mostre:
A) Quantas pessoas foram cadastradas.
B) Uma listagem com as pessoas mais pesadas.
C) Uma listagem com as pessoas mais leves. """
dados = []
pessoas = []
maiorPeso = menorPeso = 0

while True:
    nome = input("Nome: ").strip()
    peso = float(input("Peso: "))

    dados = [nome, peso]
    pessoas.append(dados[:])

    if len(pessoas) == 1:
        maiorPeso = menorPeso = peso
    else:
        if peso > maiorPeso:
            maiorPeso = peso
        if peso < menorPeso:
            menorPeso = peso

    continuar = input("Quer continuar [S/N]? ").strip().upper()
    if continuar == "N":
        break

print(f"\nAo todo, você cadastrou {len(pessoas)} pessoas.")

print(f"O maior peso foi de {maiorPeso:.1f}Kg. Peso de ", end="")
for p in pessoas:
    if p[1] == maiorPeso:
        print(f"[{p[0]}] ", end="")

print(f"\nO menor peso foi de {menorPeso:.1f}Kg. Peso de ", end="")
for p in pessoas:
    if p[1] == menorPeso:
        print(f"[{p[0]}] ", end="")