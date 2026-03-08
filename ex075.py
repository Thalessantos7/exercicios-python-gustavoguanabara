""" Desenvolva um programa que leia quatro valores pelo teclado e guarde-os em uma tupla. No final, mostre:
A) Quantas vezes apareceu o valor 9.
B) Em que posição foi digitado o primeiro valor 3.
C) Quais foram os números pares. """
valores = ()

for i in range(1, 5):
    valor = int(input(f"{i}º valor: "))
    valores += (valor, )

print(f"O valor 9 apareceu {valores.count(9)} vezes. \nO primeiro valor 3 foi digitado na {valores.index(3) + 1}º posição.")

print(f"Valores pares digitados:", end=" ")

for valor in valores:
    if valor % 2 == 0:
        print(valor, end=" ")