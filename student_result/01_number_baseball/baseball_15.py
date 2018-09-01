import random


def strike(a, ans, jarit):
    cnt = 0
    t = 0
    dev = 1
    while t < jarit:
        if a % (dev * 10) - a % dev == ans % (dev * 10) - ans % dev:
            cnt += 1
        t += 1
        dev *= 10
    return cnt


# 사용하지 않는 인수를 받음
def ball(a, ans):
    cnt = 0

    if a % 10 == (ans % 100) // 10 or a % 10 == ans // 100:
        cnt += 1
    if (a % 100) // 10 == ans % 10 or (a % 100) // 10 == ans // 100:
        cnt += 1
    if a // 100 == ans % 10 or a // 100 == (ans % 100) // 10:
        cnt += 1
    return cnt


# print("자릿수를 입력하시오")
jarit = 3
# jarit=int(input())

tep = list(range(10))
re = 1

while re:
    suff = tep[0]
    while tep[0] == 0 or tep[0] == suff:
        random.shuffle(tep)
    a = int(tep[0]) * 100 + int(tep[1] * 10) + int(tep[2])
    print("\n%d" % a)
    so = 1
    print("%d자리 정수만 입력하시오" % jarit)
    for i in range(10):
        ans = int(input())
        s = strike(a, ans, jarit)
        b = ball(a, ans, jarit)
        o = jarit - s - b

        if s == 3:
            print("Congraturation.", end=" ")
            so = 0
            break
        else:
            print("S:%d B:%d O:%d" % (s, b, o))

    if so == 1:
        print("Failed. 다시 플레이하려면 Y, 아니면 N을 넣어라.")
    if so == 0:
        print("다시 플레이하려면 Y, 아니면 N을 넣어라.")

    replay = "asdf"
    while replay != 'N' and replay != 'Y':
        replay = input()
        if replay != 'N' and replay != 'Y':
            print("다시 입력하시오")

    if replay == 'N':
        re = 0
    elif replay == 'Y':
        re = 1
    # 0 or 1 보다 False or True
