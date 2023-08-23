ano_nascimento = int(input('Informe o ano em que você nasceu: '))
ano_atual = int(input('Informe o ano atual: '))

idade = ano_atual - ano_nascimento
idade_meses = idade * 12
idade_dias = idade * 360
idade_semanas = idade * 52

print(f'A sua idade é igual a {idade} anos')
print(f'A sua idade em meses é igual a {idade_meses} meses')
print(f'A sua idade em dias é igual a {idade_dias} dias')
print(f'A sua idade em semanas é igual a {idade_semanas} semanas')