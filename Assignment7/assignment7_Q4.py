# is_prime function definition goes here
def is_prime(n):
    counter = 2
    prime = 0
    while 1 < counter < n:
        if n%counter == 0:
            prime+=1
    
        counter += 1

    if prime == 0 and n > 1:
        return True
    else:
        return False

num = int(input("Input an integer greater than 1: "))
if is_prime(num) == True:
    print(num,' is a prime')
elif is_prime(num) == False:
    print(num,' is not a prime')
# Call the function here and print out the appropriate message