import random
import time


def best_choose():
    for row1 in range(0, 8):  # 컴퓨터가 이길 수 있는 자리를 찾는다. 대신, 빈자리를 찾는다.
        if ttt[b_e[row1][0]] == ttt[b_e[row1][1]] == com_char and ttt[b_e[row1][2]] == "n":
            return b_e[row1][2]
        elif ttt[b_e[row1][0]] == ttt[b_e[row1][2]] == com_char and ttt[b_e[row1][1]] == "n":
            return b_e[row1][1]
        elif ttt[b_e[row1][1]] == ttt[b_e[row1][2]] == com_char and ttt[b_e[row1][0]] == "n":
            return b_e[row1][0]

    for row2 in range(0, 8):  # 사용자의 승리를 방어하기 위한 자리를 잦는다. 대신, 빈자리를 찾는다.
        if ttt[b_e[row2][0]] == ttt[b_e[row2][1]] == user_char and ttt[b_e[row2][2]] == "n":
            return b_e[row2][2]
        elif ttt[b_e[row2][0]] == ttt[b_e[row2][2]] == user_char and ttt[b_e[row2][1]] == "n":
            return b_e[row2][1]
        elif ttt[b_e[row2][1]] == ttt[b_e[row2][2]] == user_char and ttt[b_e[row2][0]] == "n":
            return b_e[row2][0]

    for cor1 in range(0, 4):  # 승리 확률이 가장 높은 코너의 빈자리를 찾는다.
        if ttt[corner[cor1]] == "n":
            return corner[cor1]

    for cor2 in range(0, 4):  # 승리 확률이 그 다음으로 높은 변의 빈자리를 찾는다.
        if ttt[side[cor2]] == "n":
            return side[cor2]

    if ttt[4] == "n":  # 마지막 남은 자리를 반환한다.
        return 4


def print_ttt():  # tictactoe판 을 출력한다.
    for i in range(0, 9):
        if i % 3 == 0:
            if ttt[i] == 'n':
                print("\n   ", end="")
            else:
                print("\n%c  " % ttt[i], end="")
        else:
            if ttt[i] == 'n':
                print("||     ", end="")
            else:
                print("||  %c  " % ttt[i], end="")
    print()


def bingo():  # com이나 사용자가 게임을 승리했는지에 대한 여부를 판단한다.
    for bin1 in range(0, 8):
        if ttt[b_e[bin1][0]] == ttt[b_e[bin1][1]] == ttt[b_e[bin1][2]] == com_char:
            print("com win!")
            return True
    for bin2 in range(0, 8):
        if ttt[b_e[bin2][0]] == ttt[b_e[bin2][1]] == ttt[b_e[bin2][2]] == user_char:
            print("user win!")
            return True
    return False


def check_ttt():  # 게임이 끝났는지에 대한 여부를 판단한다.
    if bingo():
        return True

    if 'n' in ttt:
        return False
    else:  # 더 이상 아무것도 채우지 못할 때 Draw를 출력한다.
        print("Draw!")
        return True


def judge_play(user_input):
    if user_input.isdigit() == False:  # 입력받은 숫자가 정수인지 판단한다.
        print('You have to choose only 1~10')
        return False
    elif int(user_input) < 1 or int(user_input) > 10:  # 입력받은 숫자가 1부터 9사이인지 판단한다.
        print('You have to choose only 1~10')
        return False
    else:
        return True


def judge_in(user_inp):  # 빈자리에만 O와 X를 채울 수 있도록 한다.
    if ttt[int(user_inp) - 1] == 'O' or ttt[int(user_inp) - 1] == 'X':
        print("You have to choose only blank place")
        return False
    else:
        return True


b_e = [[0, 1, 2], [3, 4, 5], [6, 7, 8], [0, 3, 6], [1, 4, 7], [2, 5, 8], [0, 4, 8],
       [2, 4, 6]]  # tictactie의 승리 조건을 리스트로 구현한다.
corner = [0, 2, 6, 8]  # 모서리를 표현하는 리스트
side = [1, 3, 5, 7]  # 변을 표현하는 리스트

while True:
    ttt = ['n', 'n', 'n', 'n', 'n', 'n', 'n', 'n', 'n']  # tictactie 테이블을 리스트로 구현한다.
    random.shuffle(corner)  # 승리 조건이나 방어 조건이외에 승리 확률이 높은 자리에 두는 경우에서 무작위적으로 선택하기 위해 섞는다.
    random.shuffle(side)  # 승리 확률이 다음으로 높은 변에서 무작위로 선택하기 위해 섞는다.

    user_char = input('Choose O or X: ').upper()  # 소문자도 받을 수 있도록 한다.
    while user_char != 'O' and user_char != 'X':
        user_char = input('Choose O or X (only O or X): ').upper()

    if user_char == 'O':
        com_char = 'X'
    else:
        com_char = 'O'

    if random.choice([True, False]):  # 무작위적으로 순서를 결정해준다.
        print("user first")
        print_ttt()
    else:
        print("com first")
        ttt[corner[0]] = com_char
        print_ttt()

    while check_ttt() == False:  # 게임이 끝나기 전까지 반복적으로 수행한다.
        print("what is your next move? (1 ~ 9): ")
        user_choose = input()
        while judge_play(user_choose) == False or judge_in(user_choose) == False:  # 입력값이 타당한지 확인한다.
            user_choose = input()
        user_choose = int(user_choose) - 1  # 정수형으로 바꿔준 후 1을 뺸다. -리스트의 첫번쨰는 0부터 시작이지만, 게임에서는 1부터 시작이기 떄문이다.
        ttt[user_choose] = user_char  # 고른 부분에 사용자의 문자를 채운다.

        if check_ttt():  # 사용자의 순서가 끝난 후 게임이 끝났는지 확인한다.
            break

        print_ttt()
        print("\ncom's turn")
        time.sleep(1)  # 게임의 흥미를 위해 컴퓨터도 생각하는 척...
        ttt[best_choose()] = com_char  # 선택할 수 있는 자리 중 최상의 자리를 선택한다.
        print_ttt()

    print(""" 
∩∧_∧∩ 
(　･ω･) 
 /　　ﾉ 
 しーU""")
    if input('\nDo you want to play again? (yes or no): ').lower().startswith(
            'y') == False:  # 사용자로 부터 값을 입력 > 소문자로 변환 > 만약 'y' 로 시작하는 문자열이라면 True, 아니면 False
        break
