print('Please enter 2 numbers', '\n Enter q to quit')

while True:
    a = input('1st num: ')
    if a == 'q':
        print('done')
        break

    b = input('2nd num: ')
    if b == 'q':
        print('done')
        break

    try:
        print(int(a) + int(b))  # 输入的都是str,怎么老不长记性呢.
    except ValueError:
        print('please retry')
    # else:
    #     continue  # 这里放else有些画蛇添足,因为你不说它也要continue的.


