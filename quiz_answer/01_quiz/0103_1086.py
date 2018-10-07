# https://code.sasa.hs.kr/problem.php?id=1086

arr = input().split(" ")
n = input()
try:
    print(arr.index(n) + 1)
except ValueError:
    print(-1)
