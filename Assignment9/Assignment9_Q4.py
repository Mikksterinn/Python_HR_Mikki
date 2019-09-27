# Here is the definition of safe_input. It should contain this exception:
def safe_input(prompt, a_type):
    value = input(prompt)
    while True:
        try:
            safe_input = a_type(value)
            return safe_input
            

        except ValueError:
            print("Error: please enter a value of", a_type)
            value = input(prompt)
    

        

# Do not change the lines below
print(safe_input('Please enter an integer: ', int))
print(safe_input('Please enter a float: ', float))
print(safe_input('Please enter a string: ', str))
