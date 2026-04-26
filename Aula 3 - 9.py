#Programa que lê o código de origem de um produto e mostra sua procedência.
#Código de origem - 1 ou 2: Procedência(Sul); Código de origem - 3 ou 4: Procedência(Sudeste); Código de origem - 5 ou 6: Procedência(Norte); Código de origem - 7 ou 8: Procedência(Nordeste); Código de origem - 9 ou 10: Procedência(Centro-Oeste)

codigo = int(input("Digite o código de origem do produto: "))

if codigo == 1 or codigo == 2:
    procedencia = "Sul"
elif codigo == 3 or codigo == 4:
    procedencia = "Sudeste"
elif codigo == 5 or codigo == 6:
    procedencia = "Norte"
elif codigo == 7 or codigo == 8:
    procedencia = "Nordeste"
elif codigo == 9 or codigo == 10:
    procedencia = "Centro-Oeste"
else:
    procedencia = "Código inválido"

print(f"A procedência do produto é: {procedencia}")

input()