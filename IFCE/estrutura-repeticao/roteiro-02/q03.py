i = 0
num = int(input("Informe um número: "))
soma_pares = 0

while (num != 0):
    if(num % 2 == 0):
        soma_pares += num
        i += 1
    num = int(input("Informe um número: "))

media = soma_pares / i
print(f"A média dos números pares informados é: {media:.2f}")