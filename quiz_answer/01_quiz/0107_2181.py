# https://code.sasa.hs.kr/problem.php?id=2181


class Calculator:
    def __init__(self):
        self.result = 0

    def add(self, a):
        self.result += a
        return self.result

    def minus(self, a):
        self.result -= a
        return self.result

    def mul(self, a):
        self.result *= a
        return self.result


a, b, c = input(), input(), input()

C = Calculator()

print(C.add(int(a)))
print(C.minus(int(b)))
print(C.mul(int(c)))
