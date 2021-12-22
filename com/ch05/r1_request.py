# !/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time : 2021/12/22 18:43
# @Author : qingwei.han
# @Desr: QQ测凶吉 -> requests中的几种返回。

import requests


class Detection:

    """根据QQ获取到对应号码的预测信息
    接口：http://japi.juhe.cn/qqevaluate/qq
    请求方式：json
    示例：http://japi.juhe.cn/qqevaluate/qq?key=您申请的appKey&qq=295424589
    key: 8dbee1fcd8627fb6699bce7b986adc45
    """

    def __init__(self, num):
        self._num = num
        self.the_app_key = '8dbee1fcd8627fb6699bce7b986adc45'

    def detect(self):
        if self._num is None or not isinstance(self._num, str):
            raise Exception('qq传参类型不为：字符串，或者qq不允许传空参')
        req_url = r'http://japi.juhe.cn/qqevaluate/qq'
        req_param = {'key': self.the_app_key, 'qq': self._num}
        headers = {'Content-Type': 'application/json;charset=utf-8'}
        res = requests.get(url=req_url, params=req_param, headers=headers)
        if res is not None:
            return res
        return '信息有误，须重新申请'


def main():
    detect = Detection('888888')
    res = detect.detect()
    print(res.json()['result']['data']['conclusion'])
    # 1. res.text, 类型：文本字符串:<class 'str'>
    print(res.text, '\n', type(res.text))
    # 2. res.json(), 类型：requests内置json解析器:<class 'dict'>
    print(res.json(), '\n', type(res.json()))
    # 3、状态码
    print('状态码：', res.status_code, '\n', type(res.status_code))
    # 4、响应头
    print('headers: ')
    print(res.headers)
    # 5、单独获取到cookies, 并转换为字典；
    cookie = res.cookies
    print(cookie)
    # 6、将获取到的Cookie变更为字典；
    print(dict(cookie))
    print(dict(cookie)['aliyungf_tc'])


if __name__ == '__main__':
    main()
