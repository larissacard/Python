fazendas = 0
acertos_met = []
teste = 1;
while True:
    cont_met = 0
    X1, Y1, X2, Y2 = input().strip().split(' ')
    X1 = int(X1)
    Y1 = int(Y1)
    X2 = int(X2)
    Y2 = int(Y2)
    if X1 == Y1 == X2 == Y2 == 0:
        break
    fazendas += 1
    met = int(input()) 
    for i in range(met):
        X, Y = input().strip().split(' ')
        X = int(X)
        Y = int(Y)
        if X >= X1 and X <= X2 and Y <= Y1 and Y >= Y2:
            cont_met += 1
    acertos_met.append(cont_met)
for i in range(fazendas):
    print('Teste {}'.format(teste))
    print('{}'.format(acertos_met[i]))
    teste+= 1
