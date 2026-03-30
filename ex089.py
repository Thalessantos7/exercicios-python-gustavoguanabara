# Crie um programa que leia nome e duas notas de vários alunos e guarde tudo em uma lista composta.
# No final, mostre um boletim contendo a média de cada um e permita que o usuário possa mostrar as notas de cada aluno individualmente.
lista = []

while True:
    nome = input("Nome: ").strip().title()
    nota1 = float(input("Primeira nota: "))
    nota2 = float(input("Segunda nota: "))

    lista.append([nome, nota1, nota2])

    continuar = input("Quer continuar [S/N]? ").strip().upper()

    if continuar == "N":
        break

print(f"\nNo. {"NOME":10} {"MÉDIA":10}")
print("-" * 20)

for i in range(len(lista)):
    media = (lista[i][1] + lista[i][2]) / 2
    print(f"{i} {lista[i][0]:2} {media:.1f}")

print("-" * 20)

while True:
    verNotas = int(input("Quer ver as notas de qual aluno [999 interrompe]? "))

    if verNotas == 999:
        break

    print(f"Notas de {lista[verNotas][0]} são: \nNota 1: {lista[verNotas][1]:.1f} \nNota 2: {lista[verNotas][2]:.1f}")
    print("-" * 20)