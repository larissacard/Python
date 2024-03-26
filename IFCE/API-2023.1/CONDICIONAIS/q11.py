peso = float(input("Informe seu peso: "))
altura = float(input("Informe sua altura: "))

imc = peso / altura **2
print(f"Seu IMC é igual a: {imc}")

if(imc < 18.5):
    print("Você está abaixo do peso.")
elif(18.5 <= imc <= 24.9):
    print("Você está com o peso normal.")
elif(25 <= imc <= 29.9):
    print("VocÊ está com sobrepeso.")
elif(30 <= imc <= 34.9):
    print("Você está com obesidade de classe 1.")
elif(35 <= imc <= 39.9):
    print("Você está com obesidade de classe 2")
else:
    print("Você está com obesidade de classe 3")