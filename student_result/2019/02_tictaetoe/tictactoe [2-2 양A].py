"""
    함수 종류
    1. help : 규칙 설명
    2. print_score : 현재까지의 스코어 및 승률 출력
    3. choose_shape : 모양을 선택
    4. choose_start : 먼저할 것인지 선택
    4. play : 현재 누구의 차례인지에 따라 행동 결정
    5. watch : 판의 현재 상태 출력
    6. get_input : 사용자가 놓을 위치를 입력 받음
    7. select : 컴퓨터가 놓을 위치를 판단
    8. check_f : 이긴 사람이 있는지 판단
    9. check_f2 : 컴퓨터가 꼭 놓아야 하는 위치가 있는지 판단
    10. write_score : 우승자를 출력하고 점수를 기록하는 함수
    11. ask_retry : 재플레이 의사 확인
"""

import random
import time


def help():
    """
    게임 규칙 도움말
    """
    print('=' * 75)
    print('Tic Tac Toe !')
    print('본 게임은 3개의 연속된 표시를 컴퓨터보다 먼저 완성하면 이기는 게임입니다')
    print()
    print('< 게임 방법 >')
    print(' 1. O,X 중 원하는 모양을 선택하세요 ')
    print(' 2. 선공 or 후공을 선택하세요 ')
    print(' 3. 숫자를 입력하여 원하는 위치를 선택하세요')
    print(' 4. 위치를 번갈아 선택하다가 3개의 연속된 표시를 먼저 완성하면 승리합니다')
    print()
    print(' * 각 위치는 다음과 같이 숫자로 표현합니다')
    print('   1 2 3')
    print('   4 5 6')
    print('   7 8 9')
    print('=' * 75)


def print_score(win_cnt):
    """
    컴퓨터와 사용자의 승리 횟수를 출력
    이긴 횟수 합이 0이 아니면 승률도 함께 출력
    """
    print('COM : %d VS YOU : %d' % (win_cnt['컴퓨터'], win_cnt['당신']))
    if win_cnt['컴퓨터'] + win_cnt['당신'] != 0:
        print('승률 : %0.2f' % (win_cnt['당신'] / (win_cnt['컴퓨터'] + win_cnt['당신'])))


def choose_shape():
    """
    사용자가 원하는 모양을 선택하도록 하는 함수
    """
    shape = input('O,X 중 원하는 모양을 입력하세요').upper()
    if shape != 'O' and shape != 'X':
        print('잘못된 입력입니다. ')
        shape = choose_shape()

    return shape


def choose_start():
    """
    사용자가 먼저 할지 나중에 할지 선택하도록 하는 함수
    """
    now = input('먼저 시작하시겠습니까? (예 : 1 / 아니오 : 0)')
    if now != '1' and now != '0':
        print('잘못된 입력입니다. ')
        now = choose_start()

    return int(now)


def play(now, board, check, shape_list, winner):
    """
    게임을 진행하는 함수
    now 가 1이면 사용자에게 직접 입력을 받고
    now 가 0이면 컴퓨터가 선택할 위치를 판단
    우승자 번호 winner 와 다음 차례의 번호 now 를 return
    """
    if now == 1:
        # 선택된 자리에 사용자의 모양을 채움
        board[get_input(board)] = shape_list[0]
        # 변화한 말판의 상태를 출력해줌
        watch(board)
        # 혹시 이겼는지 확인하고 이겼으면 우승자 번호에 1을 입력
        if check_f(board, check):
            winner = 1
        # 자신의 차례가 끝났으므로 차례를 넘겨줌
        now = 0
    else:
        # 선택된 자리에 컴퓨터의 모양을 채움
        board[select(board, check)] = shape_list[1]
        time.sleep(0.8)
        # 변화한 말판의 상태를 출력해줌
        watch(board)
        # 혹시 이겼는지 확인하고 이겼으면 우승자 번호에 0을 입력
        if check_f(board, check):
            winner = 0
        # 자신의 차례가 끝났으므로 차례를 넘겨줌
        now = 1

    return winner, now


def watch(board):
    """
    말판을 출력해주는 함수
    """
    for i in range(0, 3):
        for j in range(1, 4):
            print('%c ' % board[i * 3 + j], end=' ')
        print()
    print('=' * 35)


def get_input(board):
    """
    사용자의 입력을 받는 함수
    1 ~ 9까지의 숫자만 입력 받도록 함
    """
    print('당신의 차례입니다')
    print('숫자를 입력하세요')
    try:
        num = int(input())
    except ValueError:
        print(' 잘못된 입력 방식입니다. 다시 입력해주세요')
        num = get_input(board)
    if num >= 10 or num <= 0:
        print(' 1 ~ 9 사이의 숫자만 입력 가능합니다. 다시 입력해주세요')
        num = get_input(board)
    if board[num] != '-':
        print(' 이미 선택된 칸입니다. 다시 입력해주세요')
        num = get_input(board)

    return num


def select(board, check):
    """
    컴퓨터가 선택할 수를 판단하는 함수
    check_f2 함수를 통해 꼭 놓아야하는 위치를 먼저 판단하고
    그런 위치가 없으면 랜덤으로 위치를 선정
    """
    print('컴퓨터의 차례입니다')
    num = check_f2(board, check)
    while board[num] != '-' or num == 0:
        num = random.randrange(1, 10)

    return num


def check_f(board, check):
    """
    이겼는지 판단하는 함수
    check 리스트에 저장된 모든 가로, 세로, 대각선을 확인해 줌
    이겼으면 1을 return
    """
    for list in check:
        if board[list[0]] == board[list[1]] == board[list[2]] != '-':
            return 1
    return 0


def check_f2(board, check):
    """
    꼭 놓아야하는 곳이 있는지 확인해주는 함수
    check 리스트에 저장된 모든 가로, 세로, 대각선 중 두칸이 같게 채워져있고, 나머지 한칸이 비어있는 경우
    비어있는 칸의 인덱스를 return
    """
    for list in check:
        if board[list[0]] == board[list[1]] != '-' and board[list[2]] == '-':
            return list[2]
        elif board[list[1]] == board[list[2]] != '-' and board[list[0]] == '-':
            return list[0]
        elif board[list[0]] == board[list[2]] != '-' and board[list[1]] == '-':
            return list[1]

    return 0


def write_score(who, winner, win_cnt):
    """
    이긴 사람을 출력하고
    이긴 횟수를 1 증가시켜 점수를 기록
    """
    print('%s의 승리입니다' % (who[winner]))
    return win_cnt[who[winner]] + 1


def ask_retry():
    """
    게임을 다시 할 것인지 물어보는 함수
    잘못된 입력을 걸러냄
    """
    print('게임을 다시 하시겠습니까?')
    print('예 : 1 / 아니오 : 0')
    retry = input()
    if retry != '1' and retry != '0':
        print('잘못된 입력입니다. ')
        retry = ask_retry()
    return int(retry)


# 규칙 설명은 한번만 출력
help()

# retry == 1 이면 게임을 계속 다시 함
retry = 1

# 승자의 이름을 출력할 때 인덱스로 접근
who = ['컴퓨터', '당신']

# 이긴 횟수를 사전형으로 저장
win_cnt = {'컴퓨터': 0, '당신': 0}

# 가로, 세로, 대각선의 모든 경우를 리스트로 저장. 컴퓨터 판단 or 승리 판단 시 사용
check = [[1, 2, 3], [4, 5, 6], [7, 8, 9], [1, 4, 7], [2, 5, 8], [3, 6, 9], [1, 5, 9], [3, 5, 7]]

while retry == 1:
    # 현재까지의 스코어를 출력
    print_score(win_cnt)

    # 매 경기마다 말판을 '-'로 초기화. 인덱스는 0부터 9까지 존재. 0은 사용하지 않음
    board = ['-', '-', '-', '-', '-', '-', '-', '-', '-', '-']

    # 사용자가 원하는 모양을 입력 받음
    shape = choose_shape()

    # shape_list 의 인덱스 0에는 사용자가 원하는 모양을, 1에는 나머지 모양을 저장
    if shape == 'O':
        shape_list = ['O', 'X']
    else:
        shape_list = ['X', 'O']

    # 현재 선택권이 있는 쪽의 번호를 저장. 0이면 컴퓨터 차례, 1이면 사용자 차례
    now = choose_start()

    # 이긴 사람의 번호를 저장. 초기 상태 2가 유지되면 무승부. 2가 아니면 리스트 who 의 인덱스로 사용
    winner = 2

    # 현재까지 몇 개 칸이 채워졌는지 저장
    cnt = 1

    # 칸이 모두 찰 때까지 게임을 진행
    while cnt <= 9:
        # 게임을 진행.
        winner, now = play(now, board, check, shape_list, winner)

        # 중간에 우승자가 나오면 게임 중단
        if winner != 2:
            break

        # 칸이 채워졌으므로 칸 수 1 증가
        cnt += 1

    # 우승자가 나와서 게임이 중단된 것이면
    if winner != 2:
        # 우승자를 출력하고 점수를 기록하는 함수
        win_cnt[who[winner]] = write_score(who, winner, win_cnt)

    # 우승자가 나오지 않고 게임이 중단된 것이면
    else:
        print('무승부입니다')

    # 다시 플레이 할 것인지 여부를 묻고 저장
    retry = ask_retry()

# 최종 결과를 출력
print('< 최종 결과 >')
print_score(win_cnt)

# 코멘트를 출력
if win_cnt['컴퓨터'] >= win_cnt['당신']:
    print('아쉽습니다. 다음 번엔 더 분발해주세요')
else:
    print('대단한 실력이시네요!!')

time.sleep(3)
