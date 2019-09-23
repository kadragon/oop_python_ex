import random

t = [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']  # 돌의 배열을 저장
stone = [1, 2, 3, 4, 5, 6, 7, 8, 9]  # AI가 돌을 놓을 위치 정할 때 사용
turn = [0, 1]  # 사용자와 AI 돌 놓는 순서 정할 때 사용


def board():  # 판의 상황을 출력하기 위한 함수
    print("-----------")
    print(" %s | %s | %s" % (t[1], t[2], t[3]))
    print("-----------")
    print(" %s | %s | %s" % (t[4], t[5], t[6]))
    print("-----------")
    print(" %s | %s | %s" % (t[7], t[8], t[9]))
    print("-----------")


def win():  # 게임의 승패 결정되었는지 확인하는 함수
    if t[1] == t[2] and t[2] == t[3]:
        return t[1]
    if t[4] == t[5] and t[5] == t[6]:
        return t[4]
    if t[7] == t[8] and t[8] == t[9]:
        return t[7]
    if t[1] == t[4] and t[4] == t[7]:
        return t[1]
    if t[2] == t[5] and t[5] == t[8]:
        return t[2]
    if t[3] == t[6] and t[6] == t[9]:
        return t[3]
    if t[1] == t[5] and t[5] == t[9]:
        return t[1]
    if t[3] == t[5] and t[5] == t[7]:
        return t[3]
    else:
        return 'no'


def draw():  # 게임이 무승부인지 확인하는 함수
    flag = 1  # 무승부인지 판별하기 위한 변수

    for i in range(1, 10):
        if t[i] == ' ':  # 하나라도 t가 비어있다면
            flag = 0  # flag를 0으로 바꿈

    if flag == 1:  # 돌 모두 차있어서 아직 flag가 1이라면
        return True  # 참을 돌려줌
    else:  # 돌놓을 수 있는 곳 한 군데라도 있다면
        return False  # 거짓을 돌려줌


def alphago():  # AI가 놓을 위치 정하는 함수 무조건 이기는 경우나 지는 경우만 고려
    list = [[1, 2, 3], [4, 5, 6], [7, 8, 9], [1, 4, 7], [2, 5, 8], [3, 6, 9], [1, 5, 9], [3, 5, 7]]  # 돌 일렬로 배열되는 경우

    for i in list:
        temp = 0  # 일렬로 같은 돌이 몇개 있는지 저장하는 변수
        for j in range(0, 3):
            if t[i[j]] == ai:
                temp += 1
            if t[i[j]] == player:
                temp += -1
        if temp == 2:  # 일렬로 ai의 돌이 2개 있고 한 칸 비어있다면
            for k in range(0, 3):
                if t[i[k]] == ' ':
                    t[i[k]] = ai  # 비어있는 곳에 놓아 승리하도록 한다
                    return

    for i in list:
        temp = 0  # 일렬로 같은 돌이 몇개 있는지 저장하는 변수
        for j in range(0, 3):
            if t[i[j]] == ai:
                temp += 1
            if t[i[j]] == player:
                temp += -1
        if temp == -2:  # 일렬로 사용자의 돌이 2개 있고 한 칸 비어있다면
            for l in range(0, 3):
                if t[i[l]] == ' ':
                    t[i[l]] = ai  # 비어있는 곳에 놓아 패배를 막는다
                    return

    while 1:  # 이외의 경우는
        random.shuffle(stone)  # 랜덤으로 위치를 정해
        if t[stone[0]] == ' ':  # 그곳에 비어있다면
            t[stone[0]] = ai  # 그곳에 AI가 돌을 놓는다
            return


while 1:
    t = [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']  # 돌의 배열 초기화
    while 1:
        player = input("Do you want to play O or X? (O/X) ")  # 사용자가 플레이할 돌 종류 선택
        if player == 'o' or player == 'x':  # 소문자 입력했을 때
            player = player.upper()  # 대문자로 바꾸어줌

        if player != 'O' and player != 'X':  # O나 X 이외의 문자 입력했을 때
            print("Please input only X or O.")  # 다시 입력해달라고 요청

        if player == 'O' or player == 'X':  # 사용자가 제대로 입력했을 때
            break  # 빠져나옴

    if player == 'O':  # 사용자가 O선택했으면
        ai = 'X'  # AI가 X
    else:  # 아니면
        ai = 'O'  # AI가 O

    random.shuffle(turn)  # 랜덤으로 순서 결정

    if turn[0] == 0:  # 랜덤으로
        alphago()  # AI가 먼저 시작

    while 1:
        board()  # 배열 상황 출력
        while 1:  # 사용자가 돌 놓을 위치 정하기
            a = input("Where will you place the stone? (1~9) ")
            if a in "1 2 3 4 5 6 7 8 9".split():
                a = int(a)
            else:
                print("Please input only 1 to 9.")  # 다시 입력하도록 유도
                continue
            if t[a] != ' ':  # 놓으려는 위치에 돌이 이미 있으면
                print("stone is already placed.")  # 다시 입력하도록 유도
            else:  # 똑바로 입력했으면
                t[a] = player  # 돌 놓고
                break  # 반복문 탈출

        if win() == player:  # 사용자가 이겼다면
            board()  # 돌 배열 출력
            print("You win!!")  # 이겼다고 출력
            break  # 반복문 탈출

        if draw() == True:
            board()  # 판 상황 출력
            print("draw")  # 무승부라고 출력
            break  # 반복문 탈출

        alphago()  # AI가 돌 놓고

        if win() == ai:  # AI가 이겼다면
            board()  # 판 상황 출력
            print("You lose..")  # 사용자가 졌다고 출력
            break  # 반복문 탈출

        if draw():
            board()  # 판 상황 출력
            print("draw")  # 무승부라고 출력
            break  # 반복문 탈출

    while 1:  # 게임 다시할지 물어보는 반복문
        re = input("Do you want to play again? (Y/N) ")  # 게임 다시할지 물어보고
        if re == 'Y' or re == 'y' or re == 'N' or re == 'n':  # 제대로 입력했다면
            break  # 반복문 탈출
        else:  # 제대로 입력하지 않았다면
            print("Please input only Y or N")  # 다시 입력하도록 유도

    if re == 'Y' or re == 'y':  # 다시 한다고 하면
        continue  # 반복문 다시
    else:  # 다시 하지 않는다고 하면
        break  # 반복문 탈출
