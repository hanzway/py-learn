# !/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time : 2021/10/7 11:54
# @file: 18_vip_yield.py

"""
yield关键字的作用：
1、函数在执行过程中，截断函数的执行，将函数在执行过程中，返回一个值，当再次调用函数时，继续从刚才截断处，继续执行
2、yiled不能单独使用，必须使用在函数中，用来将函数变更为一个：生成器；
3、生成器表达式
"""

# 1. yield生成器
import random
import string


def foo_1():
    print('------->11111')
    yield 111
    print('-------->22222')
    yield 222
    print('------>333333')
    yield 333


def t01():
    g1 = foo_1()
    # print(g1) # <generator object foo_1 at 0x000002123913FA48>
    g1.__next__()
    g1.__next__()
    g1.__next__()
    g1.__next__()


employee_salary = {'tom': 100, 'jerry': 200, 'summer': 210, 'default': 300, 'avg': 150}


def foo_2(emp_name):
    print('calc the number\'s square !')
    while True:
        emp_name = yield employee_salary.get(emp_name)
        if emp_name is None or not isinstance(emp_name, str) or emp_name not in employee_salary.keys():
            emp_name = 'default'


def t02():
    g2 = foo_2(emp_name='avg')
    print(g2)
    print(g2.send(None))  # 获取生成器对象中的值的时候，第一次获取的时候，不能传值！只能传None。
    print(g2.send('jerry'))


# 3.1 三元表达式
def foo_3(num: int):
    level = None
    # num = int(input('数字：'))
    if num > 100:
        level = 'A'
    else:
        level = 'F'
    print(level)
    level = 'A' if num > 100 else 'F'
    print(level)


# 3.2 列表生成式、字典生成式
def foo_4():
    stu_score = {'summer': 90, 'tom': 120, 'jerry': 150}
    generator_list = [score + 1 for score in stu_score.values() if score > 100]
    print(generator_list)
    generator_dict = {k: random.randint(50, 120) for k in random.sample(string.ascii_letters, 10)}
    print(generator_dict)
    g_keys = ['tom_th', 'jerry_th', 'summer_th', 'rick']
    g_values = [i * 10 for i in range(10)]
    generator_dict_2 = { k : v
                        for k in g_keys if k.endswith('th')
                        for v in random.sample(g_values, 3)}
    print(generator_dict_2)


# 3.3 统计文件中args.txt的字符个数
def count_num_of_char():
    with open('args.txt', 'rt') as f:
        res = sum((len(line) for line in f))
    print(res)


# 4.函数递归调动：函数嵌套的特殊形式，函数中调用函数自己本身；
def foo_5(num):
    print('*' * num)
    if num > 5:
        return
    num += 1
    foo_5(num)


old_list = [1, [2, [3, [4,]]]]
def foo_6(the_list:list):
    """列表中包含列表，请将所有列表中元素铺平后展示在一个列表中"""
    for x in the_list:
        if isinstance(x, list):
            foo_6(x)
        else:
            print(x)


# 5. 内置函数：enumerate
def foo_7():
    d_list = [i for i in range(5)]
    random.shuffle(d_list)
    # print(list(enumerate(d_list)))
    d_tuple = (i * 10 for i in range(10))
    print(list(enumerate(d_tuple)))
    # {'tom':100, 'jerry':50}  ->  {0:100, 1:50}
    d_dict = {'tom':100, 'jerry':50}
    d_dict_new = {}
    for k,v in enumerate(d_dict.items()):
        d_dict_new[k] = v[0]
    print(d_dict)
    print(d_dict_new)


if __name__ == '__main__':
    import ch01_pkg as other
    print(other.c21())
