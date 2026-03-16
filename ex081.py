""" Crie um programa que vai ler vários números e colocar em uma lista. Depois disso, mostre:
A) Quantos números foram digitados.
B) A lista de valores, ordenada de forma decrescente.
C) Se o valor 5 foi digitado e está ou não na lista. """
cont = 0
lista = []

while True:
    valor = int(input("Digite um valor: "))
    lista.append(valor)

    continuar = input("Quer continuar [S/N]? ").strip().upper()

    if continuar == "N":
        break
    
print(f"""Você digitou {len(lista)} elementos.
Os valores em ordem decrescente são {sorted(lista, reverse=True)}
O valor 5 {"faz parte" if 5 in lista else "não faz parte"} da lista""")