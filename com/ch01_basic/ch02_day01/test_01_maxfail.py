# !/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time : 2021/05/14 18:08

"""
1.执行Pytest时，可能出现6种不同的退出code:
退出code 0: 收集并成功通过所有测试用例
退出code 1: 收集并运行了测试,部分测试用例执行失败
退出code 2: 测试执行被用户中断
退出code 3: 执行测试中发生内部错误
退出code 4: pytest命令行使用错误
退出code 5: 没有收集到测试用例
"""

# -x 表示：第一次失败后停止运行
# --maxfail=2 表示：第二次失败后停止运行
import pytest


from com.ch01_basic.ch01_pkg.Calc import Calc







class TestCalc:
    """测试类：calc"""
    calc = Calc(100, 25)
    def test_add(self):
        assert self.calc.add() == 120

    @pytest.mark.slow
    def test_sub(self):
        assert self.calc.sub() == 170

    @pytest.mark.smoke
    def test_multi(self):
        assert self.calc.multi() == 2000

    def test_div(self):
        assert self.calc.div() == 5


if __name__ == '__main__':
    pytest.main(['-vs', '--maxfail=2'])
