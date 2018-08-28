"""
Title   클래스 | Class | 10
Author  kadragon
Date    2018.08.28
"""


class Cal:
    def set_data(self, first, second):
        self.first = first
        self.second = second

    def sum(self):
        return self.first + self.second

    def sub(self):
        return self.first - self.second

    def mul(self):
        return self.first * self.second

    def div(self):
        return self.first / self.second


a = Cal()
# print(a.first)
b = Cal()

a.set_data(1, 3)
b.set_data(10, 4)

print(a.sum())  # 결과: 4
print(b.div())  # 결과: 2.5





