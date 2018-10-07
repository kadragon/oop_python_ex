# https://code.sasa.hs.kr/problem.php?id=2183


a = int(input())
b = int(input())

try:
    print(a / b)
except ZeroDivisionError:
    print("[ B must not be zero. ]")
