# Crie um programa que declare uma matriz de dimensão 3x3 e preencha com valores lidos pelo teclado.
# No final, mostre a matriz na tela, com a formatação correta.
matriz = []

for i in range(3):
    linha = []
    for j in range(3):
        linha.append(int(input(f"Digite um valor para [{i}, {j}]: ")))
    matriz.append(linha)

for l in matriz:
    for i in range(len(l)):
        print(f"[ {l[i]} ]", end=" ")
    print()