# -*- coding: utf-8 -*-
import jieba
import wordcloud
# from scipy.ndimage import imread
from matplotlib.pyplot import imread


def read_from_file(filename):
    fo = open(filename, 'r', encoding='utf-8')
    t = fo.read().strip("\n")
    fo.close()
    ls = jieba.lcut(t)
    tt = ' '.join(ls)
    return tt


def generate_wordcloud(text):
    mk = imread("image2.jpg")
    w = wordcloud.WordCloud(width=800, height=400, max_words=50, font_path="STKAITI.TTF",mask=mk,
                            background_color="white")
    w.generate(text)
    w.to_file("report_wordcloud2.png")


if __name__ == '__main__':
    txt = read_from_file("十九大.txt")
    generate_wordcloud(txt)
