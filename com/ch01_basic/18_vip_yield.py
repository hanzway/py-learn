# !/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time : 2021/10/7 11:54
# @file: 18_vip_yield.py

"""
yield关键字的作用：
1、函数在执行过程中，截断函数的执行，将函数在执行过程中，返回一个值，当再次调用函数时，继续从刚才截断处，继续执行
2、yiled不能单独使用，必须使用在函数中，用来将函数变更为一个：生成器；
"""

# 1. yield生成器
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


employee_salary = {'tom': 100, 'jerry':200, 'summer':210, 'default': 300, 'avg': 150}


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


if __name__ == '__main__':
    t02()






