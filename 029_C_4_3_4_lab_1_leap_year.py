#!/usr/bin/env python3
#Carson Black
#029_C_4_3_4_lab_1_leap_year.py


import os
if os.name == "nt": os.system("cls")
else: os.system("clear")
# Makes console much less cluttered and also makes me happy :)


def is_year_leap(year):
    return \
        year % 400 == 0 \
        or \
        ( year % 100 != 0 and year % 4 == 0 )
# If year is divisible by 400, return True. Or, if it is divisible by 4 and not 100, return True.
# If the conditions aren't met (a number that is not divisible by 400, and not by 4 excliding multiples of 100), returns False.

print()

test_data = [1900, 2000, 2016, 1987]
test_data.append(int(input("Enter an additional number to test: "))) # Asks for an additional number to run through the program

test_results = [False, True, True, False]
test_results.append(is_year_leap(test_data[-1])) # Runs the user input through the function to determine whether or not it is a leap year.

print()
print("Test Data:    ", test_data) # Prints test data for debugging purposes
print("Test results: ", test_results) # Same with results
print()

for i in range(len(test_data)):
    yr = test_data[i]
    print(yr,"->",end="")
    result = is_year_leap(yr)
    if result == test_results[i]:
        print("OK")
        if result == True: print ("Leap year")
        else: print("Not a leap year") 
    else:
        print("Failed")

print()

# Experiments on lines 6, 7, 8, 20, 23, 26, 39, 40, 44