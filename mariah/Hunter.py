#setup
import turtle
turtle.setup(width = 800, height = 1500, startx = 0, starty = 0)
window = turtle.Screen()

hunter = turtle.Turtle()
hunter.shape("turtle")

hunter.speed(500)
hunter.color("turquoise")
hunter.fillcolor("turquoise")
hunter.begin_fill()
hunter.circle(150)
hunter.speed(10)
hunter.penup()
hunter.end_fill()
hunter.left(95)
hunter.forward(300)
hunter.pendown()


hunter.color("hot pink")
hunter.fillcolor("hot pink")
hunter.begin_fill()
hunter.circle(75)
hunter.penup()
hunter.end_fill()
hunter.right(95)
hunter.forward(60)
hunter.right(95)
hunter.pendown()
hunter.begin_fill()
hunter.circle(75)
hunter.end_fill()

