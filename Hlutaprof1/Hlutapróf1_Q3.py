F = int(input('First: '))
S = int(input('Step: '))

tala = F
summa = tala

while summa < 100:
    print(tala, end=' ')
    tala += S
    summa += tala
else:
    print(tala)

print('Sum of series: ',summa)