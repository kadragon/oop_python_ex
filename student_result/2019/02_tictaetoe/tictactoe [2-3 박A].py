import random


def drawgame(board):
    # 이 함수는 틱택토를 하는 판을 짠다.
    print(' ' + board[7] + ' | ' + board[8] + ' | ' + board[9])
    print('-----------')
    print(' ' + board[4] + ' | ' + board[5] + ' | ' + board[6])
    print('-----------')
    print(' ' + board[1] + ' | ' + board[2] + ' | ' + board[3])


def PlayerLetter():
    # 플레이어가 글자 입력하게 하는 함수
    # 플레이어가 진행할 기호를 O,X중 선택하게 한다.

    letter = ''
    while not (letter == 'X' or letter == 'O'):
        print('O할래요 X할래요? O를 하고 싶으면 o를, X를 하고 싶으면 X를 누르고 엔터키를 치세요')
        letter = input().upper()

    # 선택한 것이 플레이어의 기호, 그렇지 않은 것이 컴퓨터의 기호가 되도록 함.

    if letter == 'X':
        return ['X', 'O']

    else:
        return ['O', 'X']


def determineFirst():
    # 플레이어와 컴퓨터 중 누가 먼저 할지를 랜덤으로 결정한다.
    if random.randint(0, 1) == 0:
        return 'computer'
    else:
        return 'player'


def playagain():
    # 플레이어가 다시 하기를 원하면 true, 그렇지 않으면 false를 리턴한다.
    print('다시 하실래요? 하고 싶으시면 y를, 그렇지 않다면 아무 문자를 입력하고 엔터를 치세요')
    return input().lower().startswith('y')


def makeMove(board, letter, move):
    # 게임 플레이 시 판에서 입력, 움직이게 하는 함수
    board[move] = letter


def isWinner(bo, le):
    # Given a board and a player’s letter, this function returns True if that player has won.
    # We use bo instead of board and le instead of letter so we don’t have to type as much.

    return ((bo[7] == le and bo[8] == le and bo[9] == le) or  # across the top

            (bo[4] == le and bo[5] == le and bo[6] == le) or  # across the middle
            (bo[1] == le and bo[2] == le and bo[3] == le) or  # across the bottom
            (bo[7] == le and bo[4] == le and bo[1] == le) or  # down the left side
            (bo[8] == le and bo[5] == le and bo[2] == le) or  # down the middle
            (bo[9] == le and bo[6] == le and bo[3] == le) or  # down the right side
            (bo[7] == le and bo[5] == le and bo[3] == le) or  # diagonal
            (bo[9] == le and bo[5] == le and bo[1] == le))  # diagonal


def getBoardCopy(board):
    # 판을 복제하고, 복제된 판을 리턴한다.
    dupeBoard = []
    for i in board:
        dupeBoard.append(i)
    return dupeBoard


def isSpaceFree(board, move):
    # 입력하는 공간이 비어 있는지 확인하는 함수. 비어 있을 시 true 리턴
    return board[move] == ' '


def getPlayerMove(board):
    # 플레이어가 둘 곳을 입력하는 함수

    move = ' '
    while move not in '1 2 3 4 5 6 7 8 9'.split() or not isSpaceFree(board, int(move)):
        print('어디에 두실 건가요? (1-9)')
        move = input()

    return int(move)


def chooseRandomMoveFromList(board, movesList):
    # 움직일 자리를 리턴한다.
    # 움직일 자리가 없으면 none을 리턴한다.

    possibleMoves = []

    for i in movesList:
        if isSpaceFree(board, i):
            possibleMoves.append(i)

    if len(possibleMoves) != 0:
        return random.choice(possibleMoves)

    else:
        return None


def getComputerMove(board, computerLetter):
    # 컴퓨터의 기호를 결정하고, 어디로 움직일지를 결정한다.

    if computerLetter == 'X':
        playerLetter = 'O'

    else:
        playerLetter = 'X'

    # 틱택토 AI의 알고리즘.
    # 다음 움직임에서 이길 수 있을지를 판단한다.

    for i in range(1, 10):
        copy = getBoardCopy(board)

        if isSpaceFree(copy, i):
            makeMove(copy, computerLetter, i)

            if isWinner(copy, computerLetter):
                return i

    # 플레이어가 다음 움직임에서 이길 수 있을지를 판단하고, 그렇다면 그것을 막는다.

    for i in range(1, 10):
        copy = getBoardCopy(board)

        if isSpaceFree(copy, i):
            makeMove(copy, playerLetter, i)

            if isWinner(copy, playerLetter):
                return i

    # 비어 있다면 꼭짓점 부분 중 하나의 위치에 둔다.

    move = chooseRandomMoveFromList(board, [1, 3, 7, 9])

    if move is not None:
        return move

    # 중앙이 비어 있다면 그 위치에 둔다.

    if isSpaceFree(board, 5):
        return 5

    # 한쪽 변으로 움직인다.

    return chooseRandomMoveFromList(board, [2, 4, 6, 8])


def isBoardFull(board):
    # 판의 모든 자리가 차 있다면 true를, 그렇지 않다면 false를 리턴한다.
    for i in range(1, 10):
        if isSpaceFree(board, i):
            return False

    return True


def determinewinrate(win, lose, tie):
    # 이긴횟수, 진횟수, 비긴횟수, 승률을 출력하는 함수
    print("이긴 횟수 : %d 진 횟수 : %d 비긴 횟수 : %d" % (win, lose, tie))  # 총 이긴 횟수, 비긴 횟수, 진 횟수 출력
    print("승률 : %.2f퍼센트" % (win / (win + lose + tie) * 100))  # 승률을 계산하여 출력


print('틱택토를 플레이해봅시다')

while True:
    # 판을 리셋한다.
    theBoard = [' '] * 10
    playerLetter, computerLetter = PlayerLetter()
    turn = determineFirst()
    print(turn + ' 가 먼저 합니다')
    gameIsPlaying = True

    wintime = 0  # 이긴 횟수 계산
    losetime = 0  # 진 횟수 계산
    tietime = 0  # 비긴 횟수 계산

    while gameIsPlaying:
        if turn == 'player':
            # 플레이어의 차례.
            drawgame(theBoard)
            move = getPlayerMove(theBoard)
            makeMove(theBoard, playerLetter, move)

            if isWinner(theBoard, playerLetter):
                drawgame(theBoard)
                wintime = 1 + wintime  # 이길 시 이긴 횟수에 1 추가
                print('플레이어가 이겼습니다!')
                gameIsPlaying = False
            else:
                if isBoardFull(theBoard):
                    drawgame(theBoard)
                    tietime = 1 + tietime  # 비길 시 비긴 횟수에 1 추가
                    print('무승부입니다.')
                    break
                else:
                    turn = 'computer'
        else:
            # 컴퓨터의 차례
            move = getComputerMove(theBoard, computerLetter)
            makeMove(theBoard, computerLetter, move)

            if isWinner(theBoard, computerLetter):
                drawgame(theBoard)
                losetime = losetime + 1  # 질 시 진 횟수에 1 추가
                print('컴퓨터가 이겼습니다!')
                gameIsPlaying = False
            else:
                if isBoardFull(theBoard):
                    drawgame(theBoard)
                    tietime = tietime + 1  # 비길 시 비긴 횟수에 1 추가
                    print('무승부입니다.')
                    break
                else:
                    turn = 'player'
    if not playagain():
        determinewinrate(wintime, losetime, tietime)
        break
