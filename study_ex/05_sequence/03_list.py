"""
Title   시퀀스 타입 | sequence type | list 03
Author  kadragon
Date    2018.09.02
"""

my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
my_list[0:4] = [100, 1000]  # 분할 구역 0에서 3까지의 항목이 100, 1000 으로 대체
print(my_list)

# 확장분할 연산을 이용하여 객체를 대입할 때는
# 확장분할 연산의 결과가 되는 객체의 수와 대입되는 객체의 수와 일치해야 한다는 제약이 있음
my_list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(my_list[0::2])

# my_list[0::2] = "Hi! Python"
# ValueError: attempt to assign sequence of size 10 to extended slice of size 5

# my_list[0::2] = "Hi!"
# ValueError: attempt to assign sequence of size 3 to extended slice of size 5

my_list[0::2] = "Python"
print(my_list)
