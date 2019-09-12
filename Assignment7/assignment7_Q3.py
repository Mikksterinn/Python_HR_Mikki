# The function definition goes here
def in_range(x):
    if 1 < x < 555:
        print(x,' is in range.')
    else:
        print(x, ' is outside the range!')


num = int(input("Enter a number: "))

# You call the function here
in_range(num)