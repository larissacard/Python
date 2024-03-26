############################## Usando listas ##############################
cont = 200
multiplo_sete = []

for i in range(cont):
    if(i < 200) and (i % 7 == 0):
        multiplo_sete.append(i)       
print("Os números multilos de 7 menor que 200 são:\n", multiplo_sete)

############################## Sem listas ##############################

for i in range(cont):
    if (i % 7 == 0):
        print(f"{i} é multiplo de 7.")


############################## Usando parametros aceitos pelo range ##############################
#range(start, stop, step)
for numero in range(0, cont, 7):
    print(numero)