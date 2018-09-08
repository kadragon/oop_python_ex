"""
Title       Reversi
Reference   나만의 Python Game 만들기 Chapter 15 p.316
Author      kadragon
Date        2018.09.07
"""

import sys
from copy import deepcopy
from random import randint, shuffle

H_LINE = '   +---+---+---+---+---+---+---+---+'


def draw_board(board):
    print('     1   2   3   4   5   6   7   8')
    print(H_LINE)
    for y in range(8):
        print(" %d " % (y + 1), end='')
        for x in range(8):
            print('| %s ' % board[x][y], end='')
        print('|')
        print(H_LINE)


def reset_board(board):
    for x in range(8):
        for y in range(8):
            board[x][y] = ' '

    board[3][3] = 'X'
    board[3][4] = 'O'
    board[4][3] = 'O'
    board[4][4] = 'X'


def get_new_board():
    board = []
    for i in range(8):
        board.append([' '] * 8)

    return board


def is_on_board(x, y):
    return 0 <= x <= 7 and 0 <= y <= 7


def is_valid_move(board, tile, xstart, ystart):
    if board[xstart][ystart] != ' ' or not is_on_board(xstart, ystart):
        return False

    board[xstart][ystart] = tile

    other_tile = 'O' if tile == 'X' else 'X'

    tiles_to_flip = []
    for xdirction in [-1, 0, 1]:
        for ydirction in [-1, 0, 1]:
            x, y = xstart, ystart
            x += xdirction
            y += ydirction

            if is_on_board(x, y) and board[x][y] == other_tile:
                x += xdirction
                y += ydirction
                if not is_on_board(x, y):
                    continue
                while board[x][y] == other_tile:
                    x += xdirction
                    y += ydirction
                    if not is_on_board(x, y):
                        break

                if not is_on_board(x, y):
                    continue

                if board[x][y] == tile:
                    while True:
                        x -= xdirction
                        y -= ydirction
                        if x == xstart and y == ystart:
                            break
                        tiles_to_flip.append([x, y])

    board[xstart][ystart] = ' '
    if len(tiles_to_flip) == 0:
        return False

    return tiles_to_flip


def get_valid_moves(board, tile):
    valid_moves = []
    for x in range(8):
        for y in range(8):
            if is_valid_move(board, tile, x, y):
                valid_moves.append([x, y])

    return valid_moves


def get_board_with_valid_moves(board, tile):
    dup_board = deepcopy(board)

    for x, y in get_valid_moves(dup_board, tile):
        dup_board[x][y] = '.'

    return dup_board


def get_score_of_board(board):
    x_score = 0
    o_score = 0

    for x in range(8):
        for y in range(8):
            if board[x][y] == 'X':
                x_score += 1
            if board[x][y] == 'O':
                o_score += 1

    return {'X': x_score, 'O': o_score}


def enter_player_tile():
    tile = ' '
    while not (tile == 'X' or tile == 'O'):
        tile = input('Do you want to be X or O?').upper()

    return ['X', 'O'] if tile == 'X' else ['O', 'X']


def who_goes_first():
    return 'computer' if randint(0, 1) == 0 else 'computer'


def play_again():
    return input('Do you want to play again? (yes or no)').lower().startswith('y')


def make_move(board, tile, xstart, ystart):
    tile_to_flip = is_valid_move(board, tile, xstart, ystart)

    if not tile_to_flip:
        return False

    board[xstart][ystart] = tile
    for x, y in tile_to_flip:
        board[x][y] = tile

    return True


def is_on_corner(x, y):
    return x, y in [[0, 0], [7, 0], [0, 7], [7, 7]]


def get_player_move(board, player_tile):
    digit_1_to_8 = "1 2 3 4 5 6 7 8".split()

    while True:
        move = input('Enter tour move, or type quit to end the game, or hints, to turn off/on hints.').lower()
        if move == 'quit':
            return 'quit'
        if move == 'hints':
            return 'hints'

        if len(move) == 2 and move[0] in digit_1_to_8 and move[1] in digit_1_to_8:
            x = int(move[0]) - 1
            y = int(move[1]) - 1

            if not is_valid_move(board, player_tile, x, y):
                continue
            else:
                break
        else:
            print('That is not a valid move. Type the x digit (1-8), then the y digit (1-8).')
            print('For example, 81 will be the top-right corner.')

    return [x, y]


def get_computer_move(board, computer_tile):
    possible_move = get_valid_moves(board, computer_tile)

    shuffle(possible_move)

    for x, y in possible_move:
        if is_on_corner(x, y):
            return [x, y]

    best_score = -1
    for x, y in possible_move:
        dup_board = deepcopy(board)
        make_move(dup_board, computer_tile, x, y)
        score = get_score_of_board(dup_board)[computer_tile]
        if score > best_score:
            best_move = [x, y]
            best_score = score

    return best_move


def show_points(player_tile, computer_tile, main_board):
    scores = get_score_of_board(main_board)
    print('You have %s points. The computer has %s points.' % (scores[player_tile], scores[computer_tile]))


print('Welcome to Reversi!')

while True:
    main_board = get_new_board()
    reset_board(main_board)
    player_tile, computer_tile = enter_player_tile()
    show_hints = False
    turn = who_goes_first()
    print('The %s will go first' % turn)

    while True:
        if turn == 'player':
            if show_hints:
                valid_moves_board = get_board_with_valid_moves(main_board, player_tile)
                draw_board(valid_moves_board)
            else:
                draw_board(main_board)

            show_points(player_tile, computer_tile, main_board)

            move = get_player_move(main_board, player_tile)

            if move == 'quit':
                print('Thanks for playing!')
                sys.exit()
            elif move == 'hints':
                show_hints = not show_hints
                continue
            else:
                print(move)
                make_move(main_board, player_tile, move[0], move[1])

            if get_valid_moves(main_board, computer_tile) == []:
                break
            else:
                turn = 'computer'

        else:
            draw_board(main_board)
            show_points(player_tile, computer_tile, main_board)
            input('Press Enter to see the computer\'s move.')
            x, y = get_computer_move(main_board, computer_tile)
            make_move(main_board, computer_tile, x, y)

            if get_valid_moves(main_board, player_tile) == []:
                break
            else:
                turn = 'player'

    draw_board(main_board)
    scores = get_score_of_board(main_board)
    print('X scored %s points. O scored %s points.' % (scores['X'], scores['O']))

    if scores[player_tile] > scores[computer_tile]:
        print('You beat the computer by %s points! Congratulations!' % (scores[player_tile] - scores[computer_tile]))
    elif scores[player_tile] < scores[computer_tile]:
        print('You lost. The computer beat you by %s points!' % (scores[computer_tile] - scores[player_tile]))
    else:
        print('The game was a tie!')

    if not play_again():
        break
