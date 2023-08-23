import turtle as t
def drawSquare(t,x,y,length):
	t.up()
	t.go(x,y)
	t.setheading(270)
	t.down()
	for count in range(4):
		t.forward(length)
		t.left(90)
		

