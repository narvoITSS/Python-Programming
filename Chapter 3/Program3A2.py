# Title:    Program3A2
# Author:   Nicholas Arvo
# Purpose:  Prompts the user for a number and then calculates that average for
#           the sum of all integers from 1 to the input value.

# Prompt a user for the integer input
num = int(input("Enter a number greater than 1: "))

# Create a for loop to calculate the sum between and and the input
sum = 0
for count in range(1, (num+1)): 
    sum += count

# Calculate the average based on the sum and total 0terations
average = sum/count

# Print ouput with labels
print("The total from 1 to your number is: ", sum)
print("The average of this range of numbers is: ", average)