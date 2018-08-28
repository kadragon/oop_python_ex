"""
Title   클래스 | Class | 07
Author  kadragon
Date    2018.08.28
"""

import random


class Service:
    secret = "시청각실의 장비가 있는 곳으로 가면, 맥실로 갈 수 있는 문이 있지만.. 잠겨있다."

    def __init__(self, name):
        """
        인스턴스를 만들 때 항상 실행된다!
        :param name: 사용자 명
        """
        self.name = name

    def random_select(self, a, b):
        print("%s님: %d 와 %d 사이에 선택된 숫자는 %d 입니다." % (self.name, a, b, random.randrange(a, b)))


pey = Service("강동욱")
print(pey.secret)

pey.random_select(1, 10)  # 출력: 강동욱님: 1 와 10 사이에 선택된 숫자는 4 입니다.
