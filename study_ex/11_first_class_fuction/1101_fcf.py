def square(x):
    return x * x


print(square(5))
# 결과: 25

f = square
# 변수에 함수를 할당

print(square)
# 결과: <function square at 0x109a63158>
print(f)
# 결과: <function square at 0x109a63158>
