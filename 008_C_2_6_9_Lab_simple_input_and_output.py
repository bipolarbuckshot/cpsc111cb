#!/usr/bin/env python3
#Carson Black
#008_C_2_6_9_Lab_simple_input_and_output.py


a = float(input("Input value for a: ")) # input a float value for variable a here
b = float(input("Input value for b: ")) # input a float value for variable b here

print(a + b) # output the result of addition here
print(a - b) # output the result of subtraction here
print(a * b) # output the result of multiplication here
#print(a / b) # output the result of division here. This is commented out because I will be handling the ZeroDivisionError in experiments and I want to prevent an early error.

print("\nThat's all, folks!\n")

#---Experiments below---

print("But wait, there's more!\n")

try: # Tries to divide a by b, unless b is zero and causes an error, in which case it skips to the except line and prints.
    print(a / b)
except ZeroDivisionError:
    print("Cannot divide by zero! Run the program again and choose a new value for b.")

c = float(input("Input a value for c: "))
print(a*b**c) # This should raise b to the power of c and then multiply by a.

print()

print(int(c) * "repeated message ") # Repeats the text c times.