#Programa que recebe dois números e executa as operações listadas a seguir de acordo com a escolha do usuário.
#Código(1) - Média entre os números digitados, Código(2) - Diferença do maior pelo menor, Código(3) - Produto entre os números digitados, Código(4) - Divisão do primeiro pelo segundo.

num1 = float(input("Digite o primeiro número: "))
num2 = float(input("Digite o segundo número: "))

print("\n1 - Média\n2 - Diferença\n3 - Produto\n4 - Divisão")
opcao = int(input("\nEscolha a operação: "))

if opcao == 1:
    print(f"Média: {(num1 + num2) / 2:.2f}")
elif opcao == 2:
    print(f"Diferença: {abs(num1 - num2):.2f}")
elif opcao == 3:
    print(f"Produto: {num1 * num2:.2f}")
elif opcao == 4:
    if num2 != 0:
        print(f"Divisão: {num1 / num2:.2f}")
    else:
        print("Erro: Divisão por zero.")
else:
    print("Opção inválida.")

input()