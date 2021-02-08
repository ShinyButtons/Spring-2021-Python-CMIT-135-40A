"""
CMIT-135-40A, Week 4: Assignment: Programming Assignment - Loops, Part#3
by Jennifer C. Roy 02/07/2021
Extend your guessing game from last week.  Write a program that picks a random number from 1-100.
Then ask the user to guess a number. Tell the user if the answer is higher or lower than the number
they guessed, or if they got the correct answer.  Allow them to guess again if they got the guess incorrect.
They should be able to guess numbers an infinite number of times until they get the correct answer, at which
point your loop will end.
To generate a number from 1-100 you will need the following code at the beginning of your program:

from random import randint
randomNum = randint(1,100)
"""

from random import randint

randomNum = randint(1, 100)

while True:
    guess = int(input("Guess a number I am thinking of from 1-100"))
    if guess == randomNum:
        print("Ding, Ding, you are a winner!")
        break
    elif guess < randomNum:
        print("Your guess is less than the correct answer. Try again.")
    else:
        print("Your guess is higher than the correct answer. Try again.")
