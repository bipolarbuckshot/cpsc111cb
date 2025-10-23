#!usr/bin/env python3
#Carson Black
#021_C_3_2_15_Lab_2_collatzs_hypothesis.py

import time

c0 = int(input("Enter an integer to be checked.\n: "))
entry = c0

steps = 0
while c0 != 1:
    if c0 % 2 == 0:
        c0 = int(c0 / 2)
    else:
        c0 = 3 * c0 + 1
    steps += 1
    print(f"intermediate value #{steps:<4}: {c0}") # Experimenting with f-strings I found online
    time.sleep(0.004 + ((steps / 750) / (c0))) # For that dramatic "wheel of fortune" effect


print(f"Steps: {steps}")

if c0 == 1:
    print(f"\nThe number {entry} works with Collatz's hypothesis.")
else:
    c0 /= 0 # Crashes the program if an impossible number occurs because I like to be funny sometimes


# Experimentation throughout the program this time.