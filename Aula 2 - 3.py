#Programa que recebe a base maior, a base menor e a altura de um trapézio. Também calcula e exibe sua área.

base_maior = float(input("Digite a base maior: "))
base_menor = float(input("Digite a base menor: "))
altura = float(input("Digite a altura: "))

area = (base_maior + base_menor) * altura / 2
print(f"A área do trapézio é: {area:.2f}")

input()