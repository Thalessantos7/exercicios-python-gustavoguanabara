# Escreva um programa que leia um valor em metros e o exiba convertido em centímetros e milímetros.
m = float(input("Digite um valor em metros: "))
cm = m * 100
mm = m * 1000

print(f"{m}m em cm = {cm:.0f}cm \n{m}m em mm = {mm:.0f}mm")