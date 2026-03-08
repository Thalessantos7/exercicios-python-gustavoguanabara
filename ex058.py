# Melhore o jogo do DESAFIO 28 onde o computador vai “pensar” em um número entre 0 e 10.
# Só que agora o jogador vai tentar adivinhar até acertar, mostrando no final
# quantos palpites foram necessários para vencer.
from random import randrange

print(f"""{"-=-" * 25}
Pensarei em um número entre 0 e 10. Tente adivinhar qual número eu pensei...
{"-=-" * 25}""")

palpite = int(input("Qual é seu palpite? "))
numMagico = randrange(11)
tentativas = 1

while palpite != numMagico:
    tentativas += 1
    if palpite < numMagico:
        palpite = int(input("Mais... Tente novamente. \nQual é seu palpite? "))
    else:
        palpite = int(input("Menos... Tente novamente. \nQual é seu palpite? "))
print(f"Você acertou com {tentativas} tentativas. Parabéns!")