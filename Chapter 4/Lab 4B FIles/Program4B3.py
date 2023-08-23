# Title:    Program4B3
# Author:   Nicholas Arvo
# Purpose:  This program will read an unknown number of names from a file.
#           Take this information and display out first name, initial, and last name.

inputFile = open("Lab4B3.txt", 'r')

for line in inputFile:
    line = line.strip().split(',')
    name = line[1] + line[2] + ". " + line[0]
    print(name.strip())
