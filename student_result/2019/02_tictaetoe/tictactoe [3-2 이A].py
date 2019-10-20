import random

board = []  # 생성한 게임판 객체
for i in range(9):
    board.append(' ')  # 3*3을 만들기 위해 빈칸 append

win = 0  # 승리 횟수 받는 객체
lose = 0  # 패배 횟수 받는 객체
tie = 0  # 무승부 횟수 받는 객체
total = 0  # 게임 횟수 받는 객체

row1 = [0, 1, 2]
row2 = [3, 4, 5]
row3 = [6, 7, 8]
col1 = [0, 3, 6]
col2 = [1, 4, 7]
col3 = [2, 5, 8]
dig1 = [0, 4, 8]
dig2 = [2, 4, 6]
allcase = [row1, row2, row3, col1, col2, col3, dig1, dig2]  # 승리 판별할 때 확인해야 하는 위치 리스트를 담은 리스트 객체


def percentage(num):
    """
    비율(승률 등) 계산 함수
    :param num: 원하는 항목 (승리, 패배 등)
    :return: 그에 대한 비율
    """
    return num / total


def initial():
    """
    게임판 초기화 함수
    :return: None
    """
    for index in range(9):
        board[index] = ' '


def showboard():
    """
    현재의 게임판 상태를 보여주는 함수
    :return: None
    """
    print(" " + board[0] + " | " + board[1] + " | " + board[2])
    print("ㅡㅡㅡㅡㅡ")
    print(" " + board[3] + " | " + board[4] + " | " + board[5])
    print("ㅡㅡㅡㅡㅡ")
    print(" " + board[6] + " | " + board[7] + " | " + board[8])


def check(index, usermark, pcmark):
    """
    현재 allcase 중 특정 요소에서 user_mark와 pc_mark가 어떻게 배치되어 있는지 보여주는 함수
    :param pcmark: 컴퓨터의 말
    :param usermark: 사용자의 말
    :param index: allcase에서의 index
    :return: [(), (), (): 특정 인덱스의 게임판에 user_mark가 들어있으면 2, pc_mark가 들어있으면 1, 비어있으면 0]
    """
    ind = 0
    checklist = [None, None, None]
    for j in allcase[index]:
        if board[j] == usermark:
            checklist[ind] = 2
        elif board[j] == pcmark:
            checklist[ind] = 1
        else:
            checklist[ind] = 0
        ind += 1
    return checklist


def isfullboard():
    """
    게임판이 모두 채워졌는지 확인하는 함수
    :return: None
    """

    flag = 0
    for i in range(9):
        if board[i] == ' ':
            flag = 1

    if not flag:  # 빈칸이 없다!
        return 1  # 다 채워졌다!

    else:
        return 0


def isempty(index):
    """
    원하는 인덱스에서의 게임판이 비어있는지 확인하는 함수
    :param index: 게임판에서의 인덱스
    :return: TRUE or FALSE
    """
    if board[index] == ' ':
        return 1
    else:
        return 0


def isfinish(mark):
    """
    게임이 끝났는지 확인하는 함수
    :param mark: 특정 마크 (O or X)
    :return: TRUE or FALSE
    """
    for index in allcase:
        if board[index[0]] == mark and board[index[1]] == mark and board[index[2]] == mark:
            return 1

    return 0


def pc_control(usermark, pcmark):
    """
    컴퓨터가 놓을 말의 위치를 분석하는 함수
    :pram pcmark: 컴퓨터의 말 (O or X)
    :return: None
    """
    numlist = list(range(9))
    random.shuffle(numlist)
    flag = 0  # 이미 놓을 합리적인 위치를 확인했는지 확인하는 객체
    for index in range(8):
        result = check(index, usermark, pcmark)
        if result.count(1) == 2 and result.count(0) == 1:  # 컴퓨터 입장: 이기자! (한 줄에 빈 칸이 1개, pc_mark 2개)
            board[allcase[index][result.index(0)]] = pcmark
            flag = 1
            break

    if flag == 0:
        for index in range(8):
            result = check(index, usermark, pcmark)
            if result.count(2) == 2 and result.count(0) == 1:  # 컴퓨터 입장: 위험 (한 줄에 빈 칸이 1개, user_mark 2개)
                board[allcase[index][result.index(0)]] = pcmark
                flag = 1
                break

    if flag == 0:
        for j in numlist:  # 랜덤으로 배치
            if isempty(j):
                board[j] = pcmark
                flag = 1
                break


def enterwrong(entered, letter):
    """
    사용자가 입력한 정보가 틀리게 입력되는지 확인하는 함수
    :param entered: 입력된 문자
    :param letter: 입력되어야 하는 문자
    :return: TRUE or FALSE
    """
    if entered == letter:
        return 0
    else:
        return 1


print("TICTACTOE 게임 시작!")
print("1 2 3")
print("4 5 6")
print("7 8 9")
print("게임판은 다음과 같습니다. ")
print("=" * 80)

while True:
    initial()
    user_mark = input("O, X 중 말을 선택하세요. : ")
    fin = 0  # 승부가 났는지 확인하는 객체
    if enterwrong(user_mark, 'O') and enterwrong(user_mark, 'X'):
        continue
    if user_mark == 'O':
        pc_mark = 'X'
    else:
        pc_mark = 'O'

    while True:
        playfirst = input("선공, 후공을 결정하세요. (first, last) : ")
        if enterwrong(playfirst, 'first') and enterwrong(playfirst, 'last'):
            continue
        else:
            break

    if playfirst == 'last':
        pc_control(user_mark, pc_mark)
        showboard()

    while True:
        loca = input("1~9 중 위치를 입력하세요. : ")
        print()
        if loca not in ['1', '2', '3', '4', '5', '6', '7', '8', '9']:
            continue
        local = int(loca) - 1
        if not isempty(local):
            continue
        board[local] = user_mark
        pc_control(user_mark, pc_mark)
        showboard()
        print()

        if isfinish(user_mark):
            print("You WIN!")
            fin = 1
            win += 1
            break

        if isfinish(pc_mark):
            print("You LOSE!")
            fin = 1
            lose += 1
            break

        if isfullboard():
            break

    if not fin:
        tie += 1
        print("TIE!")

    total += 1
    print("현재 플레이어의 결과: 승 %.2f 무 %.2f 패 %.2f 경기 수 %d" % (percentage(win), percentage(tie), percentage(lose), total))

    while True:
        repeat = input("다시 할 것인가요? 다시 반복하려면 y, 그렇지 않으면 n을 눌러주세요. : ")
        if enterwrong(repeat, 'y') and enterwrong(repeat, 'n'):
            continue
        if repeat == 'n':
            exit()
        if repeat == 'y':
            break
