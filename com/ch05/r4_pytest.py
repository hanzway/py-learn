# !/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time : 2021/12/31 16:27

"""
pytest的测试用例：
1、test_开头的模块
2、以test_开头或者_test开头结尾的方法或函数；
3、以Test_开头的类；

"""
import random

import pytest
import requests


def add(a: int, b: int):
    return a + b


# param_data = [(10, 1, 11),(10, 2, 12), (10, 3, 13)]
param_data = [(10, 1, 11), (10, 2, 12), (10, 3, 13)]


class TestCalc():

    @pytest.mark.parametrize('a,b,c',
                             param_data,
                             ids=['TEST_0' + str(i) for i in range(len(param_data))])
    def test_add(self, a, b, c):
        assert a + b == c

    @pytest.mark.flaky(reruns=2, reruns_delay=3)
    def test_01(self):
        """test_01"""
        x = random.randint(5, 15)
        print('\nx=', x)
        assert 10 > x

    def test_02(self):
        assert 5 in [i for i in range(random.randint(1, 10))]

    def test_03(self):
        req_url = r'http://japi.juhe.cn/qqevaluate/qq'
        req_param = {'key': '8dbee1fcd8627fb6699bce7b986adc45', 'qq': '10086'}
        headers = {'Content-Type': 'application/json;charset=utf-8'}
        res = requests.get(url=req_url, params=req_param, headers=headers)
        if not res is None:
            res_json = res.json()
            # assert res_json['reason'] == 'success'
            pytest.assume(res_json['error_code'] == 0)
            pytest.assume(res_json['reason'] == 'success')
        else:
            pytest.xfail('请求的返回为：None')

    def test_telephone_zone(self):
        """获取手机的归属地"""
        req_url = 'http://apis.juhe.cn/mobile/get'
        app_key = '8dbee1fcd8627fb6699bce7b986adc45'
        req_headers = {'Content-Type': 'application/json;charset=utf-8'}
        res = requests.get(url=req_url,
                           params={'phone':'15012677100','key':app_key, 'dtype':'json'},
                           headers=req_headers).json()
        assert res['resultcode'] == '101'
        assert res['error_code'] == 10001


if __name__ == '__main__':
    pytest.main(['-vs', '--tb=line'])
