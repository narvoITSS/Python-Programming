# Title:    Program5B1
# Author:   Nicholas Arvo  
# Purpose:  This program reads and stores information from a file into a dictionary
#           variable containing names and associated ages. From there it takes user inputs
#           to determine: if the provided name exists in the file, how many times the provided age
#           appears in the file, and what the greatest age value in the file is.           

# create a dictionary of "name":age
personalInfo = {}
# read in values from file to dictioary.
file = open("Lab5B1.txt", 'r')
for line in file:
    line = line.strip().split()
    personalInfo[line[0]] = int(line[1])

# display dictionary
print("The names and ages in this file are: ")
for key, value in personalInfo.items():
    print(key,value) 

# ask user for a value to search for in dictionary
userName = input("\nWhat name would you like to search for in this file? ")
if userName in personalInfo.keys():
    print("SUCCESS: The name '" + userName + "' does exist in this file.")
else:
    print("ERROR: The name '" + userName + "' does not exist in this file.")

# ask user for an age and count how many times that age is in the file
userAge = int(input("\nWhat age would you like to search and count for in this file? "))
ageCount = 0
for value in personalInfo.values():
    if userAge == value:
        ageCount += 1
print("Total occurrences of the age '" + str(userAge) + "' in the file is:", str(ageCount))

# calcualte the highest age in the group
ages = tuple(personalInfo.values())
maxAge = 0
for index in range(len(ages)):
    if ages[index] > maxAge:
        maxAge = ages[index]
print("\nThe highest age in the file is:", maxAge)

