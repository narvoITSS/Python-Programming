# Title:    Program3B2
# Author:   Nicholas Arvo
# Purpose:  This program will ask the user for two intgers. If the second
#           integer provided by the user is larger the prompt for the inputs
#           will continually loop. This program will then print out if
#           either the numbers or their respective sum and difference is evenly
#           divisble by 10.

userInt1 = 0
userInt2 = 1

while(userInt2 > userInt1 or userInt2 == userInt1):
    print("Please enter two numbers, the first should be the larger of the two.")
    userInt1 = int(input("Integer 1: "))
    userInt2 = int(input("Integer 2: "))

inputSum = userInt1 + userInt2
inputDiff = userInt1 - userInt2

if(userInt1 % 10 == 0 or userInt2 % 10 == 0):
    print("We have 10's!")
elif(inputSum % 10 == 0 or inputDiff % 10 == 0):
    print("We have 10's!")
else:
    print("No 10's here.")
