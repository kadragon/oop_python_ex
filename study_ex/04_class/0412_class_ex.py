"""
Title   클래스 | Class | 12
Author  kadragon
Date    2018.08.28
"""


class house_sasa:
    sub_title = "SASA "

    def set_name(self, name):
        self.user_name = self.sub_title + name


pey = house_sasa()
pey.set_name("강동욱")

print(pey.user_name)




