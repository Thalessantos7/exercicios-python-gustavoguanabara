# Faça um programa que leia um ângulo qualquer e mostre na tela o valor do seno, cosseno e tangente desse ângulo.
from math import sin, cos, tan, radians
angulo = float(input("Digite um ângulo: "))
seno = sin(radians(angulo))
cosseno = cos(radians(angulo))
tangente = tan(radians(angulo))

print(f"""Seno: {seno:.2f}
Cosseno: {cosseno:.2f}
Tangente: {tangente:.2f}""")