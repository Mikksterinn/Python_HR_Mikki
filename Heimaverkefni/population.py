ar = float(input("Years: ")) # The input is the number of years in a float format.
folksfjoldi = 307357870 # Number of people at the beginning.
sek = 31536000 # Number of seconds in a year.
sek_tot = ar*sek # Total number of seconds being tested.
ar_heil = int(ar) # Changing from float to integers for the years.

if ar >= 0: # If the input of years is positive or equal to zero we do the calculation.
    sum = sek_tot/7 + sek_tot/35 - sek_tot/13 + folksfjoldi # The number of people after x years.
    summan = int(sum) # Changing from float to int.
    print("New population after ", ar_heil , " years is " , summan ) # printing the outcome.

else: # If the input is negative we print an error message.
    print("Invalid input!")
    
