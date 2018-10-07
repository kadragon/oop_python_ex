# https://code.sasa.hs.kr/problem.php?id=2182


class UnCompleteCal:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def div(self):
        pass


class CompleteCal(UnCompleteCal):
    def div(self):
        return self.a / self.b


a, b = input().split()
div_cal = CompleteCal(int(a), int(b))
print(div_cal.div())
