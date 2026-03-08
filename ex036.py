""" Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa.
Pergunte o valor da casa, o salário do comprador e em quantos anos ele vai pagar.
prestação mensal não pode exceder 30% do salário ou então o empréstimo será negado. """
valorDaCasa = float(input("Qual é o valor da casa? R$"))
salario = float(input("Qual é o salário do comprador? R$"))
anos = int(input("Quantos anos de financiamento? "))
prestacao = valorDaCasa / (anos * 12)

if prestacao <= (salario * 30.0 / 100.0):
    print(f"Para pagar uma casa de R${valorDaCasa:.2f} em {anos} anos a prestação será de R${prestacao:.2f} \nEmpréstimo CONCEDIDO!") 
else:
    print(f"Para pagar uma casa de R${valorDaCasa:.2f} em {anos} anos a prestação será de R${prestacao:.2f} \nEmpréstimo NEGADO!")