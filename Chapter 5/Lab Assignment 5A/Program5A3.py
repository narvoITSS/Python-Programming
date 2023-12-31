# Title:        Program5A3
# Author:       Nicholas Arvo
# Purpose:      This program reads a sequence of numbers from a file and
#               determines if the values in this sequence are always going up
#               or always going down.

file = open("Lab5A35.txt", 'r')
fileInput = file.read().split()

intList = []
for values in fileInput:
    intList.append(int(values))
print("The integers in this file are:")
print(intList)

# Determine if successive values are always increasing or decreasing
# two count variables, for a series to be always increasing should be equal to length - 1
increaseCount = 0
decreaseCount = 0
index = 0

for index in range(len(intList)):
    if intList[index] is intList[-1]:
        break
    elif intList[index] < intList[index+1]:
        increaseCount += 1
    elif intList[index] > intList[index+1]:
        decreaseCount += 1

# Output Strings
print("\nGoing Up Check:", end = ' ')
if increaseCount == (len(intList) -1):
    print("Passed\nThe values in this file ARE continually increasing with each successive value.")
else:
    print("Failed\nThe values in this file ARE NOT continually increasing with each successive value.")
print("\nGoing Down Check:", end = ' ')
if decreaseCount == (len(intList) -1):
    print("Passed\nThe values in this file ARE continually decreasing with each successive value.")
else:
    print("Failed\nThe values in this file ARE NOT continually decreasing with each successive value.")

if (increaseCount != (len(intList)-1)) and (decreaseCount != (len(intList)-1)):
    print("\nThe values in this file are neither continually increasing nor decreasing throughout\nthe entire sequence.")