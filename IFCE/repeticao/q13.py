def primo(numero):
    if numero <= 1:
        return False
    # Percorrer todos os números de 2 até a raiz quadrada do número
    for i in range(2, int(numero ** 0.5) + 1):
        if numero % i == 0:
            return False
    return True


numero = int(input("Digite um número: "))

if primo(numero):
    print(f"{numero} é primo.")
else:
    print(f"{numero} não é primo.")

############################## Sem função ##############################

numero = int(input("Digite um número: "))

if numero <= 1:
    print(f"O número {numero} não é primo.")
else:
    cont_divisores = 0

    for i in range(2, int(numero ** 0.5) + 1):
        if(numero % i == 0):
            cont_divisores += 1
            break

    if(cont_divisores == 0):
        print(f"O número {numero} é primo")
    else:
        print(f"O numero {numero} não é primo.")