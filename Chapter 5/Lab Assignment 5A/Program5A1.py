# Title:    Program5A1
# Author:   Nicholas Arvo   
# Purpose:  This program will read in values from an input file, calculate
#           out a sum of the first integers in that file, then prompt the
#           user for a value to count occurences of, and prompt for another value
#           they wish to remove from the list created from the read in file.

# Read the file in
file = open("Lab5A1.txt", 'r')
fileInput = file.read().split()

# Print the numbers in the file in a list
intInput = []
for values in fileInput:
    intInput.append(int(values))
print("The values in this file are:\n", intInput)

# Print the sum of the first five numbers
sum = 0
for index in range(5):
    sum += intInput[index]
print("The sum of the first five numbers in this list is:", sum)

# Count user input in list of numbers
print("\nEnter a value that you wish to count instances of in the input file: ", end = ' ')
countValue = int(input())
count = 0
for numbers in intInput:
    if numbers == countValue:
        count += 1
print("The total occurences of '" + str(countValue) + "' is: " + str(count))    
    
# Copy values of file into a new list except for a value provided as input
print("\nEnter a value you wish to remove from the previous list: ", end = ' ')
removedValue = int(input())
intInputRevised = []
for index in range(len(intInput)):
    if intInput[index] != removedValue:
        intInputRevised.append(intInput[index])
print("The values in your new list are:\n", intInputRevised)
