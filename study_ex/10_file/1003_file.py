"""
Title   file
Author  kadragon
Date    2018.09.15
"""


def init_test():
    f = open('test.txt', 'w')
    f.write('Python is simple')
    f.close()


def print_test():
    f = open('test.txt', 'r')
    print(f.read())
    f.close()


init_test()
print_test()
# 출력: Python is simple


init_test()
f = open('test.txt', 'r+')
f.write('ABCD')
print(f.read())
# 출력: on is simple
f.close()
print_test()
# 출력: ABCDon is simple


init_test()
f = open('test.txt', 'r+')
f.read()
f.write('ABCD')
f.close()
print_test()
# 출력: Python is simpleABCD
