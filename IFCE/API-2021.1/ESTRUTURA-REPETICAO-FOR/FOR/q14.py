print("-="*20)
print("Sequencia de Fibonacci")
print("-="*20)

termos = int(input("Quantos termos você quer mostrar?"))
t1= 0
t2 = 1
print(f"{t1} - {t2}", end="")
cont = 3

for i in range(3, termos + 1):
    t3 = t1 + t2
    print(f" -> {t3}", end='')
    t1 = t2
    t2 = t3




