# Faça um programa que leia o nome completo de uma pessoa, mostrando em seguida o primeiro e o último nome separadamente.
nomeCompleto = input("Digite seu nome completo: ").split()

print(f"""Primeiro nome: {nomeCompleto[0]}
Último nome: {nomeCompleto[-1]}""")