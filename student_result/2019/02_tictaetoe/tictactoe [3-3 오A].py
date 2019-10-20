import random
import copy

board = ['', '-', '-', '-', '-', '-', '-', '-', '-', '-']
win_board = [{}, {1, 2, 3}, {4, 5, 6}, {7, 8, 9}, {1, 4, 7}, {2, 5, 8}, {3, 6, 9}, {1, 5, 9}, {3, 5, 7}]
play_num = 0
win_num = 0
user = 'O'
computer = 'X'


# 화면에 현재 상태를 출력하는 함수
def nowstate():
    print("=======================\n")

    for i in range(1, 10):
        print("%c" % board[i], end='  ')
        if i % 3 == 0:
            print("\n")

    print("=======================")


# 컴퓨터가 다음 둘 곳을 판단하는 함수(두뇌)
# 추후 더 복잡하게 수를 고르는 두뇌를 추가 할 수 있음
def my_brain():
    # 사용자의 말 위치 확인
    opponent_board = []
    void_board = []
    for i in range(1, 10):
        if board[i] == 'O':
            opponent_board.append(i)
        elif board[i] == '-':
            void_board.append(i)

    # 사용자의 승리를 저지할 수 있는 수 결정(한 수 앞)
    for i in range(1, 9):
        b = win_board[i] & set(opponent_board)
        c = list(win_board[i] - b)
        if len(b) == 2 and c[0] in void_board:
            board[c[0]] = 'X'
            return c[0]

    k = random.choice(void_board)
    board[k] = 'X'
    return k


# 사용자에게 다시 플레이 할 것인지 물어보는 함수
def replay():
    print("다시 플레이 할까요?(Y/다른문자) : ", end=' ')
    answer = input()
    if answer == 'Y':
        return True
    else:
        return False


# 승률을 기록하는 함수
def rate():
    print("플레이 횟수 : %d" % play_num)
    print("승리 횟수 : %d" % win_num)
    win_rate = 0
    if play_num != 0:
        win_rate = win_num / play_num
    print("현재 승률 : %.3f" % win_rate)


# 사용자의 턴
def user():
    while True:
        try:
            print("수를 둘 위치를 입력해주세요(1~9) : ", end=' ')
            b = int(input())
            # 입력 오류 확인
            # 1~9 사이의 정수를 입력했는지
            # 빈 위치에 입력했는지
            domain = {1, 2, 3, 4, 5, 6, 7, 8, 9}
            if not (b in domain):
                raise Exception
            if board[b] != '-':
                raise Exception
            board[b] = 'O'
            break
        except:
            print("다시 입력하세요.")
    # 결과 확인(선공일때 9번째 수가 무승부일지, 승리일지 결정)
    if gameresult():
        nowstate()
        return True


# 컴퓨터의 턴
def computer():
    # 컴퓨터 두뇌 가동
    my_brain()
    # 결과 확인(후공일때 9번째 수가 무승부일지, 승리일지 결정)
    if gameresult():
        nowstate()
        return True


# 경기의 승무패를 결정하여 그 결과를 출력하는 함수
def gameresult():
    global play_num
    global win_num

    type = 0
    if board.count('-') > 0:
        type = 1

    # 사용자와 컴퓨터의 말 위치 확인
    user_board = []
    computer_board = []
    for i in range(1, 10):
        if board[i] == 'O':
            user_board.append(i)
        elif board[i] == 'X':
            computer_board.append(i)

    for i in range(1, 9):
        b = win_board[i] & set(user_board)
        c = win_board[i] & set(computer_board)
        if len(b) == 3:
            print("=======================")
            print("당신의 승리!")
            # 승률에 반영됨
            play_num += 1
            win_num += 1
            return True
        elif len(c) == 3:
            print("=======================")
            print("컴퓨터의 승리!")
            # 승률에 반영됨
            play_num += 1
            return True
        elif type == 0:
            print("=======================")
            print("무승부")
            # 승률에 반영됨
            play_num += 1
            return True


def gameplay():
    # 보드 초기화
    global board
    board = ['', '-', '-', '-', '-', '-', '-', '-', '-', '-']
    # 안내의 말 및 전적 표시
    print("▶게임을 시작합니다.")
    print("▶당신의 말은 'O'로 표시됩니다.")
    rate()
    # 선공/후공 결정, 입력 오류 확인
    while True:
        try:
            print("선공(O)/후공(X) : ", end=' ')
            a = input()
            domain = {'O', 'X'}
            if not (a in domain):
                raise Exception
            break
        except:
            print("다시 입력하세요")

    if a == 'O':
        while True:
            nowstate()
            # 사용자의 수 입력
            if user():
                break
            # 컴퓨터의 수 입력
            if computer():
                break
    else:
        while True:
            # 컴퓨터의 수 입력
            if computer():
                break
            nowstate()
            # 사용자의 수 입력
            if user():
                break

    # 게임 재시작
    if replay():
        gameplay()
    else:
        return


gameplay()
