"""
Title   시퀀스 타입 | sequence type | tuple 11
Author  kadragon
Date    2018.09.02
"""

import sys

tp = 1, 2
my_list = [1, 2]

print(sys.getsizeof(tp))
# 결과: 64

print(sys.getsizeof(my_list))
# 결과: 80
