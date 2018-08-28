"""
Title   클래스 | Class | 03
Author  kadragon
Date    2018.08.28
"""


class Calculator:
    """
    덧샘을 해주고 결과를 저장하는 계산기
    """
    def __init__(self):     # 초기화
        self.result = 0

    def adder(self, num):   # 덧샘
        self.result += num
        return self.result


cal1 = Calculator()
cal2 = Calculator()

print(cal1.adder(3))    # 결과: 3
print(cal1.adder(4))    # 결과: 4

print(cal2.adder(3))    # 결과: 3
print(cal2.adder(7))    # 결과: 10
