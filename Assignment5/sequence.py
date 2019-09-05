n = int(input("Enter the length of the sequence: ")) # Do not change this line

counter_int = 3
num_1 = 1
print(num_1)
num_2 = 2
print(num_2)
num_3 = 3
print(num_3)

while counter_int <= n-1:
    sum = num_1 + num_2 +num_3
    print(sum)
    counter_int += 1
    num_1 = num_2
    num_2 = num_3
    num_3 = sum
