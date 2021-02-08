"""
CMIT-135-40A, Week 4: Assignment: Programming Assignment - Loops, Part #1
by Jennifer C. Roy 02/07/2021
Write a program that counts down from 10. Implement your program first with a while loop.
Now implement your program with a for loop. Include both versions in your submission file.
"""
# Part 1 of assignment including the while loop and the for loop
n = 11
while n >=1:
    n -= 1
    print(n)

for n in range(10, -1, -1):
    print(n)
