numeros = []

for i in range(3):
    num = int(input("Informe um número qualquer: "))
    numeros.append(num)

ordemCresc = sorted(numeros)

print("Números em ordem crescente:")

for i in ordemCresc:
    print(i)