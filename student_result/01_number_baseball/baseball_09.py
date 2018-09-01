import random

# 변수를 선언할때에는 var_length OR varLength 와 같은 형태로 선언
canplayidx = 10
answer = []
flag = 0
numberlen = 0

numberlen = int(input('문제를 풀어볼 자리수를 입력하시오 : '))


def find_error(temp):
    if len(temp) != numberlen:
        return 0
    if len(temp) == 1:
        return 1
    for i in range(len(temp)):
        for j in range(len(temp)):
            if i != j and temp[i] == temp[j]:
                return 2
    return 3


def heart(temp):
    print('생명바 : ', end='')
    for i in range(temp):
        print('0', end='')
    print('')


def find_checking(temp):
    if temp[0] == temp[1] or temp[1] == temp[2] or temp[2] == temp[0]:
        return False
    return True


# 모든 함수는 단일 행동을 하게 설계하는 것이 유지보수 측면에서 효율적임
# 너무 많은 부분이 메인에 있음
for i in range(3):
    t = random.randint(0, 9)
    t = str(t)
    answer.append(t)

while not find_checking(answer):

    del answer[2]
    del answer[1]
    del answer[0]

    for i in range(3):
        t = random.randint(0, 9)
        t = str(t)
        answer.append(t)

for playtime in range(canplayidx):
    heart(canplayidx - playtime)

    a = 0
    strike = 0
    ball = 0

    a = input('Give me your answer : ').split()
    checking = find_error(a)
    if a == ['answer']:
        print(answer)
        print()
        continue

    if checking <= 2:
        if checking == 0:
            print('ERROR l 숫자는 띄어쓰기가 들어간 세 자리입니다. ㅣ ERROR')
        elif checking == 2:
            print('ERROR l 같은 숫자를 입력하지 마시오. ㅣ ERROR')
        print('')
        continue

    for i in range(3):
        for j in range(3):
            if answer[i] == a[j]:
                if i == j:
                    strike += 1
                else:
                    ball += 1

    if strike == 3:
        print("축하해요!!!!! 이젠 끝났어요!!!!")
        print('')
        flag = 1
        break
    else:
        print("$$ 결과는 %d STRIKE %d BALL %d OUT 입니다 $$" % (strike, ball, 3 - strike - ball))
        print('')

if flag != 1:
    print("아쉽네요. 정답은 ")
    print(answer)
    print(" 이거였어요.")
