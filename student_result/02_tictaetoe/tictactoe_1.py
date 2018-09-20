import random

symbol = False  # True: O, False: X
board = []  # Board(-1: no symbol, else: symbol(T/F))
lane = [[0, 1, 2], [3, 4, 5], [6, 7, 8], [0, 3, 6], [1, 4, 7], [2, 5, 8], [0, 4, 8], [2, 4, 6]]  # lanes


# ask symbol of user. (parameter: X; return: X)
def choose_shape():
    global symbol
    sym = input("Select your symbol. (O/X) ").upper()
    if sym.startswith("O"):
        symbol = True
        return
    elif sym.startswith("X"):
        symbol = False
        return
    else:
        print("Please answer correctly.")
        choose_shape()


# preparing for game, and set order. (parameter: X; return: boolean)
def reset():
    global board
    board = [[-1, -1, -1], [-1, -1, -1], [-1, -1, -1]]
    return (random.random() > 0.5)


# print gameboard. (parameter: X; return: X)
def print_board():
    global board
    for i in range(3):
        print("-" * 13)
        for j in range(3):
            print("| ", end="")
            if board[i][j] == -1:
                print(" ", end=" ")
            elif board[i][j]:
                print("O", end=" ")
            else:
                print("X", end=" ")
        print("|")
    print("-" * 13)


# get place from user to mark symbol. (parameter: X; return: int)
def get_place():
    global board
    place = input("Choose place to mark. (0~8, in regular sequence) ")
    try:
        place = int(place)
        if 0 <= place and place <= 8 and board[place // 3][place % 3] == -1:
            return place
        else:
            print("Please answer correctly.")
            return get_place()
    except:
        print("Please answer correctly.")
        return get_place()


# mark symbol. (parameter: int, bool; return: X)
# explanation about second parameter:
# True: mark user's symbol.
# False: mark computer's symbol.
def set_board(a, is_user=True):
    global board
    global symbol
    if board[a // 3][a % 3] != -1:
        raise NotImplementedError
    board[a // 3][a % 3] = symbol if is_user else not symbol
    return


# computer marks its symbol. (parameter: X; return: X)
def computer_do():
    global board
    k = last(False)
    if k[0]:
        set_board(k[1], False)
        return
    k = last(True)
    if k[0]:
        set_board(k[1], False)
        return

    k = 0
    while board[k // 3][k % 3] != -1:
        k = random.randint(0, 8)
    set_board(k, False)
    return


# return list of board fret. (parameter: list, return: list)
# parameter: one element of lane list
# return: fret information of parameter(-1/symbol/not symbol)
def lines(p):
    global board
    q = []
    for i in p:
        r = i // 3
        c = i % 3
        q.append(board[r][c])
    return q


# determine to attack/defend. (parameter: bool; return: list(size: 2. bool, int))
# explanation about parameter:
# True: check whether player can win
# False: check whether computer can win
# explanation about return:
# [0]: shows whether it's time to attack or defend
# [1]: target place on board if [0] is True
def last(pang):
    global symbol
    global lane
    for i in lane:
        k = lines(i)
        if k.count(symbol if pang else not symbol) == 2:
            for j in range(3):
                if k[j] == -1:
                    return [True, i[j]]
    return [False, -1]


# check if game is clear and print result. (parameter: X; return: int)
# 0: tie, 1: victory, 2: defeated
def game_clear():
    global board
    global symbol
    global lane
    for i in lane:
        k = lines(i)
        cnt = k.count(-1)
        if cnt == 3:
            continue
        else:
            cnt = k.count(symbol)
            if cnt == 3:
                return 1
            cnt = k.count(not symbol)
            if cnt == 3:
                return 2
    return 0


# ask user of playing again. (parameter: X; return: boolean)
def ask_again():
    print("Do you want to play again? (Y/N)", end=" ")
    answer = input().upper()
    if answer.startswith("Y"):
        return True
    elif answer.startswith("N"):
        return False
    else:
        print("Please answer correctly.")
        return ask_again()


# main
play_again = True
choose_shape()
while play_again:  # gaming
    turn = reset()
    clear = 0  # for checking if the game is over
    for i in range(9):  # max turn: 9
        print("#%d: %s turn" % (i + 1, "your" if turn else "computer's"))
        if turn:  # user's turn
            print_board()
            set_board(get_place())
        else:  # AI's turn
            computer_do()
        turn = not turn  # switch turn
        clear = game_clear()
        if clear > 0:
            break
    if clear == 0:
        print("Tie.")
    elif clear == 1:
        print("Victory!")
    else:
        print("Defeated!")
    print("[result]")
    print_board()
    play_again = ask_again()
