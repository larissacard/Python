pessoas = int(input("Informe a quantidade de pessoas: "))
cont_idades = 0

for i in range(1, pessoas + 1):
    data_nascimento = int(input("Qual a data de nascimento? "))
    idade = 2023 - data_nascimento
    cont_idades += idade

print(cont_idades)