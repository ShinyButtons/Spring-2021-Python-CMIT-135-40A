"""
CMIT-135-40A, Week 5: Assignment - Programming with Lists, Part 2,
by Jennifer C. Roy 02/14/2021
Complete the following code. Fill in the two sections of code identified in the comments.
"""

import sys

itemsInBackpack = ["book", "computer", "keys", "travel mug"]

while True:
    print("Would you like to:")
    print("1. Add an item to the backpack?")
    print("2. Check if an item is in the backpack?")
    print("3. Quit")
    userChoice = input()

    if userChoice == "1":  # Removed redundant parenthesis. See PEP-8
        print("What item do you want to add to the backpack?")
        itemToAdd = input()

        itemsInBackpack.append(itemToAdd)

    if userChoice == "2":   # Removed redundant parenthesis. See PEP-8
        print("What item do you want to check to see if it is in the backpack?")
        itemToCheck = input()

        print(f"search result:{itemToCheck in itemsInBackpack}")

    if userChoice == "3":   # Removed redundant parenthesis. See PEP-8
        sys.exit()
