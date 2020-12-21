import json

# num = input('tell me yout favorite number: ')
target_name = 'num2.json'

# with open(target_name, 'w') as f_obj:
#     json.dump(num, f_obj)


def get_new_num():
    print("啊哦, 没找到记录呢, 请输入一个吧:")
    user_num = input("你最喜欢的数字是: ")
    return user_num
    pass


def print_num(filename):
    try:
        with open(filename) as f_obj:
            user_num = json.load(f_obj)
    except FileNotFoundError:
        user_num = get_new_num()
        with open(filename, 'w') as f_obj:
            json.dump(user_num, f_obj)
            print("You'll see "+user_num+" next time you load it.")
    else:
        print("the Number you like most is: " + user_num + ', right?')


print_num(target_name)

