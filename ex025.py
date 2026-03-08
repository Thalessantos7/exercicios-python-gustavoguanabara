# Crie um programa que leia o nome de uma pessoa e diga se ela tem “SILVA” no nome.
nomeCompleto = input("Digite seu nome completo: ").strip()

print("Você tem SILVA no nome." if "SILVA" in nomeCompleto.upper() else "Você não tem SILVA no nome.")