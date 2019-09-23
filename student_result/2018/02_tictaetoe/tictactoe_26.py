map = [[' '] * 4 for i in range(4)]  # 게임 플레이용 맵 선언
User = ' '
Com = ' '
play = 1
full = 0
WhoseTurn = 0


def Reset():  # 게임 시작 전 재설정
    global User
    global Com
    global play
    global full
    global WhoseTurn
    print("\n\n\nSTART NEW TIATACTOE GAME")  # 게임 시작 알림
    map = [[' '] * 4 for i in range(4)]  # 맵 초기화
    User = 'X'
    Com = 'O'  # 사용할 마커 저장. 기본값은 플레이어가 X 마커
    full = 0  # 게임 진척도 저장. 판이 다 차있으면 승리판정 시행
    WhoseTurn = 1  # 누구 턴인지 판별. 기본값은 플레이어 선공. 2로 나눈 나머지로 판별함


def isOK(x, y):  # 놓아도 되는지 확인
    if x < 0 or x > 2 or y < 0 or y > 2:  # 들어온 자릿값이 이상하면 0 반환
        return 0
    elif map[x][y] != ' ':  # 이미 채워진 자리면 0 반환
        return 0
    else:  # 문제없으면 1 반환
        return 1


# 메인 출력함수
def mapper(x, y, v):  # 위치정보, 놓을 말 받음
    global map
    map[x][y] = v
    global full
    full = full + 1  # 채워진 칸의 수 세기 - 게임 진행률 파악

    # 변화한 맵 출력
    print("[%c|%c|%c]" % (map[0][0], map[0][1], map[0][2]))
    print("[%c|%c|%c]" % (map[1][0], map[1][1], map[1][2]))
    print("[%c|%c|%c]" % (map[2][0], map[2][1], map[2][2]))


def SelectMarker():  # 마커 선택 함수
    global User
    global Com
    global WhoseTurn
    print("Please Select Your Mark. First Attack is X. (X or O)")
    while 1:
        Select = input().upper()  # 플레이어의 마커 고르기
        if (Select != 'X') and (Select != 'O'):  # 잘못된 입력 배제
            print("Please Select Again. ex) 'X' 'O' 'x' 'o'")
        else:
            if Select == 'X':  # 사용자의 입력에 따라 값을 반환합니다.
                User = 'X'
                WhoseTurn = 1  # X가 선공이므로 플레이어 선공으로 설정
                Com = 'O'
            else:
                User = 'O'
                WhoseTurn = 0  # O가 후공이므로 플레이어 후공으로 설정
                Com = 'X'
        return


# 플레이어 차례에 실행되는 함수
def user_turn():
    print("Your Turn")
    while 1:
        print("Where do you input? ex) '1 3' '2 2'")
        position = (input().split())  # 문자형으로 띄어쓰기 제거해 입력받음
        x = int(position[0]) - 1  # 문자형을 정수형으로 바꿈
        y = int(position[1]) - 1

        # 잘못된 입력 배제
        if isOK(x, y) == 0:
            print("Please Write Again. ex) '1 3' '2 2'")
        else:
            mapper(x, y, User)  # 위치값과 마커를 출력함수에 전달
            return  # 턴을 넘긴다


# 컴퓨터 차례에 실행되는 함수
def computer_turn():
    doX = -1  # 컴퓨터가 놓아야 할 곳
    doY = -1
    print("Computer Turn")

    # 완성 가능한지 전체탐색
    for i in range(0, 3):
        if (map[i][0] == map[i][1] == Com) and (isOK(i, 2)):
            doX = i
            doY = 2
            break
        elif (map[i][0] == map[i][2] == Com) and (isOK(i, 1)):
            doX = i
            doY = 1
            break
        elif (map[i][1] == map[i][2] == Com) and (isOK(i, 0)):
            doX = i
            doY = 0
            break
        elif (map[0][i] == map[1][i] == Com) and (isOK(2, i)):
            doX = 2
            doY = i
            break
        elif (map[0][i] == map[2][i] == Com) and (isOK(1, i)):
            doX = 1
            doY = i
            break
        elif (map[1][i] == map[2][i] == Com) and (isOK(0, i)):
            doX = 0
            doY = i
            break
    if (map[0][0] == map[1][1] == Com) and (isOK(2, 2)):
        doX = 2
        doY = 2
    elif (map[0][0] == map[2][2] == Com) and (isOK(1, 1)):
        doX = 1
        doY = 1
    elif (map[1][1] == map[2][2] == Com) and (isOK(0, 0)):
        doX = 0
        doY = 0
    elif (map[2][0] == map[1][1] == Com) and (isOK(0, 2)):
        doX = 0
        doY = 2
    elif (map[2][0] == map[0][2] == Com) and (isOK(1, 1)):
        doX = 1
        doY = 1
    elif (map[1][1] == map[0][2] == Com) and (isOK(2, 0)):
        doX = 2
        doY = 0
    if doX != -1:  # 만약 공격 가능한 곳이 있다면
        mapper(doX, doY, Com)  # 놓은 뒤
        return  # 턴 넘김


    else:  # 공격할 곳이 없다면
        for i in range(0, 3):  # 막을 곳 찾기
            if (map[i][0] == map[i][1] == User) and (isOK(i, 2)):
                doX = i
                doY = 2
                break
            elif (map[i][0] == map[i][2] == User) and (isOK(i, 1)):
                doX = i
                doY = 1
                break
            elif (map[i][1] == map[i][2] == User) and (isOK(i, 0)):
                doX = i
                doY = 0
                break
            elif (map[0][i] == map[1][i] == User) and (isOK(2, i)):
                doX = 2
                doY = i
                break
            elif (map[0][i] == map[2][i] == User) and (isOK(1, i)):
                doX = 1
                doY = i
                break
            elif (map[1][i] == map[2][i] == User) and (isOK(0, i)):
                doX = 0
                doY = i
                break
        if (map[0][0] == map[1][1] == User) and (isOK(2, 2)):
            doX = 2
            doY = 2
        elif (map[0][0] == map[2][2] == User) and (isOK(1, 1)):
            doX = 1
            doY = 1
        elif (map[1][1] == map[2][2] == User) and (isOK(0, 0)):
            doX = 0
            doY = 0
        elif (map[2][0] == map[1][1] == User) and (isOK(0, 2)):
            doX = 0
            doY = 2
        elif (map[2][0] == map[0][2] == User) and (isOK(1, 1)):
            doX = 1
            doY = 1
        elif (map[1][1] == map[0][2] == User) and (isOK(2, 0)):
            doX = 2
            doY = 0

        if (doX != -1):  # 만약 막아야 할 곳이 있다면
            mapper(doX, doY, Com)  # 놓은 뒤
            return  # 턴을 넘김

    # 최적전략에 알맞게 귀,변,중앙 순으로 가능한 위치를 탐색
    while 1:
        if isOK(0, 0):
            doX = 0
            doY = 0
        elif isOK(0, 2):
            doX = 0
            doY = 2
        elif isOK(2, 0):
            doX = 2
            doY = 0
        elif isOK(2, 2):
            doX = 2
            doY = 2
        elif isOK(1, 0):
            doX = 1
            doY = 0
        elif isOK(0, 1):
            doX = 0
            doY = 1
        elif isOK(2, 1):
            doX = 2
            doY = 1
        elif isOK(1, 2):
            doX = 1
            doY = 2
        elif isOK(1, 1):
            doX = 1
            doY = 1
        mapper(doX, doY, Com)  # 놓은 뒤
        return  # 턴을 넘김


# 다시 플레이 할지 묻는 함수 - play 값을 수정 가능한 유일한 함수임
def PlayAgain():
    while 1:  # 잘못된 입력 배제
        print("Play Again? Y or N")
        r = input().upper()
        if r == 'Y':
            play = 1  # 플레이 상태 유지
            return
        elif r == 'N':
            play = 0  # 플레이 상태 꺼짐
            return
        else:
            print("Please Input Again. ex) 'Y' 'y' 'N' 'n'")


def win():  # 승리한 마커를 반환
    if (map[0][0] == map[0][1]) and (map[0][1] == map[0][2]):
        return map[0][0]
    elif (map[1][0] == map[1][1]) and (map[1][1] == map[1][2]):
        return map[1][0]
    elif (map[2][0] == map[2][1]) and (map[2][1] == map[2][2]):
        return map[2][0]
    elif (map[0][0] == map[1][0]) and (map[1][0] == map[2][0]):
        return map[0][0]
    elif (map[0][1] == map[1][1]) and (map[1][1] == map[2][1]):
        return map[0][1]
    elif (map[0][2] == map[1][2]) and (map[1][2] == map[2][2]):
        return map[0][2]
    elif (map[0][0] == map[1][1]) and (map[1][1] == map[2][2]):
        return map[0][0]
    elif (map[0][2] == map[1][1]) and (map[1][1] == map[2][0]):
        return map[0][2]

    elif full < 9:
        return 'N'
    else:
        return 'D'


# 게임 종료 함수
def Ender():
    if win() == User:  # 플레이어가 승리시
        print("You Win !!!")
    elif win() == Com:  # 컴퓨터 승리시
        print("You Lose ...")
    elif win() == 'D':
        print("DRAW")
    return


while play == 1:  # 플레이하는 동안
    Reset()  # 새로이 시작하기 위해 리셋
    SelectMarker()  # 마커 선택
    while full < 9:  # 판이 다 찰때까지 게임 진행
        if WhoseTurn % 2 == 1:
            user_turn()
            WhoseTurn += 1
        else:
            computer_turn()
            WhoseTurn += 1
        if win() == 'X' or win() == 'O' or win() == 'D':
            break
    Ender()  # 게임 종료후 결과 출력
    PlayAgain()  # 다시 하겠냐고 물어보기
