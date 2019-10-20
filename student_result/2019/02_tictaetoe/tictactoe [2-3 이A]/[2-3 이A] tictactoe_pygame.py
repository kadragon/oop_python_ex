"""
이 코드는 tictactoe.py 를 기반으로 작성되었습니다.
"""

import random
import pygame
import time

user_OX = 0
the_board = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
user_win = 0
win_and_lose = 0
pygame.init()

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

WID = 400
LEN = 300
size = [WID, LEN]
screen = pygame.display.set_mode(size)

pygame.display.set_caption("Tic - Tac - Toe!")

font = pygame.font.Font('font_f_tictactoe.ttf', 32)

clock = pygame.time.Clock()


def print_now_board():
    global the_board

    pygame.draw.line(screen, BLACK, [WID / 3, LEN * 2 / 15], [WID / 3, LEN], 4)
    pygame.draw.line(screen, BLACK, [WID * 2 / 3, LEN * 2 / 15], [WID * 2 / 3, LEN], 4)
    pygame.draw.line(screen, BLACK, [0, LEN / 3], [WID, LEN / 3], 4)
    pygame.draw.line(screen, BLACK, [0, LEN * 2 / 3], [WID, LEN * 2 / 3], 4)

    for i in range(3):
        for j in range(3):
            position1 = WID / 3 * (j + 0.5)
            position2 = LEN / 3 * (i + 0.5)
            if the_board[i][j] == 1:
                textSurfaceObj = font.render('O', True, BLUE, WHITE)
                textRectObj = textSurfaceObj.get_rect()
                textRectObj.center = (position1, position2)
                screen.blit(textSurfaceObj, textRectObj)
            elif the_board[i][j] == -1:
                textSurfaceObj = font.render('X', True, RED, WHITE)
                textRectObj = textSurfaceObj.get_rect()
                textRectObj.center = (position1, position2)
                screen.blit(textSurfaceObj, textRectObj)
            else:
                textSurfaceObj = font.render(str(i * 3 + j), True, BLACK, WHITE)
                textRectObj = textSurfaceObj.get_rect()
                textRectObj.center = (position1, position2)
                screen.blit(textSurfaceObj, textRectObj)


def start_the_game():
    while True:

        clock.tick(10)

        for event in pygame.event.get():  # User did something
            if event.type == pygame.QUIT:  # If user clicked close.
                return 0
            if event.type == pygame.KEYUP:  # If user press any key.
                if event.key == ord('o'):
                    return 1
                elif event.key == ord('x'):
                    return -1

        screen.fill(WHITE)

        textSurfaceObj = font.render('start the game!', True, BLACK, WHITE)
        textRectObj = textSurfaceObj.get_rect()
        textRectObj.center = (WID / 2, LEN / 2)
        screen.blit(textSurfaceObj, textRectObj)

        textSurfaceObj = font.render("the first turn is 'O'", True, BLACK, WHITE)
        textRectObj = textSurfaceObj.get_rect()
        textRectObj.center = (WID / 2, LEN / 2 + 32)
        screen.blit(textSurfaceObj, textRectObj)

        textSurfaceObj = font.render("press O or X", True, BLACK, WHITE)
        textRectObj = textSurfaceObj.get_rect()
        textRectObj.center = (WID / 2, LEN / 2 + 32 * 2)
        screen.blit(textSurfaceObj, textRectObj)

        pygame.display.update()


def get_user_answer():
    global the_board
    while True:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return -1
            if event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                for i in range(3):
                    for j in range(3):
                        if (WID - 32) / 3 * j < pos[0] < (WID - 32) / 3 * (j + 1):
                            if LEN / 3 * i < pos[1] < LEN / 3 * (i + 1):
                                if the_board[i][j] == 0:
                                    return 3 * i + j

        screen.fill(WHITE)

        print_now_board()

        if user_OX == 1:
            textSurfaceObj = font.render('your turn: O', True, BLACK, WHITE)
            textRectObj = textSurfaceObj.get_rect()
            textRectObj.center = (WID / 2, 16)
            screen.blit(textSurfaceObj, textRectObj)
        else:
            textSurfaceObj = font.render('your turn: X', True, BLACK, WHITE)
            textRectObj = textSurfaceObj.get_rect()
            textRectObj.center = (WID / 2, 16)
            screen.blit(textSurfaceObj, textRectObj)

        pygame.display.update()


def check_anyone_can_win(OX):
    global the_board
    sum_diagonal1 = 0
    times_diagonal1 = 1
    sum_diagonal2 = 0
    times_diagonal2 = 1

    for i in range(3):
        sum_vertical = 0
        times_vertical = 1
        sum_parallel = 0
        times_parallel = 1

        sum_diagonal1 += the_board[i][i]
        times_diagonal1 *= the_board[i][i]
        sum_diagonal2 += the_board[i][2 - i]
        times_diagonal2 *= the_board[i][2 - i]

        for j in range(3):
            sum_vertical += the_board[j][i]
            times_vertical *= the_board[j][i]
            sum_parallel += the_board[i][j]
            times_parallel *= the_board[i][j]
        if sum_vertical == 2 * OX and times_vertical == 0:
            for j in range(3):
                if the_board[j][i] == 0:
                    return 3 * j + i
        if sum_parallel == 2 * OX and times_parallel == 0:
            for j in range(3):
                if the_board[i][j] == 0:
                    return 3 * i + j

    if sum_diagonal1 == 2 * OX and times_diagonal1 == 0:
        for i in range(3):
            if the_board[i][i] == 0:
                return i * 3 + i
    if sum_diagonal2 == 2 * OX and times_diagonal2 == 0:
        for i in range(3):
            if the_board[i][2 - i] == 0:
                return i * 3 + (2 - i)

    return -1


def get_com_answer():
    global the_board
    global user_OX

    com_OX = int(- user_OX)
    check_com_should_do = check_anyone_can_win(com_OX)

    if check_com_should_do != -1:
        return check_com_should_do

    check_com_must_do = check_anyone_can_win(user_OX)

    if check_com_must_do != -1:
        return check_com_must_do

    '''
    if the_board[1][1] == 0:
        return 1 * 3 + 1
    '''

    shuffled_list = list(range(9))
    random.shuffle(shuffled_list)

    for i in range(9):
        if the_board[shuffled_list[i] // 3][shuffled_list[i] % 3] == 0:
            return shuffled_list[i]


def check_anyone_win():
    global the_board

    sum_diagonal1 = 0
    sum_diagonal2 = 0

    for i in range(3):
        sum_parallel = 0
        sum_vertical = 0

        sum_diagonal1 += the_board[i][i]
        sum_diagonal2 += the_board[i][2 - i]

        for j in range(3):
            sum_parallel += the_board[i][j]
            sum_vertical += the_board[j][i]

        if sum_vertical == 3 or sum_vertical == -3:
            return sum_vertical // 3
        if sum_parallel == 3 or sum_parallel == -3:
            return sum_parallel // 3

    if sum_diagonal1 == 3 or sum_diagonal1 == -3:
        return sum_diagonal1 // 3
    if sum_diagonal2 == 3 or sum_diagonal2 == -3:
        return sum_diagonal2 // 3

    return 0


def do_now_turn(turn):
    global user_OX
    global the_board
    if user_OX == turn:
        user_answer = get_user_answer()
        if user_answer == -1:
            return -1
        the_board[user_answer // 3][user_answer % 3] = turn
        return user_answer
    else:
        com_answer = get_com_answer()
        the_board[com_answer // 3][com_answer % 3] = turn
        return com_answer


def check_more_game():
    while True:
        clock.tick(10)

        screen.fill(WHITE)

        for event in pygame.event.get():
            if event.type == pygame.KEYUP:
                if event.key == ord('y'):
                    return True
                if event.key == ord('n'):
                    return False
            if event.type == pygame.QUIT:
                return False

        textSurfaceObj = font.render("want more game?(y/n)", True, BLACK, WHITE)
        textRectObj = textSurfaceObj.get_rect()
        textRectObj.center = (WID / 2, LEN / 2)
        screen.blit(textSurfaceObj, textRectObj)

        textSurfaceObj = font.render("the winning rate:%05.1f %%" % (user_win / win_and_lose * 100), True, BLACK, WHITE)
        textRectObj = textSurfaceObj.get_rect()
        textRectObj.center = (WID / 2, LEN / 2 + 32)
        screen.blit(textSurfaceObj, textRectObj)

        pygame.display.update()


def Main():
    global user_OX
    global the_board
    global user_win
    global win_and_lose
    user_OX = 0
    the_board = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
    user_OX = start_the_game()

    if user_OX == 0:
        return False

    now_turn = 1

    for i in range(9):
        check_quit = do_now_turn(now_turn)
        time.sleep(0.01)

        if check_quit == -1:
            return False

        if now_turn == 1:
            now_turn = -1
        else:
            now_turn = 1

        check_win = check_anyone_win()
        if check_win != 0:
            break

    win_and_lose += 1
    if check_win == user_OX:
        user_win += 1

    while True:
        screen.fill(WHITE)

        clock.tick(10)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return False
            if event.type == pygame.MOUSEBUTTONDOWN:
                return check_more_game()

        if check_win == user_OX:
            textSurfaceObj = font.render("wow! you win!", True, BLACK, WHITE)
            textRectObj = textSurfaceObj.get_rect()
            textRectObj.center = (WID / 2, LEN / 2)
            screen.blit(textSurfaceObj, textRectObj)
        elif check_win == - user_OX:
            textSurfaceObj = font.render("computer win!", True, BLACK, WHITE)
            textRectObj = textSurfaceObj.get_rect()
            textRectObj.center = (WID / 2, 16)
            screen.blit(textSurfaceObj, textRectObj)
            print_now_board()
        else:
            print_now_board()
            textSurfaceObj = font.render("good game", True, BLACK, WHITE)
            textRectObj = textSurfaceObj.get_rect()
            textRectObj.center = (WID / 2, 16)
            screen.blit(textSurfaceObj, textRectObj)

        pygame.display.update()


while True:
    check = Main()
    if not check:
        break
