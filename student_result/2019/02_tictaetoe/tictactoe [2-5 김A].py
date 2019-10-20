# 틱택토

import random

start = 1  # 순서 결정
key = 0  # 경기 상태 및 누가 이겼는지
my = ''  # 나의 말
com = ''  # 컴퓨터의 말
map = [' '] * 10  # 판
win = 0  # 승 수
lose = 0  # 패 수
turn = 0  # 말 수
draw = 0  # 비긴 수


def figure():  # 사용자의 말 종류 고르기
    global my, com
    com = 1
    while 1:
        my = input()  # 원하는 말 선택
        if my == 'X':
            com = 'O'
            return  # 선택 후 종료
        elif my == 'O':
            com = 'X'
            return
        else:  # O,X가 아닐 시 다시 입력
            print("Input data should be X or O !!")
            print("Try again")


def order():  # 순서 랜덤 설정
    global start
    num = list(range(2))
    random.shuffle(num)
    start = num[0]


def attack():  # 내 공격 차례
    global start
    global my
    start = 0
    print("어디에 넣고 싶어 ?")
    want = input()  # 원하는 자리 입력
    try:
        if want > '9' and want < '1':  # 0~9 까지의 수가 아닐 시 다시 입력
            print("1~9까지 숫자 중에 입력해 주세요")
            return attack()
        if map[int(want)] != ' ':  # 비어 있지 않을 시 다시 입력
            print("비어있는 곳에 숫자를 넣어주세요 !!")
            return attack()

        map[int(want)] = my  # 원하는 곳에
    except:  # 숫자가 아닐 시 다시 입력
        print("숫자를 입력하세요 !!")
        return attack()


def attacked():
    global com
    global my
    global map
    global start

    start = 1
    number = list(range(9))
    random.shuffle(number)
    for i in range(9):  # 필승 자리 탐색
        if map[i + 1] == ' ':
            map[i + 1] = com
            if check() == 2:
                map[i + 1] = com
                return
            map[i + 1] = ' '
    for i in range(9):  # 필패 자리 탐색
        if map[i + 1] == ' ':
            map[i + 1] = my
            if check() == 1:
                map[i + 1] = com
                return
            map[i + 1] = ' '
    for i in range(9):  # 랜덤으로 자리 배정
        if map[number[i] + 1] == ' ':
            map[number[i] + 1] = com
            return


lines = [[1, 2, 3], [4, 5, 6], [7, 8, 9], [1, 4, 7], [2, 5, 8], [3, 6, 9], [1, 5, 9], [3, 5, 7]]  # 이길 수 있는 자리 모음


def check():
    global win
    global lose
    global map
    global finish

    finish = 0
    for i in lines:
        if map[i[0]] == map[i[1]] == map[i[2]]:
            if map[i[0]] == ' ':
                continue
            if map[i[0]] == my:  # 내가 이김
                win += 1
                finish = 1
            if map[i[1]] == com:  # 컴이 이김
                lose += 1
                finish = 2
    return finish  # 누가 이겼는지 반환


def again():  # 게임 다시 할거니?
    global key
    global map
    global turn
    print("게임을 한 번 더 하시겠습니까? (Y/N)")
    yorn = input()  # 의사를 보여줘
    if yorn == 'Y':  # 게임 다시 실행
        key = 0
        map = [' '] * 10
        turn = 0
    elif yorn == 'N':  # 게임 종료
        return
    else:  # Y,N 이 아닐 경우 다시 입력
        print("Y 또는 N를 입력해주세요")
        return again()


def P_win():  # 승률 출력 함수
    if lose == 0 and win == 0 and draw == 0:  # 게임을 한판도 안했을 시
        return
    else:  # 승률 출력
        print("현재 승률은 %d 입니다 !!" % (win / (win + lose + draw)))


def printf():  # 판상태 출력
    print("---------------")
    print("| %c | %c | %c |" % (map[1], map[2], map[3]))
    print("---------------")
    print("| %c | %c | %c |" % (map[4], map[5], map[6]))
    print("---------------")
    print("| %c | %c | %c |" % (map[7], map[8], map[9]))
    print("---------------")


print("What do you want to be?  X or O ?? :")
figure()
while key == 0:
    order()
    while key == 0:
        if turn >= 9:  # 비긴 경우(말 수가 9번 이상)
            key = 3
            draw += 1
            break
        printf()
        if start:  # 내 차례인 경우
            attack()
        else:  # 컴 차례인 경우
            attacked()
        key = check()  # 누가 이겼는지 체크
        if key == 1:  # 내가 이김
            print("당신이 이겼어요 ~!")
        elif key == 2:  # 컴이 이김
            print("바보 ! 당신은 졌어요 ㅜㅠㅠㅠ")
        turn += 1
    if key == 3:  # 비김
        print("당신은 비겼어요")

    P_win()  # 승률 출력
    again()  # 다시 할거임?
