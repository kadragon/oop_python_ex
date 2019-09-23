import random

TEXT_LINE = 13


def display_intro():  # intro 함수 python 에서는 함수를 def 을 이용하여 정의한다. 반환형을 명시하지 않는다.
    print('=' * 80)
    print("""
    This is Tic Tac Toe!
    Choose O or X
    """)
    print('=' * 80)


def show_now():
    print('-' * TEXT_LINE)
    for i in range(0, 3):
        print('|', end='')
        for j in range(0, 3):
            print(' ' + board[i][j] + ' ', end='|')
        print('')
        print('-' * TEXT_LINE)


def check_num(a, b):
    switch = 0
    if 3 >= a >= 1 and 3 >= b >= 1:
        return True
    else:
        return False


def insert(team, a, b):
    board[a - 1][b - 1] = team


def win_point():
    for i in range(0, 3):
        if board[i][0] == board[i][1] == board[i][2] == team:
            print("You win congratulation")
            return True
        if board[i][0] == board[i][1] == board[i][2] == enemy:
            print("You lose try again")
            return True
    for i in range(0, 3):
        if board[0][i] == board[1][i] == board[2][i] == team:
            print("You win congratulation")
            return True
        if board[0][i] == board[1][i] == board[2][i] == enemy:
            print("You lose try again")
            return True
    if board[0][0] == board[1][1] == board[2][2] == team:
        print("You win congratulation")
        return True
    if board[0][0] == board[1][1] == board[2][2] == enemy:
        print("You lose try again")
        return True
    if board[0][2] == board[1][1] == board[2][0] == team:
        print("You win congratulation")
        return True
    if board[0][2] == board[1][1] == board[2][0] == enemy:
        print("You lose try again")
        return True
    return False


def enemy_turn(enemy):
    k = list(range(3))
    l = list(range(3))
    while True:
        random.shuffle(k)
        random.shuffle(l)
        if board[k[0]][l[0]] == ' ':  # 백의 자리에 0이 있으면 다시
            break
    board[k[0]][l[0]] = enemy


board = [['', '', ''], ['', '', ''], ['', '', '']]
play_again = 'yes'  # 플레이를 지속할지를 입력 받아 임시 저장하는 공간
while play_again == 'yes' or play_again == 'y':
    board = [[' ', ' ', ' '], [' ', ' ', ' '], [' ', ' ', ' ']]
    display_intro()
    team = input()
    while True:
        if team == 'O' or team == 'X':
            break
        else:
            print('choose Again (O or X)')
            team = input()
    if team == 'O':
        enemy = 'X'
    else:
        enemy = 'O'
    show_now()
    print("""
        You choose %s team. You goes first!
        Check where you want to draw        ex) first row, first column -> 1 1
        """ % team)
    life = 1  # 게임의 종료여부를 확인하는 임시변수
    while life == 1:
        a, b = map(int, input().split())
        if check_num(a, b) is False:
            continue
        insert(team, a, b)
        enemy_turn(enemy)
        show_now()
        if win_point():
            life = 0
    play_again = input('Do you want to play again? (yes or no): ')
