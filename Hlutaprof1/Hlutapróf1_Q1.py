aldur = int(input('Enter your age: '))

if aldur > 0:
    if 0 < aldur < 34:
        print('Young')
    elif 34 < aldur < 50:
        print('Mature')
    elif 50 < aldur < 69:
        print('Middle-aged')
    elif aldur > 69:
        print('Old')
else: 
    print('Invalid age')