# Your function definition goes here
def count_case(input_string):
    c_upper = 0
    c_lower = 0
    for chr in input_string:
        if chr.isupper():
            c_upper += 1
        elif chr.islower():
            c_lower += 1
    
    return(c_upper,c_lower)


user_input = input("Enter a string: ")

# Call the function here
(upper,lower) = count_case(user_input)
print("Upper case count: ", upper)
print("Lower case count: ", lower)