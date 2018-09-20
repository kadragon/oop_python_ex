import random


# Board 출력
def PrintBoard():
    print()
    print('-' * 13)
    print('| %s | %s | %s |' % (board[1], board[2], board[3]))
    print('-' * 13)
    print('| %s | %s | %s |' % (board[4], board[5], board[6]))
    print('-' * 13)
    print('| %s | %s | %s |' % (board[7], board[8], board[9]))
    print('-' * 13)
    print()
    return


# 유저가 두는 경우
def userturn():
    print("Your Turn. Input 1~9")
    buff = input()
    # 잘못된 입력 처리
    while len(buff) != 1 or buff[0] not in '1 2 3 4 5 6 7 8 9'.split() or vis[int(buff[0])] != 0:
        print("Try again")
        buff = input()
    # int형으로 변환
    buff = int(buff)
    vis[buff] = UserMark


# 컴퓨터의 차례
def computerturn():
    # 처음에는 왼쪽 위 귀퉁이를 차지
    if Times == 1:
        vis[1] = ComMark
    # 두 번째로 두는 경우
    elif Times == 2:
        # 가운데가 비어 있으면 차지
        if vis[5] == 0:
            vis[5] = ComMark
        # 상대방이 가운데를 뒀을 경우 남은 네 귀퉁이 중 하나 차지
        else:
            GoTo = []
            if vis[1] == 0: GoTo.append(1)
            if vis[3] == 0: GoTo.append(3)
            if vis[7] == 0: GoTo.append(7)
            if vis[9] == 0: GoTo.append(9)
            vis[random.choice(GoTo)] = ComMark
    # 세 번째로 두는 경우
    elif Times == 3:
        # 가운데가 비어 있으면 차지
        if vis[5] == 0:
            vis[5] = ComMark
        # 아닌 경우 반대쪽 구석 귀퉁이 차지
        else:
            vis[9] = ComMark
    else:
        # 나머지 경우 승리/패배 경우의 수 체크
        if FindWin() != 0:
            vis[FindWin()] = ComMark
        elif FindDanger() != 0:
            vis[FindDanger()] = ComMark
        # 나머지는 Random 하게 착수
        else:
            GoTo = []
            for i in range(1, 10):
                if vis[i] == 0:
                    GoTo.append(i)
            vis[random.choice(GoTo)] = ComMark
    return


# 컴퓨터가 승리하는 경우 찾기
def FindWin():
    for i in WIN:
        cnt = 0
        # 두 군데가 같은 경우 cnt가 1이 됨
        if vis[i[0]] == vis[i[1]] and vis[i[0]] == ComMark: cnt += 1
        if vis[i[1]] == vis[i[2]] and vis[i[1]] == ComMark: cnt += 1
        if vis[i[0]] == vis[i[2]] and vis[i[2]] == ComMark: cnt += 1
        if cnt == 1:
            # 세 곳 중 비어 있는 곳을 반환
            if vis[i[0]] == 0: return i[0]
            if vis[i[1]] == 0: return i[1]
            if vis[i[2]] == 0: return i[2]

    return 0


# 컴퓨터가 패배하는 경우 찾기
# FindWin과 같은 알고리즘
def FindDanger():
    for i in WIN:
        cnt = 0
        if vis[i[0]] == vis[i[1]] and vis[i[0]] == UserMark: cnt += 1
        if vis[i[1]] == vis[i[2]] and vis[i[1]] == UserMark: cnt += 1
        if vis[i[0]] == vis[i[2]] and vis[i[2]] == UserMark: cnt += 1
        if cnt == 1:
            if vis[i[0]] == 0: return i[0]
            if vis[i[1]] == 0: return i[1]
            if vis[i[2]] == 0: return i[2]

    return 0


# 게임이 끝났는지 판별
def gameisend():
    for i in WIN:
        cnt = 0
        if vis[i[0]] == vis[i[1]] and vis[i[0]] != 0: cnt += 1
        if vis[i[1]] == vis[i[2]] and vis[i[1]] != 0: cnt += 1
        if vis[i[0]] == vis[i[2]] and vis[i[2]] != 0: cnt += 1
        if cnt == 3:
            return i[0]

    return 0


# 보드 출력을 위한 보드 생성
def makeboard():
    # 1: X, 2: O
    for i in range(1, 10):
        if vis[i] == 0:
            board[i] = ' '
        if vis[i] == 1:
            board[i] = 'X'
        if vis[i] == 2:
            board[i] = 'O'
    return


# 게임 시작

Game = 1

while Game == 1:
    # vis: 숫자로 된 board 배열
    # board: 출력을 위한 배열
    # win: 한 줄이 되는 경우
    # Turn: 1은 컴퓨터, 2는 유저 Times: 턴수
    vis = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    board = [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']
    WIN = [[1, 2, 3], [4, 5, 6], [7, 8, 9], [1, 4, 7], [2, 5, 8], [3, 6, 9], [1, 5, 9], [3, 5, 7]]
    Turn = 0
    Times = 0
    ComMark = 0
    UserMark = 0

    print("""
Let's Play Tic Tac Toe!
Please enter X or O
X will start the game first
    """
          )

    makeboard()

    # 유저의 X나 O를 입력받음
    # 원래 규칙에 따라 X가 선공임
    M = input()
    while len(M) != 1 or (M != 'X' and M != 'O'):
        print('PLEASE write X or O !!!!')
        M = input()

    # 입력에 따라 유저와 컴퓨터의 마크 지정
    # 유저 선공인 경우 유저 턴 진행
    if M == 'X':
        UserMark = 1
        ComMark = 2
        userturn()
        Times += 1
    else:
        UserMark = 2
        ComMark = 1

    # 보드 만들고 출력
    makeboard()
    PrintBoard()
    Turn = 1

    # 최대 9턴까지
    while Times < 9:
        Times += 1
        if Turn == 1:
            print("Computer's Turn:")
            # 컴퓨터 턴 진행
            computerturn()
            # 보드 만들고 출력
            makeboard()
            PrintBoard()
            Turn = 0
            if gameisend() != 0:
                print("Computer's Win!")
                break
        else:
            # 유저 턴 진행
            userturn()
            # 보드 만들고 출력
            makeboard()
            PrintBoard()
            Turn = 1
            if gameisend() != 0:
                print("You Win!")
                break

    # 꽉 차서 끝날 경우 무승부 출력
    if Times == 9:
        print("DRAW")

    # 게임 재실행 여부 확인
    print("Play Again? Yes: O NO: X")
    T = input()
    while len(T) != 1 or (T != 'X' and T != 'O'):
        print('PLEASE write X or O !!!!')
        T = input()
    if T == 'O':
        Game = 1
    else:
        Game = 0
