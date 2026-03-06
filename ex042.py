""" Refaça o DESAFIO 35 dos triângulos, acrescentando o recurso de mostrar que tipo de triângulo será formado:
– EQUILÁTERO: todos os lados iguais
– ISÓSCELES: dois lados iguais, um diferente
– ESCALENO: todos os lados diferentes """
reta1 = float(input("Primeiro segmento: "))
reta2 = float(input("Segundo segmento: "))
reta3 = float(input("Terceiro segmento: "))

if reta1 < reta2 + reta3 and reta2 < reta1 + reta3 and reta3 < reta1 + reta2:
    if reta1 == reta2 == reta3:
        print("Os segmentos acima PODEM FORMAR um triângulo EQUILÁTERO.")
    elif reta1 != reta2 != reta3:
        print("Os segmentos acima PODEM FORMAR um triângulo ESCALENO.")
    else:
        print("Os segmentos acima PODEM FORMAR um triângulo ISÓSCELES.")
else:
    print("Os segmentos acima NÃO PODEM FORMAR um triângulo.")