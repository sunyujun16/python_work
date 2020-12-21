"""习题9(-3, -5 ,-7 ,-8, -11, -12)"""


class User():
    """这是一个储存用户信息的类"""

    def __init__(self, first_name, last_name, age, wife):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.wife = wife
        self.full_name = self.first_name.title() + self.last_name.title()

    def describe_user(self):
        if self.age != 1:
            print("He is " + self.full_name + ", he is " + str(self.age) + " years old, his wife is " + self.wife)
        else:
            print('Fuck off!')

    def greet_user(self):
        print("Hello, " + self.full_name + ".")

