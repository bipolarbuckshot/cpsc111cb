#!/usr/bin/env python3
#Carson Black
#Module_8_Project_Carson_Black.py


import sys # For sys.exit later on
import os # To check os type in order to clear the console



def clearConsole(): # function to clear the console when called.
    if os.name == "nt": # nt is Windows
        os.system("cls")
    else:               # everything else can be assumed to be either MacOS or Linux.
        os.system("clear")



def numValidCheck(numGuess):
    while 1: # Endless loop until return
        value = input(numGuess) # Variable to store user input
        if value.lower() == "quit":
            if exitGame(): # If user inputs "quit", then it will call the exitGame function, which must evaluate to True to continue through to sys.exit().
                sys.exit() # If we get a return, input was received as "y" and program is ended.
            else:
                continue
        if value.isdigit(): # isdigit method checks to ensure value is, in fact, digit (made up of 0-9)
            num = int(value)
            if num >= 1 and num <= 100: # If number is >= 1 and also <= 100, it returns the numberto the play function, where it was called from.
                return num
        print("Type a number from 1 to 100 or type \"quit\" to exit the game.")



def guessValidCheck(numGuess):
    # This is the exact same code as above, but with a different print line at the end, intended for the guesser this time around.
    while 1:
        value = input(numGuess)
        if value.lower() == "quit":
            if exitGame():
                sys.exit()
            else:
                continue
        if value.isdigit(): 
            num = int(value)
            if num >= 1 and num <= 100:
                return num
        print("Guess a number from 1 to 100 or type \"quit\" to exit the game.")



def exitGame():
    return input("Exit game? [y/n]: ") == "y" # Returns to wherever exitGame was called and quits the program in input is "y", otherwise continues like nothing hapened.



def play(player1, player2): 
    # I figured out that you can just code it as if the first configuration of players are playing, and the code in def main() will swap them later.

    print(f"{player1}'s turn! Pick a secret number from 1 to 100 for {player2} to guess.")
    secretNum = numValidCheck(f"{player1}, enter your secret number (will be hidden)\n: ")

    clearConsole()

    guessCount = 0
    while 1:
        guess = guessValidCheck(f"{player2}, enter a guess from 1 to 100.\n: ")
        guessCount += 1 # Counts the number of guesses by increasing guessCount by 1 for each guess.
        if guess < secretNum: # I think this pretty much explains itself.
            print("Guess higher.")
        elif guess > secretNum:
            print("Guess lower.")
        else:
            if guessCount == 1:
                print(f"Correct answer. {player2} got the answer on the first try!")
            else:
                print(f"Correct answer. {player2} took {guessCount} guesses to find the number.")
                break



def main():
    print("Welcome to the most boring game ever made, brought to you by the worst coder in the world!\n\
Please have 2 of your finest victims at the ready for a soul-crushing 3 minute number guessing game!\n")
    player1 = "Player 1" # defining these so that the code above can print something decent looking.
    player2 = "Player 2" # I could have let the user enter their own name, but that just adds an unnecessary step to the setup each time.
                         # If you want to configure your name in-game, just do it here in the .py file.
    while 1: # Endless loop until player exits the game.
        play(player1, player2) # Plays the game, then switches the players and goes again.
        player1, player2 = player2, player1 # Switches sides after each round is over.



main() # Runs the entire program.