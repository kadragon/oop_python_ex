import copy
import random

b = [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']  # 문자 형태로 나타내줄 틱택토 보드

re = False  # 개임을 다시 할 지 여부
play = True

my_pick = 0
com_pick = 0
win = 0
fill = 0


def rule():
    # 게임설명
    print("-" * 40)
    print("          틱택토 게임 설명")
    print("-" * 40)
    print("1. O와 X 중 어느 것으로 플레이할 지 선택해주세요.")
    print("2. 틱택토 보드판은 다음과 같이 보여집니다. 자신의 순서가 오면 배치할 위치를 숫자로 입력해주세요.")
    print("=" * 19)
    print("|  1  |  2  |  3  |")
    print("=" * 19)
    print("|  4  |  5  |  6  |")
    print("=" * 19)
    print("|  7  |  8  |  9  |")
    print("=" * 19)
    print("3. 가로, 세로, 대각선 중 자신의 모양으로 먼저 3칸을 채우는 플레이어가 승리합니다.")
    print("-" * 40)


def play_ascii():
    print("=" * 19)
    print("|  %s  |  %s  |  %s  |" % (b[0], b[1], b[2]))
    print("=" * 19)
    print("|  %s  |  %s  |  %s  |" % (b[3], b[4], b[5]))
    print("=" * 19)
    print("|  %s  |  %s  |  %s  |" % (b[6], b[7], b[8]))
    print("=" * 19)


def play_ox():
    """
    사용자가 o,x 중 어느것으로 플레이할 지 선택
    소문자는 자동으로 대분자로 변환
    """
    while True:
        oorx = input("O와 X 중 어떤 것으로 플레이 할 지 선택해주세요 : ").upper()
        if oorx == "O" or oorx == "X":
            return oorx.upper()
        elif oorx != "O" and oorx != "X":
            print("O와 X 중 하나를 입력해주세요.")


def play_whofirst(player):
    """
    사용자와 컴퓨터 중 누가 먼저 시작할지 결정.
    안내 메시지를 출력하고 먼저 시작하는 쪽을 반환.
    """
    list = ['O', 'X']
    first = random.choice(list)
    if first == 'O':
        if player == first:
            print("\n당신 = O  컴퓨터 = X")
            print("당신부터 시작합니다.\n")
            return 'O'
        else:
            print("\n당신 = X  컴퓨터 = O")
            print("컴퓨터부터 시작합니다.\n")
            return 'O'
    elif first == 'X':
        if player == first:
            print("\n당신 = X  컴퓨터 = O")
            print("당신부터 시작합니다.\n")
            return 'X'
        else:
            print("\n당신 = O  컴퓨터 = X")
            print("컴퓨터부터 시작합니다.\n")
            return 'X'


def play_choose(player):
    """
    문자를 쓸 칸을 고름.
    플레이어가 고른 칸이 비어있는지 확인.
    비어있지 않을 시 다시 입력받도록.
    비어 있다면 입력받은 값을 리턴.
    """
    while True:
        num = int(input("%s를 채울 칸을 선택해주세요(1~9) : " % player))
        if num in range(1, 10):
            if b[num - 1] == ' ':
                return num - 1
            else:
                print("비어있는 칸에만 채울 수 있습니다.")
        else:
            print("1에서 9 사이의 숫자로 입력해주세요.")


def play_check():
    """
    빈칸이 존재하는지 확인
    빈칸 존재여부를 반환
    """
    fill = 0
    for i in range(0, 9):
        if b[i] != ' ':
            fill += 1
        else:
            pass
    if fill == 9:
        return False  # 채워진 칸이 9개면 False 반환
    else:
        return True  # 빈칸이 존재하면 True 반환


def play_O():
    """
    사용자 또는 컴퓨터의 선택에 따라 O 쓰기
    다음 차례가 계속 진행할 지 여부를 반환.
    """
    if my_pick == 'O':
        num = play_choose(my_pick)
    else:
        num = play_logic(com_pick, my_pick)
    b[num] = 'O'

    if not play_result('O'):
        return True
    else:
        return False


def play_X():
    """
    사용자 또는 컴퓨터의 선택에 따라 X 쓰기
    다음 차례가 계속 진행할 지 여부를 반환.
    """
    if my_pick == 'X':
        num = play_choose(my_pick)
    else:
        num = play_logic(com_pick, my_pick)
    b[num] = 'X'

    if not play_result('X'):
        return True
    else:
        return False


def play_logic(com, player):
    """
    컴퓨터가 채울곳 계산.
    비어있는 칸 중 최적의 칸을 찾음.
    컴퓨터가 채울 칸을 리턴.
    """
    before_win = -1
    cnt = 0
    f = 0

    c = [3, 2, 3, 2, 4, 2, 3, 2, 3]

    for i in range(0, 9, 3):  # 컴퓨터가 가로줄에서 이기기 직전인 곳 찾기
        for j in range(0, 3):
            if b[i + j] == com:
                cnt += 1
            elif b[i + j] != com:
                before_win = i + j
        if cnt == 2:
            c[before_win] += 200
            cnt = 0
            before_win = -1
        else:
            cnt = 0
            before_win = -1
    for i in range(0, 3):  # 컴퓨터가 세로줄에서 이기기 직전인 곳 찾기
        for j in range(0, 9, 3):
            if b[i+j] == com:
                cnt += 1
            elif b[i+j] != com:
                before_win = i+j
        if cnt == 2:
            c[before_win] += 200
            cnt = 0
            before_win = -1
        else:
            cnt = 0
            before_win = -1
    for i in range(0, 9, 4):  # 컴퓨터가 대각선에서 이기기 직전인 곳 찾기
        if b[i] == com:
            cnt += 1
        elif b[i] != com:
            before_win = i
    if cnt == 2:
        c[before_win] += 200
        cnt = 0
        before_win = -1
    else:
        cnt = 0
        before_win = -1
    for i in range(2, 7, 2):  # 컴퓨터가 대각선에서 이기기 직전인 곳 찾기
        if b[i] == com:
            cnt += 1
        elif b[i] != com:
            before_win = i
    if cnt == 2:
        c[before_win] += 200
        cnt = 0
        before_win = -1
    else:
        cnt = 0
        before_win = -1
    for i in range(0, 9):  # 컴퓨터의 문자 주변에 20씩 추가
        if b[i] == com:
            for j in [-3, -1, 1, 3]:
                if 0 <= i + j <= 8:
                    c[i + j] += 20
                else:
                    pass


    for i in range(0, 9, 3):  # 플레이어가 가로줄에서 이기기 직전인 곳 찾기
        for j in range(0, 3):
            if b[i + j] == player:
                cnt += 1
            elif b[i + j] != player:
                before_win = i + j
        if cnt == 2:
            c[before_win] += 100
            cnt = 0
            before_win = -1
        else:
            cnt = 0
            before_win = -1
    for i in range(0, 3):  # 플레이어가 세로줄에서 이기기 직전인 곳 찾기
        for j in range(0, 9, 3):
            if b[i+j] == player:
                cnt += 1
            elif b[i+j] != player:
                before_win = i+j
        if cnt == 2:
            c[before_win] += 100
            cnt = 0
            before_win = -1
        else:
            cnt = 0
            before_win = -1
    for i in range(0, 9, 4):  # 플레이어가 대각선에서 이기기 직전인 곳 찾기
        if b[i] == player:
            cnt += 1
        elif b[i] != player:
            before_win = i
    if cnt == 2:
        c[before_win] += 100
        cnt = 0
        before_win = -1
    else:
        cnt = 0
        before_win = -1
    for i in range(2, 7, 2):  # 플레이어가 대각선에서 이기기 직전인 곳 찾기
        if b[i] == player:
            cnt += 1
        elif b[i] != player:
            before_win = i
    if cnt == 2:
        c[before_win] += 100
        cnt = 0
        before_win = -1
    else:
        cnt = 0
        before_win = -1
    for i in range(0, 9):  # 상대의 문자 주변에 10씩 추가
        if b[i] == player:
            for j in [-3, -1, 1, 3]:
                if 0 <= i + j <= 8:
                    c[i + j] += 10
                else:
                    pass


    for i in range(9):  # 문자가 채워진 칸 0으로
        if b[i] != ' ':
            c[i] = 0
    '''
    for i in range(9):   # 처음 컴퓨터가 둘 때는 랜덤으로, 이후부터는 cc값 큰 곳
        if c[i] <= 10:
            f += 1
    if f == 9:
        return random.choice(range(0, 9))
    else:
        cc = copy.deepcopy(c)
        cc.sort()
        return c.index(cc[-1])'''
    cc = copy.deepcopy(c)
    cc.sort()
    return c.index(cc[-1])


def play_result(turn):
    """
    결과 보드 표시.
    무승부의 경우 무승부임을 알림.
    승리자가 있을 경우 알림.
    게임이 끝났는지 여부를 반환.
    :param turn: 가장 마지막에 문자를 채운 차례(호출한 차례)
    :return: 승리자 존재여부(True or False)
    """
    play_ascii()
    cnt = 0

    for i in range(0, 3):
        if b[3 * i + 0] == b[3 * i + 1] == b[3 * i + 2] == turn:
            cnt += 1
        elif b[i] == b[i + 3] == b[i + 6] == turn:
            cnt += 1
        elif b[0] == b[4] == b[8] == turn:
            cnt += 1
        elif b[2] == b[4] == b[6] == turn:
            cnt += 1

    if cnt > 0:
        if turn == my_pick:
            print("당신이 승리하였습니다!\n")
            return True
        else:
            print("컴퓨터에 패배하였습니다!\n")
            return True
    elif not play_check():
        print("무승부!\n")
        return True
    else:
        print("\n")
        return False


def ask_again():
    """
    사용자에게 다시 플레이 할지 물음
    :return: 재시작 여부(True or False)
    """
    while True:
        again = input("게임을 다시 진행하시겠습니까? Yes / No : ").upper()
        if again == 'YES':
            return True
        elif again == 'NO':
            return False
        else:
            print("Yes 또는 No를 입력해주세요.")


while True:
    for i in range(0, 9):
        b[i] = ' '  # 초기화

    rule()

    if play_ox() == 'O':
        my_pick = 'O'
        com_pick = 'X'
    else:
        my_pick = 'X'
        com_pick = 'O'

    whofirst = play_whofirst(my_pick)  # 어떤 문자가 먼저 시작인지

    if whofirst == my_pick:
        play_ascii()  # 플레이어가 맨 처음 시작할 때는 친절하게 빈 칸을 띄워주자.

    while whofirst == 'O':
        if play_O():
            if not play_X():
                break
        else:
            break
    while whofirst == 'X':
        if play_X():
            if not play_O():
                break
        else:
            break

    re = ask_again()
    if not re:
        break
    else:
        pass
