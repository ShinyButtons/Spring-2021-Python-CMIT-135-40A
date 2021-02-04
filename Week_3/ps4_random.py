"""
CMIT-135-40A, Week 3: Assignment: Conditional Logic Programs, Program #3
by Jennifer C. Roy 01/31/2021

Implement a random number guessing game. The computer will pick a number at random from 0-9,
the user will be asked to guess the number.  Inform the user if they get the answer correct.
"""
from random import randint

randomNum = randint(0, 9)
try:

    gn = int(input("Guess a number between 0-9:"))
    if randomNum == gn:
        print("Ding! Ding! You're correct!")
    else:
        print("You're wrong!")
except ValueError:
    print("You didn't enter a number!")
