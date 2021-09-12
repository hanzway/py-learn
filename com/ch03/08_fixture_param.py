#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/9/12 19:41
import random

import pytest

the_user_data = [
    {'user':'tom', 'password':'123456'},
    {'user':'Jerry', 'password':'654321'},
    {'user':'Morty', 'password':'11'},
    {'user':'Morty', 'password': '77'},
]


@pytest.fixture(scope='function')
def login_r(request):
    # 可以通过dict形式，虽然传递的是一个参数，但通过key的方式可以达到类似传入多个参数的效果
    username = request.param['user']
    password = request.param['password']
    print('\n打开首页，准备登录，登录用户:{}----{}'.format(username, password))
    if password:
        return True
    else:
        return False


# 说明： 这是pytest的参数化数据驱动，indirect=True时，表示：将login_r当作函数去执行,不写时，默认为：false.
# 也就是：测试用例中的参数，既是参数，也是一个需要提前运行的函数的名字。
@pytest.mark.parametrize('login_r', the_user_data, indirect=True)
def test_login(login_r):
    # 登陆用例
    login_result = login_r
    print('\n测试该用例中，登陆的返回值是： {}'.format(login_result))
    assert login_result, '\n用户名与密码不匹配，登陆失败。'



if __name__ == '__main__':
    pytest.main(['-vs'])
