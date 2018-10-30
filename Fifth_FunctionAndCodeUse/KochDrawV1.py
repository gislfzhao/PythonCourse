# Draw koch curve, V1.0
import turtle
from time import sleep


def koch(size, n):
    if n == 0:
        turtle.forward(size)
    else:
        for angle in [0, 60, -120, 60]:
            turtle.left(angle)
            koch(size / 3, n - 1)


def main_curve():
    # printer = turtle 表示创建一个turtle实例对象
    size = 600
    turtle.hideturtle()
    # turtle.tracer(False)
    turtle.penup()
    turtle.goto(-size / 2, 0)
    turtle.pendown()
    for i in range(10):
        turtle.clear()
        turtle.pendown()
        koch(size, i)
        sleep(1.0)
        turtle.penup()
        turtle.home()
        turtle.goto(-size / 2, 0)
    turtle.penup()
    turtle.done()


def main_snow_curve():
    size = 400
    n = 5
    turtle.penup()
    turtle.goto(- size / 2, size / 3)
    turtle.pendown()
    # for i in range(3):
    #     koch(size, n)
    #     turtle.right(120)
    koch(size, n)
    turtle.right(120)
    koch(size, n)
    turtle.right(120)
    koch(size, n)
    # turtle.hideturtle()
    turtle.mainloop()


if __name__ == "__main__":
    main_snow_curve()
