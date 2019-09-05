# 1. Finding and printing all positive two digit numbers whose square of the sum of its digits is equal to the number.
for i in range(10,100):
    i_str = str(i) #Converting i to a string with two string values.
    tugur = int(i_str[0]) #Converting the first digit in the number back to an integer.
    tala = int(i_str[1]) #Converting the second digit in the number back to an integer.
    summa = tugur + tala #Summing up the two digits.
    if summa**2 == i:
        print(i)


# 2.Finding and printing all positive numbers < 100 with exactly 10 divisors.
counter = 0
for i in range(1,100):
    for j in range(1,i+1):
        if i%j == 0: # Checking how many divisors the number i has.
            counter += 1
    if counter == 10:
        print(i)
    counter = 0
