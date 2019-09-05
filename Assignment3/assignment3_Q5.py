n = int(input("Input a natural number: "))
counter = 2
prime = 0
while 1 < counter <= n:
    if n%counter == 0 and counter != n:
        prime+=1
    
    counter += 1

if prime == 0 and n > 1:
    print('Prime')
else:
    print('Not prime')