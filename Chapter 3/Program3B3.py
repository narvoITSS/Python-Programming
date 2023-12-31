# Title:    Program3B3
# Author:   Nicholas Arvo
# Purpose:  This program will roll two dice 5 times. Each time it will
#           find the sum of the two dice and at the end print out the
#           largest sum of the dice rolls. 

from random import randint

largestSum = 0

for count in range(5):
    dice1 = randint(1,6)
    dice2 = randint(1,6)
    print("Your dice rolls are: " + str(dice1) + " and " + str(dice2))

    tempSum = dice1 + dice2
    if(tempSum > largestSum):
        largestSum = tempSum

print("The largest sum of all the dice roll pairs was: ", largestSum)