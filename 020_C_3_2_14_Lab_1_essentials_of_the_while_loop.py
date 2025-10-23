#!usr/bin/env python3
#Carson Black
#020_C_3_2_14_Lab_1_essentials_of_the_while_loop.py

blocks = int(input("Enter the number of blocks: "))

height = 0 # Height starts at 0
blocks_next_layer = 1 # First layer needs at least 1 block
while blocks >= blocks_next_layer:
    height += 1
#    print(height) # Used these to try and figure out how the math worked.
    blocks_next_layer += 1
#    print(blocks_next_layer)
    blocks -= height
#    print(height)
#    print()

# I had no idea how this math worked, so I had to look it up.
# Translated what I found into this code.

print("The height of the pyramid:", height)

#---Experiments below---

sum = blocks + height + blocks_next_layer # Just messing around with stuff
print(sum)
import time
while sum > 0:
    print(sum)
    time.sleep(sum/100)
    sum -= 1