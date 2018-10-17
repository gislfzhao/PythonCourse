# Draw Seven Digital Tubes
import time
import turtle


def draw_gap():     # draw the gap between the lines
    turtle.penup()
    turtle.forward(5)


def draw_line(draw):    # draw the line of digit
    draw_gap()
    turtle.pendown() if draw else turtle.penup()
    turtle.forward(35)
    draw_gap()
    turtle.right(90)


def draw_digit(digit):  # draw the digit
    # draw the top of digit
    draw_line(True) if digit in ['2', '3', '4', '5', '6', '8', '9'] else draw_line(False)
    draw_line(True) if digit in ['0', '1', '3', '4', '5', '6', '7', '8', '9'] else draw_line(False)
    draw_line(True) if digit in ['0', '2', '3', '5', '6', '8', '9'] else draw_line(False)
    draw_line(True) if digit in ['0', '2', '6', '8'] else draw_line(False)
    turtle.left(90)
    # draw the upper of digit
    draw_line(True) if digit in ['0', '4', '5', '6', '8', '9'] else draw_line(False)
    draw_line(True) if digit in ['0', '2', '3', '5', '6', '7', '8', '9'] else draw_line(False)
    draw_line(True) if digit in ['0', '1', '2', '3', '4', '7', '8', '9'] else draw_line(False)
    # prepare to draw the next digit
    turtle.left(180)
    turtle.penup()
    turtle.forward(20)


def draw_date(date):    # draw the digits of date
    for i in date:
        draw_digit(i)


def get_localtime():    # get the string of the local time
    return time.strftime("%Y%m%d%H%M%S", time.localtime())


def main():
    turtle.speed(0)
    turtle.penup()
    turtle.forward(-300)
    turtle.pensize(4)
    turtle.hideturtle()
    turtle.done()


main()
