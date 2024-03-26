valor_no_intervalo = 0
valor_fora_intervalo = 0

for numero in range(10):
    valor = int(input("Informe um número qualquer: "))
    if (10 <= valor <= 50):
        valor_no_intervalo += 1
    else:
        valor_fora_intervalo += 1

print(f"Quantidade de valores dentro do intervalo: {valor_no_intervalo}")
print(f"Quantidade de valores fora do intervalo: {valor_fora_intervalo}")