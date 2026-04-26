#Programa que lê três valores inteiros A, B e C e diz se a soma de A+B é menor que C.

A = int(input("Digite o valor de A: "))
B = int(input("Digite o valor de B: "))
C = int(input("Digite o valor de C: "))

if A + B < C:
    print("A soma de A + B é menor que C")
else:
    print("A soma de A + B não é menor que C")

input()