produto_um = int(input("Informe o valor do produto: "))
produto_dois = int(input("Informe o valor do segundo produto: "))

if(produto_um < produto_dois):
    print("Você deve comprar o primeiro produto!")
elif(produto_um > produto_dois):
    print("Você deve comprar o segundo produto!")
else:
    print("Os dois produtos tem o mesmo valor. Escolha qualquer um.")
