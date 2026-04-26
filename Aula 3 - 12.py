#Programa que calcula e exibe o salário reajustado de um funcionário.
#Percentual de aumento: Abaixo de R$ 300,00 - 45% / Entre R$ 300,00 e R$ 600,00 (incluindo-os) - 25% / Acima de R$ 600,00 - 15%

salario = float(input("Digite o salário do funcionário: "))

if salario < 300:
    aumento = 0.45
elif salario <= 600:
    aumento = 0.25
else:
    aumento = 0.15

salario_reajustado = salario * (1 + aumento)
print(f"Salário reajustado: R${salario_reajustado:.2f}")

input()