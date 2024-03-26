num = int(input("Informe um número: "))

if(num % 2 == 0):
    if(num % 10 == 0):
        print(f"O número {num} é divisivel por 2 e por 10.")
    else:
        print(f"O número {num} é divisível por 2")
elif(num % 5 == 0):
    print(f"O número {num} é divisível por 5")
else: 
    print(f"O número {num} não é divisível por 2, 5 ou 10.")