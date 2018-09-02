"""
Title   시퀀스 타입 | sequence type | tuple 10
Author  kadragon
Date    2018.09.02
"""

"""
튜플(tuple)은 리스트와 구조적으로는 동일한 자료형
단,  immutable 객체로 생성된 후에 내용을 바꿀 수 없는 특성을 지니고 있음.

리스트와 동일하게 사용 할 수 있으나, 
append, extend, insert, pop 등은 사용할 수 없음.
"""

tp = 1, 2, 3, 4
print(tp)
# 결과: (1, 2, 3, 4)

tp_2 = 'hello', 'python', 1, 2, 3, [4, 5, 6]
print(tp_2)
# 결과: ('hello', 'python', 1, 2, 3, [4, 5, 6])

tp_3 = (1, 2, 3, 4)
print(tp_3)
# 결과: (1, 2, 3, 4)
