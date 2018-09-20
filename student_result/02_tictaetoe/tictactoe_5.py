# 필요한 모듈 import
import random
import copy

BOARD_SIZE = 3  # 게임판의 가로/세로 크기

board = [[' ' for i in range(BOARD_SIZE)]
         for j in range(BOARD_SIZE)]  # 게임판 초기화


def printCurrentBoard():  # 현재 보드를 출력

    print("-" * (BOARD_SIZE * 4 + 1))
    for i in range(BOARD_SIZE):

        for j in range(BOARD_SIZE):
            print("|", end=' ')  # 칸과 칸 사이를 '|'로 구분
            print(board[i][j], end=' ')
        print("|")
        print("-" * (BOARD_SIZE * 4 + 1))


def getPlayerMove():  # 플레이어의 수를 입력받음

    while True:  # 올바른 입력을 할때까지 반복
        try:
            a = int(input("Your Move?"))
            # 입력을 바탕으로 x 와 y 좌표를 계산
            a -= 1
            x = a // BOARD_SIZE
            y = a % BOARD_SIZE

            if board[x][y] in ('O', 'X'):  # 만약 이미 말이 있는 자리라면 다시 입력
                print("Find a emptier space!")
                continue
            break
        except ValueError:  # 만약 a가 숫자가 아니라면 다시 입력
            print("Error, Try again")
            #print(a, x, y)
            continue
        except IndexError:  # 좌표가 보드를 벗어날 경우 다시 입력
            print("Error, Try again")
            #print(a, x, y)
            continue

    return x, y  # 플레이어가 놓은 좌표 반환


def isWin(board, icon):  # 현 상태에서 승리자가 있는지 판별

    # icon은 승리를 판별할 대상(플레이어 혹은 컴퓨터)의 말 모양

    for i in range(BOARD_SIZE):  # 가로와 세로 방향 확인
        flag1 = True
        flag2 = True
        for j in range(BOARD_SIZE):
            if board[i][j] != icon:  # 가로방향에 icon과 다른 모양이 있으면 False
                flag1 = False
            if board[j][i] != icon:  # 세로방향에 icon과 다른 모양이 있으면 False
                flag2 = False
        if flag1 is True or flag2 is True:  # 이기는 경우가 있을 경우 True 리턴
            # print(flag1,flag2)
            return True

    flag1 = True
    flag2 = True
    for i in range(BOARD_SIZE):  # 대각선 확인
        for j in range(BOARD_SIZE):
            if i == j:  # 오른쪽 아래 방향 대각선 확인
                if board[i][j] != icon:
                    flag1 = False

            if i + j == BOARD_SIZE - 1:  # 왼쪽 아래 방향 대각선 확인
                if board[i][j] != icon:
                    flag2 = False

    if flag1 is True or flag2 is True:  # 이기는 경우가 있을 경우 True 리턴
        # print(flag1,flag2)
        return True

    return False  # 모든 경우를 확인해 승리 경우가 없으면 False 리턴


def getComputerMove():  # 컴퓨터의 수를 계산

    for icon in (computerIcon, playerIcon):
        # 뒀을때 컴퓨터가 이기는 위치, 플레이어가 이기는 위치 차례로 확인
        for i in range(BOARD_SIZE):
            for j in range(BOARD_SIZE):
                if board[i][j] != ' ':
                    continue
                newBoard = copy.deepcopy(board)  # 보드를 복제
                newBoard[i][j] = icon  # 복제한 보드의 현재 위치에 말 놓음
                if isWin(newBoard, icon):  # 승리했는지 확인
                    return i, j  # 승리했다면 좌표 리턴

    # 네 귀퉁이 확인해 빈 자리 있으면 리턴
    if board[0][0] == ' ':
        return 0, 0
    if board[0][BOARD_SIZE - 1] == ' ':
        return 0, BOARD_SIZE - 1
    if board[BOARD_SIZE - 1][0] == ' ':
        return BOARD_SIZE - 1, 0
    if board[BOARD_SIZE - 1][BOARD_SIZE - 1] == ' ':
        return BOARD_SIZE - 1, BOARD_SIZE - 1

    # 남은 자리에서 중간 제외하고 빈 자리 있으면 리턴
    for i in range(BOARD_SIZE):
        for j in range(BOARD_SIZE):
            if (i, j) == (BOARD_SIZE // 2, BOARD_SIZE // 2):
                continue
            if board[i][j] == ' ':
                return i, j

    # 중간이 비었으면 리턴
    if board[BOARD_SIZE // 2][BOARD_SIZE // 2] == ' ':
        return BOARD_SIZE // 2, BOARD_SIZE // 2

    # 빈 자리 없으면 -1, -1 리턴(그럴 경우 없음)
    return - 1, -1


def init():  # 게임 다시 시작시 보드 초기화

    for i in range(BOARD_SIZE):
        for j in range(BOARD_SIZE):
            board[i][j] = ' '


def askPlayAgain():  # 다시 플레이할지 확인

    while True:  # 올바른 입력을 할때까지 반복

        ret = input("Play Again?(Yes, No) ").upper()
        if ret.startswith("Y") or ret.startswith("N"):  # Y나 N으로 시작하면 올바른 입력으로 판단
            break
        else:  # 아닐 경우 다시 입력
            print("Choose 'Yes' or 'No'")
            continue

    # Y일 경우 True, N일 경우 False 리턴
    return True if ret.startswith("Y") else False


if __name__ == '__main__':  # 배운거 써먹어봤어요
    isPlay = True
    while isPlay:  # 플레이 중이라면

        init()  # 보드 초기화
        playerIcon = None
        while playerIcon not in ('X', 'O'):  # 플레이어의 모양 입력
            playerIcon = input('Choose your Icon(O, X)').upper()

        computerIcon = 'X' if playerIcon == 'O' else 'O'  # 컴퓨터의 모양 결정

        # 선공, 후공 결정
        # 턴 수를 2로 나눈 나머지로 선공, 후공 판별
        print("Flip the Coin!")
        playerTurn = random.randint(0, 1)
        print("You go First!" if playerTurn == 0 else "You go Second!")

        flag = False  # 무승부 여부 판별 flag

        for i in range(BOARD_SIZE ** 2):
            if i % 2 == playerTurn:  # 플레이어의 턴이라면
                print("Your Turn!")
                printCurrentBoard()  # 보드 출력
                x, y = getPlayerMove()  # 수 입력
                board[x][y] = playerIcon
                if isWin(board, playerIcon):  # 만약 승리했다면
                    flag = True
                    print("You Won!")
                    break

            else:  # 컴퓨터의 턴이라면
                print("Computer's Turn!")
                x, y = getComputerMove()  # 컴퓨터 수 판별
                board[x][y] = computerIcon
                printCurrentBoard()  # 보드 출력
                if isWin(board, computerIcon):  # 만약 승리했다면
                    flag = True
                    print("You lost!")
                    break

        if flag is False:  # 만약 무승부라면
            print("Tie!")  # 무승부 출력
        isPlay = askPlayAgain()
