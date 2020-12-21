filename = 'programming.txt'

# Do not touch this, it will rewrite your file!!!

# with open(filename, 'w') as file_sun:
#     file_sun.write('I\'ve met many people, none of them could be as beautiful as you.')
#     file_sun.write('奕含')

# This is much safer, it only add contents at the end.
with open(filename, 'a') as file_sun:
    file_sun.write('\n但除非有什么特别的缘分\n')
    file_sun.write('否则我们看起来不大可能同路而行')
    file_sun.write('\n祝我们的余生像秋天的果实一样饱满,像山河四季一样多姿,如厚重的土地一般泰然.')


