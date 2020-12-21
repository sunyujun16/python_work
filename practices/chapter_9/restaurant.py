"""This is a set of all restaurants."""


class Restaurant():
    """don't know what to write...."""

    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = 0

    def describe_restaurant(self):
        print("以吾之名；" + self.restaurant_name)
        print("江湖无情；" + self.cuisine_type)

    @staticmethod
    def open_restaurant(self):
        print("I'm open...")

    def set_number_served(self, num):
        if num >= self.number_served:
            self.number_served = num
        else:
            print("Fuck off!")

    def increment_number_served(self, plus_num):
        if plus_num < 0:
            print("Fuck off")
        else:
            self.number_served += plus_num

