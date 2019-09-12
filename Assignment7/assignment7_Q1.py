# find_min function definition goes here
def find_min(first,second):
    if first < second:
        return first
    elif second < first:
        return second
    elif first == second:
        return first

first = int(input("Enter first number: "))
second = int(input("Enter second number: "))

minimum = find_min(first,second)
# Call the function here
print("Minimum: ", minimum)