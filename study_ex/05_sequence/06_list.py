"""
Title   시퀀스 타입 | sequence type | list 06
Author  kadragon
Date    2018.09.02
"""

# mutable / immutable

my_str_1 = "Hi! SASA"
my_str_2 = "Hi! SASA"

print(my_str_1 is my_str_2)
# 결과: True

my_list_1 = [1, 2, 3, 4, 5]
my_list_2 = my_list_1
# 결과: True

print(my_list_1 is my_list_2)

my_list_2 = my_list_2 + [77]
print(my_list_1 is my_list_2)
# 결과: False


my_list_1 = [1, 2, 3, 4, 5]
my_list_2 = my_list_1

my_list_2.append(77)
print(my_list_1 is my_list_2)
# 결과: True
print(my_list_1)
# 결과: [1, 2, 3, 4, 5, 77]
