nome = input()
salario = float(input())
tvendas = float(input())
comissao = (tvendas * 0.15) + salario
print('TOTAL = R$ {:.2f}'.format(comissao))
