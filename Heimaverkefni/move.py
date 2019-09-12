# The function used to create the line of x's and o's
def position(coordinate): # Defining the function name and the input variable.
    field_range = 10
    playing_field = '' # Starting off with an empty string 
    for i in range(1, field_range+1):
        if i == coordinate:
            playing_field += 'o'
        else:
            playing_field += 'x'
    return playing_field

coordinate = int(input('Input a position between 1 and 10: '))

starting_pos = position(coordinate)

print(starting_pos)
print('l - for moving left')
print('r - for moving right')
print('Any other letter for quitting')

movement = input('Input your choice: ')

while movement == 'l' or movement == 'r':
    if movement == 'r' and coordinate < 10:
        coordinate += 1
    elif movement == 'l' and coordinate > 1:
        coordinate -= 1
    
    print(position(coordinate))
    movement = input('Input your choice: ')

print(position(coordinate))