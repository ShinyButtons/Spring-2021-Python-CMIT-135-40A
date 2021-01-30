"""
CMIT-135-40A, Week 3: Assignment: Conditional Logic Programs, Program #1
by Jennifer C. Roy 01/29/2021

Voters rights are established by the United State Constitution and by state law. All whom are eligible, go vote.
"""
age = int(input("Question: Are you eligible to vote? Please, enter your age:"))
if age >= 18:
    status = "are of voting age."
else:
    status = "must be 18 to vote."
print("Answer: You", status, )
