# !/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time : 2021/10/4 16:47
# @Author : qingwei.han

"""
1、给定一个列表，统计列表中每个元素出来的次数，用一个字典表示：
key是列表中的元素，value是list中该元素出现的次数
"""
import heapq
import random
from collections import Counter

original_list = [random.randint(0, 20) for _ in range(30)]


def t01():
    the_dict = dict.fromkeys(original_list, 0)
    for i in original_list:
        the_dict[i] += 1
    # print(the_dict)
    ordered_dict = sorted(((v, k) for k, v in the_dict.items()), reverse=True)
    print(heapq.nlargest(3, ordered_dict))
    # print(ordered_dict[0:3])


def counter_most_common():
    c = Counter(original_list)
    print(c.most_common(3))


from functools import reduce


# 2、统计多个字典中的公共的键
def get_dict_common_key():
    all_key = 'abcdefghijklmi'
    d1 = {k: random.randint(3, 6) for k in random.sample(all_key, random.randint(3, 6))}
    d2 = {k: random.randint(3, 6) for k in random.sample(all_key, random.randint(3, 6))}
    d3 = {k: random.randint(3, 6) for k in random.sample(all_key, random.randint(3, 6))}
    d4 = {k: random.randint(3, 6) for k in random.sample(all_key, random.randint(3, 6))}
    d = [d1, d2, d3, d4]
    # 求多个字典d1到d4的公有键：
    print(reduce(lambda x, y: x & y, map(dict.keys, d)))


if __name__ == '__main__':
    get_dict_common_key()
