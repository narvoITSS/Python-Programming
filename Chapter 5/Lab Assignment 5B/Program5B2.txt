# Title:    Program5B2
# Author:   Nicholas Arvo
# Purpose:  This program prompts the user to provide a new name for a variable. 
#           From there it checks if that input meets the criteria for legal variable names
#           in Python. The result of these checks are printed out to the user, including when 
#           necessary what criteria the provided name fails under Python's naming guidelines.

# Read a set of words in from the text file, Lab5B2.txt, and put it into a tuple named reservedWords
reservedWordsList = []
file = open('Lab5B2.txt', 'r')
for line in file:
    line = line.strip().split()
    for words in line:
        reservedWordsList.append(words)
reservedWords = tuple(reservedWordsList)

# Print reservedWords
print("The following are reserved words that can not be used as variable names: ")
for word in reservedWords:
    if word != reservedWords[-1]:
        print(word + ', ', end = '')
    else:
        print(word)

# ask the user to enter a variable name
userVariable = input("\nPlease enter a valid name for a new variable: ")

# Flag variables used to represent if userVariable is a valid input
flagReservedWord = False
flagLeadingNumber = False
flagIllegalChar = False

# 1) Valid variables can not be: a reserved word
if userVariable in reservedWords:
    flagReservedWord = True
    print("ERROR! Your variable can not be named a Python reserved word.")

# 2) Valid variables can not: start with a number
if userVariable[0].isnumeric():
    flagLeadingNumber = True
    print("ERROR! Your variable can not start with a number.")   

# 3) Loop through the characters in the variable name to make sure they are allowed.
for char in userVariable:    
    # Valid variables can be: numbers, letters or underscore.    
    if char.isalnum() or char == '_':
        pass
    else:
        flagIllegalChar = True
        print("ERROR! Your variable contains an illegal character at: ", char)

# After looping through the variable name characters,
# print a statement to say if the name is valid or 
# invalid. If it’s invalid, state the reason why    

if flagReservedWord or flagIllegalChar or flagLeadingNumber:
    print("ERROR! The value '" + userVariable + "' is not a valid variable name!")
else:
    print("SUCCESS! The value '"+ userVariable + "' is a valid variable name!")