# Crie um programa que vai ler vários números e colocar em uma lista. Depois disso, crie duas listas extras que
# vão conter apenas os valores pares e os valores ímpares digitados, respectivamente.Ao final, mostre o conteúdo das três listas geradas.
lista = []
listaPares = []
listaImpares = []

while True:
    valor = int(input("Digite um valor: "))
    lista.append(valor)

    listaPares.append(valor) if valor % 2 == 0 else listaImpares.append(valor)

    continuar = input("Quer continuar [S/N]? ").strip().upper()

    if continuar == "N":
        break

print(f"""A lista completa é {lista}
A lista de pares é {listaPares}
A lista de ímpares é {listaImpares}""")