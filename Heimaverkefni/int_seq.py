num = int(input('Enter an integer: ')) #initial input.
cumsum = 0 #Cumulative sum.
odda = 0 #Counter for odd numbers.
slett = 0 #Counter for even numbers.
num_max = 0 #Current maximum input value.

if num > 0: #Checking initial input value.
    while num > 0: #Checking the current input value.
        cumsum += num #Adding the current input value to the cumulative sum.

        if num%2 == 0: #Checking if current input value is even.
            slett += 1 #Adding to the even number counter.
        else:
            odda += 1 #Adding to the odd number counter.

        num_max = max(num_max, num) #Updating the maximum input value by compairing the current maximum to the current input value.
        print('Cumulative total: ',cumsum)
        num = int(input('Enter an integer: ')) #Updating the current input value which is then checked by the While function.

    print('Largest number: ',num_max)
    print('Count of even numbers: ',slett)
    print('Count of odd numbers: ',odda)


