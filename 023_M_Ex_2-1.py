#!/usr/bin/env python3
#Carson Black
#023_M_Ex_2-1.py

import os

def clearConsole(): # My function to make the program easier to look at.
    if os.name == "nt":
        os.system("cls")
    else:
        os.system("clear")

clearConsole()

# display a welcome message
# print("The Miles Per Gallon program")
# print()

# get input from the user
validInput = False
while validInput == False:
    try: # handles errors described in 2-1
        print("The Miles Per Gallon program\n") # display a welcome message
        milesDriven= float(input("Enter miles driven . . . . : ")) # collect user inputs
        gallonsUsed= float(input("Enter gallons of gas used. : "))
        gallonCost = float(input("Enter cost per gallon. . . : "))
        validInput = True # set variable to true to break the loop
    except ValueError:
        input("Invalid input! Press enter to try again...")
        clearConsole()

# calculate miles per gallon
mpg = round(milesDriven / gallonsUsed, 1) # the second argument here dictates the number of decimal places it rounds to.

# calculate the total gas cost
totalCost = round(gallonsUsed * gallonCost, 1) # combined definition and rounding in one line

# calculate cost per mile
mileCost = round(totalCost / milesDriven, 1)
            
# format and display the result
print()
print(f"Miles Per Gallon: {mpg}")
print(f"Total gas cost: {totalCost}")
print(f"Cost per mile: {mileCost}")

input("\nPress enter when finished...\n")
clearConsole()