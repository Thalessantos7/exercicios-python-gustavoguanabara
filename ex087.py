""" Aprimore o desafio anterior, mostrando no final: 
A) A soma de todos os valores pares digitados.
B) A soma dos valores da terceira coluna.
C) O maior valor da segunda linha. """
matriz = []
somaPares = 0

for i in range(3):
    linha = []
    for j in range(3):
        valor = int(input(f"Digite um valor para [{i}, {j}]: "))

        if valor % 2 == 0:
            somaPares += valor
        linha.append(valor)
    matriz.append(linha)

for l in matriz:
    for i in range(len(l)):
        print(f"[ {l[i]} ]", end=" ")
    print()

print(f"""\nA soma dos valores pares é {somaPares}.
A soma dos valores da terceira coluna é {matriz[0][2] + matriz[1][2] + matriz[2][2]}.
O maior valor da segunda linha é {max(matriz[1])}.""")