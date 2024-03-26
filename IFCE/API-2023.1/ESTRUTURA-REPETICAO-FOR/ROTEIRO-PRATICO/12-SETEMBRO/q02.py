i = 0
soma_salario = 0
soma_filhos = 0
salario_ate_cem = 0
salario_maior = 0
print("-="*40)
print("Caso deseje encerrar o programa informe um valor negativo em salario.")
print("-="*40)
salario = float(input("Valor do salario: "))

while (salario > 0):
    soma_salario += salario

    if(salario > salario_maior):
        salario_maior = salario
    
    if(salario <= 100):
        salario_ate_cem += 1 

    qtd_filhos = int(input("Digite o número de filhos: "))

    
    if (qtd_filhos >= 0):
        soma_filhos += qtd_filhos

    salario = float(input("Valor do salario: "))

    i += 1

media_salario = soma_salario / i
media_filhos = soma_filhos / i
per_pessoas = salario_ate_cem * i/100

print(f"A média do salário da população é: {media_salario:.2f}")
print(f"A média do número de filhos da populaçao: {media_filhos:.2f}")
print(f"Maior salario informado: {salario_maior}")
print(f"Percentual de pessoas com salário até 100,00 reais: {per_pessoas}")