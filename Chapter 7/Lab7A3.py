# Title:    Lab7A3
# Author:   Nicholas Arvo
# Purpose:  This program will create four rows of four dots each. Every dot in the row is
#           equally spaced 50 units on both the x and y axises apart from the last. Each row begins
#           50 units above and to left of the prior row.          

from turtle import Turtle

def main():
    # Initial setup
    Leonardo = Turtle()
    Leonardo.pencolor("blue")
    Leonardo.speed("fast")
    Leonardo.shape("turtle")
    Leonardo.up()
    
    # Position Turtle under first dot location (50 units under). Face upwards.
    Leonardo.goto(0,-200)
    Leonardo.left(90)
    
    firstPos = ()
    # Drop rows
    for count in range(4):
        Leonardo.forward(50)
        firstPos = Leonardo.position()
        dropRow(Leonardo)

        # Return to starting location and move to new row location
        # Move 50 units to the left and 50 unit upwards for new first dot location
        Leonardo.goto(firstPos)
        Leonardo.left(90)
        Leonardo.forward(50)
        Leonardo.right(90)
        
    # Return to beginning location
    Leonardo.goto(0,-200)
    
def dropRow(turtle):
    # drop size 20 dots
    for count in range(4):
        turtle.dot(20)
        turtle.right(90)
        turtle.forward(50)
        turtle.left(90)
        turtle.forward(50)
        
if __name__ == "__main__":
    main()
