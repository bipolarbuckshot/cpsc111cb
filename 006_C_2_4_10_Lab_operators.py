#!/usr/bin/env python3
#Carson Black
#006_C_2_4_10_Lab_operators.py

x = 0 # Define variable x.
x = float(x) # Ensure x is stored as a float rather than a string or int.
y = (3 * x**3) - (2 * x**2) + (3 * x) - 1 # Added parentheses around each term even though order of operations would have worked it out. Improves readability.
print("y =", y) # Should print y = -1.0 or whatever the answer comes to.

x = 1
x = float(x)
y = (3 * x**3) - (2 * x**2) + (3 * x) - 1
print("y =", y)

x = -1
x = float(x)
y = (3 * x**3) - (2 * x**2) + (3 * x) - 1
print("y =", y)

#---Experiments below---

print("\nExperiments below.\n")

print("Formula is 3x^3 - 2x^2 + 3x - 1.")
calcCount = 0 # defining a variable to be incremented for each time a calculation is performed
while calcCount < 5: # loops until calcCount is not less than 5
    x = input("Enter a number to be calculated: ") # Asks for a number to be fed through the formula
    x = float(x) 
    y = (3 * x**3) - (2 * x**2) + (3 * x) - 1
    print("y =", y)
    calcCount += 1 # Increases the value of calcCount by 1 for each time the code finishes.
# The code should finish executing after 5 input/calculation/print cycles.

print("\nNext experiment:\n")

print("Input values below.")
a = float(input("x^3 * ?: "))
b = float(input("x^2 * ?: "))
c = float(input("x^1 * ?: "))
d = float(input("1 * ?: "))

y = (a * x**3) + (b * x**2) + (c * x) + d # Had to make sure all of the signs were + because I copied and pasted the line before modifying.

print("y =", y)