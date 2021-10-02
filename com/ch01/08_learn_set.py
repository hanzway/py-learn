#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/10/2 11:59
# @Author  : ksu will han
# @File    : 08_learn_set.py
# @Software: PyCharm

# 创建集合，前提条件：集合中的每个元素都必须是可哈希的，既：不可变。

def t01():
    s1 = set('hello world!')
    print(s1)


# function:给列表去重
def t02():
    l1 = ['hello', 'tom', 'hello', 'jerry']
    no_same_list = list(set(l1))
    print(no_same_list)

# 集合中的元素必须是可哈希的，
# 既：不可变的，报错内容【TypeError: unhashable type: 'list'】
def t03():
    l2 = [3, 100, [100, 200], 'hello']
    s2 = set(l2)
    print(s2)

# 给集合中添加一个元素
def set_update():
    s3 = set('hello')
    s3.add('world')
    print(s3)
    s3.update('world')
    print(s3)
    s3.update([12, 'eeee'])
    print(s3)

def set_clear():
    s4 = set([100, 200, 300, 400, 500])
    print(s4)
    s4.clear()
    print(s4)


# 集合的关系测试：成员和集合的关系；集合与集合之间的关系
def set_member():
    s5 = set('hello')
    print(s5)
    print('h' in s5)
    # 联合，交集，差集
    s6 = set('world')
    print(s5 | s6) # 并集 s6.union()
    print(s5 & s6) # 交集 s6.intersection()
    print(s5 - s6) # 差集 s5.difference()
    print(s5 ^ s6) # 对称差集，先获取交集，将除了交集的其他元素组成一个新的集合


if __name__ == '__main__':
    set_member()

