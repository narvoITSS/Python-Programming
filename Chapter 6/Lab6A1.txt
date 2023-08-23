# Title:    Lab6A1
# Author:   Nicholas Arvo
# Purpose:  This program will read in lines from a file containing the number of
#           sides a shape has and the length of the equal sides. Using this information it 
#           will determine the corresponding geometric shape and calculate the area.


from math import sqrt

def square(length):
    area = length ** 2
    print("Shape: Square\nArea:", "%0.2f"%area)

def hexagon(length):
    # Area of Hexagon = ((3√3)*length^2)/2
    area = (3*sqrt(3)*(length ** 2))/2
    print("Shape Hexagon\nArea: " + "%0.2f"%area)

def octagon(length):
    # Area of Octagon = 2(x^2)(1 + sqrt(2)
    area = (2 * (length ** 2)) * (1 + sqrt(2))
    print("Shape: Octagon\nArea:", "%0.2f"%area)

def main():
    # Each line will have an integer with the number of sides that the shape 
    # has and a second value with the side length.
    file = open("Lab6A1.txt", 'r')
    for line in file:
        line = line.split()
        sideCount = int(line[0])
        sideLength = float(line[1])
        
        # 1) Print the numbers of sides AND the side length
        # 2) Call appropriate function based on readline information
        if sideCount == 4:
            print("Number of sides:", sideCount)
            print("Side Length:", sideLength)
            square(sideLength)
            print()
        elif sideCount == 6:
            print("Number of sides:", sideCount)
            print("Side Length:", sideLength)
            hexagon(sideLength)
            print()
        elif sideCount == 8:
            print("Number of sides:", sideCount)
            print("Side Length:", sideLength)
            octagon(sideLength)
            print()
        else:
            print("ERROR! Improper number of sides detected.\n")

if __name__ == "__main__":
    main()
