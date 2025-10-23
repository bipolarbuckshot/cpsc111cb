#!/usr/bin/env python3
#Carson Black
#013_C_3_1_11_Lab_2_essentials_of_if_else.py

income = float(input("Enter the annual income: "))

if income <= 85528 and income >= 0: # changed < to <= due to wording of the prompt "not higher than". Also added a check for income less than zero for the else statement below.
	tax = income * 0.18 - 556.02
# Write the rest of your code here.

elif income > 85528:
	tax = 14839.02 + ((income - 85528) * 0.32)
else: # This is here in case an income below 0 is entered.
	tax = 0
	print("Income entered is below 0.")

if tax < 0:
	tax = 0

tax = round(tax, 0)
print("The tax is:", tax, "thalers")

#---Experiments below---

if income == 64000 or income == 80000:
	print("You will get a tax credit for being extra awesome.")
elif income == 44444:
	print("You will receive a tax penalty for not being very awesome.")
else:
	pass
