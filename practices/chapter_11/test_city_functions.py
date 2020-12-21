"""测试city_functions.py模块的函数"""


import unittest
from city_functions import describe_city


class TestDescribeCity(unittest.TestCase):  # 第一次没有注意继承父类,导致 run 0 tests, 当时就懵逼了.
    """测试函数describe_city"""

    def test_city_country(self):
        """测试,当不输入人口参数时运行状况"""
        city_country = describe_city('NewYork', 'China')
        self.assertEqual(city_country, 'NewYork is in China')

    def test_city_country_population(self):
        """测试,当输入人口参数时运行状况"""
        city_country = describe_city('NewYork', 'China', 10000000)
        self.assertEqual(city_country, 'NewYork is in China, and the population is 10000000')


unittest.main()
