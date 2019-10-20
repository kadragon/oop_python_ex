import random

play = True
playtime = 0
wintime = 0
start_message = """
=========  =====       ===
   | |      | |      ==
   | |      | |     =
   | |      | |     =
   | |      | |      ==
   | |     =====       ===

Welcome to Tic-Tac-Toe Game!
You will fight with this computer!
You'll have playground like this
1 | 2 | 3
=========
4 | 5 | 6
=========
7 | 8 | 9
type the number between 1 to 9
순서는 랜덤으로 정해집니다.

Good Luck!
"""


def player_order():
    """
    player의 순서를 결정해주는 함수
    :return: str
    """
    a = random.randrange(0, 2)  # 순서는 랜덤임
    if a is 0:
        return 'F'
    else:
        return 'S'


def input_letter():
    """
    player가 'X', 'O'중 선택한 것을 받아들이는 함수
    :return: str
    """
    trash = []
    O_list = ['o', 'O']
    X_list = ['x', 'X']
    while True:
        try:
            print("Choose your letter( type O or X )")
            a = input()
            if a in O_list:
                trash.append('O')
            elif a in X_list:
                trash.append('X')
            return trash[0]  # 만약 입력값이 O나 X의 형태가 아니면 여기서 오류남
        except Exception as inst:
            print(inst)
            print("Input is wrong. Please type again")


def create_map():
    """
    틱택토의 3*3 배열을 구현한 list를 전달하는 함수
    :return: list
    """
    matrix = [[0] * 3 for _ in range(3)]  # 2차원 배열
    return matrix


def tic_tac_toe_input():
    """
    player의 input을 받는 함수
    :return: int
    """
    global playground
    t_input = []
    while True:
        try:
            a = input()
            if len(a) is 1 and 0 < int(a) < 10 and a.isdecimal():
                if playground[(int(a) - 1) // 3][(int(a) - 1) % 3] is 0:
                    t_input.append(int(a))  # 조건 확인하고 넣기
            return t_input[0]  # 만약 조건에 안맞아서 넣지 못하면 여기서 오류남
        except Exception as inst:
            print(inst)
            print("Input is wrong. Please type again(1~9)")


def isvictory(player, computer):
    """
    한 줄 (가로, 세로, 대각선)에 있는 player가 놓은 돌의 수와 computer가 놓은 돌의 수를 바탕으로 게임의 승패를 알려주는 함수
    :param player: int
    :param computer: int
    :return: bool
    """
    if player is 3 or computer is 3:  # 한 줄에 3개 있다는 건 끝났다는 것
        if player is 3:
            print("Congratulation! Player win!")
        elif computer is 3:
            print("You Lose... Good Luck next time...")
        return True
    return False


def isdanger(player, computer):
    """
    한 줄 (가로, 세로, 대각선)에 있는 player가 놓은 돌의 수와 computer가 놓은 돌의 수를 바탕으로
    이번 턴에 computer가 지지 않기 위해 막아야하는지를 알려주는 함수
    :param player: int
    :param computer: int
    :return: bool
    """
    if player + computer is not 3 and player is 2:  # 만약 한줄에 3개중 2개가 차있고 하나가 비었다면 위험하다는 거지
        return True
    else:
        return False


def where_to_block(i, tic_type):
    """
    tic_type에 따라 가로, 세로, 대각선을 검사하여
    어떤 곳에 computer가 돌을 놓아야 player의 승리를 저지할 수 있는지 알려주는 함수
    :param i: int
    :param tic_type: str
    :return: list
    """
    global playground
    ans = []
    if tic_type is 'horizontal':  # 가로 검사하기
        for j in range(3):
            if playground[i][j] is 0:
                ans.append(i)
                ans.append(j)
                return ans
    elif tic_type is 'vertical':  # 세로 검사하기
        for j in range(3):
            if playground[j][i] is 0:
                ans.append(j)
                ans.append(i)
                return ans
    elif tic_type is "diagonal1":  # 대각선 검사하기 \ 이방향
        for i in range(3):
            if playground[i][i] is 0:
                ans.append(i)
                ans.append(i)
                return ans
    elif tic_type is "diagonal2":  # 대각선 검사하기 / 이방향
        for i in range(3):
            if playground[i][2 - i] is 0:
                ans.append(i)
                ans.append(2 - i)
                return ans


def tmp():
    """
    밑의 close_to_victory 함수의 default 값을 넣기 위한 쓰레기 함수
    :return: none
    """


def close_to_victory(letter, func, func2=tmp):
    """
    한 줄 (가로, 세로, 대각선)을 검사하여 주어진 function에 따라
    computer가 player의 승리를 막기 위해 놓아야 할 곳을 알려주거나
    game에 승패나 났는지 알려주는 함수
    :param letter: str
    :param func: function
    :param func2: function
    :return: list
    """
    ans = []
    global playground
    ground = playground
    unletter = 'O' if letter is 'X' else 'X'  # 모든 함수는 letter가 사용자의 입력임. unletter는 computer의 letter.
    L = 0  # 그 줄에 존재하는 player의 갯수
    computer_L = 0  # 그 줄에 존재하는 computer의 갯수
    for i in range(3):  # 가로 검사하기
        L = ground[i].count(letter)
        computer_L = ground[i].count(unletter)
        if func(L, computer_L):
            try:  # func2가 있는 건 isdanger()용 임
                return func2(i, 'horizontal')
            except:  # func2가 없는 건 isvictory()용 임
                ans.append(True)
                ans.append(True)
                return ans

        L = 0
        computer_L = 0

    for i in range(3):  # 세로 검사하기
        for j in range(3):
            if ground[j][i] is letter:
                L += 1
            if ground[j][i] is unletter:
                computer_L += 1
        if func(L, computer_L):
            try:  # func2가 있는 건 isdanger()용 임
                return func2(i, 'vertical')
            except:  # func2가 없는 건 isvictory()용 임
                ans.append(True)
                ans.append(True)
                return ans
        L = 0
        computer_L = 0

    for i in range(3):  # 대각선 검사하기 \ 이방향
        if ground[i][i] is letter:
            L += 1
        if ground[i][i] is unletter:
            computer_L += 1
    if func(L, computer_L):
        try:  # func2가 있는 건 isdanger()용 임
            return func2(i, 'diagonal1')
        except:  # func2가 없는 건 isvictory()용 임
            ans.append(True)
            ans.append(True)
            return ans
    L = 0
    computer_L = 0

    for i in range(3):  # 대각선 검사하기 / 이방향
        if ground[i][2 - i] is letter:
            L += 1
        if ground[i][2 - i] is unletter:
            computer_L += 1
    if func(L, computer_L):
        try:  # func2가 있는 건 isdanger()용 임
            return func2(i, 'diagonal2')
        except:  # func2가 없는 건 isvictory()용 임
            ans.append(True)
            ans.append(True)
            return ans

    ans.append(False)
    ans.append(False)
    return ans


def computer_tic(letter):
    """
    컴퓨터의 턴에 컴퓨터가 해야 할 최선의 수를 알려주는 함수
    :param letter: str
    :return: int, int
    """
    global playground
    unletter = 'O' if letter is 'X' else 'X'
    player = close_to_victory(letter, isdanger, where_to_block)  # 막아야 할 곳
    computer = close_to_victory(unletter, isdanger, where_to_block)  # 승리하기 위해 놓아야 할 곳
    if computer is not None and type(computer[0]) is not bool:  # 컴퓨터가 승리할 수 있으면 놓기
        return computer[0], computer[1]
    elif player is not None and type(player[0]) is not bool:  # 플레이어가 승리할 것 같으면 막기
        return player[0], player[1]
    else:  # 아니면 랜덤으로 고르기
        while True:
            x = random.randrange(0, 3)
            y = random.randrange(0, 3)
            if playground[x][y] is 0:  # 단 무언가 있으면 안됨
                return x, y


def print_tic_tac_toe():
    """
    틱택토 게임판을 print 해주는 함수
    :return: none
    """
    global playground
    for i in range(3):
        for j in range(3):
            if playground[i][j] is not 0:
                print(playground[i][j], end='')
            else:
                print(' ', end='')
            if j is not 2:
                print("|", end='')
        print("")
        print('-' * 5)
    print("")
    print("=" * 30)
    print("")


def player_turn(letter):
    """
    player의 턴임을 알려주고 입력을 받아 그 입력을 게임판에 표시하는 함수
    :param letter: str
    :return: none
    """
    global playground
    print("Your Turn! Please type number(1~9)")
    a = tic_tac_toe_input()
    playground[(a - 1) // 3][(a - 1) % 3] = letter
    print_tic_tac_toe()


def computer_turn(letter):
    """
    computer 의 차례임을 알려주고 computer 의 입력을 받아 그 입력을 게임판에 표시하는 함수
    :param letter: str
    :return: none
    """
    unletter = 'X' if letter is 'O' else 'O'
    global playground
    print("Computer's Turn:")
    x, y = computer_tic(letter)
    playground[x][y] = unletter
    print_tic_tac_toe()


def play_tic_tac_toe(letter, order_player):
    """
    틱택토 한판을 담당하는 함수
    :param letter: str
    :param order_player: str
    :return: none
    """
    win = False
    global playground
    global wintime
    i = 0
    if order_player is 'F':  # 만약 player 가 먼저하는 차례라면
        while i < 9:
            player_turn(letter)
            a = close_to_victory(letter, isvictory)  # 승리했는지 검사
            i += 1
            if a[0] or i is 9:  # 승리했거나 횟수가 끝났다면
                wintime += 1
                win = a[0]
                break
            computer_turn(letter)
            a = close_to_victory(letter, isvictory)  # 승리했는지 검사
            if a[0]:
                win = a[0]
                break
            i += 1

    else:  # 만약 computer 가 먼저하는 차례라면
        while i < 9:
            computer_turn(letter)
            a = close_to_victory(letter, isvictory)  # 승리했는지 검사
            i += 1
            if a[0] or i is 9:  # 승리했거나 횟수가 끝났다면
                win = a[0]
                break
            player_turn(letter)
            a = close_to_victory(letter, isvictory)  # 승리했는지 검사
            if a[0]:
                wintime += 1
                win = a[0]
                break
            i += 1
    if i is 9 and not win:
        print("DRAW!")


def ask_try_again():
    """
    player 가 게임을 다시 하고 싶은지 묻고 이를 bool 의 형태로 바꿔 전달하는 함수
    :return: bool
    """
    print('=' * 30)
    print("Will You Try Again? (y/n)")
    while True:
        try:
            r = input()
            yes_or_no_list = []
            yes_list = ['y', 'Y', 'yes', 'Yes', 'YES']
            no_list = ['n', 'N', 'no', 'No', 'NO', 'nope']
            if r in yes_list:
                yes_or_no_list.append(True)
            elif r in no_list:
                yes_or_no_list.append(False)
            val = yes_or_no_list[0]
            return val
        except Exception as inst:
            print("Error :", inst)
            print("Input is wrong. Please type again(y/n)")


def winning_rate():
    """
    player 의 승률을 print 해주는 함
    :return: none
    """
    global wintime
    global playtime
    print("\nWinning rate is %.2f %%\n" % (wintime / playtime * 100))


playground = []
while play:
    print(start_message)  # 시작 메세지 출력
    print('=' * 30)
    print('')
    playtime += 1
    playground = create_map()  # 맵 생성하고
    player_latter = input_letter()  # 문자 고르고
    order = player_order()  # 순서 랜덤으로 뽑힌 후
    print("Your letter is ", player_latter)
    play_tic_tac_toe(player_latter, order)  # 게임 시작
    winning_rate()  # 승률 표시
    play = ask_try_again()  # 다시 할 것인지 물어보기
print("Goodbye")
