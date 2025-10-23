#!usr/bin/env python3
#Carson Black
#015_C_3_2_4_Lab_1_guess_the_number.py


secret_number = 777

print(
"""
+================================+
| Welcome to my game, muggle!    |
| Enter an integer number        |
| and guess what number I've     |
| picked for you.                |
| So, what is the secret number? |
+================================+
""")

guess = 0
num_of_guesses = 0 # Part of experiments
while guess != secret_number:
    guess = int(input("Enter an integer to try and guess the secret number.\n: "))
    if guess != secret_number:
        print("Ha ha! You're stuck in my loop!")
        num_of_guesses += 1 # Part of experiments
    else:
        print("Well done, muggle! You are free now.")

#---Experiments below---

print()

if num_of_guesses >= 10: # Self-explanatory enough, I would think
    print("Took you long enough!")
else:
    print("Looks like you've cracked the code!")