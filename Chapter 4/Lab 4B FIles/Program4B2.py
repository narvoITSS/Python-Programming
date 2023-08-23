# Title:    Program4B2
# Author:   Nicholas Arvo
# Purpose:  This program will read in two words from a line in a file. Split
#           those words into individual strings and then create a new word by
#           combining the character at an index value that iterates through
#           the total length of each strings.


fileInput = open("Lab4B2.txt", 'r')
fileStrings = fileInput.readline().split()

string1 = fileStrings[0]
string2 = fileStrings[1]
combinedString = ''

for index in range(len(string1)):
    combinedString += string1[index] + string2[index]
print(combinedString)
