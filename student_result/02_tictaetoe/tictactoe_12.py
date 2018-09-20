import random


def showBoard(board):  # 작업된 게임판을 출력
    print('=' * 80)
    print("""
      %c |  %c  | %c
    --- | --- | ---
      %c |  %c  | %c
    --- | --- | ---
      %c |  %c  | %c
    """ % (board[1], board[2], board[3], board[4], board[5], board[6], board[7], board[8], board[9]))
    print('=' * 80)


def inputPlayerLetter():  # 사용자가 O,X중 원하는 돌을 선택
    letter = ''
    while True:
        print('Choose X or O')
        letter = input().upper()
        if (letter == 'X' or letter == 'O'):
            break
        print('Only X or O!')

    if letter == 'X':
        return ['X', 'O']
    else:
        return ['O', 'X']


def whoGoFirst():  # 선공을 랜덤으로 정함
    if random.randint(0, 1) == 0:
        return 'com'
    else:
        return 'player'


def playAgain():  # 다시 할지 물어보는 함수
    print('You want to play again? (yes or no)')
    return input().lower().startswith('y')


def makeMove(board, letter, move):  # 게임판에 move위치에 돌을 놓는다
    print(move, type(move))
    board[move] = letter


def copyBoard(board):  # 화면에 내보내기 전 작업을 할 보드 생성
    otherBoard = []

    for i in board:
        otherBoard.append(i)

    return otherBoard


def isWinner(b, l):  # b보드에서 l 돌이 이겼는지 확인
    return ((b[7] == l and b[8] == l and b[9] == l) or
            (b[4] == l and b[5] == l and b[6] == l) or
            (b[1] == l and b[2] == l and b[3] == l) or
            (b[7] == l and b[4] == l and b[1] == l) or
            (b[8] == l and b[5] == l and b[2] == l) or
            (b[9] == l and b[6] == l and b[3] == l) or
            (b[1] == l and b[5] == l and b[9] == l) or
            (b[3] == l and b[5] == l and b[7] == l))


def isSpaceEmpty(board, move):  # 돌을 놓을 공간이 비어있는지 확인
    return board[move] == ' '


def isBoardFull(board):  # 게임판이 꽉찼는지 확인
    for i in range(1, 10):
        if isSpaceEmpty(board, i):
            return False
    return True


def getPlayerMove(board):  # 사용자가 놓는곳을 입력받아 반환
    move = ''
    while move not in '1 2 3 4 5 6 7 8 9'.split() or not isSpaceEmpty(board, int(move)):  # 원하는 곳이 비어있어야함
        print('Where do you want to put? input a number in 1~9')
        move = input()
    return int(move)


def chooseRandomMoveFromList(board, moveList):  # 이동가능한 리스트에서 위치를 랜덤으로 정함
    possibleMoves = []
    for i in moveList:
        if isSpaceEmpty(board, i):
            possibleMoves.append(i)
    if len(possibleMoves) != 0:
        return random.choice(possibleMoves)
    else:
        return None


def getComputerMove(board, computerLetter):  # 게임판과 컴퓨터의 돌을 넘겨주고 컴퓨터가 놓을 위치를 반환
    if computerLetter == 'X':
        playerLetter = 'O'
    else:
        playerLetter = 'X'

    # 틱택토 AI의 알고리즘
    # 1. 다음 돌로 이길수 있다면 그위치에 놓음
    for i in range(1, 10):
        copy = copyBoard(board)
        if isSpaceEmpty(copy, i):
            makeMove(copy, computerLetter, i)
            if isWinner(copy, computerLetter):
                print(i)
                return i

    # 2. 사용자가 이길수 있는지 확인하고 방어함
    for i in range(1, 10):
        copy = copyBoard(board)
        if isSpaceEmpty(copy, i):
            makeMove(copy, playerLetter, i)
            if isWinner(copy, playerLetter):
                print(i)
                return i

    # 3. 1,3,7,9 코너중 하나를 먼저 가져감
    move = chooseRandomMoveFromList(board, [1, 3, 7, 9])
    if move != None:
        return move

    # 4. 가운데가 비어있다면 가져감
    if isSpaceEmpty(board, 5):
        return 5

    # 5. 네 변중 하나를 가져감
    move = chooseRandomMoveFromList(board, [2, 4, 6, 8])
    if move != None:
        return move


# 게임 시작
print('Tic Tac Toe!')

while True:  # 반복게임 루프
    gameBoard = [' '] * 10  # 게임판 초기화
    playerLetter, computerLetter = inputPlayerLetter()  # 사용자와 컴퓨터 돌결정
    turn = whoGoFirst()  # 선공
    print('The ' + turn + ' will go first.')
    isPlaying = True

    while isPlaying:
        if turn == 'player':
            # 사용자 차례
            showBoard(gameBoard)
            move = getPlayerMove(gameBoard)
            makeMove(gameBoard, playerLetter, move)

            if isWinner(gameBoard, playerLetter):
                showBoard(gameBoard)
                print('You win the game!!!!!')
                isPlaying = False
            else:
                if isBoardFull(gameBoard):
                    print(gameBoard)
                    showBoard(gameBoard)
                    print('The game is a tie!')
                    break
                else:
                    turn = 'com'

        else:
            # 컴퓨터 차례
            move = getComputerMove(gameBoard, computerLetter)
            makeMove(gameBoard, computerLetter, move)

            if isWinner(gameBoard, computerLetter):
                showBoard(gameBoard)
                print('You lose...')
                isPlaying = False
            else:
                if isBoardFull(gameBoard):
                    print(gameBoard)
                    showBoard(gameBoard)
                    print('The game is a tie!')
                    break
                else:
                    turn = 'player'

    if not playAgain():
        break
