""" Desenvolva um programa que pergunte a distância de uma viagem em Km.
Calcule o preço da passagem, cobrando R$0,50 por Km para viagens
de até 200Km e R$0,45 parta viagens mais longas. """
distancia = float(input("Qual é a distância da viagem? "))

print(f"Preço da passagem: R${0.50 * distancia:.2f}" if distancia <= 200 else f"Preço da passagem: R${0.45 * distancia:.2f}")