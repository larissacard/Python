i = 0
soma = 0
maior_num = 0
menor_num = 0
soma_pares = 0
impar = 0
num = int(input("Digite um número: "))

while (num > 0): 
    soma += num
    if(num % 2 == 0):
        soma_pares += num
    else:
        impar += 1
    
    if(num > maior_num):
        maior_num = num
    
    if(menor_num > num) or (menor_num == 0):
        menor_num = num

    num = int(input("Digite um número: "))
    i += 1


media = soma / i
percentual = impar * i / 100
media_pares = soma_pares / i

print(f"Soma dos números digitados: {soma}")
print(f"Quantidade de números digitados: {i}")
print(f"A média dos números digitados: {media:.2f}")
print(f"Maior número: {maior_num}")
print(f"Menor número: {menor_num}")
print(f"Média dos números pares: {media_pares:.2f}")
print(f"Percentua de números ímpares: {impar:.2f}")

    
    