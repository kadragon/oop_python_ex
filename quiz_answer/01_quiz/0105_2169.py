# https://code.sasa.hs.kr/problem.php?id=2169

n = int(input())

buf = []

for i in range(n):
    k = int(input())
    buf.append(k)

buf = list(set(buf))
buf.sort()

for i in buf:
    print(i, end=" ")
