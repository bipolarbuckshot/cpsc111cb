#!/usr/bin/env python3
#Carson Black
#017_C_3_2_9_Lab_2_the_break_statement-Stuck.py

while True:
    word = input("Enter a word: ")
    if word == "chupacabra":
        print("You've successfully left the loop.")
        break

#---Experiments below---

import time

i = 0 # increment variable
while True:
    i += 1 # increments by 1
    print(i) # prints current increment value
    time.sleep(0.01) # waits 0.01 seconds
    if i == 40: # When it reaches 40, the loop breaks
        break