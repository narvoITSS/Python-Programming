# Title:    Program4A2
# Author:   Nicholas Arvo
# Purpose:  This program prompts the user for a sentence. Next this
#           sentence will be spliced to find the first letter
#           of each word and print this out back to the console.


userInput = input("Please enter a sentence: ")
userInput = userInput.split()

for words in userInput:
    print(words[0], end = '')
