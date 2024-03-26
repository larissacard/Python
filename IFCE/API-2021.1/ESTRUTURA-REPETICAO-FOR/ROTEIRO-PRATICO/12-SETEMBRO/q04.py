i = 1

while (i <= 20):
    n = int(input("Informe um numero: "))
    
    for num in range(1, n + 1):
        print(f"{n} x {num}: {n * num}")
    i += 1