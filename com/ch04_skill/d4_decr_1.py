# !/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time : 2021/3/1 9:41
# @Author : qingwei.han

"""
1.什么是装饰器:在不改变被装饰器对象的源代码和调用方式的前提下，为被装饰对象添加新功能，比如：计算函数的运行时间，打印函数的被调用时间；
    （1）为函数或类增加附加功能，增加功能的函数或类；
    （2）装饰器：定义一个函数，这个函数用来给其他函数添加额外的功能；
    （3）装饰器函数本身的存在没有任何含义，是为其他类或其他函数的存在才有意义？
     (4)装饰器就是在不修改被装饰器对象源代码和调用方式的前提下，为被装饰对象添加新功能。
        - 函数体不变；
        - 函数名不变；
        - 函数的参数个数不变；
2.如何定义装饰器：
2.1、函数通过第一层的参数传，函数的参数通过第二层的里面的闭包函数的参数传；

2.2、
"""
# def index(*args, **kwargs):
#     print(args)
#     print(kwargs)
#
#
# def wrapper(*args, **kwargs):
#     index(*args, **kwargs)
#
#
# def t01():
#     wrapper(1, 2, 3, x=11, y=22, z=33)
##################################################
import time

# def outer(func):
#     add_time = 60 * 60
#     def wrapper(*args, **kwargs):
#         print(time.strftime('%Y-%m-%d %X', time.localtime(time.time() + add_time)))
#         rlt = func(*args, **kwargs)
#         return rlt
#     return wrapper

# 3、定义一个函数，打印出函数的执行时间；

def calc_time(func):
    """传参有两种方式：
        1、通过函数的形式参数传入到函数体中；
        2、给函数包一层，将当前函数作为局部函数，从外部函数给内部函数传参数；
        3、tips：外部函数返回内部函数的引用。
    """
    def wrapper(*args, **kwargs):
        start_t = time.time()
        result = func(*args, **kwargs)
        end_t = time.time() + 10
        print(end_t - start_t)
        return result
    return wrapper

def t01(num1, num2):
    start_t = time.time()
    result = num1 + num2
    end_t = time.time()
    print(end_t - start_t)
    return result

def t02(num1, num2):
    start_t = time.time()
    result = num1 - num2
    end_t = time.time()
    print(end_t - start_t)
    return result


# 装饰器的本质：偷梁换柱：t03 = calc_time(t03)
# <function calc_time.<locals>.wrapper at 0x0000020772B4AF78>
@calc_time
def t03(num1, num2):
    return num1 * num2


if __name__ == '__main__':
    print(t03(100, 2))
