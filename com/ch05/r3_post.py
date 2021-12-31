# !/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time : 2021/12/31 14:31
# @Author : qingwei.han
# @Desc: 给方法中添加附件内容
import random

import pytest
import requests

"""
常见的请求格式：
1、application/json
2、application/x-www-form-urlencoded name=tom&age=100&hobby=football
3、multipart/form-data:这一种是表单格式的：data=***
4、text/xml  data=
"""


def test_req_get():
    """request.get, 参数为：data"""
    number = '10086'
    qq_key = '8dbee1fcd8627fb6699bce7b986adc45'
    req_url = r'http://japi.juhe.cn/qqevaluate/qq'
    req_param = {'key': qq_key,
                 'qq': number}
    headers = {'Content-Type': 'application/json;charset=utf-8'}
    res = requests.get(url=req_url, params=req_param, headers=headers)
    print(res.json())


def test_req_post():
    """requests: body中的参数可以为：json 或者：data"""
    number = '64543646346'
    qq_key = '8dbee1fcd8627fb6699bce7b986adc45'
    req_url = r'http://japi.juhe.cn/qqevaluate/qq'
    req_param = {'key': qq_key,
                 'qq': number}
    headers = {'Content-Type': 'application/json;charset=utf-8'}
    res = requests.post(url=req_url, params=req_param, headers=headers)
    print(res.json())


@pytest.mark.skip
def test_post_01():
    host = r'http://49.235.92.12:9000'
    login_url = '/api/v1/login/'  # 接口文档
    body_data = {'username': 'test', 'password': "''.join([random.randint(1,9) for _ in range(10)]"}
    res = requests.post(url= host + login_url, json= body_data)
    print(res.text)


@pytest.mark.skip
def test_post_02():
    host = r'http://49.235.92.12:9000'
    login_url = '/api/v4/login/'  # 接口文档Path;
    req_url = host + login_url
    req_header = {'Content-Type': 'application/x-www-form-urlencoded'}
    body_data = {'username': 'test',
                 'password': "''.join([random.randint(1,9) for _ in range(10)]"}
    # data
    res = requests.post(url=req_url, data=body_data, headers=req_header)
    print(res.text)


@pytest.mark.skip
def test_post_03():
    host = r'http://49.235.92.12:9000'
    login_url = '/api/v4/login/'  # 接口文档Path;
    req_url = host + login_url
    req_header = {'Content-Type': 'text/xml'}
    body_data = {'username': 'test',
                 'password': "''.join([random.randint(1,9) for _ in range(10)]"}
    # data
    res = requests.post(url=req_url, data=body_data, headers=req_header)
    print(res.text)


if __name__ == '__main__':
    pytest.main(['-vs', 'r3_post.py::test_req_post'])

