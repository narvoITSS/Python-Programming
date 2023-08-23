# Title: Lab7A1
# Author: Nicholas Arvo
# Purpose: This program utilizes the turtle module to draw a happy little home with a nice tree and a sunny sky.

from turtle import Turtle

def main():
    # Colors
    skyBlue = (202,236,240)
    windowBlue = (139,190,250)
    
    # Dimensions: 500x500 pixels
    t = Turtle()
    t.speed(0) # speed to fastests
    t.up()
    
    # 1) Draw Background (square)
    t.goto(-250,250)
    t.begin_fill()
    t.fillcolor(skyBlue)
    drawShape(t,4,500)
    t.end_fill()

    # 2) Draw grass
    t.goto(-250,-175)
    t.begin_fill()
    t.fillcolor("green")
    t.forward(500)
    t.right(90)
    t.forward(75)
    t.right(90)
    t.forward(500)
    t.right(90)
    t.forward(75)
    t.end_fill()
    t.right(90)
    
    # 3) Draw base (square)
    t.goto(75,-75)
    t.begin_fill()
    t.fillcolor("red")
    drawShape(t,4,100)
    t.end_fill()
    
    # 4) Draw door (rectangle)
    t.goto(115,-135)
    t.begin_fill()
    t.fillcolor("brown")
    t.forward(20)
    t.right(90)
    t.forward(40)
    t.right(90)
    t.forward(20)
    t.right(90)
    t.forward(40)
    t.right(90)
    t.end_fill()

    # 5) Draw Window 1
    t.goto(85,-115)
    t.begin_fill()
    t.fillcolor(windowBlue)
    drawShape(t,4,25)
    t.end_fill()

    # 6) Draw Window 2
    t.goto(140,-115)
    t.begin_fill()
    t.fillcolor(windowBlue)
    drawShape(t,4,25)
    t.end_fill()
    

    # 7) Draw Attic
    t.goto(125,25)
    t.right(60)
    t.begin_fill()
    t.fillcolor("brown")
    drawShape(t,3,125)
    t.end_fill()
    t.right(180)

    # 8) Draw Attic Window
    t.left(60)
    t.goto(125,-15)
    t.begin_fill()
    t.fillcolor(windowBlue)
    t.circle(20)
    t.end_fill()
    
    # 9) Draw Sun (circle)
    t.goto(-150,220)
    t.right(60)
    t.begin_fill()
    t.fillcolor("yellow")
    t.circle(45)
    t.end_fill()
    
    # 10) Draw Tree Trunk (rectangle)
    t.goto(-125,-175)
    t.setheading(0)
    t.begin_fill()
    t.fillcolor("brown")
    t.left(90)
    t.forward(75)
    t.right(90)
    t.forward(25)
    t.right(90)
    t.forward(75)
    t.right(90)
    t.forward(25)
    t.end_fill()
    
    # 11) Draw Leaves (hexagon)
    t.home()
    t.goto(-135,-45)
    t.begin_fill()
    t.fillcolor("green")
    drawShape(t,6,45)
    t.end_fill()

    t.goto(-250,250)

def drawShape(turtle, side_number, length):
    turtle.down()
    for count in range(side_number):
        turtle.forward(length)
        turtle.right(360/side_number)
    turtle.up()
    
if __name__ == "__main__":
    main()

