"""
Title   클래스 | Class | 05
Author  kadragon
Date    2018.08.28
"""

import random


class Service:
    secret = "시청각실의 장비가 있는 곳으로 가면, 맥실로 갈 수 있는 문이 있지만.. 잠겨있다."

    def random_select(self, a, b):
        print("%d 와 %d 사이에 선택된 숫자는 %d 입니다." % (a, b, random.randrange(a, b)))


pey = Service()

print(pey.secret)
pey.random_select(1, 10)  # 1 와 10 사이에 선택된 숫자는 7 입니다.
