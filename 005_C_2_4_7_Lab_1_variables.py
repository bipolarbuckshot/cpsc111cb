#!usr/bin/env python3
#Carson Black
#005_C_2_4_7_Lab_1_variables.py

john = 2 # Defining variables
mary = 5
adam = 7

print(john, mary, adam, sep=", ") # Print the three values separated by a comma and a space

total_apples = john + mary + adam # Variable defined as the sum of all 3 other variables
print(total_apples)

print()

#---Experiments below---

success = False
while success == False : # While loop to keep asking for an input until a valid number is given.
    try: # Try/except to handle the type and value errors that arise from non-number inputs.
        week = input("How many weeks have they been accumulating apples?\n")
        week = float(week) * 1.0
        success = True # If the code results in no errors, success becomes true and the while loop is stopped.
    except TypeError: # If someone enters a letter or something not a number, it will run the code below.
        print("Your entry was not a number! Try again.\n")
    except ValueError:
        print("Your entry was not a number! Try again.\n")

apples_per_week = 2
print(apples_per_week, "apples are obtained per week by each person.")

john += (int(week) * apples_per_week) # john += ... is the same as john = john + ...
mary += (int(week) * apples_per_week) # These lines are adding the product of the number of weeks and the apples obtained per week to the existing john variable.
adam += (int(week) * apples_per_week)

print("John, Mary, and Adam have ", john, ", ", mary, ", and ", adam, " apples respectively.", sep="")
