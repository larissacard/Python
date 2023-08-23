def arremessos():
    pontos = 0

    for a in range(3):
        arremesso = input().split()
        x = int(arremesso[0])
        d = int(arremesso[1])
        pontos += x * d
    return pontos



N = int(input())

for i in range(N):
    pJoao = arremessos()
    pMaria = arremessos()

    if pJoao > pMaria:
        print('JOAO')
    else:
        print('MARIA')
