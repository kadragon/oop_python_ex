# https://code.sasa.hs.kr/problem.php?id=2184


def convert_int(func, list, i):
    ret = []

    for a in list:
        ret.append(func(a, i))

    return ret


list = map(int, input().split())
k = int(input())

convert_list = convert_int(pow, list, k)
print(convert_list)
