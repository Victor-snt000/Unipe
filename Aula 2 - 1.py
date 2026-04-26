#Algoritmo que recebe o ano de nascimento de uma pessoa e o ano atual, calculando e mostrando a idade desta pessoa e quantos anos ela terá em 2025.

ano_nascimento = int(input("Ano de nascimento: "))
ano_atual = int(input("Ano atual: "))

print(f"Idade atual: {ano_atual - ano_nascimento} anos.")
print(f"Em 2025: {2025 - ano_nascimento} anos.")

input()