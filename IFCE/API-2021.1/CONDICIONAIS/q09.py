nota_um = float(input("Informe a primeira nota do aluno: "))
nota_dois = float(input("Informe a segunda nota do aluno: "))

media = ((nota_um * 2) + (nota_dois * 3)) / 5

print(media)
if(media >= 7):
    print("O aluno foi aprovado!!")
else: 
    print("O aluno foi reprovado.")