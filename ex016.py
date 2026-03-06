# Crie um programa que leia um número Real qualquer pelo teclado e mostre na tela a sua porção Inteira.
from math import trunc
real = float(input("Digite qualquer número real: "))

print(f"Número real digitado: {real} \nPorção inteira: {trunc(real)}")