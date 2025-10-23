#!/usr/bin/env python3
#Carson Black
#Module_8_Project_Carson_Black.py


'''
I borrowed some code I wrote for my midterm for this
because it all works the way I want it to for my
intended purpose. Mostly the text coloring stuff.
I made clearConsole() for this program, and borrowed
it for my midterm. Resourcefulness is not lost on
me, at least not for now. Have fun with my terrible
little game that took me several hours to figure out
how to make!
'''


import sys # For sys.exit later on
import os # To check os type in order to clear the console


class tc: # 'tc' stands for text color. To be used with f strings.
    R = '\033[91m' # Red
    G = '\033[92m' # Green
    Y = '\033[93m' # Yellow
    B = '\033[94m' # Blue
    x = '\033[0m'  # reset code
# If you see something like {tc.R}, that means the following text inside the f-string will be printed red.
# {tc.x} resets the color back to white, or if you are one of the 4 people who use light theme, black. (probably, I wouldn't know)


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
            num = int(value) # num is easier to work with so I just did that
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
    clearConsole()
    print(f"{tc.Y}{player1}{tc.x}'s turn! Pick a secret number from 1 to 100 for {tc.G}{player2}{tc.x} to guess.")
    secretNum = numValidCheck(f"{tc.Y}{player1}{tc.x}, enter your secret number (will be hidden)\n: ")

    clearConsole()

    guessCount = 0
    while 1:
        guess = guessValidCheck(f"{tc.G}{player2}{tc.x}, enter a guess from 1 to 100.\n: ")
        clearConsole()
        guessCount += 1 # Counts the number of guesses by increasing guessCount by 1 for each guess.
        if guess < secretNum: # I think this pretty much explains itself.
            print(f"{tc.R}Guess higher.{tc.x} (Previous guess: {tc.Y}{guess}{tc.x})")
        elif guess > secretNum:
            print(f"{tc.R}Guess lower.{tc.x}  (Previous guess: {tc.Y}{guess}{tc.x})")
        else:
            if guessCount == 1:
                print(f"Correct answer. {tc.G}{player2}{tc.x} got the answer on the first try!")
                input(f"\n{tc.Y}Press enter to go back to the main menu...{tc.x}\n")
            else:
                print(f"Correct answer. {tc.G}{player2}{tc.x} took {tc.Y}{guessCount}{tc.x} guesses to find the number.")
                input(f"\n{tc.Y}Press enter to go back to the main menu...{tc.x}\n")
            break



def main():
    clearConsole()
    print(f"{tc.Y}Welcome to the most boring game ever made, brought to you by the worst coder in the world!\n\
Please have 2 of your finest victims at the ready for a soul-crushing 3 minute number guessing game!{tc.x}\n")
    players = [str(input("Enter player 1's name: ")), str(input("Enter player 2's name: "))] # Obligatory list per the rubric.
    player1 = players[0] # defining these so that the code above can print something decent looking.
    player2 = players[1] # user enters their desired name.
    while 1: # Endless loop until player exits the game.
        play(player1, player2) # Plays the game, then switches the players and goes again.
        player1, player2 = player2, player1 # Switches sides after each round is over.



main() # Runs the entire program.