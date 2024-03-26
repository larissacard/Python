tentativas = 0

while tentativas < 3:
    login = input("Digite o login: ")
    senha = input("Digite a senha: ")

    if login == "admin" and senha == "admin123":
        print("Login realizado com sucesso.")
        tentativas = 3
    else:
        print("\033[31m-="*30)
        print("Login ou Senha inválido(s). Tente novamente.")
        print("-=" * 30, '\033[m')
        tentativas += 1

if tentativas == 3:
    print("Você realizou três tentativas de acesso. Tente novamente mais tarde.")

