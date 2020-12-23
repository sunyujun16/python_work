"""不好使咋回事儿呢"""

import unittest
from employee import Employee


class TestEmployee(unittest.TestCase):
    """测试Employee类"""

    def setUp(self):
        """创建一个Employee的实例Jack"""
        self.jack = Employee('jack', 'trump', 50000)
        print(self.jack.fullname)

    def test_give_raise_default(self):
        """测试give_raise方法默认参数时运行状况"""
        a = self.jack.payment
        self.jack.give_raise()
        b = self.jack.payment
        self.assertTrue(int(b) - int(a) == 5000)

    def test_give_raise_not_default(self):
        """测试give_raise方法给定参数'10'美元时运行状况"""
        a = self.jack.payment
        self.jack.give_raise(10)
        b = self.jack.payment
        self.assertTrue(int(b) - int(a) == 10)


unittest.main()

# OK了,要注意运行方式选择不同会导致不出测试报告的问题 !!!!!!!要在菜单栏的Run下面手动选择!!!!
