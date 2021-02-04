"""
CMIT-135-40A, Week 3: Assignment: Conditional Logic Programs, Program #1
by Jennifer C. Roy 01/29/2021

Voters rights are established by the United State Constitution and by state law. All whom are eligible, go vote.
"""


def get_input():
    return input("Question: Are you eligible to vote? Please, enter your age:")


inp = ""
while inp == "":
    try:
        inp = get_input()
        age = int(inp)
        if age >= 18:
            status = "are of voting age."
        else:
            status = "must be 18 to vote."
        print(f"Answer: You {status}")
    except ValueError:
        print("That's not a real age.")
