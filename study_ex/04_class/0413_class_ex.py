"""
Title   클래스 | Class | 13
Author  kadragon
Date    2018.08.28
"""


class house_sasa:
    sub_title = "SASA "

    def set_name(self, name):
        self.target_name = self.sub_title + name

    def go_place(self, place):
        print("%s, %s 로 이동중..!" % (self.target_name, place))


pey = house_sasa()
# pey.set_name("강동욱")

print(pey.target_name)
pey.go_place("S402")




