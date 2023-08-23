# Title:    Program4A1
# Author:   Nicholas Arvo
# Purpose:  Checks two words entered by the user against each other to
#           determine if the words share the same first and last letter.
#           additionally checks if the 2nd word is contained
#           inside the first word. Print corresponding output to user.

print("Please begin by entering two words.")

word1 = input("Enter the 1st word: ")
word2 = input("Enter the 2nd word: ")

# compairing first and last letters of the strings
if word1[0] == word2[0] and word1[-1] == word2[-1]:
    print("These two words share a common first and last letter.")
else:
    print("These two words do not share a common letter in their first and last letters.")

# check if word2 is inside word1
if word2 in word1:
    print("The second word \"" + word2 + "\" is contained in the first word \"" + word1 + "\".")
else:
    print("The second word \"" + word2 + "\" is NOT contained in the first word \"" + word1 + "\".")
        