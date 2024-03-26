tentativas = 0

while tentativas < 3:
    login = input("Digite o login: ")
    senha = input("Digite a senha: ")

    if login == "admin" and senha == "admin123":
        print("Login realizado com sucesso.")
        tentativas = 3
    else:
        print("Login ou Senha inválido(s). Tente novamente.")
        tentativas += 1

if tentativas == 3:
    print("Você realizou três tentativas de acesso. Tente novamente mais tarde.")


