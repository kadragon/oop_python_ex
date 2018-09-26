# Generator Expression
g = (n * n for n in range(21))

# g는 generator 객체
print(type(g))  # 결과: <class 'generator'>

# 10개 출력
for i in range(10):
    value = next(g)
    print(value)

# 나머지 모두 출력
for x in g:
    print(x)
