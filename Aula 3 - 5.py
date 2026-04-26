#Programa que verifica a validade de uma senha fornecida pelo usuário. Se o usuário digitar a senha '123456', escrever a mensagem 'Acesso liberado'. Caso contrário, escrever 'Acesso negado'.

senha = input("Digite a senha: ")

if senha == "123456":
    print("Acesso liberado")
else:
    print("Acesso negado")

input()