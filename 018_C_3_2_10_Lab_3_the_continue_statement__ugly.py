#!usr/bin/env python3
#Carson Black
#018_C_3_2_10_Lab_3_the_continue_statement__ugly.py

# Prompt the user to enter a word
# and assign it to the user_word variable.

user_word = input("Enter a word: ")

user_word = user_word.upper()

for letter in user_word:
    # Complete the body of the for loop.
    if letter in "AEIOU":
        continue
    print(letter)

#---Experiments below---

print("\n-----\n")

for letter in user_word: # Consonant eater instead
    if letter in "BCDFGHJKLMNPQRSTVWXYZ":
        continue
    print(letter)