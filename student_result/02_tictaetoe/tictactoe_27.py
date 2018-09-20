"""
Title       Tic Tac Toe
Reference   https://inventwithpython.com/chapter10.html
Author      EunjeOh
Date        2018.09.09
"""

import random

a = [1, 3, 7, 9]    # 컴퓨터가 이길 확률에 따라 표식을 둘 경우의 우선순위 1순위
b = [2, 4, 6, 8]    # 컴퓨터가 이길 확률에 따라 표식을 둘 경우의 우선순위 3순위

def drawBoard(board):
    # 3X3 보드 정보(각 1X1 정사각형에 들어갈 문자)를 입력받아, 3X3 보드를 그린다.
    print("-" * 11)
    print("%2s |%2s |%2s" % (board[1], board[2], board[3]))
    print("-" * 11)
    print("%2s |%2s |%2s" % (board[4], board[5], board[6]))
    print("-" * 11)
    print("%2s |%2s |%2s" % (board[7], board[8], board[9]))
    print("-" * 11)

def tutorial():
    # 인수를 입력받지 않고, 틱택토 게임 방법에 대해 설명한다.
    print("Welcome to Tic Tac Toe!")
    drawBoard(['', '1', '2', '3', '4', '5', '6', '7', '8', '9'])    # 보드의 인덱스에서 0은 제외한다.
    print("If you choose X or O, the computer becomes the other.")
    print("If a player gets three of their marks on the board in a row, column, and diagonal, the player wins.")
    print("When the board fills up with neither player winning, the game ends in a tie.")
    print("-" * 99)

def selectPlayer():
    # 인수를 입력받지 않고, 사용자로부터 O 또는 X의 표식을 선택할 수 있게 한다.
    # [사용자, 컴퓨터]의 형식으로 표식(O 또는 X)을 리턴한다.
    user = ''
    while user not in 'O X'.split():
        user = input("Do you want to be X or O? ").strip().upper()
    if user == 'X':
        return ['X', 'O']
    else:
        return ['O', 'X']

def whoGoesFirst():
    # 인수를 입력받지 않고, 사용자와 컴퓨터 중 먼저 시작할 플레이어를 랜덤으로 정한다.
    playFirst = random.choice(['user', 'computer'])
    print("The %s will go first." % playFirst)
    return playFirst

def isSpaceFree(board, move):
    # 3X3 보드 정보를 입력받아, 표식을 둘 수 있는 곳인지(3X3 보드에서 빈 곳인지) 체크한다.
    return board[move] == ''

def getBoardCopy(board):
    # 3X3 보드 정보를 입력받아 컴퓨터가 표식을 둘 경우, 컴퓨터 혹은 사용자가 승리할 수 있는 곳인지 확인하기 위해 3X3 보드를 복제한다.
    dupBoard = []
    for i in board:
        dupBoard.append(i)
    return dupBoard

def Move(board, move, letter):
    # 3X3 보드 정보, 표식을 둘 위치, 표식을 입력받아 3X3 보드에 표식을 둔다.
    board[move] = letter

def getUserMove(board):
    # 3X3 보드 정보를 입력받아, 사용자로부터 입력을 받을 때 표식을 둘 수 있는 위치를 찾아 리턴한다.
    # 사용자가 X 또는 O가 아닌 이상한 값을 입력해도, 제대로 입력하도록 유도한다.
    move = ''
    while move not in '1 2 3 4 5 6 7 8 9'.split() or not (isSpaceFree(board, int(move))):
        move = input("What is your next move? (1~9) ").strip()
    return int(move)

def getComputerMove(board, computerletter):
    # 3X3 보드 정보와 컴퓨터의 표식을 입력받아, 컴퓨터가 표식을 둘 수 있는 위치를 판단하여 리턴한다. (심플한 인공지능)
    global a, b
    if computerletter == 'X':
        userletter = 'O'
    else:
        userletter = 'X'
    # 표식을 둘 위치의 우선 순위는 표식을 둘 수 있는 곳, 컴퓨터가 승리할 수 있는 곳, 사용자가 승리할 수 있는 곳, 이길 확률이 높은 곳 순이다.
    # 이길 확률은 3X3 보드의 모서리(1,3,7,9), 중앙(5), 나머지(2,4,6,8) 순으로 높기 때문에, 컴퓨터는 이 순서로 표식을 두기로 하자.
    for i in range(1, 10):
        copy = getBoardCopy(board)
        if isSpaceFree(copy, i):    # 표식을 둘 수 있는 곳인가?
            Move(copy, i, computerletter)
            if isWinner(copy, computerletter):    # 컴퓨터가 승리할 수 있는 곳인가?
                return i
    for i in range(1, 10):
        copy = getBoardCopy(board)
        if isSpaceFree(copy, i):    # 표식을 둘 수 있는 곳인가?
            Move(copy, i, userletter)
            if isWinner(copy, userletter):    # 사용자가 승리할 수 있는 곳인가?
                return i
    # 이길 확률이 높은 곳에 두자.
    random.shuffle(a)   # 리스트 a를 랜덤하게 섞는다.
    for i in a:    # 1순위 : 1,3,7,9
        copy = getBoardCopy(board)
        if isSpaceFree(copy, i):
            return i
    copy = getBoardCopy(board)
    if isSpaceFree(copy, 5):    # 2순위 : 5
        return 5
    random.shuffle(b)   # 리스트 b를 랜덤하게 섞는다.
    for i in b:    # 3순위 : 2,4,6,8
        copy = getBoardCopy(board)
        if isSpaceFree(copy, i):
            return i

def isWinner(bo, le):   # board, letter
    # 3X3 보드와 표식을 입력받아, 승리 여부를 부울대수로 리턴한다.
    # 행, 열, 대각선 중 1개에 표식이 3개 채워지면 승리한다.
    return ((bo[1] == le and bo[2] == le and bo[3] == le) or
            (bo[4] == le and bo[5] == le and bo[6] == le) or
            (bo[7] == le and bo[8] == le and bo[9] == le) or
            (bo[1] == le and bo[4] == le and bo[7] == le) or
            (bo[2] == le and bo[5] == le and bo[8] == le) or
            (bo[3] == le and bo[6] == le and bo[9] == le) or
            (bo[1] == le and bo[5] == le and bo[9] == le) or
            (bo[3] == le and bo[5] == le and bo[7] == le))

def isBoardFull(board):
    # 3X3 보드 정보를 입력받아, 3X3 보드가 전부 채워졌는지 부울대수로 리턴한다.
    for i in range(1, 10):
        if isSpaceFree(board, i):   # 3X3 보드의 어떤 위치에도 표식을 둘 수 없으면, 보드가 전부 채워진 것이다.
            return False
    return True

def playAgain():
    # 인수를 입력을 받지 않고, 사용자로부터 다시 게임을 할지 여부를 리턴한다.
    return input("Do you want to play again? (yes or no) ").strip().lower().startswith("y")

while True:
    tutorial()
    user, computer = selectPlayer()
    board = ['', '', '', '', '', '', '', '', '', '']
    turn = whoGoesFirst()
    isGamePlaying = True
    while isGamePlaying:
        if turn == 'user':  # 사용자의 턴일 때
            Move(board, getUserMove(board), user)
            drawBoard(board)    # 사용자가 표식을 새로 둔 3X3 보드를 그린다.
            if isWinner(board, user):   # 사용자의 승리했을 때.
                print("Wow! You won the game!")
                isGamePlaying = False
            else:   # 사용자가 승리하지 않았을 때
                if isBoardFull(board):  # 3X3 보드가 전부 채워졌으면 비긴 것이다.
                    print("The game is tie!")
                    break
                else:   # 3X3 보드가 전부 채워지지 않았으면 다음 턴은 컴퓨터이다.
                    turn = 'computer'
        else:   # 컴퓨터의 턴일 때
            Move(board, getComputerMove(board, computer), computer)
            drawBoard(board)    # 컴퓨터가 표식을 새로 둔 3X3 보드를 그린다.
            if isWinner(board, computer):   # 컴퓨터가 승리했을 때
                print("Oh, no! Computer won the game! You lose...")
                isGamePlaying = False
            else:   # 컴퓨터가 승리하지 않았을 때
                if isBoardFull(board):  # 3X3 보드가 전부 채워졌으면 비긴 것이다.
                    print("The game is tie!")
                    break
                else:   # 3X3 보드가 전부 채워지지 않았으면 다음 턴은 사용자이다.
                    turn = 'user'
    if not(playAgain()):    # 재게임.
        break