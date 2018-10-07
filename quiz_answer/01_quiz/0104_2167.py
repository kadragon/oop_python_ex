# https://code.sasa.hs.kr/problem.php?id=2167

tall = {}
for i in range(10):
    name, h = input().split()
    tall[name] = h

print(tall['J'])
print(tall['F'])
print(tall['E'])
