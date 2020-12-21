"""Different ways of open files"""

'''
- Normal way:
with open('pi_digits.txt') as file_object:
    contents = file_object.read()
    print(contents)

print(contents.rstrip())

print('I love LiuYihan')


- Assign the filename to parameters:
filename = 'pi_digits.txt'

with open(filename) as file_object:
    for line in file_object:
        print(line.rstrip())

- This won't work:
with open('pi_digits.txt') as file_object:
for line in file_object:
    print(line.rstrip()) 

Traceback (most recent call last):
  File "/home/tlxy/python_work/practices/chapter_10/pi_digits.py", line 15, in <module>
    for line in file_object:
ValueError: I/O operation on closed file.
'''

filename = 'pi_digits.txt'

with open(filename) as file_object:
    lines = file_object.readlines()

for line in lines:
    print(line.rstrip())

# All is string
# All is string
