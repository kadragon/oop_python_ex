"""
Title       Reversi
Reference   나만의 Python Game 만들기 Chapter 15 p.316
Author      kadragon
Date        2018.09.07
"""

import sys
from copy import deepcopy
from random import randint, shuffle


def draw_board(board):
    """
    사용중인 board 를 입력 받아, 현재의 보드 상태를 Console 에 출력하여 알려준다.
    :param board: 사용중인 board 2차원 보드 [0~7][0~7]
    """
    H_LINE = '   +---+---+---+---+---+---+---+---+'

    print('     1   2   3   4   5   6   7   8')
    print(H_LINE)
    for y in range(8):
        print(" %d " % (y + 1), end='')
        for x in range(8):
            print('| %s ' % board[x][y], end='')
        print('|')
        print(H_LINE)


def reset_board(board):
    """
    새로운 게임을 위해서 board 를 초기화 한다.
    Reversi 의 경우 시작점이 정해져 있고, 모든 list 의 값을 ' ' 으로 초기화 한다.
    :param board: 초기화 할 board[8][8]
    :return:
    """
    for x in range(8):
        for y in range(8):
            board[x][y] = ' '

    board[3][3] = 'X'
    board[3][4] = 'O'
    board[4][3] = 'O'
    board[4][4] = 'X'


def get_new_board():
    """
    게임의 상태를 저장할 board list type 객체를 생성한다.
    크기는 8 * 8
    :return: ' ' 로 초기화 되어 있는 8 * 8 크기의 list type 객체
    """
    board = []
    for i in range(8):
        board.append([' '] * 8)

    return board


def is_on_board(x, y):
    """
    x, y 값이 모두 0~7 사이에 있어 board 위에 있는 위치인지 판단한다.
    :param x: 가로 좌표
    :param y: 세로 좌표
    :return: True or False
    """
    return 0 <= x <= 7 and 0 <= y <= 7


def is_valid_move(board, tile, xstart, ystart):
    """
    Reversi Role 에 따라 각가의 턴에서 둘 수 있는 곳이 제한되어 있다.
    입력 받은 x, y 값을 기준으로 둘 수 있는 곳인지 판단한다.
    :param board: 판단하고자 하는 보드
    :param tile: 'O' or 'X'
    :param xstart: 두고 싶은 X 좌표
    :param ystart: 두고 싶은 Y 좌표
    :return: 둘수 없다면 False, 둘 수 있다면, 그 곳에 두었을때 뒤집어야 하는 리스트를 반환한다.
    """
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
    """
    둘 수 있는 곳의 좌표를 찾는다.
    :param board: 판단하고자 하는 보드
    :param tile: 'O' or 'X'
    :return: 둘 수 있는 곳의 [x, y] 로 이루어진 목록
    """
    valid_moves = []
    for x in range(8):
        for y in range(8):
            if is_valid_move(board, tile, x, y):
                valid_moves.append([x, y])

    return valid_moves


def get_board_with_valid_moves(board, tile):
    """
    보드 한개과 타일을 받아서, 그 타일이 둘 수 있는 곳을 '.' 으로 표기 하여 반환한다.
    Hints 를 켰을때, 출력하기 위함
    :param board: 판단하고 싶은 board
    :param tile: 'O' or 'X'
    :return: 둘 수 있는 곳을 '.' 으로 표기한 board 를 반환
    """
    dup_board = deepcopy(board)

    for x, y in get_valid_moves(dup_board, tile):
        dup_board[x][y] = '.'

    return dup_board


def get_score_of_board(board):
    """
    보드를 확인하여, 'X', 'O' 의 점수를 계산한다.
    :param board: 판단하고 싶은 보드
    :return: 'X', 'Y' 로 이루어진 dictionary type
    """
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
    """
    플레이어가 사용하고 싶은 tile 를 선택하여, 컴퓨터 것과 사용자 것을 반환한다.
    :return: ['플레이어 Pick', '컴퓨터 tile']
    """
    tile = ' '
    while not (tile == 'X' or tile == 'O'):
        tile = input('Do you want to be X or O?').upper()

    return ['X', 'O'] if tile == 'X' else ['O', 'X']


def who_goes_first():
    """
    누가 먼저 둘지 randint 를 활용하여 판단한다.
    :return: computer or player
    """
    return 'computer' if randint(0, 1) == 0 else 'player'


def play_again():
    """
    다시 플레이 할지 입력 받는다.
    :return: True or False
    """
    return input('Do you want to play again? (yes or no)').lower().startswith('y')


def make_move(board, tile, xstart, ystart):
    """
    현재 보드와 tile, x, y 좌표를 받아 is_valid_move 를 활용 둘수 있는 곳인지 판단한 후
    둘 수 있는 곳이라면 tile_to_flip 값을 활용하여 tile 을 뒤집는다.
    :param board: 뒤집고자 하는 board
    :param tile: 'O' or 'X'
    :param xstart: 두고자 하는 'X' 좌표
    :param ystart: 두고자 하는 'Y' 좌표
    :return: x, y 에 두어서 무언가 일어났다면 True, 아무일도 일어나지 않았다면 False 를 반환
    """
    tile_to_flip = is_valid_move(board, tile, xstart, ystart)

    if not tile_to_flip:
        return False

    board[xstart][ystart] = tile
    for x, y in tile_to_flip:
        board[x][y] = tile

    return True


def is_on_corner(x, y):
    """
    Reversi 에서 corner 에 나의 tile 이 있을 경우 승률이 매우 높다.
    따라서, 컴퓨터가 둘때 corner 에 둘 수 있다면 우선순위를 높게 주기 위한 메소드
    :param x: 두고 싶은 x 좌표
    :param y: 두고 싶은 y 좌표
    :return: corner 라면 True, 아니라면 False
    """
    return x, y in [[0, 0], [7, 0], [0, 7], [7, 7]]


def get_player_move(board, player_tile):
    """
    플레이어 턴에 사용자로부터 값을 입력 받아 처리하는 메소드
    'quit' 가 입력 될 경우 게임을 종료
    'hints' 가 입력 될 경우 hint 을 보여주는 board 로 변환
    'xy' 가 입력 될 경우
        1) 제대로 2글자가 입력되었는지?
        2) 1~8까지의 문자인지
        3) 둘수 있는 곳에 두었는지
    를 확인한다.
    :param board: 판단하고자 하는 보드
    :param player_tile: 플레이어가 사용하고 있는 tile
    :return: quit or hints, or [x, y]
    """
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
    """
    컴퓨터 턴일때 가장 점수를 많이 얻을 수 있는 곳을 전체 탐색하여 선택한다.
    1) 둘수 있는 곳을 get_valid_moves 를 활용하여 찾고
    2) deepcopy 를 활용, 복사한 보드를 활용하여
    3) 그 곳에 두었을때의 점수를 get_score_of_board 를 활용하여 찾는다.
    4) 가장 높은 점수를 얻을 수 있는 곳을 [x, y] 형태의 리스트로 반환한다.
    :param board: 판단하고 싶은 보드
    :param computer_tile: 컴퓨터의 tile
    :return: 가장 높은 점수를 얻을 수 있는 [x, y]
    """
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
    """
    점수를 출력해주는 함수
    :param player_tile:
    :param computer_tile:
    :param main_board:
    """
    scores = get_score_of_board(main_board)
    print('You have %s points. The computer has %s points.' % (scores[player_tile], scores[computer_tile]))


print('Welcome to Reversi!')

while True:
    main_board = get_new_board()  # 게임이 시작하면 새로운 보드를 만든다.
    reset_board(main_board)  # 만들어진 보드를 초기화 한다.
    player_tile, computer_tile = enter_player_tile()  # tile 설정

    show_hints = False  # hints 의 초기 값은 False 로

    turn = who_goes_first()  # 누가 먼저 둘지..!
    print('The %s will go first' % turn)  # 안내하고 시작!

    while True:
        # player 의 turn 일때!
        if turn == 'player':
            if show_hints:
                valid_moves_board = get_board_with_valid_moves(main_board, player_tile)
                draw_board(valid_moves_board)
            else:
                draw_board(main_board)

            # 현재의 점수 상태를 보여준다.
            show_points(player_tile, computer_tile, main_board)

            # 사용자로 부터 입력받는다.
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

            # 둘 수 있는 곳이 없으면 게임을 종료한다.
            # 두었다면, computer 턴!
            if not get_valid_moves(main_board, computer_tile):
                break
            else:
                turn = 'computer'
        # 컴퓨터 차례일때!
        else:
            draw_board(main_board)
            show_points(player_tile, computer_tile, main_board)

            # 컴퓨터가 바로 두는 것이 아니라, Enter 를 눌러야 두도록 변경한다.
            input('Press Enter to see the computer\'s move.')

            x, y = get_computer_move(main_board, computer_tile)
            make_move(main_board, computer_tile, x, y)

            # 둘 수 있는 곳이 없으면 게임을 종료한다.
            # 두었다면, player 턴!
            if not get_valid_moves(main_board, player_tile):
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
