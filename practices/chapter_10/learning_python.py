"""open a file"""

filename = 'learning_python.txt'

with open(filename) as file_by_sun:
    print(file_by_sun.read())
    print('='*30)

with open(filename) as file_by_sun:
    for line in file_by_sun:
        print(line.strip())
    print('='*30)

with open(filename) as file_by_sun:
    lines = file_by_sun.readlines()

print(lines)

with open(filename) as file_by_sun:
    for line in file_by_sun:
        line = line.replace('Python', 'C')
        print(line.rstrip())
