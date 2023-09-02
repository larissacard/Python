nota_um = float(input("Informe a primeira nota do aluno: "))
nota_dois = float(input("Informe a segunda nota do aluno: "))

media_artimetica = (nota_um + nota_dois) / 2

print(f"A nota do aluno é igual a {media_artimetica}.")

if(media_artimetica < 3):
    print("Aluno reprovado!")
elif(3 <= media_artimetica <= 7):
    print("Aluno terá que fazer o exame final.")
else: 
    print("Aluno aprovado!")
    