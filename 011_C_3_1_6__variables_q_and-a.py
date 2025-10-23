#!/usr/bin/env python3
#Carson Black
#011_C_3_1_6__variables_q_and-a.py


n = int(input("Type a number\n: "))
print(n >= 100)

#---Experiments below---

print()

finish = False
while finish == False: # Loop to keep testing numbers until a number >= 100 is given
    try:
        n = int(input("Type another number.\n: "))
        if n >= 100:
            print("The number entered is at least 100.")
            finish = True # Breaks the loop
        else:
            print("The number entered is less than 100.\n")
    except ValueError: # If a float is entered, this code is run.
        print("Invalid response! Please enter an integer.\n")