retornar = True

def intervalo(x, y):
    for i in range(x, y + 1):
        print(i)

def media(numero):
    soma = 0
    for i in range(numero):
        num = int(input("Informe o valor: "))
        soma += num
    media_de_numeros = soma / numero
    print(f"A média é igual a: {media_de_numeros} ")

def tabuada(numero):
    for i in range(1, 10 + 1):
        print(f"{numero} X {i} = {numero * i}")

while retornar:
    print("-=" * 10)
    print("Menu de opções")
    print("-=" * 10)

    print("1. Intervalo de Valores")
    print("2. Média de Números")
    print("3. Tabuada da Multiplicação")
    print("4. Sair")

    opcao = int(input("Informe o número de alguma opção acima para continuar: "))
    if(opcao == 1):
        x = int(input("Informe o primeiro valor: "))
        y = int(input("Informe o segundo valor: "))
        intervalo(x, y)
    elif(opcao == 2):
        n = int(input("Informe quantos valores devem ser lidos: "))
        media(n)
    elif(opcao == 3):
        n = int(input("Informe um número: "))
        tabuada(n)
    elif(opcao == 4):
        print("Até logo!!")
        retornar = False
    else:
        print("\033[31m-="*45)
        print("O número digitado é invalido. Por favor, escolha um dos números mostrados no menu.")
        print("-=" * 45, '\033[m')
