from turtle import Turtle

def main():
    t = Turtle()
    t.shape("turtle")
    t.up()

    # drop first row
    t.goto(-200,0)
    dropRow(t)
    # drop second row
    t.goto(-200,50)
    dropRow(t)

    # drop third row
    t.goto(-200,100)
    dropRow(t)

    # drop fourth row
    t.goto(-200,150)
    dropRow(t)
    
def dropRow(t):
    t.dot(20)
    t.forward(50)
    t.dot(20)
    t.forward(50)
    t.dot(20)
    t.forward(50)
    t.dot(20)
    t.forward(50)
    t.dot(20)
    t.forward(50)
     

if __name__ == "__main__":
    main()
