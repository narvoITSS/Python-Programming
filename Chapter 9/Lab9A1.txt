# Title:    Lab9A1
# Author:   Nicholas Arvo
# Purpose:  This program will create a class to calculate the distance between
#           to points on a graph.

def main():
    ''' i. Ask the user to input values for the x & y for both points (so they’ll be entering 4 values.)
        ii. Instantiate an object of type DistanceCalculator (you choose the variable namefor it.)
        iii. Call the method to calculate the distance
        iv. Use the __str__ method to print all the values of the object.'''
    point1 = []
    point2 = []

    print("Please enter the coordinates for the two points below.\n")
    print("Point 1:")
    point1.append(float(input("x value: ")))
    point1.append(float(input("y value: ")))
    print()

    print("Point 2:")
    point2.append(float(input("x value: ")))
    point2.append(float(input("y value: ")))
    
    testVariable = DistanceCalculator(point1[0], point1[-1], point2[0], point2[-1])
    testVariable.getDistance()
    print(testVariable)

class DistanceCalculator(object):
    '''This program will create a class to calculate the distance between
        to points on a graph.'''
    def __init__(self, input_x1, input_y1, input_x2, input_y2):
        self.x1 = input_x1
        self.y1 = input_y1
        self.x2 = input_x2
        self.y2 = input_y2
        self.distance = 0.00
    
    def __str__(self):
        '''Return a string of all instance variables with appropriate label.
        Only 2 decimal digits of precision'''
        returnString = ""
        returnString += "X1: " + str(self.x1) + ', '
        returnString += "Y1: " + str(self.y1) + ';  '
        returnString += "X2: " + str(self.x2) + ', '
        returnString += "Y2: " + str(self.y2) + '; --> '
        returnString += "the distance will be %0.2f" % (self.distance)
        return returnString

    def getDistance(self):
        from math import sqrt
        self.distance = sqrt(((self.x2 - self.x1) ** 2) + ((self.y2 - self.y1) ** 2))
        return self.distance

if __name__ == "__main__":
    try:
        main()
    except ValueError:
        print("Invalid entry detected!")