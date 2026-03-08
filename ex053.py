# Crie um programa que leia uma frase qualquer e diga se ela é um palíndromo, desconsiderando os espaços. Exemplos de palíndromos:
# APÓS A SOPA, A SACADA DA CASA, A TORRE DA DERROTA, O LOBO AMA O BOLO, ANOTARAM A DATA DA MARATONA.
frase = input("Digite uma frase: ").upper().strip()
palavras = frase.split()
fraseJunta = ''.join(palavras)

if fraseJunta[::-1] == fraseJunta:
    print(f"O inverso de {fraseJunta} é {fraseJunta[::-1]} \nTemos um palíndromo!")
else:
    print(f"O inverso de {fraseJunta} é {fraseJunta[::-1]} \nNão temos um palíndromo!")