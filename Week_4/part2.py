"""
CMIT-135-40A, Week 4: Assignment: Programming Assignment - Loops, Part #2
by Jennifer C. Roy 02/07/2021
Write a program that prints 2^n
where n goes from 1 to 100. Print one answer per line (note: you are answering the question,
how high can you count on 100 fingers). Write your program using a 'for' loop.  Reminder '**' is the operator
for exponents, so for example 4**3 is 4 to the third power, or 4 * 4 * 4 which equals 64.
"""
# Part 2 of assignment including N^2 with counting on 100 fingers
for n in range(0, 101):
    print(2 ** n)
