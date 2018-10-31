# -*- coding: utf-8 -*-
import jieba
import wordcloud
import time
# from scipy.ndimage import imread
from imageio import imread as im1
from matplotlib.pyplot import imread as im2


def read_from_file(filename):
    fo = open(filename, 'r', encoding='utf-8-sig')
    t = fo.read().strip('\n')
    fo.close()
    ls = jieba.lcut(t)
    if '\n' in ls:
        for i in range(len(ls)-1, -1, -1):      # 倒序循环
            if ls[i] == "\n":
                ls.pop(i)
    print(ls)
    tt = ' '.join(ls)
    return tt


def read_from_file2(filename):
    fo = open(filename, 'r', encoding='utf-8-sig')
    ls = fo.readlines()
    ls = list(map(lambda st: st.strip(), ls))
    tt = ' '.join(ls)
    fo.close()
    return tt


def read_from_file3(filename):
    fo = open(filename, 'r', encoding='utf-8-sig')
    t = fo.read().strip('\n')
    return t.strip("\n")


def generate_wordcloud(text, filename):
    mk = im1("World.jpg")
    w = wordcloud.WordCloud(width=1100, height=700, font_path="SIMLI.TTF", min_font_size=1,
                            background_color="black")
    w.generate(text)
    store_file = filename.split('.')[0] + time.strftime("_%Y%m%d_%H%M%S", time.localtime()) + ".png"
    print(store_file)
    w.to_file(store_file)


if __name__ == '__main__':
    file_name = "2017LUP-FLUS.txt"
    txt = read_from_file3(file_name)
    generate_wordcloud(txt, file_name)
