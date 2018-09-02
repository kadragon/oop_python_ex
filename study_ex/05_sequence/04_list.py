"""
Title   시퀀스 타입 | sequence type | list 04
Author  kadragon
Date    2018.09.02
"""

my_list = [1, 2, 3, 4, 5]
print(my_list + [100])
# 결과: [1, 2, 3, 4, 5, 100]

print(my_list)
# 결과: [1, 2, 3, 4, 5]

my_list.append(100)
print(my_list)
# 결과: [1, 2, 3, 4, 5, 100]

my_list.append([200, 300])
print(my_list)
# 결과: [1, 2, 3, 4, 5, 100, [200, 300]]

my_list = [1, 2, 3, 4, 5]
my_list.extend([100, 200, 300])
print(my_list)
# 결과: [1, 2, 3, 4, 5, 100, 200, 300]

my_list = [1, 2, 3, 4, 5]
my_list += [100, 200, 300]
print(my_list)
# 결과: [1, 2, 3, 4, 5, 100, 200, 300]

my_list = [1, 2, 3, 4, 5]
my_list.insert(0, -77)
print(my_list)
# 결과: [-77, 1, 2, 3, 4, 5]

my_list.insert(1, 0)
print(my_list)
# 결과: [-77, 0, 1, 2, 3, 4, 5]

my_list.insert(-1, 100)
print(my_list)
# 결과: [-77, 0, 1, 2, 3, 4, 100, 5]

my_list.insert(len(my_list), 1000)
print(my_list)
# 결과: [-77, 0, 1, 2, 3, 4, 100, 5, 1000]
