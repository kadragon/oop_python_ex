# Generator 함수
def gen():
    yield 1
    yield 2
    yield 3


# Generator 객체
g = gen()
print(type(g))  # 결과: <class 'generator'>

# next() 함수 사용
n = next(g)
print(n)  # 1
n = next(g)
print(n)  # 2
n = next(g)
print(n)  # 3

# for 루프 사용 가능
for x in gen():
    print(x)
