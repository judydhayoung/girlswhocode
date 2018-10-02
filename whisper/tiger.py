import turtle
tiger = turtle.Turtle()
tiger.shape("turtle")
tiger.pendown()
tiger.pendown()

tiger.fillcolor("orange")
tiger.begin_fill()
tiger.forward(150)
tiger.left(90)
tiger.forward(80)
tiger.left(90)
tiger.forward(150)
tiger.left(90)
tiger.forward(80)
tiger.end_fill()

#go back to ears

tiger.fillcolor("black")
tiger.begin_fill()
tiger.penup()
tiger.backward(80)
tiger.left(90)
tiger.pendown()

tiger.forward(40)
tiger.left(90)
tiger.forward(40)
tiger.left(90)
tiger.forward(40)
tiger.left(90)
tiger.forward(40)
tiger.end_fill()

tiger.left(90)
tiger.forward(150)

tiger.fillcolor("black")
tiger.begin_fill()
tiger.left(90)
tiger.forward(40)
tiger.left(90)
tiger.forward(40)
tiger.left(90)
tiger.forward(40)
tiger.end_fill()

