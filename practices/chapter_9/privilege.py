from users import User


class Privilege(object):
    def __init__(self):
        self.privileges = ["先斩后奏", "皇权特许"]

    def show_privileges(self):
        print(self.privileges)
        print("这，就是西厂。够不够清楚？")


class Admin(User):
    def __init__(self, first_name, last_name, age, wife):
        super(Admin, self).__init__(first_name, last_name, age, wife)
        self.privileges = Privilege()


# administrator = Admin("Sun", "Yujun", 26, "LiuYihan")
# administrator.privileges.show_privileges()
