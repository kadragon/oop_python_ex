"""
Title   시퀀스 타입 | sequence type | list 07
Author  kadragon
Date    2018.09.02
"""

import copy

my_list_1 = [1, 2, 3, 4, 5]
my_list_2 = my_list_1

print(my_list_1 is my_list_2)
# 결과: True

my_list_2 = copy.copy(my_list_1)
print(my_list_1 is my_list_2)
# 결과: False

n_list_1 = [[1, 2, 3, 4, 5], 'python', 3.6, 3.7]
n_list_2 = copy.copy(n_list_1)

print(n_list_2)
# 결과: [[1, 2, 3, 4, 5], 'python', 3.6, 3.7]
n_list_1[0][0] = 100

print(n_list_2)
# 결과: [[100, 2, 3, 4, 5], 'python', 3.6, 3.7]
print(n_list_1[0] is n_list_2[0])
# 결과: True

n_list_1 = [[1, 2, 3, 4, 5], 'python', 3.6, 3.7]
n_list_2 = copy.deepcopy(n_list_1)
n_list_1[0][0] = 100
print(n_list_2)
# 결과: [[1, 2, 3, 4, 5], 'python', 3.6, 3.7]
