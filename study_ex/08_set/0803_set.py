"""
Title   셋 타입 | set
Author  kadragon
Date    2018.09.08
"""

my_card = {1, 10, 11, 37, 58, 72, 91, 99}

my_card.add(7)
my_card.add(55)
my_card.add(99)

print(my_card)
# 결과: {1, 99, 37, 7, 72, 10, 11, 55, 58, 91}

my_card = my_card.union([7, 55, 99, 2, 3, 4])
print(my_card)
# 결과: {1, 2, 99, 3, 37, 4, 7, 72, 10, 11, 55, 58, 91}

my_set = {1, 2, 3, 4}
my_set.remove(4)

print(my_set)
# 결과: {1, 2, 3}

# my_set.remove(4)
# KeyError: 4

my_set.discard(4)
