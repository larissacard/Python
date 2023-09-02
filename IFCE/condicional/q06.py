ano_nascimento = int(input("Em que ano você nasceu? "))
ano_atual = int(input("Qual o ano atual? "))

idade = ano_atual - ano_nascimento

if(idade >= 18):
    print("Parabéns!! Você está apto(a) a tirar a carteira de motorista!!")
else:
    print("Poxa, você não tem a idade minima para tirar a carteira de motorista.")