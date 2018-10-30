# DrawClock

from datetime import *
from turtle import *


# 移动距离，但是不绘制
def skip(step):
    penup()
    forward(step)
    pendown()


# 画表盘
def draw_clock(radius):
    reset()  # 将乌龟返回初始位置
    # pendown()
    # # dot(20, "red")
    # circle(10)
    # penup()
    pensize(7)
    for i in range(60):
        skip(radius)
        if i % 5 == 0:
            forward(20)
            skip(-radius - 20)
        else:
            dot(5)  # 绘制圆点turtle.dot(直径)
            skip(-radius)
        right(6)


def mk_hand(name, length):
    reset()
    skip(-length * 0.1)
    begin_poly()    # 开始记录多边形的顶点
    forward(length * 1.1)
    end_poly()  # 停止记录多边形的顶点
    hand_form = get_poly()      # 返回记录的多边形
    '''''
    begin_poly -- 开始记录，end_poly -- 结束记录,get_poly -- 绘画记录点
    '''
    register_shape(name, hand_form)  # 给hand_form形状起名,注册一个图形


def init():
    global secHand, minHand, hurHand, printer, printer2  # 定义这三个是全局变量
    mode("logo")
    '''
    三种模式：standard，logo,world。
                turtle方向    默认运动方向
    standard:    向右（朝东）  逆时针
    logo    :    向上（朝北）  顺时针
    world -- 自定义
    '''

    mk_hand("secHand", 125)
    mk_hand("minHand", 130)
    mk_hand("hurHand", 90)
    secHand = Turtle()  # 类似于secHand = turtle (import turtle)，也是创建新的Turtle实例对象
    secHand.shape("secHand")  # 对于该turtle变量赋值形状(设置turtle的形状，默认为classic), 绘制图形
    secHand.hideturtle()
    minHand = Turtle()  # 创建一个新的Turtle实例对象
    minHand.shape("minHand")
    # minHand.hideturtle()
    hurHand = Turtle()
    hurHand.shape("hurHand")
    for hand in secHand, minHand, hurHand:
        hand.shapesize(1, 1, 3)  # 调整三根指针的粗细
        hand.speed(0)
    printer = Turtle()
    printer2 = Turtle()
    printer.hideturtle()  # 隐藏箭头
    printer2.hideturtle()
    printer.penup()


def week(t):
    day_names = ["星期一", "星期二", "星期三", "星期四", "星期五", "星期六", "星期日"]
    return day_names[t.weekday()]


def date(t):
    y = t.year
    m = t.month
    d = t.day
    return "%04d %02d %02d" % (y, m, d)


def local_time(t):
    h = t.hour
    m = t.minute
    s = t.second
    return "%02d:%02d:%02d" % (h, m, s)


# 钟表更新
def tick():
    t = datetime.today()
    second = t.second + t.microsecond * 0.000001
    minute = t.minute + second / 60.0
    hour = t.hour + minute / 60.0
    secHand.setheading(6 * second)  # 重新设置朝向，设置指针的方向角度
    minHand.setheading(6 * minute)
    hurHand.setheading(30 * hour)
    tracer(False)
    printer.hideturtle()
    printer.forward(65)  # 前进65写星期
    printer.write(week(t), align="center", font=("Courier", 14, "bold"))
    printer.back(130)  # 退后130写日期
    printer.write(date(t), align="center", font=("Arial", 16, "normal"))
    printer2.penup()
    printer2.clear()
    printer2.back(110)  # 退后30写时间
    printer2.write(local_time(t), align="center", font=("Courier", 14, "bold"))
    printer2.home()
    # write函数中可以把指定的内容进行书写
    printer.home()
    tracer(True)
    ontimer(tick, 100)  # 计时函数用来控制刷新时间。单位-毫秒


def main():
    tracer(False)  # 关闭绘画追踪，可以用于加速绘画复杂图形
    init()
    draw_clock(160)
    hideturtle()    # 隐藏turtle的形状
    tracer(True)
    tick()
    mainloop()  # mainloop则是主窗口的成员函数， 不会响应鼠标事件,与done()函数相对应
    # 开始接收鼠标的和键盘的操作。你现在就能够通过鼠标缩放以及关闭这个窗口了。


if __name__ == "__main__":
    main()

