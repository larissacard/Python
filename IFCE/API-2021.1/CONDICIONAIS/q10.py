consumo_veiculo = float(input("Informe quanto seu veiculo consome de gasolina por km: "))
preco_gasolina = float(input("Qual o valor da gasolina? "))
distancia = float(input("Informe a distancia da viagem: "))
orcamento = float(input("Informe o seu orçamento para essa viagem: "))

valor_gasto = (distancia / consumo_veiculo) * preco_gasolina

if(valor_gasto > orcamento):
    print(f"Não será possível realizar a viagem, pois o valor a ser gasto ultrapassará o orçamento em {valor_gasto - orcamento} reais")
else:
    print("Você poderá viajar com o seu orçamento.")