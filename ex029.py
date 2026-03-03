""" Escreva um programa que leia a velocidade de um carro.
Se ele ultrapassar 80Km/h, mostre uma mensagem dizendo que ele foi multado.
A multa vai custar R$7,00 por cada Km acima do limite. """
velocidade = float(input("Velocidade do carro: "))

if velocidade > 80.0:
    print("VOCÊ FOI MULTADO POR EXCESSO DE VELOCIDADE!")
    print(f"A multa vai custar R${(velocidade - 80.0) * 7.0:.2f}!")
    print("Dirija com cuidado! Tenha um bom dia!")
else:
    print("Dirija com cuidado! Tenha um bom dia!")
    