# Crie um programa que tenha uma tupla única com nomes de produtos e seus respectivos preços, na sequência.
# No final, mostre uma listagem de preços, organizando os dados em forma tabular.
produtos = ("Lápis", 1.75,
            "Borracha", 2.00,
            "Caderno", 15.90,
            "Estojo", 25.00,
            "Transferidor", 4.20,
            "Compasso", 9.99,
            "Mochila", 120.32,
            "Canetas", 22.30,
            "Livro", 34.90)


print(f"{'-' * 40}\n{"LISTAGEM DE PREÇOS":^38}\n{'-' * 40}")
cont = 1

for i in range(0, 17, 2):
    print(f"{produtos[i]}{'.' * 25}R$ {produtos[cont]:.2f}")
    cont += 2

print(f"{'-' * 40}")