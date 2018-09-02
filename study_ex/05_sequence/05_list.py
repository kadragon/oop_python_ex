"""
Title   시퀀스 타입 | sequence type | list 05
Author  kadragon
Date    2018.09.02
"""

my_list = ['hi', 'python', 3.5]
del my_list[2]
print(my_list)
# 결과: ['hi', 'python']

my_list = [1, 2, 3, 4, 5]
del my_list[0:4]
print(my_list)
# 결과: [5]

my_list = [1, 2, 3, 4, 5]
del my_list[::2]
print(my_list)
# 결과: [2, 4]

my_list = [1, 2, 3, 4, 5]
my_list.remove(3)
print(my_list)
# 결과: [1, 2, 4, 5]

my_list = [1, 2, 3, 4, 5]
print(my_list.pop())
# 결과: 5
print(my_list)
# 결과: [1, 2, 3, 4]

print(my_list.pop(0))
# 결과: 1
print(my_list)
# 결과: [2, 3, 4]
