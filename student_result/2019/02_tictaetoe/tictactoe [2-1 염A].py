import sys
import random

board = ['*', '*', '*', '*', '*', '*', '*', '*', '*']  # 플레이어에게 시각적으로 보이는 게임보드
calc_board = [0, 0, 0, 0, 0, 0, 0, 0, 0]  # 컴퓨터 내에서 계산하는 데 쓰이는 게임보드

Ai_win = 0  # 컴퓨터 승리 횟수
Player_win = 0  # 플레이어 승리 횟수
draw = 0  # 비긴 횟수
starter = 0  # 누가 시작하나요?


def random_starter():  # a가 0이면 플레이어 먼저 a가 1이면 컴퓨터 먼저
    a = random.randrange(2)
    return a


def cal_win_rate(pw, aw, d):  # 승률 계산 함수   승,패,무 가 변수
    if pw + aw + d == 0:  # 한번도 경기를 안함
        print("아직 승률을 계산하기 위한 정보가 없습니다!")
        return 0
    a = (pw * 100) / (pw + aw + d)  # 승률 계산
    print("현재 승률입니다! : ", a, "%")
    return a


def play_game():  # 게임 시작을 묻는 함수
    while 1:
        print("틱택토 게임에 오신 것을 환영합니다! 게임을 진행하시겠습니까? Yes/No")
        ans = input()

        if ans in "Yes yes Y y".split():
            print("게임을 시작합니당")
            return 1

        elif ans in 'NO No n N'.split():
            print("게임을 종료합니다")
            sys.exit()

        else:
            print("제대로 입력하세여여")


def select_team():  # 자신이 O 를 할 건지 X를 할 건지 고르는 함수
    while 1:
        print('O/X 중 하나를 영어 대문자로 입력해 주세요')
        OorX = input()  # O 인지 X 인지 입력받음
        if OorX == 'O' or OorX == 'X':  # 제대로 입력함
            print('당신은 ', OorX, ' 입니다 게임을 플레이 해 봅시다!')
            if OorX == 'O':
                ai_side = 100  # 컴퓨터는 반대로 지정해줌
                ai_OorX = 'X'
                return [OorX, 1, ai_OorX, ai_side]  # 여기서 1은 컴퓨터에서 계산하는 데 쓰인다. 1이 O, 100이 X를 의미한다
            else:  # 반대로 해 줌
                ai_side = 1
                ai_OorX = 'O'
                return [OorX, 100, ai_OorX, ai_side]
        else:
            print('제대로 좀 입력하세용')


def now():  # 현재 게임 상황 시각화, 사용자에게 보여주는 것 이므로 board 리스트 사용
    print(board[0], "    |   ", board[1], "   |   ", board[2])
    print("-------------------------")
    print(board[3], "    |   ", board[4], "   |   ", board[5])
    print("-------------------------")
    print(board[6], "    |   ", board[7], "   |   ", board[8])
    print()
    print()
    print()
    print("---------------------------")


def get_cord(OorX, side):  # 좌표 입력받는 함수
    while 1:
        print("_______________________________________")
        print('당신의 차례입니다! 1 에서 9 중 숫자를 입력 해 주세요 숫자가 의미하는 좌표는 다음과 같습니다')  # 번호 입력으로 좌표를 입력받음
        print("1    |   2   |   3")
        print("-------------------")
        print("4    |   5   |   6")
        print("-------------------")
        print("7    |   8   |   9")
        cord = input()
        if cord in ['1', '2', '3', '4', '5', '6', '7', '8', '9']:  # 1-9면 입력 성공
            if calc_board[int(cord) - 1] != 0:  # 중복 체크, calc_board 배열 사용
                print("중복된 칸에 입력 할 수 없습니다!!!! 다시 해세요")
                continue
            board[int(cord) - 1] = OorX  # 성공적으로 입력
            calc_board[int(cord) - 1] = side  # 컴퓨터 내 계산을 위해 calc_board도 해준다
            print(cord, "를 입력했군요! 현재 상황입니다!------------------------- * 표시는 아무것도 없다는 뜻 입니다!")
            now()  # 입력 상황 보여주기
            return
        else:
            print('제대로 좀 입력하세용')


def no_winner():
    if '*' in board:  # board 에 빈칸이 없는데 승패가 나지 않았으므로 무승부 결정하는 과정
        return 0
    else:
        return 1


def check(turn):  # 승패가 결정났는지 확인하는 함수, turn 은 컴퓨터 내부에서 O 또는 X를 의미하는 것으로 1 또는 100을 입력받는다. 승패가 결정나면 1을 반환한다
    for i in range(3):
        if calc_board[3 * i] + calc_board[3 * i + 2] + calc_board[3 * i + 1] == 3 * turn:  # 가로줄
            return 1
        if calc_board[i] + calc_board[i + 3] + calc_board[i + 6] == 3 * turn:  # 세로줄
            return 1

    if calc_board[0] + calc_board[4] + calc_board[8] == 3 * turn or calc_board[2] + calc_board[4] + calc_board[
        6] == 3 * turn:  # 대각선
        return 1

    return 0


def ai(OorX, side, Ai_OorX, Ai_side):  # 컴퓨터의 플레이 알고리즘
    for i in range(3):  # 이 반복문은 한 줄에 2개가 있는 곳을 찾고 플레이어의 승리를 막을 수 있는 곳에 수를 둔다
        if calc_board[3 * i] + calc_board[3 * i + 2] + calc_board[3 * i + 1] == 2 * side:  # 가로
            for j in range(3):
                if calc_board[3 * i + j] == 0:
                    calc_board[3 * i + j] = Ai_side
                    board[3 * i + j] = Ai_OorX
            return
        if calc_board[i] + calc_board[i + 3] + calc_board[i + 6] == 2 * side:  # 세로
            for j in range(3):
                if calc_board[i + 3 * j] == 0:
                    calc_board[3 * j + i] = Ai_side
                    board[3 * j + i] = Ai_OorX
            return

    if calc_board[0] + calc_board[4] + calc_board[8] == 2 * side:  # 대각선
        for i in range(3):
            if calc_board[4 * i] == 0:
                calc_board[4 * i] = Ai_side
                board[4 * i] = Ai_OorX
                return

    if calc_board[2] + calc_board[4] + calc_board[6] == 2 * side:  # 대각선
        for i in range(3):
            if calc_board[i * 2 + 2] == 0:
                calc_board[i * 2 + 2] = Ai_side
                board[i * 2 + 2] = Ai_OorX
                return

    while True:  # 상대방 승리 조건이 없으므로 랜덤으로 중복되지 않은 곳에 수를 둔다
        a = random.randrange(9)

        if calc_board[a] == 0:
            calc_board[a] = Ai_side
            board[a] = Ai_OorX
            return


def do_it_again():  # 게임 재시작에 관한 함수
    while True:
        print("다시 하시겠습니까?   Y/N")
        ans = input()
        if ans in ['Yes', 'YES', 'Y', 'yes']:
            print("게임을 다시 시작합니다!")
            global board  # 게임보드 초기화한다
            board = ['*', '*', '*', '*', '*', '*', '*', '*', '*']
            global calc_board
            calc_board = [0, 0, 0, 0, 0, 0, 0, 0, 0]
            return 1
        elif ans in ['No', 'NO', 'no', 'N']:  # 게임종료
            print("게임을 종료합니다!")
            sys.exit()
            return 0
        else:
            print("제대로좀 입력해주세영~~~")


game_start = 1  # 새로 시작하는 지에 대한 여부

while True:
    if game_start:  # 새로운 시작
        cal_win_rate(Player_win, Ai_win, draw)  # 승률 계산
        play_game()  # 게임 시작 물어봄
        x = select_team()  # 팀 고르기, 배열을 반환하므로 각각 알맞은 변수 할당
        OorX = x[0]  # 예시, 내가 O를 고르면 OorX = 'O', side = 1, Ai_OorX = 'X', Ai_side = 100
        side = int(x[1])
        Ai_OorX = x[2]
        Ai_side = int(x[3])
        stater = random_starter()
        game_start = 0
    if starter == 1 or starter == 100:  # starter 가 1이면 플레이어가 먼저 시작한다
        starter = 100
        get_cord(OorX, side)  # 좌표 입력

        if no_winner():  # 턴을 하자마자 바로 무승부 판정
            print("비겼네요!")
            game_start = 1  # 새로 시작 모드 켜기
            draw = draw + 1  # 승 무 패 횟수 갱신
            cal_win_rate(Player_win, Ai_win, draw)  # 승률 계산
            do_it_again()  # 다시 할 건지 물어보는 함수
            continue

        if check(side):  # 무승부 아니라면 승 판정, 플레이어가 수를 두자마자 판단하므로 여기서 승 판단이 나면 무조건 플레이어가 승리했다는 뜻이다.
            print("당신이 이겼네요! 축하드립나다!")
            game_start = 1
            Player_win = Player_win + 1
            cal_win_rate(Player_win, Ai_win, draw)
            do_it_again()
            continue

    if starter == 0 or starter == 100:
        starter = 100
        ai(OorX, side, Ai_OorX, Ai_side)  # 컴퓨터 턴 진행
        print("컴퓨터가 자신의 턴을 진행하였습니다! 다음과 같은 수를 두엇군요!------------------------------")
        now()  # 컴퓨터가 놓은 수 보여주기

        if no_winner():  # 컴퓨터가 수를 둔 후 바로 판정
            print("비겼네요!")
            game_start = 1
            draw = draw + 1
            cal_win_rate(Player_win, Ai_win, draw)
            do_it_again()
            continue

    if check(Ai_side):  # 컴퓨터가 승리했는지 판단한다.
        print("당신이 패배했네요... 아쉽군요!")
        game_start = 1
        Ai_win = Ai_win + 1
        cal_win_rate(Player_win, Ai_win, draw)
        do_it_again()
        continue
