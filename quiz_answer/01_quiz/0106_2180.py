# https://code.sasa.hs.kr/problem.php?id=2180


class RamenMaker:
    def __init__(self, name):
        self.name = name

    def maker(self):
        return self.name + ' making complete'


rm1 = RamenMaker('raccoon')
rm2 = RamenMaker('udon')

print(rm1.maker())
print(rm2.maker())
