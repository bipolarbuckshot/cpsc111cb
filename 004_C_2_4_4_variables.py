#!usr/bin/env python3
#Carson Black
#004_C_2_4_4_variables.py

var = 6
account_balance = 4050.0
client_name = 'Joe Mama'
print(var, "$" + str(account_balance), client_name) # Added a dollar sign before the balance, and needed to use the account_balance variable as a string to add the $ without an error since you can't add strings and floats.

print() # separator

#print(Var) results in NameError as Var is not var.

#---Experiments below---

number_of_apples = input("How many apples?:  ") # Asks for the number of apples. You can enter a string and it will still work.
print(number_of_apples, "apples fell from the tree.")

print() # separator

var2 = 2
print(var, var2) # Prints the 2 separate var and var2 variables next to each other.
