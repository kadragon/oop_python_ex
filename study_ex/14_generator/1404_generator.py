import sys

size = 100000

# List 형식
a = [i for i in range(size)]

print(a)
# 결과: [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, ...

print("Memory: %d" % sys.getsizeof(a))
# 결과: Memory: 824464

print(len(list(a)))  # 결과: 100000
print(len(list(a)))  # 결과: 100000


# Generator 형식
b = (i for i in range(size))

print(b)
# 결과: <generator object <genexpr> at 0x107996048>

print("Memory: %d" % sys.getsizeof(b))
# 결과: Memory: 120

print(len(list(b)))  # 결과: 100000
print(len(list(b)))  # 결과: 0
