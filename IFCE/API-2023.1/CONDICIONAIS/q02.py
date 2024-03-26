numero = int(input('Digite um número: '))
par_impar = numero % 2

if(par_impar == 0):
    print(f"O número {numero} é PAR!")
else:
    print(f"O número {numero} é IMPAR")