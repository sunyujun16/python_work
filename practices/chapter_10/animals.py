file_names_self = ['cats.txt', 'dogs.txt', 'pigs.txt']


def add_line(file_names):
    """打印每行,并在末尾添加写入次数的行"""

    for file_name in file_names:
        try:
            with open(file_name, 'r+') as file_sun:
                lines = file_sun.readlines()
                file_sun.write('\nwritten in.')
        except FileNotFoundError:
            pass
            # print('Sorry, '+file_name+" doesn't exist.")
        else:
            for line in lines:
                print(line.rstrip())


add_line(file_names_self)
