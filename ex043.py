""" Desenvolva uma lógica que leia o peso e a altura de uma pessoa, calcule seu
Índice de Massa Corporal (IMC) e mostre seu status, de acordo com a tabela abaixo:
– IMC abaixo de 18,5: Abaixo do Peso
– Entre 18,5 e 25: Peso Ideal
– 25 até 30: Sobrepeso
– 30 até 40: Obesidade
– Acima de 40: Obesidade Mórbida """
peso = int(input("Seu peso: "))
altura = float(input("Sua altura: "))
imc = peso / (altura * altura)

if imc < 18.5:
    print(f"Seu IMC é de {imc:.1f}, você está abaixo do peso.")
elif 18.5 <= imc < 25.0:
    print(f"Seu IMC é de {imc:.1f}, você está no peso ideal.")
elif 25.0 <= imc < 30.0:
    print(f"Seu IMC é de {imc:.1f}, você está com sobrepeso.")
elif 30.0 <= imc <= 40.0:
    print(f"Seu IMC é de {imc:.1f}, você está com obesidade.")
else:
    print(f"Seu IMC é de {imc:.1f}, você está com obesidade mórbida.")