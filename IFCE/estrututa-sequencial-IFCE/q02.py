salario_fixo = int(input("Informe o valor do salário: "))
valor_vendas = int(input("Informe o valor das vendas: "))
comissao = valor_vendas * 5/100
valor_total = salario_fixo + comissao

print(f"O funcionario deve receber o valor de {valor_total} reais refente ao salario e vendas(incluindo a comissão).")