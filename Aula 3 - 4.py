#Programa que recebe três notas de um aluno, calcula sua média final e diz se o mesmo está aprovado ou reprovado (se sua média for maior que 5, estará aprovado).

nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))
nota3 = float(input("Digite a terceira nota: "))

media = (nota1 + nota2 + nota3) / 3
status = "Aprovado" if media >= 5 else "Reprovado"

print(f"Média final: {media:.2f}")
print(f"Status: {status}")

input()