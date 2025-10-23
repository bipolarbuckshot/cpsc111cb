#!/usr/bin/env python3
#Carson Black
#016_C_3_2_7_Lab_1_essentials_of_the_for_loop.py

import time

# Write a for loop that counts to five.
    # Body of the loop - print the loop iteration number and the word "Mississippi".
    # Body of the loop - use: time.sleep(1)

for count in range(1, 6):
    print(count, "Mississipi")
    time.sleep(1)

# Write a print function with the final message.

print("Ready or not, here I come!")

#---Experiments below---

i = 0 # increment variable
while i < 4:
    i += 1
    print(i)
    time.sleep(0.25) # Just messing with time.sleep() to count to 4 over the time span of 1 second