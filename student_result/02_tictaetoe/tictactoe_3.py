import random
import time

# intro, show_board, print_winner 함수 내 '=' 출력 횟수
NUMBER_DASH = 50
# 공백과 플레이어와 AI의 말 모양
NO_MARK = '　'
MARKS = ('Ｏ', 'Ｘ')


# 게임 처음 시작 시 게임 설명, 입력 방법 출력하는 함수. 중간에 2초씩 쉬는 구간 3개 있음.
# 매개변수 없음, 반환값 없음.
def intro():
    print('=' * NUMBER_DASH)
    print('Tic Tac Toe')
    print('=' * NUMBER_DASH)
    time.sleep(2)  # 2초 휴식
    print('게임 설명')
    print('플레이어와 컴퓨터가 차례로 3x3 크기의 게임판 위에 말을 놓습니다.')
    print('한 줄이 자신의 말로 가득 찬다면 승리합니다.')
    time.sleep(2)  # 2초 휴식
    print('입력 방법')
    print('┌─┬─┬─┐')  # 폰트에 따라서 레이아웃이 뭉개질 수 있다.
    print('│１│２│３│')
    print('├─┼─┼─┤')
    print('│４│５│６│')
    print('├─┼─┼─┤')
    print('│７│８│９│')
    print('└─┴─┴─┘')
    print('각 칸에 쓰인 숫자를 입력하면 그 칸에 말을 놓을 수 있습니다.')
    time.sleep(2)  # 2초 휴식
    print('=' * NUMBER_DASH)


# 게임을 재시작할 지 입력받는 함수.
# 매개변수 없음, 반환값 bool: 재시작할 시 True 아닐 시 False.
def chk_restart():
    while True:
        s = input('게임을 다시 시작하시겠습니까?(Y/N) : ')
        s = s.upper()  # 전부 대문자로 변경
        if s.startswith('Y'):  # Y로 시작하면 True 반환
            return True
        elif s.startswith('N'):  # N으로 시작하면 False 반환
            return False
        else:  # 둘 다 아니면 다시 입력
            print('형식에 맞게 입력해주세요.')


# 플레이어가 플레이할 말을 입력받는 함수.
# 매개변수 없음, 반환값 튜플: (<플레이어의 말>, <AI의 말>).
def choose_mark():
    while True:
        s = input('O와 X 중 말을 선택하세요.(O/X) : ')
        s = s.upper()  # 전부 대문자로 변경
        if s == 'O':  # O이면,
            return MARKS[0], MARKS[1]
        elif s == 'X':  # X이면,
            return MARKS[1], MARKS[0]
        else:  # 둘 다 아니면 다시 입력
            print('형식에 맞게 입력해주세요.')


# 먼저 시작할 것인지 입력받는 함수. 먼저 시작하면 0, 아니면 1 반환.
# 매개변수 없음, 반환값 정수: 0 또는 1.
def choose_first():
    while True:
        s = input('먼저 시작하시겠습니까?(Y/N) : ')
        s = s.upper()  # 전부 대문자로 변경
        if s.startswith('Y'):  # Y로 시작하면 0 반환
            return 0
        elif s.startswith('N'):  # N으로 시작하면 1 반환
            return 1
        else:  # 둘 다 아니면 다시 입력
            print('형식에 맞게 입력해주세요.')


# 게임판에 말을 놓는 함수.
# 매개변수 board: 게임판 r: 행 c: 열 char: 문자, 반환값 없음.
def place_mark(board, r, c, char):
    board[r][c] = char


# 어디에 말을 놓을지 입력받는 함수.
# 매개변수 board: 게임판 p_mark: 플레이어의 말의 문자, 반환값 없음.
def get_input(board, p_mark):
    while True:
        s = input('어디에 놓으시겠습니까?(1~9) : ')
        if s.isdigit() and 1 <= int(s) <= 9:  # 1~9의 정수인지 검사
            s = int(s)
            r = (s - 1) // 3  # 행
            c = (s - 1) % 3  # 열
            if board[r][c] != NO_MARK:
                print('이미 말이 놓여 있습니다.')
                continue
            place_mark(board, r, c, p_mark)
            break
        else:
            print('형식에 맞게 입력해주세요.')


# 어느 라인에 두 개 이상의 검사할 말이 있는지 검사한 후 있으면 나머지 한 칸에 말을 놓는 함수.
# 매개변수 board: 게임판 tu: 검사할 라인 튜플 mark_to_chk: 검사할 말의 문자 mark: 놓을 말의 문자, 반환값 bool: 말을 놓았으면 True 놓지 못했으면 False.
def chk_two_consecutive_marks(board, tu, mark_to_chk, mark):
    if board[tu[0]][tu[1]] == board[tu[2]][tu[3]] == mark_to_chk and board[tu[4]][tu[5]] == NO_MARK:
        place_mark(board, tu[4], tu[5], mark)
        return True
    elif board[tu[0]][tu[1]] == board[tu[4]][tu[5]] == mark_to_chk and board[tu[2]][tu[3]] == NO_MARK:
        place_mark(board, tu[2], tu[3], mark)
        return True
    elif board[tu[2]][tu[3]] == board[tu[4]][tu[5]] == mark_to_chk and board[tu[0]][tu[1]] == NO_MARK:
        place_mark(board, tu[0], tu[1], mark)
        return True
    else:
        return False


# 컴퓨터가 말을 놓을 곳을 정하는 함수.
# 매개변수 board: 게임판 lines: 검사할 라인 튜플들을 모은 튜플 p_mark: 플레이어의 말의 문자 c_mark: 컴퓨터의 말의 문자, 반환값 없음.
def run_ai(board, lines, p_mark, c_mark):
    for i in lines:
        if chk_two_consecutive_marks(board, i, c_mark, c_mark):  # 컴퓨터의 말이 한 줄에 2개 있는지 검사.
            return
    for i in lines:
        if chk_two_consecutive_marks(board, i, p_mark, c_mark):  # 플레이어의 말이 한 줄에 2개 있는지 검사.
            return
    a = list(range(9))  # 0부터 8까지 리스트로 만듦.
    b = a.copy()
    for i in b:
        r = i // 3
        c = i % 3
        if board[r][c] != NO_MARK:  # 해당 칸이 차 있으면 원소 제거.
            a.remove(i)
    random.shuffle(a)  # 랜덤으로 섞어서 첫번째 원소가 가리키는 칸에 말을 놓음.
    place_mark(board, a[0] // 3, a[0] % 3, c_mark)


# 어느 라인의 3개의 말이 모두 같은 말인지 검사하여 모두 같은 말이면 그 말의 문자를 반환하고 그렇지 않으면 빈 문자열을 반환하는 함수.
# 매개변수 board: 게임판 tu: 검사할 라인 튜플, 반환값 문자열: <놓여있는 말의 문자>.
def chk_three_consecutive_marks(board, tu):
    if board[tu[0]][tu[1]] == board[tu[2]][tu[3]] == board[tu[4]][tu[5]] and board[tu[0]][tu[1]] != NO_MARK:
        return board[tu[0]][tu[1]]
    else:
        return ''


# 현재 승리한 사람이 있는지 검사하여 플레이어가 승리했으면 'p', 패배했으면 'c', 비겼으면 빈 문자열을 반환하는 함수.
# 매개변수 board: 게임판 lines: 검사할 라인 튜플들을 모은 튜플 p_mark: 플레이어의 말의 문자 c_mark: 컴퓨터의 말의 문자, 반환값 문자열: <이긴 사람>.
def chk_win(board, lines, p_mark, c_mark):
    win = ''
    for i in lines:
        win = chk_three_consecutive_marks(board, i)
        if win != '':
            break
    if win == p_mark:
        return 'p'
    elif win == c_mark:
        return 'c'
    else:
        return ''


# 게임 결과를 출력하는 함수.
# 매개변수 win: 이긴 사람의 말의 문자, 반환값 없음.
def print_winner(win):
    if win == 'p':
        print('승리하셨습니다!')
    elif win == 'c':
        print('패배하셨습니다.')
    else:
        print('비기셨습니다.')
    print('=' * NUMBER_DASH)


# 현재 게임판의 모습을 출력하는 함수.
# 매개변수 board: 게임판, 반환값 없음.
def show_board(board):
    print('=' * NUMBER_DASH)
    print('┌─┬─┬─┐')
    print('│%s│%s│%s│' % (board[0][0], board[0][1], board[0][2]))
    print('├─┼─┼─┤')
    print('│%s│%s│%s│' % (board[1][0], board[1][1], board[1][2]))
    print('├─┼─┼─┤')
    print('│%s│%s│%s│' % (board[2][0], board[2][1], board[2][2]))
    print('└─┴─┴─┘')


intro()  # 게임 설명과 입력 방법을 출력한다.
game = True
while game:
    bd = [[NO_MARK] * 3] + [[NO_MARK] * 3] + [[NO_MARK] * 3]  # 게임판
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

    player_mark, computer_mark = choose_mark()  # 말을 선택한다.
    is_not_first = choose_first()  # 먼저 시작할 것인지 선택한다.

    for turn in range(9):  # 총 9번을 반복한다.
        if turn % 2 == is_not_first:  # 플레이어 차례이면,
            show_board(bd)  # 게임판을 출력하고
            get_input(bd, player_mark)  # 놓을 말의 위치를 입력받아 놓는다.
        else:  # 컴퓨터 차례이면
            show_board(bd)  # 게임판을 출력하고
            print('컴퓨터가 말을 놓는 중...')
            time.sleep(1)  # 1초 휴식한 다음
            run_ai(bd, lines_to_win, player_mark, computer_mark)  # 컴퓨터의 말을 놓는다.
        winner = chk_win(bd, lines_to_win, player_mark, computer_mark)  # 승리한 사람이 있는지 검사한다.
        if winner != '':  # 승리한 사람이 있으면 for 문을 탈출한다.
            break
    show_board(bd)  # 게임판을 출력하고
    print_winner(winner)  # 게임 결과를 출력한다.

    game = chk_restart()  # 재시작할지 선택한다.
    print('=' * NUMBER_DASH)
