# Faça um algoritmo que leia o preço de um produto e mostre seu novo preço, com 5% de desconto.
valor = float(input("Preço do produto: "))
novoValor = valor - (5 * valor / 100)

print(f"O novo preço do produto com 5% de desconto é R${novoValor:.2f}")