# Title:    Program2B3
# Author:   Nicholas Arvo
# Purpose:  This program prompts the user for 5 test grades and then returns the corresponding
#           average of those grades.

# Variables to store user input for grades
print("Please begin by entering your received grade for the following tests.")
grade1 = float(input("Test 1: "))
grade2 = float(input("Test 2: "))
grade3 = float(input("Test 3: "))
grade4 = float(input("Test 4: "))
grade5 = float(input("Test 5: "))

# Calculate average and print out to user
averageGrade = (grade1 + grade2 + grade3 + grade4 + grade5) / 5
print("Your average test grade is:", averageGrade)