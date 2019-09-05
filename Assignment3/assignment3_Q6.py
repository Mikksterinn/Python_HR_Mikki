counter = 10
while counter < 99:
    square=counter**2
    if square < 1000 and square%100 == counter:
        print('Talan er: ', counter)
    
    counter += 1
