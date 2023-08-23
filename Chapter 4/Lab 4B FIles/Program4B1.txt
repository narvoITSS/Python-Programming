# Title:    Program4B1
# Author:   Nicholas Arvo
# Purpose:  This program will read in integers from a text file, parse them to look for odd values,
#           print those values, and then print the sum of all those odd values.

fileInput = open("Lab4B1.txt", 'r')
fileNumbers = fileInput.readline().split()
sumOfOddNums = 0

for values in fileNumbers:
   if int(values) % 2 != 0:
      print("This value '" + values + "' is odd!")
      sumOfOddNums += int(values)
print("The sum of all odd integers in this file is: ", sumOfOddNums)

