# Faça um programa que leia algo pelo teclado e mostre na tela o seu tipo primitivo e todas as informações possíveis sobre ele.
a = input("Digite algo: ")

print(f"""Tipo primitivo: {type(a)}
É um número? {a.isnumeric()}
É alfanumérico? {a.isalnum()}
É alfabético? {a.isalpha()}
Está em maiúsculo? {a.isupper()}
Está em minúsculo? {a.islower()}
Está capitalizada? {a.istitle()}
Só tem espaços? {a.isspace()}""")