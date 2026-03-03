# Crie um programa que leia o nome de uma cidade e diga se ela começa ou não com o nome “SANTO”.
cidade = input("Digite o nome de uma cidade: ").title().strip()

print(f"A cidade {cidade} começa com SANTO." if cidade[:5].upper() == "SANTO" else f"A cidade {cidade} não começa com SANTO.")