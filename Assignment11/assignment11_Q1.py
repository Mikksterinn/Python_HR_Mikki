#list_to_tuple function goes here
def list_to_tuple(a_list):
    int_list = []
    for val in a_list:
        try: 
            int_list.append(int(val))

        except ValueError:
            print('Error. Please enter only integers.')
            return ()
        
    return tuple(int_list)


# Main program starts here - DO NOT change it
a_list = input("Enter elements of list separated by commas: ").strip().split(',')
a_tuple = list_to_tuple(a_list)
print(a_tuple)