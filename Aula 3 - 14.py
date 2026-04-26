#Programa que recebe o preço de um produto, calcula e mostra, de acordo com as tabelas a seguir, o novo preço e a classificação.
#Tabela 1(Percentual de aumento) / Preço - Até R$ 50,00 - 5%; Entre R$ 50,00 E R$ 100,00 - 10%; Acima de R$ 100,00 - 15%
#Tabela 2(Classificações) / Novo Preço - Até R$ 80,00 - Barato; Entre R$ 80,00 e R$ 120,00 (inclusive) - Normal; Entre R$ 120,00 e R$ 200,00 (inclusive) - Caro; Maior que R$ 200,00 - Muito caro.

preco = float(input("Digite o preço do produto: "))

if preco <= 50:
    aumento = 0.05
elif preco <= 100:
    aumento = 0.10
else:
    aumento = 0.15

novo_preco = preco * (1 + aumento)

if novo_preco <= 80:
    classificacao = "Barato"
elif novo_preco <= 120:
    classificacao = "Normal"
elif novo_preco <= 200:
    classificacao = "Caro"
else:
    classificacao = "Muito caro"

print(f"Novo preço: R${novo_preco:.2f}\nClassificação: {classificacao}")

input()