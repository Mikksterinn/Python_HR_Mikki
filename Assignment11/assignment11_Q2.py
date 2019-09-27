
def get_list():
    a_list = input("Enter elements of list separated by commas: ").strip().split(',')
    return a_list

def even_sum(a_list):
    sum_even = 0
    for val in a_list:
        if int(val)%2 == 0:
            sum_even += int(val)
    return sum_even
# Main program starts here - DO NOT change it
a_list = get_list()
print(even_sum(a_list))
