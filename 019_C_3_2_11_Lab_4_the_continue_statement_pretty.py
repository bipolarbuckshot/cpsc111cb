#!usr/bin/env python3
#Carson Black
#019_C_3_2_11_Lab_4_the_continue_statement_pretty.py

# Prompt the user to enter a word
# and assign it to the user_word variable.

user_word = input("Enter a word: ")

user_word = user_word.upper()

word_without_vowels = ""

for letter in user_word:
    if letter in "AEIOU":
        continue # If a vowel is detected at the current position, skip and rerun the loop for the next letter.
    word_without_vowels += letter # Concatenates each letter to the word to build the vowel-less word.
print(word_without_vowels)

#---Experiments below---

print("\n-----\n") # Divider for console readability

user_word = input("Enter another word: ") # Ask for another word for the below code to use

word_without_vowels = ""

for letter in user_word:
    if letter in "AEIOUaeiou": # Added lowercase letters as well.
        continue # If a vowel is detected at the current position, skip and rerun the loop for the next letter.
    word_without_vowels += letter # Concatenates each letter to the word to build the vowel-less word.
print(word_without_vowels)

# This should print the word as typed, with capitals and lowercase intact.