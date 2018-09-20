import random, time

def start():  # 게임 시작 화면, 말 선택하기
    print("-" * 80)
    print("Let's play Tic-Tac-Toe!!!")
    print()
    ret = input("Choose your character ( O / X ) : ")
    print()
    while True:
        if ret in ['O', 'o', '0']:
            return True
        elif ret in ['X', 'x']:
            return False
        else:
            ret = input("Please choose again ( O / X ) : ")
            print()

def randomly():  # 순서 정하기
    if random.randint(0, 1) is 0:
        print("Computer will start first!")
        print()
        return True
    else:
        print("You can start first!")
        print()
        return False

board = [[3*i+j+1 for j in range(3)] for i in range(3)]  # 게임 판이 될 리스트!

def printBoard():  # 게임 보드를 출력하는 함수
    print('-' * 13)
    for i in range(3):
        print('| ' + str(board[i][0]) + ' | ' + str(board[i][1]) + ' | ' + str(board[i][2]) + ' |')
        print('-' * 13)

def isEmpty(i, j):  # (i, j)가 비었는지 확인하는 함수
    if board[i][j] is 3*i+j+1:
        return True
    return False

reserve = []  # 말을 놓을 후보 위치를 저장

def check(mode, character):  # 상대의 말을 어디에 놓아야 할 지 체크!
    x, y = 0, 0  # 나의 말과 상대의 말이 각각 몇 개 인지 저장
    if 0 <= mode <= 2:  # 가로 1~3줄 검사
        for i in range(3):
            if board[mode][i] is ('O' if character else 'X'):
                x += 1
            elif board[mode][i] is ('X' if character else 'O'):
                y += 1
        if x is 2 and y is 0:  # 상대의 말이 두 개 있는 경우에는 막아야 함
            for i in range(3):
                if isEmpty(mode, i):
                    reserve.append([mode, i])
                    break
    elif 3 <= mode <= 5:  # 세로 1~3줄 검사: 같은 방법으로
        for i in range(3):
            if board[i][mode-3] is ('O' if character else 'X'):
                x += 1
            elif board[i][mode-3] is ('X' if character else 'O'):
                y += 1
        if x is 2 and y is 0:
            for i in range(3):
                if isEmpty(i, mode-3):
                    reserve.append([i, mode-3])
                    break
    elif mode is 6:  # 양 대각선 검사
        for i in range(3):
            if board[i][i] is ('O' if character else 'X'):
                x += 1
            elif board[i][i] is ('X' if character else 'O'):
                y += 1
        if x is 2 and y is 0:
            for i in range(3):
                if isEmpty(i, i):
                    reserve.append([i, i])
                    break
    elif mode is 7:
        for i in range(3):
            if board[i][2-i] is ('O' if character else 'X'):
                x += 1
            elif board[i][2-i] is ('X' if character else 'O'):
                y += 1
        if x is 2 and y is 0:
            for i in range(3):
                if isEmpty(i, 2-i):
                    reserve.append([i, 2-i])
                    break

def isDone(mode, character):  # 게임이 끝났는지 검사
    x, y = 0, 0  # 나의 말과 상대의 말이 각각 몇 개 인지 저장
    if 0 <= mode <= 2:  # 가로 1~3줄 검사
        for i in range(3):
            if board[mode][i] is ('O' if character else 'X'):
                x += 1
            elif board[mode][i] is ('X' if character else 'O'):
                y += 1
    elif 3 <= mode <= 5:  # 세로 1~3줄 검사
        for i in range(3):
            if board[i][mode - 3] is ('O' if character else 'X'):
                x += 1
            elif board[i][mode - 3] is ('X' if character else 'O'):
                y += 1
    elif mode is 6:  # 양 대각선 검사
        for i in range(3):
            if board[i][i] is ('O' if character else 'X'):
                x += 1
            elif board[i][i] is ('X' if character else 'O'):
                y += 1
    elif mode is 7:
        for i in range(3):
            if board[i][2 - i] is ('O' if character else 'X'):
                x += 1
            elif board[i][2 - i] is ('X' if character else 'O'):
                y += 1
    if x is 3 and y is 0:  # 내 말이 3개가 있는 줄이 있는가?
        return 1
    elif x is 0 and y is 3:  # 상대의 말이 3개가 있는 줄이 있는가?
        return 2
    else:  # 완료된 줄이 없는가?
        return False

playAgain = True
Done = False

while playAgain:
    character = start()  # 나의 말: True : O / False : X
    first = randomly()  # True : Computer / False : Player가 먼저 진행

    for i in range(9):  # 턴 실행 횟수는 최대 9번
        printBoard()
        if first:  # 컴퓨터의 차례, 중요하지 않은 조건부터 탐색하며 점점 갱신하는 방식으로 선택
            print("It's my turn!")
            print("Please wait...")
            print()
            x, y = 0, 0
            while True:  # 일단 임의로 위치 선정
                x = random.randint(0, 2)
                y = random.randint(0, 2)
                if isEmpty(x, y):
                    break
            for j in range(8):  # 방어해야 하는 위치를 탐색
                check(j, character)
            if len(reserve) :
                ran = random.randint(0, len(reserve)-1)
                x, y = reserve[ran][0],reserve[ran][1]
            reserve = []
            for j in range(8):  # 이길 수 있는 위치를 탐색
                check(j, not character)
            if len(reserve):
                ran = random.randint(0, len(reserve) - 1)
                x, y = reserve[ran][0], reserve[ran][1]
            reserve = []
            board[x][y] = ('X' if character else 'O')  # 선택한 위치에 말을 놓는다
            time.sleep(1)

        else:  # 나의 차례
            available = []
            print("Your turn!")
            print("Choose your place", end = '')
            for i in range(3):
                for j in range(3):
                    if isEmpty(i, j):
                        print(", %d" % board[i][j], end = '')
                        available.append(3*i+j+1)  # 선택 가능한 위치 모두 출력
            print(" available : ", end = '')
            while True:
                choice = input()
                if (len(choice) is 1 and '0' <= choice <= '9'):
                    choice = int(choice)
                    if choice in available:
                        break
                print("Choose again", end = '')
                for i in available:
                    print(", %d" % i, end = '')
                print(" : ", end = '')
            print()
            board[(choice-1)//3][(choice-1)%3] = ('O' if character else 'X')  # 선택한 위치에 말 놓기
        first = not first  # 순서 바꾸기

        for j in range(8):  # 모든 줄을 보며 게임이 끝났는지 확인
            Done = isDone(j, character)
            if Done is not False:
                break
        if Done is not False:
            break
        
    printBoard()

    if Done is 1:
        print("You win!!!")
    elif Done is 2:
        print("You lose!")
    else:
        print("Tie!")
    print("Will you play again? ( Y / N ) : ", end = '')  # 다시 할래요?
    while True:
        response = input()
        if response in ['Y', 'y', 'Yes', 'yes', 'YES', 'O', 'o']:
            print()
            print()
            print()
            board = [[3*i+j+1 for j in range(3)] for i in range(3)]  # 게임 판 리셋
            break
        elif response in ['N', 'n', 'No', 'no', 'NO', 'X', 'x']:
            playAgain = False
            break
        else:
            print("Please choose again ( Y / N ) : ", end = '')
