peso_anterior = int(input('Informe seu peso de 3 meses atras: '))
peso_atual = int(input('Informe seu peso mais atual: '))

diferenca = ((peso_atual - peso_anterior) / peso_anterior) * 100

if(diferenca >= 0):
    print(f'Houve um aumento de {diferenca}% no seu peso.')
else:
    print(f'Houve uma diminuição de {diferenca}% no seu peso.')