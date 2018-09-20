from random import randint
from time import sleep

flag1 = True  # 게임 반복 요건
flag2 = True  # 게임 실행 요건
player = -1  # O X 확인
complayer = -1  # 컴퓨터 OX 결정
ground = ['1', '2', '3', '4', '5', '6', '7', '8', '9']  # 맵 설정
location = -1  # 플레이어가 놓을 위치
status = [[0, 0, 3], [0, 0, 3], [0, 0, 3], [0, 0, 3], [0, 0, 3], [0, 0, 3], [0, 0, 3],
          [0, 0, 3]]  # 판이 채워진 상황, 각 열과 행, 대각선 정보에 O의 개수, X의 개수, 빈칸의 개수가 담김


def inputset(u, k):
    global status
    global ground

    if k:
        ground[u - 1] = 'O'
    else:
        ground[u - 1] = 'X'

    if u == 1:
        status[0][k] += 1
        status[0][2] -= 1
        status[3][k] += 1
        status[3][2] -= 1
        status[6][k] += 1
        status[6][2] -= 1
    elif u == 2:
        status[0][k] += 1
        status[0][2] -= 1
        status[4][k] += 1
        status[4][2] -= 1
    elif u == 3:
        status[0][k] += 1
        status[0][2] -= 1
        status[5][k] += 1
        status[5][2] -= 1
        status[7][k] += 1
        status[7][2] -= 1
    elif u == 4:
        status[1][k] += 1
        status[1][2] -= 1
        status[3][k] += 1
        status[3][2] -= 1
    elif u == 5:
        status[1][k] += 1
        status[1][2] -= 1
        status[4][k] += 1
        status[4][2] -= 1
        status[6][k] += 1
        status[6][2] -= 1
        status[7][k] += 1
        status[7][2] -= 1
    elif u == 6:
        status[1][k] += 1
        status[1][2] -= 1
        status[5][k] += 1
        status[5][2] -= 1
    elif u == 7:
        status[2][k] += 1
        status[2][2] -= 1
        status[3][k] += 1
        status[3][2] -= 1
        status[7][k] += 1
        status[7][2] -= 1
    elif u == 8:
        status[2][k] += 1
        status[2][2] -= 1
        status[4][k] += 1
        status[4][2] -= 1
    elif u == 9:
        status[2][k] += 1
        status[2][2] -= 1
        status[5][k] += 1
        status[5][2] -= 1
        status[6][k] += 1
        status[6][2] -= 1

    return


def output():  # 판 출력
    print('\t------------------')
    for i in range(3):
        print('\t------------------')
        print("\t || %s | %s | %s ||" % (ground[i * 3], ground[i * 3 + 1], ground[i * 3 + 2]))
        print('\t------------------')
    print('\t------------------\n\n')


def choose():  # OX 입력 받기
    global player
    global complayer
    flag3 = True  # 입력 반복해 받을 때 요건
    c = 0
    while flag3:
        c += 1
        if c > 10:
            print("\n\tHey, It isn't funny. OK?\n")
        try:  # 오류 처리
            player = input('\tO or X  You decide : ').upper()  # 입력 대문자로 받기
            if player == 'O' or player == 'X':
                if player == 'O':
                    complayer = 0
                    player = 1
                else:
                    complayer = 1
                    player = 0
                b = randint(0, 1)
                if b == 0:  # 컴퓨터가 먼저 한다면
                    print('\n\tI\'ll do first\n')
                    computer()
                    check()
                else:
                    print('\n\tYou do first\n')
                    output()

                flag3 = False
                break
        except:
            continue

    return


def play():  # 플레이어에게 돌을 놓을 곳 입력 받기
    global player
    global ground
    global location

    flag3 = True  # 입력 반복해 받을 때 요건
    c = 0
    while flag3:
        c += 1
        if c > 10:
            print('\n\tOh please... seriously?\n')
        try:
            location = int(input('\tWhich place? (1~9) : '))
            if location < 1 or location > 9:  # 범위 설정
                continue
            if ground[location - 1] == 'O' or ground[location - 1] == 'X':  # 위치 확인
                print('\n\tSorry, but the place is full\n')
                continue
            inputset(location, player)
            flag3 = False
        except:
            continue

    return


def check():  # 승패 확인하기
    global status
    global player
    global complayer
    global flag1
    global flag2
    global ground

    output()

    c = 0  # 꽉찼는지 알아보기
    for i in range(9):
        if ground[i] != 'O' and ground[i] != 'X':
            break
        else:
            c += 1

    if c == 9:
        draw()
        return

    for i in range(8):  # 어느 한 곳이 채워저 있는지 확인
        if status[i][player] == 3:
            win()
            return
        elif status[i][complayer] == 3:
            lose()
            return
    return


def win():
    global flag1
    global flag2

    print('YOU WIN!!')
    print('\n\tGG\n')
    flag1 = False
    flag2 = False


def lose():
    global flag1
    global flag2

    print('You LOSE!!')
    print('\n\tNAGA!!!!\n')
    flag1 = False
    flag2 = False


def draw():
    global flag1
    global flag2

    print('\n\tOh, a DRAW? Interesting\n')
    flag1 = False
    flag2 = False


def unset(t):  # 두개 있을 때 남은 빈자리 찾기
    global ground

    if t == 6:  # \대각선
        init = 0
        j = 4
    elif t == 7:  # /대각선
        init = 2
        j = 2
    elif t > 2:  # 열
        init = t - 3
        j = 3
    else:  # 행
        init = t * 3
        j = 1

    for i in range(3):
        if ground[init + j * i] != 'O' and ground[init + j * i] != 'X':  # 빈 곳 찾기
            return init + j * i + 1

    return


def computer():
    global ground
    global location
    global player
    global complayer
    global status

    edge = (1, 3, 7, 9)
    side = (2, 4, 6, 8)

    sleep(1)
    print('\n\tThinking...\n')
    sleep(1)

    for i in range(8):  # 어느 한 곳이 2개가 있는지 확인
        if status[i][complayer] == 2 and status[i][2] == 1:
            inputset(unset(i), complayer)
            return
        elif status[i][player] == 2 and status[i][2] == 1:
            inputset(unset(i), complayer)
            return

    h = randint(0, 3)

    if location == -1:  # 맨 처음 놓을 때
        inputset(edge[h], complayer)
        return

    if ground[4] == '5':  # 가운데가 비어있을 때
        inputset(5, complayer)
        return

    for i in range(6, 8):  # 대각선 먼저 채우기
        if status[i][2] == 1:
            inputset(unset(i), complayer)
            return

    for i in edge:  # 귀 먼저 채우기
        if ground[i - 1] != 'O' and ground[i - 1] != 'X':
            inputset(i, complayer)
            return

    for i in side:  # 변 먼저 채우기
        if ground[i - 1] != 'O' and ground[i - 1] != 'X':
            inputset(i, complayer)
            return

    for i in range(len(ground)):  # 혹시라도 남은 곳이 있으면 채우기(그럴리 없겠지만)
        if ground[i] != 'O' and ground[i] != 'X':
            inputset(i + 1, complayer)
            return

    return


def ask_initial():
    global flag1
    global flag2
    global location
    global ground
    global status

    try:
        x = input('\tRe? : ').lower()
        if x == 'yes' or x == 'y' or x == 'okay' or x == 'ok' or x == 'gogo' or x == 'gg' or x == 're' or x == 'start':
            print('\n\tWell then\n')
            flag1 = True
            flag3 = False
        else:
            print('Bye Bye')
            return
    except:
        print('Bye Bye')
        return
    flag2 = True
    ground = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
    location = -1
    status = [[0, 0, 3], [0, 0, 3], [0, 0, 3], [0, 0, 3], [0, 0, 3], [0, 0, 3], [0, 0, 3], [0, 0, 3]]


print('\n\n\tStarting Tic-Tac-To...\n\n')

sleep(1)

while flag1:
    choose()
    while flag2:
        play()
        check()
        if flag2:
            computer()
            check()
    ask_initial()
