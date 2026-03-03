# Escreva um programa em Python que leia um número inteiro qualquer e peça para o usuário escolher 
# qual será a base de conversão: 1 para binário, 2 para octal e 3 para hexadecimal.
num = int(input("Digite um número inteiro: "))
baseDeConversao = int(input(f"""-----Escolha qual será a base de conversão-----
[1] Binário
[2] Octal
[3] Hexadecimal
Sua escolha: """))

match baseDeConversao:
    case 1:
        print(f"O número {num} em binário fica {bin(num)}")
    case 2:
        print(f"O número {num} em octal fica {oct(num)}")
    case 3:
        print(f"O número {num} em hexadecimal fica {hex(num)}")