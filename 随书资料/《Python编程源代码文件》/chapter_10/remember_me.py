import json


def get_stored_username():
    """Get stored username if available."""
    filename = 'username.json'
    try:
        with open(filename) as f_obj:
            username = json.load(f_obj)
    except FileNotFoundError:
        return None
    else:
        return username


def get_new_username():
    """Prompt for a new username."""
    username = input("What is your name? ")
    filename = 'username.json'
    with open(filename, 'w') as f_obj:
        json.dump(username, f_obj)
    return username


def name_isright():
    filename = 'username.json'
    with open(filename, 'r') as f_obj:
        print(json.load(f_obj))
        print("这是你名吗?")
        a = input('y/n: ')  # 这里可以加个循环,保证程序不会因为输入者sb而中断,懒得加了
        if a == 'y':
            return True
        else:
            return False


def say_welcome(username):
    print("Welcome back, "+username+"!")


def add_name():
    username = get_new_username()
    print("We'll remember you when you come back, " + username + "!")


def greet_user():
    """Greet the user by name."""
    username = get_stored_username()
    if username:
        if name_isright():
            say_welcome(username)
        else:
            add_name()
    else:
        add_name()


greet_user()
