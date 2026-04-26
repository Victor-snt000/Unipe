#Programa que lê o número de gols marcados pelo Flamengo e o número de gols marcados pelo vasco e escreve o nome do time vencedor. Caso não haja vencedor, escreve empate.

gols_flamengo = int(input("Digite o número de gols do Flamengo: "))
gols_vasco = int(input("Digite o número de gols do Vasco: "))

if gols_flamengo > gols_vasco:
    vencedor = "Flamengo"
elif gols_vasco > gols_flamengo:
    vencedor = "Vasco"
else:
    vencedor = "EMPATE"

print(f"O time vencedor é: {vencedor}")

input()