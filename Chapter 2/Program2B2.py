# Title:    Program2B2
# Author:   Nicholas Arvo
# Purpose   Calculate the total number of trees that can fit on along a fence edge based on
#           data provided from the user.

# User inputs
fenceLength = float(input("What is the total length in feet of the back fence? "))
treeRadius = float(input("What is the radius in feet of the trees you will be planting? "))
treeType = input("What type of trees will you be planting? ")

# Calculate number of trees: fenceLength // tree diameter
numberOfTrees = fenceLength // (2 * treeRadius)

# Print output
print("The number of", treeType, "trees is", int(numberOfTrees))
