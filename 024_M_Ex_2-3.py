#!/usr/bin/env python3
#Carson Black
#024_M_Ex_2-3.py

import os

def clearConsole(): # My function to make the program easier to look at.
    if os.name == "nt":
        os.system("cls")
    else:
        os.system("clear")

clearConsole()

# get input from the user
validInput = False
while validInput == False:
    try:
        print("The Area and Perimeter program\n") # display a welcome message
        length = float(input("Enter length: ")) # attempt to get user input
        width = float(input("Enter width : "))
        validInput = True # set variable to true in case of valid inputs being received (float or int, no string allowed as it cannot be cast to a float)
    except ValueError:
        input("Invalid input. Press enter to try again...")
        clearConsole()

# calculate area and perimeter
area = length * width
perimeter = 2*length + 2*width

# format and display the result
print()
print(f"Area: {area} square units")
print(f"Perimeter: {perimeter} units")

print("\nVisual representation:\n")

if length < 3: # defining variable spacer for the math below
    spacer = 3
else:
    spacer = 2

print(" " * int(length/(4-spacer)+(length/spacer)), int(length), sep="")
for i in range(int(width)):
    if i == 0:
        print("▓" * int(length) * 2, sep="", end="") # first line doesn't put \n at the beginning.
    else:
        print("\n", "▓" * int(length) * 2, sep="", end="") # prints 2 for every length because the boxes are about half as wide as they are tall.
    if i == int(width//2):
        print(" ", int(width), sep="", end="") # prints the width about halfway down the side of the box

print("\n")
input("Bye!")
clearConsole()