# Title: Lab7A2
# Author: Nicholas Arvo
# Purpose: This program will drop a pattern of dots representing the layout of setup bowling pins.

from turtle import Turtle

def main():
    # Initial setup
    Donatello = Turtle()
    Donatello.pencolor("purple")
    Donatello.shape("turtle")
    Donatello.up()
    
    # Position Turtle under first dot location (50 units under). Face upwards.
    Donatello.goto(0,-200)
    Donatello.left(90)

    # How many dots to drop in each dropRow function. Will decrement with each loop iteration below.
    dotCount = 4
    
    # Drop rows
    for count in range(4):
        dropRow(Donatello,dotCount)
        # Subtract 1 for next row
        dotCount -= 1
    # Return to beginning location
    Donatello.goto(0,-200)
    
def dropRow(turtle,dots):
    turtle.forward(50)
    firstPos = turtle.position()
    # drop size 20 dots
    for count in range(dots):
        turtle.dot(20)
        turtle.right(90)
        turtle.forward(50)
        turtle.left(90)
        turtle.forward(50)
        
    # Return to starting location and move to new row location
    returnToStart(turtle,firstPos)
        
def returnToStart(turtle,initialPosition):
    # Move 50 units to the left and 50 unit upwards for new first dot location
    turtle.goto(initialPosition)
    turtle.left(90)
    turtle.forward(50)
    turtle.right(90)
    return

if __name__ == "__main__":
    main()
