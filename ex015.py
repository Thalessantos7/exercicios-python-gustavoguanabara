# Escreva um programa que pergunte a quantidade de Km percorridos
# por um carro alugado e a quantidade de dias pelos quais ele foi alugado.
# Calcule o preço a pagar, sabendo que o carro custa R$60 por dia e R$0,15 por Km rodado.
km = float(input("Quantos km foram percorridos? "))
dias = int(input("Quantos dias alugados? "))
valorAPagar = dias * 60 + km * 0.15

print(f"Preço a pagar: R${valorAPagar:.2f}")