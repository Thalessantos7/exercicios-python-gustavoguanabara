""" Crie um programa que leia o nome completo de uma pessoa e mostre:
– O nome com todas as letras maiúsculas e minúsculas.
– Quantas letras ao todo (sem considerar espaços).
– Quantas letras tem o primeiro nome. """
nomeCompleto = input("Digite seu nome completo: ")
nomeSeparado = nomeCompleto.split()

print(f"""Tudo maiúsculo: {nomeCompleto.upper()}
Tudo minúsculo: {nomeCompleto.lower()}
Quantas letras ao todo? {len(nomeCompleto) - nomeCompleto.count(" ")}
Quantas letras tem o primeiro nome? {len(nomeSeparado[0])}""")