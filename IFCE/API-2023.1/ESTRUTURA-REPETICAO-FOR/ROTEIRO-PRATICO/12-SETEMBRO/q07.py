def primo(n):
    divisiveis = 0
    for i in range(1, n + 1):
        if(n % i == 0):
            divisiveis += 1
    if(divisiveis == 2):
        print(f"O número {n} é primo.")
    else: 
        print(f"O número {n} não é primo.")

for i in range(1, 20 + 1):
    primo(i)