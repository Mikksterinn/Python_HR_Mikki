# The function used to create the string of x's and the singular "o".
def position(o_coordinate): # Defining the function name and the input variable.
    FIELD_RANGE = 10 # The maximum range of the string.
    playing_field = '' # Starting off with an empty string.
    for i in range(1, FIELD_RANGE+1): # The for loop adds x's to the empty string for every number other than the o_coordinate.
        if i == o_coordinate:
            playing_field += 'o'
        else:
            playing_field += 'x'
    return playing_field # The function returns the constructed string of x's and the "o" where the "o" is in the position of the o_coordinate.
# End of function.

coordinate = int(input('Input a position between 1 and 10: ')) # The user input for the initial o_coordinate.

starting_pos = position(coordinate) # Sending the initial o_coordinate to the position function.
print(starting_pos) # Printing the initial string.

print('l - for moving left') # Printing the user instructions for the rest of the program.
print('r - for moving right')
print('Any other letter for quitting')

movement = input('Input your choice: ') # The variable used in the while loop to move the "o" either to the right or left.

while movement == 'l' or movement == 'r':
    if movement == 'r' and coordinate < 10: # The "and" statement is there to make sure the "o" doesn't go outside the range of the string.
        coordinate += 1 # if the user chooses "r" then the o_coordinate gets 1 added to it and thus the "o" shifts to the right when the string is constructed.
    elif movement == 'l' and coordinate > 1: # The "and" statement is there to make sure the "o" doesn't go outside the range of the string.
        coordinate -= 1 # if the user chooses "l" then the o_coordinate gets 1 subtracted from it and thus the "o" shifts to the left when the string is constructed.
    # If neither of the if statements are fulfilled then the o_coordinate is unchanged and the "o" doesn't move.

    print(position(coordinate)) # Sending the new o_coordinate to the position function and printing out the resulting string.
    movement = input('Input your choice: ') # Updating the movement variable which is then checked by the while loop.

print(position(coordinate)) # Printing out the final string when the user selects something other than "l" or "r".