# Faça um algoritmo que leia o salário de um funcionário e mostre seu novo salário, com 15% de aumento.
salario = float(input("Digite o salário do funcionário: "))
novoSalario = salario + (15 * salario / 100)

print(f"O novo salário do funcionário com 15% de aumento é R${novoSalario:.2f}")