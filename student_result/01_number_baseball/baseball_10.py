import random
import re  # 정규표현


# 변수를 선언할때에는 var_length OR varLength 와 같은 형태로 선언
def makeanswer():  # 정답 만들기
    num_list = list(range(10))
    random.shuffle(num_list)
    # print(num_list[:3])
    return num_list[:3]


def number_input():  # 입력 받기
    user_input = input()

    regex = re.compile(r'\d\s\d\s\d')
    mo = regex.search(user_input)

    if mo is None:
        print("다시 입력해주세요")
    else:
        number_user = list(map(int, mo.group().split(' ')))
    return number_user


def count(ans, ges):
    b = 0
    s = 0
    o = 0

    for i in range(3):
        if ges[i] == ans[i]:
            s += 1
        elif ges[i] in ans:
            b += 1
        else:
            o += 1
    return b, s, o


# 메인
print('guess and type three digits')

while True:
    answer = makeanswer()

    while True:
        guess = number_input()
        ball, strike, out = count(answer, guess)  # 볼 스트라이크 아웃 개수 카운트
        print("%dS %dB %dO" % (strike, ball, out))
        if strike == 3:  # 다 맞추면 break
            break

    print("press 'y' to continue")
    cts = input()
    if cts != 'y':
        break
