# !/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time : 2021/10/4 10:13
# @Author : qingwei.han

# 题目1：给定字典dict，如何对字典中的值进行排序，得到排序后的字典
import random

student_names = ['jerry', 'summer', 'rick', 'morty']

original_dict = {name: random.randint(50, 100) \
                 for name in student_names}


def sorted_1_dict():
    print(original_dict)
    # 内置函数sorted
    list_1 = [(v, k) for k, v in original_dict.items()]
    print(dict(sorted(list_1, reverse=True)))


def sorted_2_dict():
    list_2 = list(zip(original_dict.values(), original_dict.keys()))
    print({k: v for v, k in sorted(list_2, reverse=False)})


def sorted_3_dict():
    sorted_dict = sorted(original_dict.items(),
                         key=lambda item: item[1],
                         reverse=True)
    sorted_2 = list(enumerate(sorted_dict, 1))
    sorted_3 = {name: (rank, score) for rank, (name, score) in sorted_2}
    print(sorted_3)


def get_rank_score():
    s1 = {i for i in range(1, 5)}
    print(list(enumerate(s1, 1)))


if __name__ == '__main__':
    sorted_3_dict()
