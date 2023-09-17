valido = False

while valido != True:
    login = input("Informe o usuário: ")
    senha = input("Informe a senha: ")

    if(login == "admin" and senha == "admin123"):
        print("\033[32m-="*20)
        print("Login realizado com sucesso!")
        print("-="*20)
        valido = True
    else:
        print("\033[31m-="*30)
        print("Login ou senha invalido(s)!. Tente novamente.")
        print("-=" * 30, '\033[m')