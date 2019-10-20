import random

Owin = 0
Xwin = 0
gameturn = 0


class Tictactoe:
    def __init__(self):
        self.x0y0 = 0
        self.x1y0 = 0
        self.x2y0 = 0
        self.x0y1 = 0
        self.x1y1 = 0
        self.x2y1 = 0
        self.x0y2 = 0
        self.x1y2 = 0
        self.x2y2 = 0
    # 틱택토 판을 객체로 생성, 좌표가 비었으면 0, O면 1, X면 2로 값을 표시


selff = Tictactoe()


def clean():
    global selff
    selff.x0y0 = 0
    selff.x1y0 = 0
    selff.x2y0 = 0
    selff.x0y1 = 0
    selff.x1y1 = 0
    selff.x2y1 = 0
    selff.x0y2 = 0
    selff.x1y2 = 0
    selff.x2y2 = 0


# 틱택토 게임 재시작을 위한 초기화 함수


def checkcheck(check):
    if check == 1:
        print("O", end='')
    elif check == -1:
        print("X", end='')
    else:
        print(" ", end='')
    # 주어진 x,y 좌표가 비었는지, O인지, X인지 체크해서 출력하는 코드


def Ticprint():
    global selff
    tictactoe = selff
    print("-----------")
    print(" ", end='')

    checkcheck(tictactoe.x0y0)

    print(" | ", end='')

    checkcheck(tictactoe.x1y0)

    print(" | ", end='')

    checkcheck(tictactoe.x2y0)

    print(" ")
    # 첫 줄 출력

    print("-----------")
    print(" ", end='')
    checkcheck(tictactoe.x0y1)

    print(" | ", end='')

    checkcheck(tictactoe.x1y1)

    print(" | ", end='')

    checkcheck(tictactoe.x2y1)

    print(" ")
    # 둘째 줄 출력

    print("-----------")
    print(" ", end='')
    checkcheck(tictactoe.x0y2)

    print(" | ", end='')

    checkcheck(tictactoe.x1y2)

    print(" | ", end='')

    checkcheck(tictactoe.x2y2)

    print(" ")
    print("\n")
    # 각 자리를 출력해서 틱택토를 출력하는 코드


def win_check():
    global Owin
    global Xwin
    global selff
    if selff.x0y0 + selff.x1y0 + selff.x2y0 == 3:
        Owin = Owin + 1
        print("O 승리! (O 승점 : ", end='')
        print(Owin, end='')
        print(")")
        print("(X승점 : ", end='')
        print(Xwin, end='')
        print(")")
        return 1
    elif selff.x0y0 + selff.x1y0 + selff.x2y0 == -3:
        Xwin = Xwin + 1
        print("X 승리! (X승점 : ", end='')
        print(Xwin, end='')
        print(")")
        print("(O 승점 : ", end='')
        print(Owin, end='')
        print(")")
        return 2
        # 가로 첫째줄

    if selff.x0y1 + selff.x1y1 + selff.x2y1 == 3:
        Owin = Owin + 1
        print("O 승리! (O 승점 : ", end='')
        print(Owin, end='')
        print(")")
        print("(X승점 : ", end='')
        print(Xwin, end='')
        print(")")
        return 1
    elif selff.x0y1 + selff.x1y1 + selff.x2y1 == -3:
        Xwin = Xwin + 1
        print("X 승리! (X승점 : ", end='')
        print(Xwin, end='')
        print(")")
        print("(O 승점 : ", end='')
        print(Owin, end='')
        print(")")
        return 2
        # 가로 둘째줄

    if selff.x0y2 + selff.x1y2 + selff.x2y2 == 3:
        Owin = Owin + 1
        print("O 승리! (O 승점 : ", end='')
        print(Owin, end='')
        print(")")
        print("(X승점 : ", end='')
        print(Xwin, end='')
        print(")")
        return 1
    elif selff.x0y2 + selff.x1y2 + selff.x2y2 == -3:
        Xwin = Xwin + 1
        print("X 승리! (X승점 : ", end='')
        print(Xwin, end='')
        print(")")
        print("(O 승점 : ", end='')
        print(Owin, end='')
        print(")")
        return 2
        # 가로 세째줄

    if selff.x0y0 + selff.x0y1 + selff.x0y2 == 3:
        Owin = Owin + 1
        print("O 승리! (O 승점 : ", end='')
        print(Owin, end='')
        print(")")
        print("(X승점 : ", end='')
        print(Xwin, end='')
        print(")")
        return 1
    elif selff.x0y0 + selff.x0y1 + selff.x0y2 == -3:
        Xwin = Xwin + 1
        print("X 승리! (X승점 : ", end='')
        print(Xwin, end='')
        print(")")
        print("(O 승점 : ", end='')
        print(Owin, end='')
        print(")")
        return 2
        # 세로 첫째줄

    if selff.x1y0 + selff.x1y1 + selff.x1y2 == 3:
        Owin = Owin + 1
        print("O 승리! (O 승점 : ", end='')
        print(Owin, end='')
        print(")")
        print("(X승점 : ", end='')
        print(Xwin, end='')
        print(")")
        return 1
    elif selff.x1y0 + selff.x1y1 + selff.x1y2 == -3:
        Xwin = Xwin + 1
        print("X 승리! (X승점 : ", end='')
        print(Xwin, end='')
        print(")")
        print("(O 승점 : ", end='')
        print(Owin, end='')
        print(")")
        return 2
        # 세로 둘째줄

    if selff.x2y0 + selff.x2y1 + selff.x2y2 == 3:
        Owin = Owin + 1
        print("O 승리! (O 승점 : ", end='')
        print(Owin, end='')
        print(")")
        print("(X승점 : ", end='')
        print(Xwin, end='')
        print(")")
        return 1
    elif selff.x2y0 + selff.x2y1 + selff.x2y2 == -3:
        Xwin = Xwin + 1
        print("X 승리! (X승점 : ", end='')
        print(Xwin, end='')
        print(")")
        print("(O 승점 : ", end='')
        print(Owin, end='')
        print(")")
        return 2
        # 세로 셋째줄

    if selff.x0y0 + selff.x1y1 + selff.x2y2 == 3:
        Owin = Owin + 1
        print("O 승리! (O 승점 : ", end='')
        print(Owin, end='')
        print(")")
        print("(X승점 : ", end='')
        print(Xwin, end='')
        print(")")
        return 1
    elif selff.x0y0 + selff.x1y1 + selff.x2y2 == -3:
        Xwin = Xwin + 1
        print("X 승리! (X승점 : ", end='')
        print(Xwin, end='')
        print(")")
        print("(O 승점 : ", end='')
        print(Owin, end='')
        print(")")
        return 2

    if selff.x0y2 + selff.x1y1 + selff.x2y0 == 3:
        Owin = Owin + 1
        print("O 승리! (O 승점 : ", end='')
        print(Owin, end='')
        print(")")
        print("(X승점 : ", end='')
        print(Xwin, end='')
        print(")")
        return 1
    elif selff.x0y2 + selff.x1y1 + selff.x2y0 == -3:
        Xwin = Xwin + 1
        print("X 승리! (X승점 : ", end='')
        print(Xwin, end='')
        print(")")
        print("(O 승점 : ", end='')
        print(Owin, end='')
        print(")")
        return 2

    return 0
    # 게임을 이겼는지 판단하는 함수


def checkerror(x, y):
    global selff
    if x == 0:
        if y == 0:
            if selff.x0y0 != 0:
                return 1
            else:
                return 0
        elif y == 1:
            if selff.x0y1 != 0:
                return 1
            else:
                return 0
        elif y == 2:
            if selff.x0y2 != 0:
                return 1
            else:
                return 0

    elif x == 1:
        if y == 0:
            if selff.x1y0 != 0:
                return 1
            else:
                return 0
        elif y == 1:
            if selff.x1y1 != 0:
                return 1
            else:
                return 0
        elif y == 2:
            if selff.x1y2 != 0:
                return 1
            else:
                return 0

    elif x == 2:
        if y == 0:
            if selff.x2y0 != 0:
                return 1
            else:
                return 0
        elif y == 1:
            if selff.x2y1 != 0:
                return 1
            else:
                return 0
        elif y == 2:
            if selff.x2y2 != 0:
                return 1
            else:
                return 0
    # 지정한 칸이 비어있는지 확인하는 함수


def ticinput(x, y, ox):
    global selff
    if x == 0:
        if y == 0:
            selff.x0y0 = ox
        elif y == 1:
            selff.x0y1 = ox
        elif y == 2:
            selff.x0y2 = ox

    elif x == 1:
        if y == 0:
            selff.x1y0 = ox
        elif y == 1:
            selff.x1y1 = ox
        elif y == 2:
            selff.x1y2 = ox

    elif x == 2:
        if y == 0:
            selff.x2y0 = ox
        elif y == 1:
            selff.x2y1 = ox
        elif y == 2:
            selff.x2y2 = ox
    # 빈칸에 O,X를 입력하는 함수


def dangercheck():
    global Owin
    global Xwin
    global selff
    if selff.x0y0 + selff.x1y0 + selff.x2y0 == -2:
        if checkerror(0, 0) == 0:
            selff.x0y0 = -1
            return 1
        elif checkerror(1, 0) == 0:
            selff.x1y0 = -1
            return 1
        elif checkerror(2, 0) == 0:
            selff.x2y0 = -1
            return 1

    if selff.x0y1 + selff.x1y1 + selff.x2y1 == -2:
        if checkerror(0, 1) == 0:
            selff.x0y1 = -1
            return 1
        elif checkerror(1, 1) == 0:
            selff.x1y1 = -1
            return 1
        elif checkerror(2, 1) == 0:
            selff.x2y1 = -1
            return 1

    if selff.x0y2 + selff.x1y2 + selff.x2y2 == -2:
        if checkerror(0, 2) == 0:
            selff.x0y2 = -1
            return 1
        elif checkerror(1, 2) == 0:
            selff.x1y2 = -1
            return 1
        elif checkerror(2, 2) == 0:
            selff.x2y2 = -1
            return 1

    if selff.x0y0 + selff.x0y1 + selff.x0y2 == -2:
        if checkerror(0, 0) == 0:
            selff.x0y0 = -1
            return 1
        elif checkerror(0, 1) == 0:
            selff.x0y1 = -1
            return 1
        elif checkerror(0, 2) == 0:
            selff.x0y2 = -1
            return 1

    if selff.x1y0 + selff.x1y1 + selff.x1y2 == -2:
        if checkerror(1, 0) == 0:
            selff.x1y0 = -1
            return 1
        elif checkerror(1, 1) == 0:
            selff.x1y1 = -1
            return 1
        elif checkerror(1, 2) == 0:
            selff.x1y2 = -1
            return 1

    if selff.x2y0 + selff.x2y1 + selff.x2y2 == -2:
        if checkerror(2, 0) == 0:
            selff.x2y0 = -1
            return 1
        elif checkerror(2, 1) == 0:
            selff.x2y1 = -1
            return 1
        elif checkerror(2, 2) == 0:
            selff.x2y2 = -1
            return 1

    if selff.x0y0 + selff.x1y1 + selff.x2y2 == -2:
        if checkerror(0, 0) == 0:
            selff.x0y0 = -1
            return 1
        elif checkerror(1, 1) == 0:
            selff.x1y1 = -1
            return 1
        elif checkerror(2, 2) == 0:
            selff.x2y2 = -1
            return 1

    if selff.x0y2 + selff.x1y1 + selff.x2y0 == -2:
        if checkerror(0, 2) == 0:
            selff.x0y2 = -1
            return 1
        elif checkerror(1, 1) == 0:
            selff.x1y1 = -1
            return 1
        elif checkerror(2, 0) == 0:
            selff.x2y0 = -1
            return 1

    # ddd
    if selff.x0y0 + selff.x1y0 + selff.x2y0 == 2:
        if checkerror(0, 0) == 0:
            selff.x0y0 = -1
            return 1
        elif checkerror(1, 0) == 0:
            selff.x1y0 = -1
            return 1
        elif checkerror(2, 0) == 0:
            selff.x2y0 = -1
            return 1

    if selff.x0y1 + selff.x1y1 + selff.x2y1 == 2:
        if checkerror(0, 1) == 0:
            selff.x0y1 = -1
            return 1
        elif checkerror(1, 1) == 0:
            selff.x1y1 = -1
            return 1
        elif checkerror(2, 1) == 0:
            selff.x2y1 = -1
            return 1

    if selff.x0y2 + selff.x1y2 + selff.x2y2 == 2:
        if checkerror(0, 2) == 0:
            selff.x0y2 = -1
            return 1
        elif checkerror(1, 2) == 0:
            selff.x1y2 = -1
            return 1
        elif checkerror(2, 2) == 0:
            selff.x2y2 = -1
            return 1

    if selff.x0y0 + selff.x0y1 + selff.x0y2 == 2:
        if checkerror(0, 0) == 0:
            selff.x0y0 = -1
            return 1
        elif checkerror(0, 1) == 0:
            selff.x0y1 = -1
            return 1
        elif checkerror(0, 2) == 0:
            selff.x0y2 = -1
            return 1

    if selff.x1y0 + selff.x1y1 + selff.x1y2 == 2:
        if checkerror(1, 0) == 0:
            selff.x1y0 = -1
            return 1
        elif checkerror(1, 1) == 0:
            selff.x1y1 = -1
            return 1
        elif checkerror(1, 2) == 0:
            selff.x1y2 = -1
            return 1

    if selff.x2y0 + selff.x2y1 + selff.x2y2 == 2:
        if checkerror(2, 0) == 0:
            selff.x2y0 = -1
            return 1
        elif checkerror(2, 1) == 0:
            selff.x2y1 = -1
            return 1
        elif checkerror(2, 2) == 0:
            selff.x2y2 = -1
            return 1

    if selff.x0y0 + selff.x1y1 + selff.x2y2 == 2:
        if checkerror(0, 0) == 0:
            selff.x0y0 = -1
            return 1
        elif checkerror(1, 1) == 0:
            selff.x1y1 = -1
            return 1
        elif checkerror(2, 2) == 0:
            selff.x2y2 = -1
            return 1

    if selff.x0y2 + selff.x1y1 + selff.x2y0 == 2:
        if checkerror(0, 2) == 0:
            selff.x0y2 = -1
            return 1
        elif checkerror(1, 1) == 0:
            selff.x1y1 = -1
            return 1
        elif checkerror(2, 0) == 0:
            selff.x2y0 = -1
            return 1
    return 0
    # 컴퓨터가 이길 수 있거나 두지 않으면 지는 위치가 있으면 거기를 우선적으로 두는 함수


def randompic():
    global selff
    while (1):
        xx = random.randrange(0, 3)
        yy = random.randrange(0, 3)

        if checkerror(xx, yy) == 0:
            ticinput(xx, yy, -1)
            break


# 위험하지 않은 상황일때 컴퓨터가 랜덤한 위치에 두도록 하는 함수


def oneturn():
    global selff
    global Owin
    global Xwin
    global gameturn

    gameturn = gameturn + 1

    try:
        if gameturn == 5:
            Ticprint()
            print("무승부")
            print("(O 승점 : ", end='')
            print(Owin, end='')
            print(")")
            print("(X승점 : ", end='')
            print(Xwin, end='')
            print(")")
            return 1

        x, y = map(int, input().split(','))
        if checkerror(x, y) == 1:
            raise Exception
        ticinput(x, y, 1)
        Ticprint()

        if win_check() != 0:
            return 1

        if dangercheck() == 1:
            pass
        else:
            randompic()

        Ticprint()
        if win_check() != 0:
            return 1

        return 0

    except Exception:
        print('다시 입력하세요!')
        gameturn = gameturn - 1
        if gameturn < 0:
            gameturn = 0
        return 0
    # 사용자와 컴퓨터가 각각 한 번씩 두는 셋트


def gameplay():
    global gameturn
    clean()
    gameturn = 0
    while (1):
        if oneturn() == 1:
            break
    try:
        print("한 판 더? (Y/N)")
        ans = input()
        if ans == 'Y':
            Ticplay()
            gameplay()
        elif ans == 'N':
            print("ㅂㅇ")
    except Exception:
        print("잘못 입력함 ㅂㅇ")
    # 게임의 메인 파일. 다시 시작 여부또한 판별


Ticprint()
gameplay()
