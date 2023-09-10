dentro_intervalo = 0
fora_intervalo = 0

for numero in range(10):
    valor = int(input("Informe um número qualquer: "))
    if (10 <= valor <= 50):
        dentro_intervalo += 1
    else:
        fora_intervalo += 1

print(f"Valores dentro do intervalo: {dentro_intervalo}")
print(f"Valores fora do intervalo: {fora_intervalo}")