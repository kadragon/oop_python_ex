import random  # 컴퓨터가 놓을 곳을 랜덤으로 정하기 위함
import time  # 대사가 시간차로 나오도록 하기 위함

T = 0  # 총 게임 시행 횟수
W = 0  # 사용자가 이긴 횟수
COM = ''  # 컴퓨터의 말을 저장하는 변수
USER = ''  # 사용자의 말을 저장하는 변수
State = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]  # 게임판의 상태를 저장하는 리스트


def nextlocation():  # 컴퓨터가 다음 놓을 자리를 정하는 함수
    flag = 0
    global State
    for i in range(1, 10):  # 사용자가 이기는 자리를 찾는 for문
        if State[i] != 'O' and State[i] != 'X':
            State[i] = USER
            if gameover() == 1:
                State[i] = i
                return i
            State[i] = i
    L = list(range(1, 10))  # 사용자가 이기는 자리가 없을 때 랜덤으로 놓을 자리를 결정
    random.shuffle(L)
    for i in L:
        if State[i] != 'O' and State[i] != 'X':
            return i


def nowstate():  # 현재 상태를 출력하는 함수
    print("=============")
    print("| %s | %s | %s |" % (State[1], State[2], State[3]))
    print("=============")
    print("| %s | %s | %s |" % (State[4], State[5], State[6]))
    print("=============")
    print("| %s | %s | %s |" % (State[7], State[8], State[9]))
    print("=============")


def replay():  # 다시 플레이 할지 물어보는 함수
    global T, State
    check = input()
    if check != 'y' and check != 'n':  # 잘못된 입력
        print("잘못된 입력입니다. y / n 만 입력해 주세요.")
        replay()
    elif check == 'y':  # 다시플레이한다
        for i in range(1, 10):
            State[i] = i
        playgame()
    elif check == 'n':  # 다시 플레이하지 않는다
        print("즐거운 시간이었습니다. 안녕히가세요.")


def winpercent():  # 승률을 반환하는 함수
    global T, W
    return W / T * 100


def rule():  # 규칙을 설명해주는 함수
    check = input()
    if check != 'y' and check != 'n':  # 잘못된 입력
        print("잘못된 입력입니다. y / n 만 입력해 주세요.")
        rule()
    elif check == 'y':  # 규칙을 안다고 답함
        print("규칙을 아시는 군요. 그렇다면 게임을 플레이 하시겠습니까? ( y / n )")
        startgame()
    elif check == 'n':  # 규칙을 모른다고 답함
        print("TicTacToe 게임은 3X3 게임판에서 하는 게임입니다.")
        print("두명이서 돌아가며 돌을 놓게 되며, 3개의 연속된 돌을 놓은 사람이 이기는 규칙입니다.")
        print("연속된 돌을 판단할 때 대각선으로 놓은 돌도 인정됩니다.")
        time.sleep(1.5)
        print("규칙에 대한 설명을 들으셨는데, 게임을 플레이 하시겠습니까? ( y / n )")
        startgame()


def startgame():  # 게임 시작하는 함수
    check = input()
    if check != 'y' and check != 'n':  # 잘못된 입력
        print("잘못된 입력입니다. y / n 만 입력해 주세요.")
        startgame()
    elif check == 'y':  # 게임을 한다고 답함
        playgame()
    elif check == 'n':  # 게임을 하고 싶지 않다고 답함
        print("게임을 플레이하고싶지 않으시군요. 그럼 다음에 뵙겠습니다.")
        time.sleep(1)
        print("안녕히가세요.")


def playgame():  # 게임을 플레이하는 함수
    global T
    print("그럼, 게임을 시작하겠습니다.")
    time.sleep(1)
    print("당신의 말을 선택하세요 ( O / X )")
    choose()
    print("좋습니다. 당신은 %s 말을 선택하셨습니다." % USER)
    if USER == 'X':  # 사용자가 X 말 선택 선공
        print("당신은 X 말을 선택하셨기 때문에, 당신의 공격으로 게임을 시작합니다.")
        T += 1
        play()
    elif USER == 'O':  # 사용자가 O 말 선택 후공
        print("당신은 O 말을 선택하셨기 때문에, 컴퓨터의 공격으로 게임을 시작합니다.")
        time.sleep(1)
        print("컴퓨터 공격 중...")
        time.sleep(1)
        State[nextlocation()] = COM
        T += 1
        play()


def gameover():  # 게임이 끝났는지 알아보는 함수
    for i in range(3):  # 가로 세로로 게임이 끝날 조건을 만족했는지 본다
        if State[i * 3 + 1] == State[i * 3 + 2] == State[i * 3 + 3] == USER:
            return 1
        elif State[i * 3 + 1] == State[i * 3 + 2] == State[i * 3 + 3] == COM:
            return 2
        elif State[i + 1] == State[i + 4] == State[i + 7] == USER:
            return 1
        elif State[i + 1] == State[i + 4] == State[i + 7] == COM:
            return 2
    if State[1] == State[5] == State[9] == USER:  # 대각선으로 게임이 끝날 조건을 만족했는지 본다
        return 1
    elif State[1] == State[5] == State[9] == COM:
        return 2
    elif State[3] == State[5] == State[7] == USER:
        return 1
    elif State[3] == State[5] == State[7] == COM:
        return 2
    flag = 0
    for i in range(1, 10):  # 판에 더이상 둘 곳이 없는지 본다
        if State[i] != 'O' and State[i] != 'X':
            flag += 1
    if flag == 0:
        return 3
    return 0


def play():  # 게임이 진짜 플레이되는 함수
    global W
    while gameover() == 0:  # 게임이 끝날 때까지 반복
        nowstate()
        print("당신의 차례입니다. 말을 놓고 싶은 위치를 입력하세요. ( 1 ~ 9 )")
        userturn()
        if gameover() == 1:  # 사용자가 승리함
            nowstate()
            print("당신의 승리입니다! 축하드립니다.")
            W += 1
            time.sleep(1)
            print("당신의 승률은 %.2f percent 입니다." % float(winpercent()))
            time.sleep(1)
            print("다시 플레이 하시겠습니까? ( y / n )")
            replay()
            return
        elif gameover() == 3:  # 무승부
            nowstate()
            print("아쉽습니다. 무승부네요.")
            time.sleep(1)
            print("당신의 승률은 %.2f percent 입니다." % float(winpercent()))
            time.sleep(1)
            print("다시 플레이 하시겠습니까? ( y / n )")
            replay()
            return
        print("컴퓨터 공격중...")
        time.sleep(1)
        State[nextlocation()] = COM
        if gameover() == 2:  # 컴퓨터 승리
            nowstate()
            print("당신의 패배입니다! 정말 아쉽네요.")
            time.sleep(1)
            print("당신의 승률은 %.2f percent 입니다." % float(winpercent()))
            time.sleep(1)
            print("다시 플레이 하시겠습니까? ( y / n )")
            replay()
            return
        if gameover() == 3:  # 무승부
            nowstate()
            print("아쉽습니다. 무승부네요.")
            time.sleep(1)
            print("당신의 승률은 %.2f percent 입니다." % float(winpercent()))
            time.sleep(1)
            print("다시 플레이 하시겠습니까? ( y / n )")
            replay()
            return


def userturn():  # 사용자가 말을 놓을 곳을 정하는 함수
    check = input()
    if check != '1' and check != '2' and check != '3' and check != '4' and check != '5' and check != '6' and check != '7' and check != '8' and check != '9':
        print("잘못된 입력입니다. 1 ~ 9 사이의 숫자만 입력해 주세요.")  # 잘못된 입력
        print("다시 선택해 주세요. ( 1 ~ 9 )")
        userturn()
    elif subcheck(check) == 1:  # 이미 말이 놓여있는 곳
        print("잘못된 입력입니다. 이미 말이 있는 곳에는 놓을 수 없습니다.")
        print("다시 선택해 주세요. ( 1 ~ 9 )")
        userturn()
    else:  # 말을 놓아도 되는 곳
        State[int(check)] = USER


def subcheck(check):  # 이미 말이 놓여있는지 확인하는 함수
    if State[int(check)] == 'O' or State[int(check)] == 'X':
        return 1
    else:
        return 0


def choose():  # 사용자가 O, X 중 말을 고르는 함수
    global COM, USER
    check = input()
    if check != 'O' and check != 'X':
        print("잘못된 입력입니다. O / X 만 입력해주세요.")
        choose()
    elif check == 'O':
        COM = 'X'
        USER = 'O'
    elif check == 'X':
        COM = 'O'
        USER = 'X'


print("TicTacToe 게임에 오신걸 환영합니다.")
time.sleep(1)
print("게임 규칙을 아시나요? ( y / n )")
rule()
