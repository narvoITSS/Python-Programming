# Title:    Program3A3
# Author:   Nicholas Arvo
# Purpose:  This program asks a user for user for 5 integer inputs
#           and prints out of these numbers are odd or even.

for count in range(5):
    userNum = int(input("Please enter an integer: "))
    if userNum % 2 == 0:
        print("This number is even. \n")
    else:
        print("This number is odd. \n")
