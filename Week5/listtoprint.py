"""
CMIT-135-40A, Week 5: Assignment - Programming with Lists, Part 1,
by Jennifer C. Roy 02/14/2021
Write a program that prints a list with all the items separated by a comma and a space, with and inserted
before the last item. For example, the above list would print 'apples, bananas, tofu, and cats'. But your
program should be able to work with any list not just the one shown above. Because of this, you will need
to use a loop in case the list to print is shorter or longer than the above list. Make sure your program
works for all user inputs. For instance, we wouldn't want to print "and" or commas if the list only contains
one item.
"""

listToPrint = []
while True:
    newWord = input("Enter a word to add to the list (press return to stop adding words) > ")
    if newWord == "":
        break
    else:
        listToPrint.append(newWord)
print(",".join(listToPrint))  # The power of Python is its rich set of functions to process strings and list of data.
