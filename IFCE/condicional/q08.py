num = int(input("Informe um número: "))

if(num > 0):
    print(f"O número {num} é \033[1;33mpositivo\033[m")
elif(num == 0):
    print(f"O número {num} é \033[1mnulo\033[m")
else:
    print(f"O número {num} é \033[1;31mnegativo\033[m")