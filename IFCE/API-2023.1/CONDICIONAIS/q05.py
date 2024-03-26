numUm = int(input("Informe o primeiro número: "))
numDois = int(input("Informe o segundo número: "))
numTres = int(input("Informe o terceiro número: "))

soma = numUm + numDois

print(f"{numUm} + {numDois}: {soma}")

if (soma >= numTres):
    print(f"A soma {soma} dos dois primeiros número é maior ou igual que o número {numTres}")
else:
    print(f"A soma dos dois primeiros números não é maior ou igual a {numTres}")