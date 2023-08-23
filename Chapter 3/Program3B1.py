# Title:    Program3B1
# Author:   Nicholas Arvo
# Purpose:  This program is a while loop that takes user input
#           and if that input is an even number adds it to a sum
#           when the user enters '9999' the loop will exit.

userInput = 0
sum = 0

while userInput != 9999:
    userInput = (int(input("Please enter an integer: ")))
    if(userInput % 2 == 0):
        sum += userInput
print("The sum of all the even integers you entered is: ", sum)