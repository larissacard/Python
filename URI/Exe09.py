N = int(input())
horas = N//3600
N %= 3600
min = N //60
N %= 60
print('{}:{}:{}'.format(horas, min, N))
