"""
CMIT-135-40A, Week 4: Assignment: Programming Assignment - Loops, Part#4
by Jennifer C. Roy 02/07/2021
Extra Credit - 5 possible points - Write a program that generates the multiplication table for
numbers 1-10. Use two for loops to complete your program. You will need to put one for loop inside
of the other for loop. As an extra challenge, see if you can get the indention to look correct.
"""

for a in range(1, 11):
    for b in range(1, 11):
        c = a * b
        print(c, end=" ")
    print()
