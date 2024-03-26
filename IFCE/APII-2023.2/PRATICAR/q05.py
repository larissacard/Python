def dosagem_em_mg(peso):
    if(peso == 5 or peso == 9):
        dosagem = 120
    elif(peso == 9.1 or peso == 16):
        dosagem = 200
    elif(peso > 16):
        dosagem = 400
    return dosagem

def calcular_gotas(dosagem):
    qtd_mg = peso * dosagem
    qtd_ml = qtd_mg / 500
    qtd_gotas = qtd_ml * 20
    return qtd_gotas
    
peso = float(input('Informe o peso da criança: '))
print(f"A quantidade correta de gotas para criança é: ",calcular_gotas(dosagem_em_mg(peso)))