N = int(input())
contF = 0
contM = 0

for i in range (N):
    nome, sexo = input().split()

    if sexo == 'F':
        contF += 1
    elif sexo == 'M':
        contM += 1

print('{} carrinhos'.format(contM))
print('{} bonecas'.format(contF))
