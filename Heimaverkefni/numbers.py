#Finds and prints all positive two digit numbers whose square of the sum of its digits is equal to the number.
#Finds and prints all positive numbers < 100 with exactly 10 divisors.

for i in range(10,99):
    i_str = str(i)
    tugur = int(i_str[0])
    tala = int(i_str[1])
    summa = tugur + tala
    if summa**2 == i:
        print(i)
