import random, time

NOTHING = '　'  # 공백
HORSE = ('Ｏ', 'Ｘ')  # 말 모양
play_num = 0  # 게임 횟수
win_num = 0  # 승리 횟수


def choose_horse():  # 말을 선택하는 함수.
    while True:
        s = input('말을 선택하세요. (O/X) : ')
        s = s.upper()
        if s == 'O':
            return HORSE[0], HORSE[1]
        elif s == 'X':
            return HORSE[1], HORSE[0]
        else:
            print('다시 입력해주시길 바랍니다.')


def choose_first():  # 시작 순서를 정하는 함수
    while True:
        a = input('랜덤으로 순서를 정할까요? (Y/N) : ')
        a = a.upper()
        if a == 'Y':
            b = random.randrange(2)
            if b == 0:
                print("컴퓨터가 먼저 시작합니다.")
                return 1
            else:
                print("플레이어가 먼저 시작합니다.")
                return 0
        elif a == 'N':
            s = input('먼저 시작하시겠습니까? (Y/N) : ')
            s = s.upper()
            if s == 'Y':
                return 0
            elif s == 'N':
                return 1
            else:
                print('다시 입력해주시길 바랍니다.')
        else:
            print('다시 입력해주시길 바랍니다.')


def where(board, playhorse):  # 어디에 놓을지 입력받는 함수, playhorse: 플레이어의 말의 문자
    while True:
        s = input('어디에 놓으시겠습니까?(1~9) : ')
        if s.isdigit() and 1 <= int(s) <= 9:  # 1~9인지 확인
            s = int(s)
            c = (s - 1) % 3  # 열
            r = (s - 1) // 3  # 행
            if board[r][c] != NOTHING:
                print('이미 말이 있습니다.')
                continue
            place_horse(board, r, c, playhorse)
            break
        else:
            print('다시 입력해주시길 바랍니다.')


def place_horse(board, r, c, here):  # 게임판에 말을 놓는 함수.
    board[r][c] = here


def show_board(board):  # 현재 게임판의 모습을 출력하는 함수.
    print('┌~~┬~~┬~~┐')
    print('│%s│%s│%s│' % (board[0][0], board[0][1], board[0][2]))
    print('├~~┼~~┼~~┤')
    print('│%s│%s│%s│' % (board[1][0], board[1][1], board[1][2]))
    print('├~~┼~~┼~~┤')
    print('│%s│%s│%s│' % (board[2][0], board[2][1], board[2][2]))
    print('└~~┴~~┴~~┘')


def place_com(board, lines, playhorse, comhorse):  # 컴퓨터가 말을 놓을 곳을 정하는 함수, lines: 검사할 라인 튜플들을 모은 튜플
    for i in lines:
        if chk_two_rows(board, i, comhorse, comhorse):  # 컴퓨터의 말이 한 줄에 2개 있는지 검사.
            return
    for i in lines:
        if chk_two_rows(board, i, playhorse, comhorse):  # 플레이어의 말이 한 줄에 2개 있는지 검사.
            return
    eight = list(range(9))  # 0부터 8까지 리스트
    eightt = eight.copy()
    for i in eightt:
        r = i // 3
        c = i % 3
        if board[r][c] != NOTHING:  # 해당 칸이 차 있으면 원소 제거.
            eight.remove(i)
    random.shuffle(eight)  # 랜덤으로 섞음
    place_horse(board, eight[0] // 3, eight[0] % 3, comhorse)  # 첫 번째 원소가 가리키는 칸에 말을 놓음.


# 어느 라인에 두 개의 말이 있으면 나머지 한 칸에 말을 놓는 함수.
def chk_two_rows(board, tu, horse_to_chk, horse):  # tu: 검사할 라인 튜플, horse_to_chk: 검사할 말의 문자, horse: 놓을 말의 문자
    if board[tu[0]][tu[1]] == board[tu[2]][tu[3]] == horse_to_chk and board[tu[4]][tu[5]] == NOTHING:
        place_horse(board, tu[4], tu[5], horse)
        return True
    elif board[tu[0]][tu[1]] == board[tu[4]][tu[5]] == horse_to_chk and board[tu[2]][tu[3]] == NOTHING:
        place_horse(board, tu[2], tu[3], horse)
        return True
    elif board[tu[2]][tu[3]] == board[tu[4]][tu[5]] == horse_to_chk and board[tu[0]][tu[1]] == NOTHING:
        place_horse(board, tu[0], tu[1], horse)
        return True
    else:
        return False


def chk_three_rows(board, tu):  # 라인의 3개의 말이 같은 말이면 그 말의 문자를 반환하는 함수.
    if board[tu[0]][tu[1]] == board[tu[2]][tu[3]] == board[tu[4]][tu[5]] and board[tu[0]][tu[1]] != NOTHING:
        return board[tu[0]][tu[1]]  # 놓여있는 말의 문자 반환
    else:
        return ''  # 없으면 빈 문자열 반환


def chk_win(board, lines, playhorse, comhorse):  # 승리자 검사 함수
    win = ''
    global win_num
    for i in lines:
        win = chk_three_rows(board, i)
        if win != '':
            break
    if win == playhorse:
        win_num += 1
        return 'p'  # 승리하면 p 반환
    elif win == comhorse:
        return 'c'  # 패배하면 c 반환
    else:
        return ''  # 비기면 빈 문자열 반환


def print_winner(win):  # 게임 결과를 출력하는 함수.
    global play_num
    play_num += 1  # 게임 횟수 1 증가
    win_rate()
    if win == 'p':
        print('승리하셨습니다! ><')
    elif win == 'c':
        print('패배하셨습니다ㅜㅜ')
    else:
        print('비기셨습니다...')


def chk_restart():  # 게임을 재시작할 지 입력받는 함수.
    while True:
        s = input('게임을 다시 하겠습니까? (Y/N) : ')
        s = s.upper()  # 대문자로 변경
        if s == 'Y':  # Y면 True 반환
            return True
        elif s == 'N':  # N이면 False 반환
            return False
        else:  # 둘 다 아니면 다시 입력
            print('다시 입력해주시길 바랍니다.')


def win_rate():
    global win_num
    global play_num
    rate = (win_num / play_num)
    print("%d %d" % (win_num, play_num))
    print("승률 : %f" % rate)


print('Tic Tac Toe')
time.sleep(1)  # 2초 기다린다
print('한 줄이 자신의 말로 가득 차면 승리합니다.')
time.sleep(1)
print('┌~~┬~~┬~~┐')
print('│１│２│３│')
print('├~~┼~~┼~~┤')
print('│４│５│６│')
print('├~~┼~~┼~~┤')
print('│７│８│９│')
print('└~~┴~~┴~~┘')
print('각 칸에 쓰인 숫자를 입력하면 그 칸에 말을 놓을 수 있습니다.')
time.sleep(1)
game = True
while game:
    bd = [[NOTHING] * 3] + [[NOTHING] * 3] + [[NOTHING] * 3]  # 게임판
    lines_to_win = (  # 승패를 판단하기 위해 검사해야 할 구역들
        (0, 0, 0, 1, 0, 2),  # (<1번 칸의 행>, <1번 칸의 열>, <2번 칸의 행>, <2번 칸의 열>, <3번 칸의 행>, <3번 칸의 열>)
        (1, 0, 1, 1, 1, 2),
        (2, 0, 2, 1, 2, 2),
        (0, 0, 1, 0, 2, 0),
        (0, 1, 1, 1, 2, 1),
        (0, 2, 1, 2, 2, 2),
        (0, 0, 1, 1, 2, 2),
        (0, 2, 1, 1, 2, 0)
    )
    winner = ''
    player_horse, computer_horse = choose_horse()  # 말을 선택
    is_not_first = choose_first()  # 순서 선택
    for turn in range(9):
        if turn % 2 == is_not_first:  # 플레이어 차례의 경우
            show_board(bd)  # 게임판 출력
            where(bd, player_horse)  # 말의 위치 선택
        else:  # 컴퓨터 차례의 경우
            print('컴퓨터가 말을 놓는 중...')
            time.sleep(1)
            place_com(bd, lines_to_win, player_horse, computer_horse)  # 컴퓨터의 말을 놓는다.
        winner = chk_win(bd, lines_to_win, player_horse, computer_horse)  # 승리한 사람이 있는지 검사
        if winner != '':  # 승리자가 있으면 반복문 탈출
            break
    show_board(bd)  # 게임판 출력
    print_winner(winner)  # 게임 결과 출력
    game = chk_restart()  # 재시작 선택
