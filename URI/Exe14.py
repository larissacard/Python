E,F,C = input().split(' ')
E = int(E)
F =  int(F)
C = int(C)

gvazia = E + F
consu = 0

while gvazia >= C:
    gvazia = gvazia - C
    consu = consu + 1
    gvazia = gvazia + 1
print(consu)
