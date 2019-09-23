# tic tac toe game
# 2018.09.04
# YoungKeun Jung

import random
import time


# board index
# 0 1 2
# 3 4 5
# 6 7 8


# Check 'char' wins the game. (Parameter: str, Return: int)
# if 'char' wins return 1, else return 0
def chk_win(char):
    # Winning cases
    chk = [[0, 1, 2], [3, 4, 5], [6, 7, 8], [0, 3, 6], [1, 4, 7], [2, 5, 8], [0, 4, 8], [2, 4, 6]]

    for k in range(8):  # Check all cases
        flag = 1
        for i in chk[k]:
            if data[i] != char:  # Change the flag to 0 if there is another 'char' in the data[i]
                flag = 0
                break
        if flag == 1:  # flag -> 1 : 'char' wins
            return 1

    return 0  # flag -> no one wins


# Check if board if full. (Return: int)
# if full return 1, else return 0
def is_full():
    flag = 1
    for i in range(9):  # Check 9 spaces
        if data[i] == ' ':  # flag->0 : there is blank space
            flag = 0
    return flag


# Print board. (Parameter : list, list)
def print_board(m, d):
    for i in range(0, 7):
        for j in range(0, 7):
            if j % 2 == 0 or i % 2 == 0:  # print frame of board
                print(m[i][j], end=' ')
            else:  # print data of board
                print(d[3 * int((i - 1) / 2) + int((j + 1) / 2) - 1], end=' ')
        print()


# get new user input (1~9) (Return: input(str))
def new():
    user_in = input('''Choose where to put it ( 1 ~ 9 ): ''')
    # Check if user input is valid (1~9)
    while (not user_in.isnumeric()) or (user_in == '0') or (int(user_in) >= 10):
        user_in = input('''Invalid Input
Choose where to put it ( 1 ~ 9 ): ''')
    return user_in


# user turn method
def turn_user():
    print("\nYour Turn!")
    loc = int(new()) - 1
    # Check if user input location is Occupied
    while data[loc] != ' ':
        print("Location Occupied... Pick another Number")
        loc = int(new()) - 1
    # Update data
    data[loc] = user


# Computer's turn method
def turn_com():
    print("\nComputer's Turn!")
    time.sleep(1.5)

    # Computer winning situation
    for i in range(9):
        if data[i] == ' ':
            data[i] = computer  # computer places 'computer symbol' in data[i]
            if chk_win(computer) == 1:  # check if computer wins
                return  # if wins computer places...
            else:
                data[i] = ' '  # else replace 'computer symbol' with ' '(blank)

    # User winning situation -> Defend
    for i in range(9):
        if data[i] == ' ':
            data[i] = user  # user places 'user symbol' in data[i]
            if chk_win(user) == 1:  # check if user wins
                data[i] = computer  # if wins computer places instead of user
                return
            else:
                data[i] = ' '  # else replace 'user symbol' with ' '(blank)

    # Else situation
    buf = [0, 2, 6, 8]  # First Priority location
    random.shuffle(buf)  # Shuffle
    for i in buf:
        if data[i] == ' ':  # Check if location is empty
            data[i] = computer  # if it's empty -> place
            return

    if data[4] == ' ':  # Second Priority location
        data[4] = computer  # if empty -> place
        return

    buf = [1, 3, 5, 7]  # Third Priority location
    random.shuffle(buf)  # Shuffle
    for i in buf:
        if data[i] == ' ':
            data[i] = computer  # if it's empty -> place
            return


game = 'R'  # game==1 -> game in process
while game == 'R':

    # Pre Define Data
    # board's edge
    board = [['-', '-', '-', '-', '-', '-', '-'], ['|', ' ', '|', ' ', '|', ' ', '|'],
             ['-', '-', '-', '-', '-', '-', '-'],
             ['|', ' ', '|', ' ', '|', ' ', '|'], ['-', '-', '-', '-', '-', '-', '-'],
             ['|', ' ', '|', ' ', '|', ' ', '|'],
             ['-', '-', '-', '-', '-', '-', '-']]
    # board data
    data = [' '] * 9

    # Welcome / Game Rule Explain
    print("\nWelcome Tic Tac Toe!")
    print("Enter the number on each board to play the game.")
    print_board(board, list(range(1, 10)))
    print()

    # user input -> X or O
    user = input('''Do you want to be X or O ? : ''')
    user = user.upper()
    # User input Error management
    while not (user == 'O' or user == 'X'):
        user = input('''Invalid input. Please try again
Do you want to be X or O ? : ''')
        user = user.upper()

    # assign symbols to user and computer
    if user == 'X':
        computer = 'O'
    else:
        computer = 'X'

    # Randomize order
    print("\nRandomizing order...")
    time.sleep(1)

    seq = [-1, 1]  # ctrl who's turn
    random.shuffle(seq)

    if seq[0] == -1:  # user turn first
        print("You do it first!")
    else:  # computer's turn first
        print("Computer does it first")

    win = 0  # check var if someone win
    # Proceed game until board if full
    while is_full() != 1:
        if seq[0] == -1:  # if user's turn
            turn_user()  # user turn method
            if chk_win(user) == 1:  # if user wins
                print_board(board, data)  # print final board
                print("\nUser wins!")  # print winning message
                win = 1  # win chk var
                break
        else:  # if computer's turn
            turn_com()  # computer's turn method
            if chk_win(computer) == 1:  # if computer wins
                print_board(board, data)  # print final board
                print("\nComputer wins!")  # print computer winning message
                win = 1  # win chk var
                break
        seq[0] = seq[0] * -1  # turn change
        print_board(board, data)  # print board

    if win == 0:  # check if draw
        print("\nDraw")

    game = input("\nInput R to restart, others to Exit...").upper()  # check if restart
