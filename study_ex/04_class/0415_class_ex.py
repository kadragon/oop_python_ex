"""
Title   클래스 | Class | 15
Author  kadragon
Date    2018.08.28
"""


class house_sasa:
    sub_title = "SASA "

    def __init__(self, name):
        self.target_name = self.sub_title + name

    def go_place(self, place):
        print("%s, %s 로 이동중..!" % (self.target_name, place))


class house_sjgl(house_sasa):
    sub_title = "SJGL "


pey = house_sjgl("강동욱")

print(pey.target_name)
pey.go_place("S402")




