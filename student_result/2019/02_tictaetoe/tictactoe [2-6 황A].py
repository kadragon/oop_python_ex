import random

board = [['1', '2', '3'],
         ['4', '5', '6'],
         ['7', '8', '9']]
a = 0
user = 'A'
cpu = 'B'
winner = 'C'
win = 0
drw = 0
los = 0
lis = [0, 1, 2]


def intro():  # 인트로, 말 선택
    global a, user, cpu
    print("2616 황인서 || 틱택토 게임")
    print("저를 이기실 수 있나요?")
    print("O와 X 중 당신의 말을 선택하세요.")
    while 1:
        user = input()
        if user == 'O':
            cpu = 'X'
            break
        elif user == 'X':
            cpu = 'O'
            break
        else:
            print("다시 입력하세요.")

    print("=" * 30)


def winning_rate():  # 승률 계산
    return win / (win + drw + los)


def status():  # 현재 상태 출력
    for i in lis:
        print(board[i][0], board[i][1], board[i][2])


def decide():  # 게임이 끝났을까요?
    global winner
    for i in lis:
        if (board[i][0] == board[i][1] == board[i][2]):
            winner = board[i][0]
        elif (board[0][i] == board[1][i] == board[2][i]):
            winner = board[0][i]
    if (board[0][0] == board[1][1] == board[1][2]):
        winner = board[0][0]
    elif (board[2][0] == board[1][1] == board[0][2]):
        winner = board[2][0]


def play_usr():  # 플레이어에게 입력 받기
    global board
    print("입력할 칸을 선택하세요.")
    while 1:
        dol = int(input())
        dolr = (dol - 1) // 3
        dolc = (dol - 1) % 3
        if board[dolr][dolc] != cpu and board[dolr][dolc] != user:
            board[dolr][dolc] = user
            break
        else:
            print("다시 입력하세요.")


def play_cpu():  # 컴퓨터가 돌을 놓는 알고리즘
    global board
    print("제가 둘 차례입니다.")
    dapr = -1
    dapc = -1
    # 상대의 끝내기 상황과 내 끝내기 상황이 겹치면 내가 그냥 끝내면 되므로 공격을 우선!
    for i in lis:  # 공격
        if board[i][2 - i] == board[(i + 1) % 3][2 - (i + 1) % 3] == cpu and board[(i + 2) % 3][
            2 - (i + 2) % 3] != user and board[(i + 2) % 3][2 - (i + 2) % 3] != cpu:
            dapr = (i + 2) % 3
            dapc = 2 - (i + 2) % 3
        elif board[i][i] == board[(i + 1) % 3][(i + 1) % 3] == cpu and board[(i + 2) % 3][(i + 2) % 3] != user and \
                board[(i + 2) % 3][(i + 2) % 3] != cpu:
            dapr = (i + 2) % 3
            dapc = (i + 2) % 3
        for j in lis:
            if board[i][j] == board[i][(j + 1) % 3] == cpu and board[i][(j + 2) % 3] != user and board[i][
                (j + 2) % 3] != cpu:
                dapr = i
                dapc = (j + 2) % 3
            elif board[i][j] == board[(i + 1) % 3][j] == cpu and board[(i + 2) % 3][j] != user and board[(i + 2) % 3][
                j] != cpu:
                dapr = (i + 2) % 3
                dapc = j
    if (board[dapr][dapc] == user or board[dapr][dapc] == cpu) or dapc == dapr == -1:  # 공격을 못 하면
        dapr = -1
        dapc = -1
        for i in lis:  # 수비
            if board[i][2 - i] == board[(i + 1) % 3][2 - (i + 1) % 3] == user and board[(i + 2) % 3][
                2 - (i + 2) % 3] != user and board[(i + 2) % 3][2 - (i + 2) % 3] != cpu:
                dapr = (i + 2) % 3
                dapc = 2 - (i + 2) % 3

            elif board[i][i] == board[(i + 1) % 3][(i + 1) % 3] == user and board[(i + 2) % 3][(i + 2) % 3] != user and \
                    board[(i + 2) % 3][(i + 2) % 3] != cpu:
                dapr = (i + 2) % 3
                dapc = (i + 2) % 3

            for j in lis:
                if board[i][j] == board[i][(j + 1) % 3] == user and board[i][(j + 2) % 3] != user and board[i][
                    (j + 2) % 3] != cpu:
                    dapr = i
                    dapc = (j + 2) % 3

                elif board[i][j] == board[(i + 1) % 3][j] == user and board[(i + 2) % 3][j] != user and \
                        board[(i + 2) % 3][j] != cpu:
                    dapr = (i + 2) % 3
                    dapc = j

        if dapr == -1 and dapc == -1 or (board[dapr][dapc] == user or board[dapr][dapc] == cpu):  # 공격도 수비도 못하면
            index = -1
            while index <= 9:
                index += 1
                if board[index // 3][index % 3] != user and board[index // 3][index % 3] != cpu:
                    dapr = index // 3
                    dapc = index % 3
                    break
    dap = dapr * 3 + dapc + 1  # 자리 번호 생성
    board[dapr][dapc] = cpu
    print("저는 %d번 자리에 둘게요." % dap)


def game():  # 게임을 해 보자
    global win, drw, los, a, winner, board  # 앞의 함수들도 그렇지만 global은 맨 처음으로
    cnt = 0
    print("선공과 후공은 랜덤으로 결정할게요.")
    list = [1, 2]
    a = random.choice(list)
    if a == 1:
        print("당신은 선공입니다.")
    else:
        print("당신은 후공입니다.")
    print("그럼 게임을 시작해볼까요?")
    print("현재 상황입니다.")
    print("숫자가 써 있는 칸이 빈 칸,")
    print("%c가 써 있는 칸이 당신이 놓은 칸," % user)
    print("%c가 써 있는 칸이 제가 놓은 칸입니다." % cpu)
    decide()
    while winner == 'C' and cnt < 9:
        status()
        if a == 1:
            play_usr()
            a = 2
            cnt += 1
        else:
            play_cpu()
            a = 1
            cnt += 1
        decide()
    if winner == user:
        print("승자는 당신입니다.")
        win += 1
    elif winner == cpu:
        print("제가 이겼군요.")
        los += 1
    else:
        print("비겼습니다.")
        drw += 1
    print("당신은 %d승 %d무 %d패로, 승률은 %.3f입니다." % (win, drw, los, winning_rate()))
    winner = "C"
    board = [['1', '2', '3'],
             ['4', '5', '6'],
             ['7', '8', '9']]
    ask_regame()


def ask_regame():
    print("다시 하시려면 Y를, 그렇지 않으면 다른 키를 누르세요.")
    ans = input()
    if ans == 'Y':
        game()


intro()
game()
