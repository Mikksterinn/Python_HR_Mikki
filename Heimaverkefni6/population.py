def open_file(filename):
    ''' Opens file if it excists.'''
    
    try:
        file = open(filename,'r')
        return file
    
    except IOError:
        print('Filename ', filename, 'not found!')


def get_year(file_object):
    '''Creates a list of available years in the file.'''
   
    years = file_object.readline().strip().split() # Extracting the first line out of the file and storing it as a list.
    return years


def input_year(years): # The intake of the function is the first line in the file. Extracted with 'get_year' function.
    '''Asks the user to input a year and checks if it is valid.'''
    
    input_year = input('Enter year: ') # Prompting the user to input a year.
    counter = -1 # Counter used later to fetch the numbers for the selected year out of the sorted list. Starts at -1 because the first object in the 'years' list is 'States'.
    
    while True:
        for value in years: 
            if value == input_year: # Compairing the objects in 'years' list with the user input.
                
                return counter # If true the while loop ends and the function returns the counter which is also the index of the selected year.
            
            counter += 1 # Updating counter for each object in 'years' list.
        
        print('Invalid year!') 
        counter = -1 # Resetting counter if user input is invalid.
        input_year = input('Enter year: ') # Prompting user again if previous input is invalid.


def create_unsorted_list(file_object, years):
    '''Creates unsorted list'''
    
    default_line_length = len(years)
    unsorted_list = [] # Each line of the file will be added to this list as a list.
    
    for line in file_object:
        line = line.strip().split() # Making line into a list.
        
        if len(line) != default_line_length: # If the length of the current line is longer than the default length the state name has two words.
            line[0:2] = [' '.join(line[0:2])] # Joining the two words into one string.
            unsorted_list.append(line) # Adding line to unsorted_list as a list object.
        
        else:
            unsorted_list.append(line) # Adding line to unsorted_list as a list object.
    
    return unsorted_list


def sort_list(unsorted_list, years):
    '''Takes unsorted list and sorts into list of tuples:(population, State) for each year.'''
    sorted_list = []
    list_per_year = []
    
    for index in range(1, len(years)): # The index is used to find the population number for each year in every list in unsorted_list.
        for val in unsorted_list:
            list_per_year.append(tuple([int(val[index]),val[0]])) # Creating the list of tuples for currently indexed year.
        
        sorted_list.append(list_per_year) # Appending the list of tuples for each year to sorted_list.
        list_per_year = [] # Resetting the list_per_year before the index changes.
    
    return sorted_list

def main():
    filename = input('Enter filename: ') # Prompting user to input filename.
    file_object = open_file(filename)
    years = get_year(file_object)
    counter = input_year(years)
    unsorted_list = create_unsorted_list(file_object, years)
    sorted_list = sort_list(unsorted_list,years)
    
    user_selected_list = sorted(sorted_list[counter]) # Using counter from 'input_year' function as index to find the sorted list for user selected year and sorting it from lowest popualtion to highest.

    print('Minimum: ', user_selected_list[0]) # Lowest population tuple is the first object in user_selected_list.
    print('Maximum: ', user_selected_list[-1]) # Highest population tuple is the last object in user_selected_list.
    
main()