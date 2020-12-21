"""定义一个员工类, 用于测试"""


class Employee(object):
    """员工类, 主要处理年薪"""

    def __init__(self, f_name, l_name, payment):
        """初始化员工的属性,包括姓、名、薪水"""
        self.fullname = (f_name + l_name).title()
        self.payment = payment

    def give_raise(self, pay_raised=5000):
        """仅用于涨工资"""
        self.payment += pay_raised

