# Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente de um triângulo retângulo. 
# Calcule e mostre o comprimento da hipotenusa.
catetoOposto = float(input("Cateto oposto: "))
catetoAdjacente = float(input("Cateto adjacente: "))
hipotenusa = (catetoOposto**2 + catetoAdjacente**2) ** 0.5

print(f"Comprimento da hipotenusa: {hipotenusa:.2f}")