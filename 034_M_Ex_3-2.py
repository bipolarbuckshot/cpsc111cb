#!/usr/bin/env python3
#Carson Black
#034_M_Ex_3-2.py


import os
def clearConsole():
    if os.name == "nt": os.system("cls")
    else: os.system("clear")
# Clears console when called no matter the OS.


while True:
    clearConsole()
    print("The Test Scores application")   
          # display a welcome message
    print()
    print("Enter test scores")
    print("Enter 'end' to end input")
    print("======================")

# initialize variables
    counter = 0
    score_total = 0
    test_score = 0
    average_score = 0

# get test scores from the user
    while test_score != 'end':
        try:
            test_score = input("Enter test score: ")
            if int(test_score) >= 0 and int(test_score) <= 100:
                score_total += int(test_score)
                counter += 1
            elif test_score == 'end':
                break
            else:
                print(f"Test score must be from 0 through 100. "
                    f"Score discarded. Try again.")
        except ValueError:
            if test_score == 'end':
                break
            else:
                print("Integers only. Score discarded. Try again.")

    # calculate average score
    try:
        average_score = round(score_total / counter)
    except ZeroDivisionError:
        print("No scores were entered.")
        average_score = None
                    
    # format and display the result
    print("======================")
    print(f"Total Score: {score_total}"
        f"\nAverage Score: {average_score}")
    print()
    # see if the user wants to do this again
    if input("Do you want to enter more scores? (y/n): ").lower() != 'y':
        break
print()
print("Bye!")


