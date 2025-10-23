#!usr/bin/env python3
#Carson Black
#025_C_3_4_6_the_basics_of_lists.py

hat_list = [1, 2, 3, 4, 5]  # This is an existing list of numbers hidden in the hat.

# Step 1: write a line of code that prompts the user
# to replace the middle number with an integer number entered by the user.

hat_list[2] = int(input("Enter an integer to replace the middle number.\n: "))

# Step 2: write a line of code that removes the last element from the list.

del hat_list[4]

# Step 3: write a line of code that prints the length of the existing list.

print(f"The new length of the list is {len(hat_list)}")

print(f"The new list in order is as follows: {hat_list}")

#---Experiments below---

hat_list.insert(0, int(input("Add a value to the beginning of the list.\n: ")))
print(hat_list)