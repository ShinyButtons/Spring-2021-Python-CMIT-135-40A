"""
CMIT-135-40A, Week 3: Assignment: Conditional Logic Programs, Program #2
by Jennifer C. Roy 01/31/2021

Ask the user to enter a grade percentage.
Convert the grade into a letter grade.
"""

grade = input("Enter your grade:")

try:
    percentage: float = float(grade)
    if 0 <= percentage < 60:
        print("F")
    elif 60 <= percentage < 70:
        print("D")
    elif 70 <= percentage < 80:
        print("C")
    elif 80 <= percentage < 90:
        print("B")
    elif 90 <= percentage:
        print("A")
    else:
        print("Invalid number")

except ValueError:
    print("Invalid grade")
