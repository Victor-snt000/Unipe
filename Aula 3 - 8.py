#Programa que solicita a idade de um atleta e define sua categoria.

idade = int(input("Digite a idade do atleta: "))

if 5 <= idade <= 10:
    categoria = "Infantil"
elif 11 <= idade <= 15:
    categoria = "Juvenil"
elif 16 <= idade <= 20:
    categoria = "Júnior"
elif 21 <= idade <= 25:
    categoria = "Profissional"
else:
    categoria = "Idade fora das categorias previstas"

print(f"A categoria do atleta é: {categoria}")

input()