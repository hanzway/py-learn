# !/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time : 2021/01/16 10:22
import pytest
import yaml

from dom.test_pytestdemo.calculator import Calc

add_data = [(10, 4, 14), (10, 6, 16), (10, 20, 30)]
div_data = [(100, 2, 50), (100, 4, 25), (100, 25, 4)]

# @pytest.fixture()
def fetch_data(request):
    """
    从yaml文件中，获取参数化数据
    trigger = request.node.get_closest_marker('fixture_name')
    `trigger.args` the result is a object of list.
    trigger_data = trigger.args[0]
    """
    with open('./ymlres/data.yml', 'rt') as f:
        yml_data = yaml.load(f, Loader=yaml.SafeLoader)
    # return yml_data[request.param]
    return yml_data[request]


class TestCalc:

    @pytest.mark.parametrize(argnames='num1,num2,expect',
                             argvalues=add_data,
                             ids=['add1', 'add2', 'add3'])
    def test_add(self, num1: int, num2: int, expect):
        cal = Calc()
        assert expect == cal.add(num1, num2)

    @pytest.mark.parametrize('num1,num2,expect', div_data, ids=['div1', 'div2', 'div3'])
    def test_div(self, num1, num2, expect):
        cal = Calc()
        assert expect == cal.div(num1, num2)

    @pytest.mark.parametrize('num1,num2,expect',
                             fetch_data('add_data'),
                             ids=['add21', 'add22', 'add23'])
    def test_add_2(self, num1: int, num2: int, expect:int):
        cal = Calc()
        assert expect == cal.add(num1, num2)

    @pytest.mark.acquire_data('add_data')
    def test_add_3(self,acquireCalc, caseDataFromYml):
        for i in caseDataFromYml:
            x,y,e = i
            assert e == acquireCalc.add(x,y)

    @pytest.mark.acquire_data('div_data')
    def test_div_2(self, acquireCalc, caseDataFromYml):
        for i in caseDataFromYml:
            x, y, e = i
            assert e == acquireCalc.div(x, y)

    @pytest.mark.acquire_data('persons$summer$hoppy$1')
    def test_yaml_data(self, caseDataFromYml):
        print('yaml data')
        assert caseDataFromYml == 'chess'

if __name__ == '__main__':
    pytest.main(['-vs', 'test_calc.py::TestCalc::test_yaml_data'])
