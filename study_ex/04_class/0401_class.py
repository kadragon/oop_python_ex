"""
Title   클래스 | Class | 01
Author  kadragon
Date    2018.08.28
"""

# 계산기의 결과를 저장하기 위하여 사용하는 변수
result = 0


def adder(num):
    global result  # global 을 이용하면 전역 변수를 사용할 수 있다.

    result += num
    return result


print(adder(3))     # 결과: 3
print(adder(4))     # 결과: 7
