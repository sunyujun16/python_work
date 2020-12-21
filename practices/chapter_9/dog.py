"""This is nothing"""


class Dog(object):
    """一次模拟小狗的简单尝试"""

    def __init__(self, name, age):
        """初始化属性，name和age"""
        self.name = name
        self.age = age

    def sit(self):
        """模拟小狗被命令时蹲下"""
        print(self.name.title()+" is now sitting.")

    def roll_over(self):
        """模拟小狗被命令时打滚"""
        print(self.name.title()+" rolled over.")


my_dog = Dog('messi', 6)

print(my_dog.name.title())

my_dog.sit()
my_dog.roll_over()
