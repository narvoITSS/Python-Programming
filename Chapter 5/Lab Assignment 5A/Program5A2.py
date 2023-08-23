# Title:        Program5A2
# Author:       Nicholas Arvo
# Purpose:      This program will generate a list of 15 integers ranging from 1 to 20. 
#               From there it will sort out the elements in the file into subsequent lists
#               based on if the value is odd or even and print respective even/odd lists to the user.

# Generate 15 rand int, store in list, print list
from random import randint
randList = []
print("Generating list of 15 random integers from 1 to 20 . . .")
for index in (range(15)):
    randList.append(randint(1,20))
print("Values:", randList)

# count the total number of odd values and print that total. 
# store odd values in a new list. print that list. Repeat for even values
oddCount = 0
oddList = []
evenCount = 0
evenList = []
for numbers in randList:
    if numbers % 2 == 0:
        evenList.append(numbers)
        evenCount += 1
    else:
        oddList.append(numbers)
        oddCount += 1
print("\nThere are " + str(evenCount) + " even integers in the random list.\nThey are:", end = ' ')
print(evenList)
print()
print("There are " + str(oddCount) + " odd integers in the random list.\nThey are:", end = ' ')
print(oddList)


