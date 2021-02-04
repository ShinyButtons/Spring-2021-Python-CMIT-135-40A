"""
CMIT-135-40A, Week 3: Assignment: Conditional Logic Programs, Program #3
by Jennifer C. Roy 01/31/2021

Write a program that asks for two numbers.
If the sum of the numbers is greater than 100, print "They add up to a big number" if it
is less than/equal to 100 than print "They add up to ____".
"""
num1 = input('Enter first number:')
num2 = input('Enter second number:')

# Declaring the value of two numbers
sum = float(num1) + float(num2)

# Displaying the sum output per Mr. Bostock's instructions
if sum > 100:
    print("They add up to a big number")
else:
    print(f'They add up to {sum}')
