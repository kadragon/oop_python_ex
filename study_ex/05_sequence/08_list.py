"""
Title   시퀀스 타입 | sequence type | list 08
Author  kadragon
Date    2018.09.02
"""

my_list = [4, 3, 1, 5, 6, 2, 7]
my_list.sort()

print(my_list)
# 결과: [1, 2, 3, 4, 5, 6, 7]

print(my_list[::-1])
# 결과: [7, 6, 5, 4, 3, 2, 1]

my_list = [4, 3, 1, 5, 6, 2, 7]
sorted_my_list = sorted(my_list)

print(my_list)
# 결과: [4, 3, 1, 5, 6, 2, 7]
print(sorted_my_list)
# 결과: [1, 2, 3, 4, 5, 6, 7]

print('p/y/t/h/o/n'.split('/'))
# 결과: ['p', 'y', 't', 'h', 'o', 'n'] / 리스트로 반환됨.

print('/'.join(['p', 'y', 't', 'h', 'o', 'n']))
# 결과: p/y/t/h/o/n
