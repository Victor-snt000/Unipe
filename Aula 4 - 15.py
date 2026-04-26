#Programa que lê um número e informa se ele é positivo, negativo ou zero.

num = float(input("Digite um número para verificar se é positivo, negativo ou zero: "))
print("Positivo" if num > 0 else "Negativo" if num < 0 else "Zero")

input()