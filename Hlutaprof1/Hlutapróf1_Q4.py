stars = int(input('Number of stars: '))

for i in range(1,stars+1):
    for j in range(0,i):
        print('*',end='')
    print()
