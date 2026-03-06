# Melhore o DESAFIO 61, perguntando para o usuário se ele quer mostrar mais alguns termos.
# O programa encerrará quando ele disser que quer mostrar 0 termos.
termo1 = int(input("Primeiro termo da PA: "))
razao = int(input("Razão da PA: "))
termo10 = termo1 + (10 - 1) * razao

while termo1 < termo10 + razao:
    print(termo1, end=" -> ")
    termo1 += razao
print("PAUSA")
maisTermos = int(input("Quantos termos a mais você quer [0 para parar]? "))
cont = 10 + maisTermos

while maisTermos != 0:
    termoMais = termo1 + (maisTermos - 1) * razao
    while termo1 < termoMais + razao:
        print(termo1, end=" -> ")
        termo1 += razao
    print("PAUSA")
    maisTermos = int(input("Quantos termos a mais você quer [0 para parar]? "))
    cont += maisTermos
print(f"Progressão finalizada com {cont} termos mostrados.")