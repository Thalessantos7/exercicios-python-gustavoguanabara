# Escreva um programa que pergunte o salário de um funcionário e calcule o valor do seu aumento.
# Para salários superiores a R$1250,00, calcule um aumento de 10%. Para os inferiores ou iguais, o aumento é de 15%.
salario = float(input("Seu salário: R$"))

if salario > 1250.0:
    print(f"Seu salário com um aumento de 10% fica R${salario + (salario * 10.0 / 100.0):.2f}")
else:
    print(f"Seu salário com um aumento de 15% fica R${salario + (salario * 15.0 / 100.0):.2f}")