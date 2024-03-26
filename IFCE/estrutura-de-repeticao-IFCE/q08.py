valido = False

while valido != True:
    login = input("Informe o usuário: ")
    senha = input("Informe a senha: ")

    if(login == "admin" and senha == "admin123"):
        print("Login realizado com sucesso!")
        valido = True
    else:
        print("Login ou senha invalido(s)!. Tente novamente.")
