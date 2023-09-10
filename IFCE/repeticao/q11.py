soma_num_pares = 0
contador = 0

for numero in range(50, 82+1):
    if (numero % 2 == 0):
        soma_num_pares += numero
        contador += 1
media = soma_num_pares / contador

print(media)
