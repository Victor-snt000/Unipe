#Programa que recebe dois números e executa as operações listadas a seguir, de acordo com a escolha do usuário.
#Código(1 ou 2) - Informar o maior número; Código(3 ou 4) - Informar o menor número; Outros Códigos - Relatar erro de código. 

num1 = float(input("Digite o primeiro número: "))
num2 = float(input("Digite o segundo número: "))

opcao = int(input("Escolha a operação (1, 2, 3, 4): "))

if opcao == 1 or opcao == 2:
    print(f"O maior número é: {max(num1, num2)}")
elif opcao == 3 or opcao == 4:
    print(f"O menor número é: {min(num1, num2)}")
else:
    print("Erro: Código inválido.")

input()