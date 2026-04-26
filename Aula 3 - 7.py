#Programa que calcula e exibe o salário reajustado de um funcionário.
#Percentual de aumento: Até R$ 300,00 - 35% / Acima de R$ 300,00 - 15%

salario = float(input("Digite o salário do funcionário: "))

if salario <= 300:
    aumento = 0.35
else:
    aumento = 0.15

salario_reajustado = salario * (1 + aumento)
print(f"Salário reajustado: R${salario_reajustado:.2f}")

input()