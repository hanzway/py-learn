#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/7/10 10:37
# @Author  : ksu will han
# @File    : 06_authType.py
# @Software: PyCharm

# 通过授权的方式自定义自己要求的类型：FileHandler
"""
说明：
(1)、obj.method1()的调用原理：
寻找method1的顺序是：先从属性字典中查找，再从类或父类中的类方法中寻找；再触发__getattr__(self, item)方法；

（2）、继承 + 派生，表面上是调用的FileHandler中的read方法，而实质上是调用的是：
属性file中的read或write方法，可以通过重写其中的read或write方法，对传入的数据进行加工后，在读取或者写入。

(3）、getattr与getattribute的区别：[理解：getattribute是大哥，getattr是小弟】
属性有或者属性没有，都会调用： getattribute.
当属性都不存在的时候，就会调用getattr.
（4）、getattribute
当属性存在时，从属性字典中dict中，根据item查找对应的value，并返回；
当属性不存在时，抛出异常信息，并提示：当前获取的属性内容不存在；
当抛出异常时，会触发__getattr__(self, item)的运行。
"""
class FileHandler:
    """ 自定义的文件处理器 """
    def __init__(self, filename, mode='r', encoding='utf-8'):
        self.filename = filename
        self.mode = mode
        self.encoding = encoding
        self.file = open(filename, mode=mode, encoding=encoding)

    def __getattr__(self, item):
        print('----->', item)
        return getattr(self.file, item)


if __name__ == '__main__':
    f1 = FileHandler('1.txt', 'w')
    f1.read


