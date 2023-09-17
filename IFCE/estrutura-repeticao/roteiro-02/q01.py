cont_negativos = 0

for num in range(5):
    numero = int(input("Informe um valor qualquer: "))
    if(numero < 0):
        cont_negativos += 1
print(f"O total de números negativo é: {cont_negativos}")