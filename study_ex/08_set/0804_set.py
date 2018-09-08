"""
Title   셋 타입 | set
Author  kadragon
Date    2018.09.08
"""

my_set = {1, 2, 3, 4, 5}
print(1 in my_set)  # True
print(10 in my_set)  # False

convert_list = list(my_set)
print(convert_list)
# 결과: [1, 2, 3, 4, 5]

my_list = [1, 10, 11, 37, 37, 37, 58, 72, 72, 91, 99]
card_set = set(my_list)
print(card_set)
# 결과: {1, 99, 37, 72, 10, 11, 58, 91}

print(sorted(list(set(sorted(my_list)))))
# 결과: [1, 10, 11, 37, 58, 72, 91, 99]
