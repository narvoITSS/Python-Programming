from turtle import Turtle
def drawSquare():
    t = Turtle()
    for count in range(4):
        t.forward(100)
        t.left(90)

def drawShape(turtle,sides,len):
    """ Draws a shape with the given number of sides and side length"""
    for i in range(sides):
        turtle.forward(len)
        turtle.right(360/sides)

def radialHexagon(turtle,n,length):
    """Draws a radial patter of n hexagons with the given length"""
    for count in range(n):
        drawShape(turtle,6,length)
        turtle.left(360/n)

def main():
    T = Turtle()
    radialHexagon(T, 10, 40)
    x = T.screen.window_width() // 2
    print(x)

if __name__ == "__main__":
    main()
