# Crie um programa onde o usuário possa digitar vários valores numéricos e cadastre-os em uma lista.
# Caso o número já exista lá dentro, ele não será adicionado. No final, serão exibidos todos os valores únicos digitados, em ordem crescente.
listaValores = []

while True:
    valor = int(input("Digite um valor: "))

    if valor in listaValores:
        print("Valor duplicado! Não vou adicionar...")
    else:
        print("Valor adicionado com sucesso...")
        listaValores.append(valor)
    
    continuar = input("Quer continuar [S/N]? ").upper().strip()

    if continuar == "N":
        print('-=-' * 20)
        break

print(f"Você digitou os valores {sorted(listaValores)}")