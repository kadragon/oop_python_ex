"""
객체지향프로그래밍 소과제 2
Tic Tac Toe game
2019.09.23
2306 박유진
"""

import random

wins = {"player": 0, "computer": 0, "totalscore": 0}  # 승수와 경기 수 저장 변수


def intro_set():
    """
    시작과 동시에 사용자의 말 (X, O)를 결정하게 하는 함수
    사용자의 입력 값을 통해 사용자의 말을 지정해주고 동시에 다른 말을 컴퓨터ㅔ게 지정해준다
    :param: 없음
    :return: 순서대로 사용자, 컴퓨터의 말이 들어있는 리스트
    """
    print("Let's play Tic Tac Toe!!")
    print("Do you want X or O?:")
    while (True):
        try:
            pick = input().upper()
            print("running...")
            if pick == 'X':
                return ['X', 'O']
                break
            elif pick == 'O':
                return ['O', 'X']
                break
            else:
                print("wrong syntax. Try again")
        except (KeyError, ValueError, TypeError, IndexError) as e:
            print("\nError (%s) \nTry again\n" % e)


def showboard():
    """
    화면에서 현재 상태를 출력하는 함수
    전역 변수인 board에 들어있는 정보를 사용자가 쉽게 읽을 수 있도록 출력해준다
    :return: 없음
    """
    for i in range(3):
        print("-" * 15)
        for j in range(3):
            print(" " + str(board[i][j]) + " ", end='')
            if j < 2:
                print(" | ", end='')
            else:
                print()
    print("-" * 15)


def alterboard():
    """
    사용자의 조작에 따라 보드판을 변경해주는 함수
    입력으로 사용자가 말을 놓고 싶어하는 칸의 행과 열을 받는다
    보드위의 칸에 놓을 수 있는 곳이면 그 자리에 입력한다.
    :return: 없음
    """
    while (True):
        print("Enter the row number and coloumn separated by a space")
        print("ex: 1 3")
        try:
            tmp = list(map(int, input().split()))
            row, col = int(tmp[0]) - 1, int(tmp[1]) - 1
            if type(board[row][col]) is int:
                print("wrong place, try again")
            else:
                board[row][col] = user
                showboard()
                break

        except (KeyError, ValueError, TypeError, IndexError) as e:
            print("\nError (%s) \nTry again\n" % e)


def complay():
    """
    컴퓨터가 다음 둘 곳을 두는 결정하는 함수.
    우선적으로 컴퓨터가 놓아서 이길 곳을 찾고, 있으면 말을 놓는다
    그 다음으로 다음 차례에 사용자가 놨을 때 이길 수 있는 곳을 막는다.
    그 외의 경우에는 랜덤한 칸을 채운다
    :return: 없음
    """
    for i in range(0, 3):  # 컴퓨터가 이기는 경우
        for j in range(0, 3):
            if board[i][j] != 'X' and board[i][j] != 'O':
                board[i][j] = com  # 이 칸에 말을 놓는다면
                if checkwin(com):  # 컴퓨터가 이기면
                    showboard()
                    print("I Win!")
                    return  # 놓을 채로 진행
                board[i][j] = ' '  # 아니면 다시 원상복귀

    for i in range(0, 3):  # 컴퓨터가 수비하는 경우
        for j in range(0, 3):
            if board[i][j] != 'X' and board[i][j] != 'O':
                board[i][j] = user
                if checkwin(user):
                    board[i][j] = com
                    showboard()
                    return
                board[i][j] = ' '

    # 랜덤한 칸 채우기
    i = random.randint(0, 2)
    j = random.randint(0, 2)

    while board[i][j] == 'X' or board[i][j] == 'O':  # 아무것도 없는 칸을 찾아야함
        i = random.randint(0, 2)
        j = random.randint(0, 2)
    board[i][j] = com
    showboard()


def checkwin(who):
    """
    사용자 또는 컴퓨터 중 누가 승리했는가를 확인하는 함수
    매개변수로 들어오는 사용자 또는 컴퓨터의 말이 연달아 3개 있는지 확인해서 승리했으면 1을 반환, 아닌 경우에는 0을 반환
    :param who: 사용자 또는 컴퓨터 중 누구가 승리했는지 받는 매개변수
    :return: 승리했으면 1, 아니면 0
    """
    for i in range(0, 3):
        if board[0][i] == board[1][i] == board[2][i] == who:  # 세로로 연달아 있는 경우
            return 1
        elif board[i][0] == board[i][1] == board[i][2] == who:  # 가로로 연달아 있는 경우
            return 1
    if (board[0][0] == board[1][1] == board[2][2] == who) or (
            board[0][2] == board[1][1] == board[2][0] == who):  # 대각선으로 연달아 있는 경우
        return 1

    return 0


def tie():
    """
    현재 보드가 무승부 상태인지 확인하는 함수
    모든 칸이 채워져있는데 승이 없는 경우에 무승부 여부를 반환한다
    :return: 1이면 무승부, 0이면 무승부가 아니다
    """
    tie = True
    for i in range(0, 3):
        for j in range(0, 3):
            if board[i][j] == ' ':
                tie = False
    if checkwin(user) or checkwin(com):
        tie = False

    if tie:
        return 1
    return 0


def winstats(doprint):
    """
    승률을 기록하고 반환하는 함수.
    승리가 있거나 무승부인 경우에 누구의 승부인지 판단하고 각각의 승수를 증가한후 승률을 계산하여 출력
    승률을 승수와 경기 수를 바탕으로 계산되고, 승수는 전역변수로 표현한다.
    :param doprint: 승률에 대한 정보를 출력할 것인지 받는 매개변수. True이면 출력, False이면 출력하지 않는다
    :return: 없음
    """
    if checkwin(user) == 1:  # 사용자가 이긴 경우
        wins["player"] += 1  # 사용자의 승수 증가
        wins["totalscore"] += 1  # 전체 경기 수 증가
    elif checkwin(com) == 1:  # 컴퓨터가 이긴 경우
        wins["computer"] += 1
        wins["totalscore"] += 1

    if tie():  # 무승부인 경우
        wins["totalscore"] += 1

    if doprint:  # 출력하는 부분
        print("Win Stats:")
        print("Player:" + str(wins["player"]) + "/" + str(wins["totalscore"]))
        print(str((wins["player"] / wins["totalscore"]) * 100) + "%")
        print()
        print("Computer:" + str(wins["computer"]) + "/" + str(wins["totalscore"]))
        print(str((wins["computer"] / wins["totalscore"]) * 100) + "%")
        print()


def playagain():
    """
    사용자에게 다시 플레이 할 것인지 물어보는 함수
    제대로 된 입력을 받는지까지 재입력받는다.
    :return: 다시 플레이하는 경우에 1, 아닌 경우에 0
    """
    print("Would you like to play again? (yes or no)")
    while True:
        try:
            ans = input()
            if ans in ["Yes", "yes", "y", "Y"]:  # 다시 도전하면 While문을 돎
                print('reset...')
                return 1
            elif ans in ["No", "no", "N", "n"]:
                print("ending game")
                return 0
            else:
                print("Wrong input. Try again...")
        except (KeyError, ValueError, TypeError, IndexError) as e:
            print("%s check input..." % e)


while True:
    board = [[' ', ' ', ' '], [' ', ' ', ' '], [' ', ' ', ' ']]  # 시작하는 보드
    user, com = intro_set()  # 사용자와 컴퓨터 말 정하기
    order = random.randint(0, 1)  # 순서 정하기는 랜덤
    if order:
        print("You go first!")  # order ==1 사용자 먼저
    else:
        print("I'll go first!")
    showboard()  # 초기 판 보여주기
    while True:
        if order:
            alterboard()  # 사용자가 말 놓기
        else:
            complay()  # 컴퓨터가 말 놓기
        if checkwin(user):  # 사용자가 이긴 경우
            print("Congrats U win!")
            winstats(True)
            break
        elif checkwin(com):  # 컴퓨터가 이긴 경우
            print("I win!")
            winstats(True)
            break
        elif tie():  # 무승부인 경우
            print("Tie!")
            winstats(True)
            break

        order = not order  # 다음 플레이어 차례

    if playagain() is False:  # 다시 플레이 할지 물어본다
        break
