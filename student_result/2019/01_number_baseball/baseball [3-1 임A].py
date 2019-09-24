import random

숫자의수 = 3
시도횟수 = 10
말한횟수 = 0


def 정답숫자함수(숫자의수):  # 이 함수는 정답을 생성해주는 함수입니다.
    numbers = list(range(10))
    random.shuffle(numbers)  # 숫자를 램덤으로 선정해줍니다.
    정답 = ''  # 정답을 담을 변수를 설정해줍니다.
    for i in range(숫자의수):
        정답 += str(numbers[i])
    return 정답


def 판단(사용자숫자, 정답):  # 이 함수는 정답과 사용자가 입력한 숫자를 정답과 비교하는 함수입니다.
    if 사용자숫자 == 정답:  # 게임하는 사람이 입력한 숫자와 정답이 일치하면 칭찬을 출력합니다.
        return 'good job! YOU WIN! GAAANG'

    str개수 = 0  # 스트라이크, 볼, 아웃의 갯수를 일일이 변수로 설정합니다.
    bll개수 = 0
    out개수 = 0

    for i in range(len(사용자숫자)):
        if 사용자숫자[i] == 정답[i]:  # 사용자가 입력한 숫자와 정답이 순서대로 일치하면 스트라이크의 수를 1 올립니다.
            str개수 += 1
        elif 사용자숫자[i] in 정답:  # 사용자가 입력한 숫자와 정답에 있는 숫자의 종류만 일치하면 수를 1 올립니다.
            bll개수 += 1
        else:
            out개수 += 1  # 그 외인 아웃의 경우에 아웃 변수를 1 증가시킵니다.

    return '#스트~라이크! ' + str(str개수) + '     #붤. ' + str(bll개수) + '      #아_웃 ' + str(out개수)


def 정수(num):  # 사용자가 입력한 숫자가 0에서 9사이에 있는 정수인지 아닌지 판단해주는 함수입니다.
    if num == ' ':
        return False
    for i in num:
        if int(i) not in list(range(0, 10)):
            return False

    else:
        return True


def 게임스따뚜():  # 게임을 돌리는 함수입니다.
    global 숫자의수, 시도횟수, 말한횟수
    숫자의수 = 3
    시도횟수 = 10
    말한횟수 = 0


print("-" * 80)
print("내가 3자리의 숫자를 생각했어 이게 뭔지 맞혀볼래?")
print("음.. 단서들에 대해 설명해줄게")
print("스트~라이크! 는 위치와 숫자가 모두 맞은 것의 개수야")
print("붤. 은 위치는 틀렸지만 맞은 숫자의 개수를 말해")
print("아_웃 은 너가 말한 숫자중 내가 생각한 숫자에 없는 숫자의 개수야")
print("알겠지??? 이제 시작한다?? GOGOGOGOGOGOGOGO!")
print("-" * 80)

while True:
    정답 = 정답숫자함수(숫자의수)
    print("너는 %s 번 시도할 수 있어" % (11 - 말한횟수))

    while 말한횟수 <= 시도횟수:
        대답 = ' '
        print("%s번째 시도야" % (말한횟수 + 1))  # 시도한 횟수를 알려주고 0에서9사이의 수가 아닌경우 재입력받습니다.
        추측 = input()
        while (len(추측) != 숫자의수) or (not 추측.isdecimal()):
            print("아니 친구야 0에서 9까지의 정수 3개를 입력해야지")
            print("%s번째 시도야" % (말한횟수 + 1))
            추측 = input()
        print(판단(추측, 정답))
        말한횟수 += 1

        if 추측 == 정답:
            break
    if 말한횟수 > 시도횟수:
        print("이제 기회는 모두 끝났어 정답은 %s야. 한번 더 해볼래? 할거면 ㅇㅇ 아니면 ㄴㄴ를 쳐줘." % 정답)
        대답 = input()

    if 대답 == 'ㅇㅇ':
        게임스따뚜()
    else:
        break
