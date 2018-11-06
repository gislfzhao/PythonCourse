# -*- coding: utf-8 -*-
import random
import time


def print_intro():
    print("这个程序模拟两个选手A和B的某种竞技比赛".center(50))
    print("程序运行需要A和B的能力值(以0到1之间的小数表示)".center(50))
    print("=" * 70)
    time.sleep(1)


def get_inputs():
    a = eval(input("请输入选手A的能力值(0-1)："))
    b = eval(input("请输入选手B的能力值(0-1)："))
    n = eval(input("模拟比赛的场次："))
    return a, b, n


def print_sim_results(wins_a, wins_b):
    n = wins_a + wins_b
    print("竞技分析开始，共模拟{}场比赛".format(n))
    print("选手A获胜{}场比赛， 占比{:0.2%}".format(wins_a, wins_a / n))
    print("选手B获胜{}场比赛， 占比{:0.2%}".format(wins_b, wins_b / n))


def sim_games(n, leval_a, leval_b):
    wins_a, wins_b = 0, 0
    for i in range(n):
        score_a, score_b = sim_one_game(leval_a, leval_b)
        if score_a > score_b:
            wins_a += 1
        else:
            wins_b += 1
    return wins_a, wins_b


def sim_one_game(leval_a, leval_b):
    score_a, score_b = 0, 0
    serve = 'A'
    while not game_over(score_a, score_b):
        if serve == 'A':
            if random.random() <= leval_a:
                score_a += 1
            else:
                serve = 'B'
        else:
            if random.random() <= leval_b:
                score_b += 1
            else:
                serve = 'A'
    return score_a, score_b


def game_over(score_a, score_b):
    return score_a >= 15 or score_b >= 15


def main():
    print_intro()
    leval_a, leval_b, n = get_inputs()
    wins_a, wins_b = sim_games(n, leval_a, leval_b)
    print_sim_results(wins_a, wins_b)


if __name__ == '__main__':
    main()
