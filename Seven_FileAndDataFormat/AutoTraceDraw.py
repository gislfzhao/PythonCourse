# -*- coding: utf-8 -*-
import turtle as t


def read_from_file(filename, path=r''):
    lists = []
    path_name = path + filename
    fo = open(path_name, 'rt', encoding='utf-8-sig') # utf-8-sig可以去除、ufeff
    # 去除换行符
    lists = list(map(lambda st: st.strip(), fo))
    # 去除引号
    lists = list(map(lambda st: list(map(eval, st.split(','))), lists))
    fo.close()
    return lists


def draw_on_data(datas):
    for data in datas:
        t.pencolor(data[3], data[4], data[5])
        t.forward(data[0])
        if data[1]:
            t.right(data[2])
        else:
            t.left(data[2])


def main():
    t.title("自动轨迹绘制")
    t.pencolor(1, 0, 0)
    t.pensize(5)
    datas = read_from_file('data.txt')
    draw_on_data(datas)
    t.hideturtle()
    t.mainloop()


if __name__ == '__main__':
    main()
