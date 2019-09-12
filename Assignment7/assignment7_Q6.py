# Your function definition goes here
def fibo(n):
    num_1 = 1
    num_2 = 0
    counter = 1
    while counter <= n:
        sum = num_1 + num_2
        num_1 = num_2
        num_2 = sum
        print(sum, end=' ')
        counter += 1



n = int(input("Input the length of Fibonacci sequence (n>=1): "))
# Call your function here        
fibo(n)