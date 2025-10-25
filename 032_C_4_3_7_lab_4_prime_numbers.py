#!/usr/bin/env python3
#Carson Black
#032_C_4_3_7_lab_4_prime_numbers.py

import os
if os.name == "nt": os.system("cls")
else: os.system("clear")

def is_prime(number):
    if number <= 1: return False

    limit = int(number ** 0.5) + 1 # limit for the calculation is one above the rounded-down square root of the number
    # if you don't find a divisor below the square root, you won't find one above either

    for i in range(2, limit):
        if number % i == 0: return False
    
    return True

maximum = int(input("Enter a maximum value to check to: ")) # Enter 20 to get the expected result from the assignment

for num in range(2, maximum + 1):
    # computer starts counting at 0, entering 11 here will actually give values up to 11
    if is_prime(num):
        print(num, end=" ") # appends each value to the end of the line with a single space as a buffer
print("\n")

# Experiments on lines 5, 6, 7, 20, 22, 26