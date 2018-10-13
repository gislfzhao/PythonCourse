# Draw Square
# import turtle
# turtle.setup(500, 500)
# turtle.pendown()
# turtle.pencolor("black")
# turtle.goto(0, 100)
# turtle.goto(100, 100)
# turtle.goto(100, 0)
# turtle.goto(0, 0)
# turtle.done()

import turtle as t
t.pensize(2)
for i in range(4):
    t.forward(100)
    t.left(90)
t.done()
