# Crie um programa onde o usuário digite uma expressão qualquer que use parênteses.
# Seu aplicativo deverá analisar se a expressão passada está com os parênteses abertos e fechados na ordem correta.
pilha = []

expressao = input("Digite uma expressão: ")
erro = 0

for caractere in expressao:
    if caractere == '(':
        pilha.append(caractere)
    elif caractere == ')':
        if len(pilha) == 0:
            erro = 1
            break
        pilha.pop()

if len(pilha) != 0:
    erro = 1

if erro == 0:
    print("Os parênteses estão corretos!")
else:
    print("Os parênteses estão incorretos!")