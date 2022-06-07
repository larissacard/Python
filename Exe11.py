N = int(input())
i = 0

def mdc(a,b):
    while b != 0:
        resto = a % b
        a = b
        b = resto
    return a

while i < N:
    a,b = input().split(" ")
    a = int(a)
    b = int(b)
    print(mdc(a,b))
    i = i + 1
