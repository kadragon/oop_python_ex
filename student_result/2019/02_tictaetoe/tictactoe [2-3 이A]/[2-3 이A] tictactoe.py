import random
import time

user_OX = 0  # 유저가 O(선)인지 X(후)인지 판단하는 변수.
user_win = 0
win_and_lose = 0
# 유저의 이긴 횟수와 전체 횟수를 저장하는 변수
the_board = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
"""
the_board: 틱택토를 진행하는 판.
0: 아직 아무것도 놓이지 않음
1: O(선)이 놓음
-1: X(후)가 놓음

the_board 는 2차원(?) 리스트로 만들어졌으나
0~8까지의 정수(n)와 (i, j)가 호환 가능하다
i = n // 3
j = n % 3
이후의 모든 the_board 연산은 이러한 특징을 이용하였다.
"""


def print_now_board():
    """
    현재 판의 상황을 출력한다.
    the_board 에서 값이 0이면 해당 부분의 번호를
    값이 1이면 O를, 값이 -1이면 X를 출력한다.
    :return: 없음
    """
    global the_board

    print("=" * 20)
    for i in range(3):
        for j in range(3):
            print(" | ", end='')
            if the_board[i][j] == 1:
                print("O", end='')  # 1일 때 O 출력
            elif the_board[i][j] == -1:
                print("X", end='')  # -1일때 X 출력
            else:
                print(i * 3 + j, end='')  # 1도, -1도 아닐 때, 즉 0일때 해당 판의 번호(0~8 정수)를 출력
        print(" |")
    print("=" * 20)


def start_the_game():
    """
    게임이 처음 시작하거나 리플레이 할 때 실행되는 함수
    플레이어가 선을 할 것인지 후를 할 것인지 입력받는다
    :return: 1(선) 혹은 -1(후)
    """
    print("=" * 20)
    print("start the new game")
    print("the first turn is 'O'")
    print("start the game, or start with 'X'")
    while True:  # 플레이어가 올바른 입력을 할 때까지 입력받는다
        start_answer = input("(start / X) >>").upper()

        if start_answer == "START" or start_answer == 'O':
            return 1
        if start_answer == "X":
            return -1


def get_user_answer():
    """
    플레이어의 차례에서 플레이어의 답을 입력받는다
    the_board 에서 0의 값을 가지는 부분만 입력받는다
    :return: 0~8사이의 정수
    """
    global the_board
    print_now_board()
    time.sleep(0.5)
    print("it's your turn")
    while True:
        try:
            user_answer = int(input("(0~8) >>"))
            if 0 <= user_answer <= 9:
                if the_board[user_answer // 3][user_answer % 3] == 0:
                    break
        except:
            pass

    return user_answer


def check_anyone_can_win(OX):
    """
    O와 X중 한 줄을 만들 수 있는 장소가 있을 때 해당 장소를 알아내는 함수
    O는 1, X는 -1로 저장했기 때문에,
    한 줄씩 원소를 더했을 때 값이 2이며 곱했을 때 값이 0이면
    그 한 줄을 다음 번의 시행으로 꽉 채울 수 있다는 뜻이므로 이를 이용하였다
    :param OX: int, 1 혹은 -1: 선을 체크할지 후를 체크할지 인자를 받아서 체크한다.
    :return: 0~8 사이의 정수. the_board 에서 OX와 동일한 번호가 한 줄을 완성할 수 있는 경우라면 어느 곳을 두어야 하는지 알아내어 리턴한다.
    """

    global the_board
    sum_diagonal1 = 0
    times_diagonal1 = 1
    # 대각선(\)을 확인하는 데에 쓰는 변수
    sum_diagonal2 = 0
    times_diagonal2 = 1
    # 대각선(/)을 확인하는 데에 쓰는 변수

    for i in range(3):
        sum_vertical = 0
        times_vertical = 1
        # 세로줄을 확인하는 데에 쓰는 변수
        sum_parallel = 0
        times_parallel = 1
        # 가로줄을 확인하는 데에 쓰는 변수

        sum_diagonal1 += the_board[i][i]
        times_diagonal1 *= the_board[i][i]
        sum_diagonal2 += the_board[i][2 - i]
        times_diagonal2 *= the_board[i][2 - i]
        # 대각선에 해당하는 값들을 더하고 곱한다.

        for j in range(3):  # 가로줄, 세로줄에 해당하는 값들을 더하고 곱한다.
            sum_vertical += the_board[j][i]
            times_vertical *= the_board[j][i]
            sum_parallel += the_board[i][j]
            times_parallel *= the_board[i][j]

        if sum_vertical == 2 * OX and times_vertical == 0:  # 세로줄이 조건을 만족했을 경우
            for j in range(3):  # 어디를 두면 이길 수도 있는지, 그 위치를 찾아 반환한다.
                if the_board[j][i] == 0:
                    return 3 * j + i
        if sum_parallel == 2 * OX and times_parallel == 0:  # 가로줄이 조건을 만족했을 경우
            for j in range(3):  # 어디를 두면 이길 수도 있는지, 그 위치를 찾아 반환한다.
                if the_board[i][j] == 0:
                    return 3 * i + j

    if sum_diagonal1 == 2 * OX and times_diagonal1 == 0:  # 대각선(\)이 조건을 만족했을 경우
        for i in range(3):  # 어디를 두면 이길 수도 있는지, 그 위치를 찾아 반환한다.
            if the_board[i][i] == 0:
                return i * 3 + i
    if sum_diagonal2 == 2 * OX and times_diagonal2 == 0:  # 대각선(/)이 조건을 만족했을 경우
        for i in range(3):  # 어디를 두면 이길 수도 있는지, 그 위치를 찾아 반환한다.
            if the_board[i][2 - i] == 0:
                return i * 3 + (2 - i)

    return -1  # 이길 수 있을 만한 경우가 없을 때, -1을 반환한다.


def get_com_answer():
    """
    컴퓨터의 수를 만들어 반환한다.
    컴퓨터는 먼저, 자신이 이번에 두면 무조건 이기는 위치를 찾는다
    그러한 위치가 없으면,
    플레이어를 막기 위한 위치를 찾는다.
    그러한 위치가 없으면,
    랜덤한 값을 택한다.
    :return: 0~8 사이의 정수. the_board의 위치에 해당한다.
    """
    global the_board
    global user_OX

    com_OX = int(- user_OX)  # 컴퓨터의 수가 무엇인지 알아낸다.
    check_com_should_do = check_anyone_can_win(com_OX)  # 이번에 두면 반드시 이기는 곳을 알아낸다
    if check_com_should_do != -1:
        return check_com_should_do

    check_com_must_do = check_anyone_can_win(user_OX)  # 플레이어를 막아야 하는 곳이 있다면
    if check_com_must_do != -1:  # 찾아서 막아낸다.
        return check_com_must_do

    '''
    # 본래 중앙을 먼저 선점하도록 코드를 만들었었음.
    if the_board[1][1] == 0:
        return 1 * 3 + 1
    '''

    shuffled_list = list(range(9))
    random.shuffle(shuffled_list)  # 랜덤하게 0~8의 정수를 섞어낸다
    for i in range(9):  # the_board에 기입되지 않았을 때만 해당 위치를 반환한다.
        if the_board[shuffled_list[i] // 3][shuffled_list[i] % 3] == 0:
            return shuffled_list[i]


def check_anyone_win():
    """
    O와 X중 누구라도 이겼는지를 체크한다.
    한 줄에 있는 원소들의 합이 3혹은 -3이 되었을 때 각각 O와 X가 이긴 것임을 이용하였다
    O가 이겼다면 1을
    X가 이겼다면 -1을
    누구도 이기지 못한 상황이라면 0을 반환한다.
    :return: 위 조건에 맞는 -1, 0, 1 중 한 가지 정수
    """
    global the_board

    sum_diagonal1 = 0  # 대각선(\)을 체크하는 변수
    sum_diagonal2 = 0  # 대각선(/)을 체크하는 변수

    for i in range(3):
        sum_parallel = 0  # 가로줄을 체크하는 변수
        sum_vertical = 0  # 세로줄을 체크하는 변수

        sum_diagonal1 += the_board[i][i]
        sum_diagonal2 += the_board[i][2 - i]
        # 대각선에 있는 원소들을 더한다

        for j in range(3):  # 가로, 세로줄의 원소들을 더한다.
            sum_parallel += the_board[i][j]
            sum_vertical += the_board[j][i]

        if sum_vertical == 3 or sum_vertical == -3:  # 세로줄이 조건을 만족했을 경우
            return sum_vertical // 3  # 1혹은 -1의 값을 반환한다.
        if sum_parallel == 3 or sum_parallel == -3:  # 가로줄이 조건을 만족했을 경우
            return sum_parallel // 3  # 1혹은 -1의 값을 반환한다.

    if sum_diagonal1 == 3 or sum_diagonal1 == -3:
        return sum_diagonal1 // 3
    if sum_diagonal2 == 3 or sum_diagonal2 == -3:
        return sum_diagonal2 // 3
    # 대각선이 조건을 만족했을 경우, 11 혹은 -1을 반환

    return 0  # 누구도 이긴 상황이 아닐 때, 0을 반환한다.


def do_now_turn(turn):
    """
    현재 턴을 진행한다
    turn 이 user_OX와 같으면 user 의 입력을 받는다.
    그렇지 않으면 컴퓨터의 답을 만든다.
    :param turn: 현재 턴의 상태. 1(선)혹은 -1(후)이다
    :return: 없음
    """
    global user_OX
    global the_board

    if user_OX == turn:  # 유저의 차례일 때
        user_answer = get_user_answer()
        the_board[user_answer // 3][user_answer % 3] = turn
    else:  # 컴퓨터의 차례일 때
        print("get com answer...")
        time.sleep(1)
        com_answer = get_com_answer()
        the_board[com_answer // 3][com_answer % 3] = turn


def check_more_game():
    """
    한 게임 더 할 것인지 묻는다.
    더 할 것이라면 True, 아니라면 False 반환
    :return: bool
    """
    print("the game is done")
    print("want more game?(y/n)")
    while True:
        try:
            user_more_game_answer = input(">>").upper()

            if user_more_game_answer == "Y":
                return True
            if user_more_game_answer == "N":
                return False
        except:
            pass


def Main():
    """
    전체적인 판을 돌리는 main 함수
    :return: check_more_game 과 같다.
    """
    global user_OX
    global the_board
    global user_win
    global win_and_lose

    user_OX = 0
    the_board = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
    check_win = 0
    # 변수들을 초기화한다.

    user_OX = start_the_game()  # 게임을 시작하며 유저의 선, 후를 받는다.
    now_turn = 1

    for i in range(9):
        do_now_turn(now_turn)  # 현재 턴을 진행한다.

        now_turn = - now_turn  # 턴 상태를 바꾼다.

        check_win = check_anyone_win()
        if check_win != 0:  # 누구라도 이겼다면, 게임을 종료한다.
            break

    win_and_lose += 1

    if check_win == user_OX:  # 유저가 이겼을 때
        user_win += 1
        print("wow! you win!")
    elif check_win == - user_OX:  # 컴퓨터가 이겼을 때
        print("")
        print("the last board")
        print_now_board()
        print("computer win!")
    else:  # 비겼을 때
        print("")
        print("the last board")
        print_now_board()
        print("good game")

    print("")
    time.sleep(0.3)

    print("the winning rate: %05.1f %%" % (user_win / win_and_lose * 100))
    time.sleep(0.5)

    return check_more_game()  # 다음 게임을 할 것인가 물어보고, 그 답을 반환


while True:
    check = Main()  # 게임을 계속 할 것인지 저장하는 변수
    if not check:  # check 가 False 일 때, 게임은 종료된다.
        print("ok. good bye!")
        break
