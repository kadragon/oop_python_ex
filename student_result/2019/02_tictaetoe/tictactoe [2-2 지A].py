import random

board = [0] * 10  # 보드 설정
for i in range(10):
    board[i] = str(i)


def computer_judgement():  # 컴퓨터가 어디에 둘지에 대해 판단하는 함수
    global board
    line_list = [[1, 2, 3], [4, 5, 6], [7, 8, 9], [1, 4, 7], [2, 5, 8], [3, 6, 9], [1, 5, 9], [3, 5, 7]]
    for line in line_list:
        cnt = 0
        for i in line:  # 각 줄 마다 있는 X와 O의 개수를 세고, O가 2개 또는 X가 2개일 경우를 판단 후 그 줄의 남은  자리에 놓게 함
            if board[i] == 'X':
                cnt -= 1
            if board[i] == 'O':
                cnt += 1
            if cnt == -2:
                for i in line:
                    if '1' <= board[i] <= '9':
                        return i
            if cnt == 2:
                for i in line:
                    if '1' <= board[i] <= '9':
                        return i
    rdn = random.randint(1, 9)
    while board[rdn] >= '9' or board[rdn] <= '1':  # 막을 필요가 없을 시 랜덤으로 X를 두는 방법
        rdn = random.randint(1, 9)
    return rdn


def end_of_game():  # 누가 이겼는지에 대한 여부 판정
    global board
    global win
    line_list = [[1, 2, 3], [4, 5, 6], [7, 8, 9], [1, 4, 7], [2, 5, 8], [3, 6, 9], [1, 5, 9], [3, 5, 7]]
    for line in line_list:
        cnt_user = 0
        cnt_com = 0
        for i in line:
            if board[i] == 'X':  # X개수 세기
                cnt_com += 2
            if board[i] == 'O':  # O개수 세기
                cnt_user += 1
            if cnt_com == 6:
                return cnt_com
            if cnt_user == 3:
                return cnt_user
    return 0


game = 0
while True:  # 메인 함수
    win = 0
    sum = 0
    game += 1
    board = [0] * 10
    for i in range(10):
        board[i] = str(i)
    print('게임을 시작하겠습니다.1~9까지의 숫자를 입력해 주시면 됩니다.')
    while sum < 9:  # 최대 9번까지 놓을 수 있기 때문에 그 후 while문 break
        print('----------------')
        print(board[1], '|', board[2], '|', board[3])  # 현 상황 표현
        print(board[4], '|', board[5], '|', board[6])
        print(board[7], '|', board[8], '|', board[9])
        print('사용자님의 차례입니다! 지지 않게 조심하세욬ㅋㅋㅋ')
        sum += 1
        flag = True  # 사용자가 입력한 값이 알맞은 값인지를 판단
        while flag:
            flag = False
            user = input("입력 : ")
            if len(user) != 1 or not '1' <= user <= '9':
                print("1~9 사이의 한 자리 숫자를 입력해주세요.")
                flag = True
            else:
                user = int(user)

        board[user] = 'O'  # 사용자가 입력한 칸을 O표시
        print('----------------')
        print(board[1], '|', board[2], '|', board[3])
        print(board[4], '|', board[5], '|', board[6])
        print(board[7], '|', board[8], '|', board[9])
        if end_of_game() != 0:  # 승 패 판단
            if end_of_game() == 6:
                print('못하시네요...연습하셔야....^^')
            else:
                print('연습하고 오겠습니다...')
                win += 1
            break
        if sum >= 9:
            break
        print('드디어 제 차례군요 하하 전 여기다 두겠습니다. 묘수죠!')
        board[computer_judgement()] = 'X'  # 컴퓨터가 판단한 곳에 X표시
        print('----------------')
        print(board[1], '|', board[2], '|', board[3])
        print(board[4], '|', board[5], '|', board[6])
        print(board[7], '|', board[8], '|', board[9])
        sum += 1
        if end_of_game() != 0:  # 승 패 판단
            if end_of_game() == 6:
                print('못하시네요...연습하셔야....^^')
            else:
                print('연습하고 오겠습니다...')
                win += 1
            break
    print("승률 : %f" % (float(win / game) * 100))  # 승률 계산 후 표시
    print('한판 더?  yes/no')  # 재개 의사 질문
    ans = input()
    if ans == 'no':  # 재개 거부시 프로그램 종
        break
