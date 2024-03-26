n = int(input("Informe um número: "))

if(n == 0):
    print("Esse número não é valido. Tente novamente!")
else:
    for i in range(1, n + 1):
        S = 1 + 1/i
        i += 1
    print(f"S = {S}")