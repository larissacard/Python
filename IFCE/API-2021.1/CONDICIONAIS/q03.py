base = int(input('Digite o número base: '))
expoente = int(input('Digite o número expoente: '))
resultado = base ** expoente

if(resultado >= 50):
    print(f"{base} elevado a {expoente} é igual a {resultado}. Maior ou igual a 50")
else: 
    print(f"{base} elevado a {expoente} é igual a {resultado}. Menor que 50 ")