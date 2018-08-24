"""
Title       틱 택 토
Reference   나만의 Python Game 만들기 Chapter 10 p.191
Author      kadragon
Date        2018.08.24
"""

# Shallow and deep copy operations
import copy
import random


def draw_board(board):
    """
    틱택토의 현재 상태를 terminal 에 그리는 함수
    ex)
     -----------
        | X | O
     -----------
        |   |
     -----------
        |   |
     -----------
    :param board: 틱택토 상태가 저장되어 있는 맵 List
    """
    print()
    print('-' * 11)
    print(' %s | %s | %s ' % (board[1], board[2], board[3]))
    print('-' * 11)
    print(' %s | %s | %s ' % (board[4], board[5], board[6]))
    print('-' * 11)
    print(' %s | %s | %s ' % (board[7], board[8], board[9]))
    print('-' * 11)
    print()


def input_player_letter():
    """
    사용자가 원하는 표시를 선택하면, 사용자와 컴퓨터의 표식을 지정하여 List 형태로 반환함.
    :return: [ '사용자가 선택한 표시', '컴퓨터의 표시' ]
    """
    letter = ' '
    while not (letter == 'X' or letter == 'O'):
        letter = input('Do you want to be X or O? : ').upper()  # upper() 는 모든 문자를 대문자로 변경해준다.
        # https://docs.python.org/ko/3/library/stdtypes.html?highlight=upper#str.upper

    return ['X', 'O'] if letter == 'X' else ['O', 'X']  # 함수의 반환은 1개의 객체만 할 수 있다. / 이 함수에서는 List 객체 1개를 반환함.


def play_again():
    """
    다시 한 번 플레이 여부를 확인하는 함수
    :return: True or False
    """
    return input('Do you want to play again? (yes or no): ').lower().startswith('y')


def make_move(board, letter, move_target):
    """
    지금 사용하고 있는 (게임판 or 테스트판) 판에 말을 놓기
    :param board: 말을 놓을 판(게임판 or 테스트판)
    :param letter: 'X' or 'O'
    :param move_target: 말을 놓을 판의 상대 위치 (1~9)
    """
    board[move_target] = letter


def is_winner(board, letter):
    """
    테스트 할 판을 입력과 말을 입력 받아서, 지금 상태가 승리 조건인지를 확인하여 반환하는 함수
     -----------
      1 | 2 | 3
     -----------
      4 | 5 | 6
     -----------
      7 | 8 | 9
     -----------
    :param board: 테스트 할 판을 입력 받음
    :param letter: 'X' or 'O'
    :return: 승리: True, 패배: False
    """
    win_list = [[1, 2, 3], [4, 5, 6], [7, 8, 9], [1, 4, 7], [2, 5, 8], [3, 6, 9], [1, 5, 9], [3, 5, 7]]
    # 'index 0, 1, 2 는 가로일때 승리 / 3, 4, 5 는 세로일때 승리 / 6, 7 는 대각일때 승리 조건' 을 저장한 이차원 list
    for k in win_list:                  # win_list 에서 값을 한개씩 꺼내와서 k 에 저장
        temp_count = 0                  # 일치 갯수를 저장할 변수 선언
        for j in k:                     # 꺼내온 1차원 list 에서 값을 한개씩 꺼내와서 j 에 저장
            if board[j] == letter:      # 일치 여부 확인
                temp_count += 1         # 일치 한다면 count 증가
                if temp_count == 3:     # count 가 3 이라면 승리한 것이기 때문에 True 를 반환
                    return True
            else:
                continue


def get_board_copy(board):
    """
    컴퓨터가 둘 곳을 결정하기 위해서, 본 판이 아닌 임시의 판을 복제하는 함수 (1)
    :param board: 본 판의 상태가 저장되어 있는 list 를 입력 받음
    :return: 복사한 list 를 반환함
    """
    dup_board = []              # 복사할 빈(empty) list 를 선언

    for i in board:             # 본 판의 list 에서 값을 하나씩 꺼낸다.
        dup_board.append(i)     # list 에 값을 추가하는 append() 모듈을 이용한다.

    return dup_board            # 만든 모듈을 반환한다.


def get_board_copy_other(board):
    """
    컴퓨터가 둘 곳을 결정하기 위해서, 본 판이 아닌 임시의 판을 복제하는 함수 (2)
    copy 라이브러리 활용 / https://docs.python.org/ko/3/library/copy.html
    :param board: 본 판의 상태가 저장되어 있는 list 를 입력 받음
    :return: 복사한 list 를 반환함
    """
    return copy.copy(board)     # Return a shallow copy of x. / 객체를 복제하여 내용은 같으나 다른 객체를 만들어 반환함
    # return copy.deepcopy(board) # Return a deep copy of x. / 2 차원 이상의 list 등을 복제 할 때에는 내부까지 모두 복제하는 deepcopy 를 사용


def is_space_free(board, move_target):
    """
    두고자 하는 곳이 비어 있는지 확인하는 함수
    :param board: 확인 할 판을 입력 받음
    :param move_target: 빈 곳의 index 를 입력 받음 (1~9)
    :return: 비어 있다면 True, 아니라면 False
    """
    return board[move_target] == ' '


def get_player_move(board):
    """
    player 에게 두고 싶은 곳을 입력 받고, 둘 수 있는지 확인하는 함수
    is_space_free() 를 활용
    :param board: 확인하고 싶은 판
    :return: int 두고 싶은 위치의 index (1~9)
    """
    player_select_move = ' '
    # 1~9 사이의 값이 입력 되었는지, 두고 싶다고 입력 한 곳이 비어 있는지 확인
    while player_select_move not in '1 2 3 4 5 6 7 8 9'.split() or not is_space_free(board, int(player_select_move)):
        player_select_move = input('What is your next move? (1-9): ')

    return int(player_select_move)


def choose_random_move_from_list(board, moves_list):
    """
    list 를 받아서 둘 수 있는 곳을 확인, 그 목록을 반환함
    :param board: 확인하고 싶은 판
    :param moves_list: 둘수 있는지 확인하고자 하는 위치 list
    :return: 둘수 있는 목록 or None
    """
    possible_moves = []
    for i in moves_list:
        if is_space_free(board, i):     # 놓고 싶은 곳이 비어 있는지 확인
            possible_moves.append(i)    # 비어 있다면, 목록을 추가하여 저장
            # https://docs.python.org/ko/3/library/array.html?highlight=append#array.array.append

    if len(possible_moves) != 0:
        return random.choice(possible_moves)
    else:
        return None


def get_computer_move(board, computer_use_letter):
    """
    weak AI 컴퓨터가 두는 곳을 결정하는 함수
    1) 내가 두었을 때 승리하는 곳이 있는지 점검
    2) 상대방이 두었을 때 승리하는 곳이 있는지 점검
    3) 모퉁이가 비어 있다면, random 으로 선점함
    4) 만약 중앙이 비어 있다면, 선점
    5) 십자 위치가 비어 있다면, random 으로 선점함
    :param board:
    :param computer_use_letter:
    :return:
    """
    player_use_letter = 'O' if computer_use_letter == 'X' else 'X'      # 각 플레이어가 사용하고 있는 표식을 확인

    for check_letter in [computer_use_letter, player_use_letter]:       # 1, 2) 컴퓨터, 플레이어 순으로 승리 할 수 있는 수가 있는지 확인 하는 반복문
        for j in range(1, 10):                                              # range(1, 10) > [1, 2, 3, 4, 5, 6, 7, 8, 9]
            copy_board = get_board_copy(board)                              # 본판을 복사해서 임시의 판을 만들어 확인에 사용한다.
            if is_space_free(copy_board, j):                                # 특정 공간이 비어 있는 확인
                make_move(copy_board, check_letter, j)                          # 특정 공간에 말을 임시로 두기
                if is_winner(copy_board, check_letter):                         # 승리하는 조건인지 확인하기
                    return j                                                        # 승리한다면 특정 위치를 반환

    suggest_move = choose_random_move_from_list(board, [1, 3, 7, 9])    # 3) 상대방이 두었을 때 승리하는 곳이 있는지 점검
    if suggest_move is not None:
        return suggest_move

    if is_space_free(board, 5):                                         # 4) 만약 중앙이 비어 있다면, 선점
        return 5

    return choose_random_move_from_list(board, [2, 4, 6, 8])            # 5) 십자 위치가 비어 있다면, random 으로 선점함


def is_board_full(board):
    """
    판에 더 둘수 있는 곳이 있는지 확인하는 모듈
    :param board: 확인하고자 하는 판
    :return: True or False
    """
    for i in range(1, 10):
        if is_space_free(board, i):     # 빈공간 인지 확인하는 함수를 활용하여 확인
            return False

    return True


# 프로그램의 시작
print('Welcome to Tic Tac Toe!')

while True:
    the_board = [' '] * 10                                          # index 를 1~9 까지 사용하기 때문에 10개짜리 문자열을 만들어줌
    player_letter, computer_letter = input_player_letter()          # 사용자가 사용하고자 하는 문자를 선택한 결과를 각각 저장함
    turn = 'computer' if random.randint(0, 1) == 0 else 'player'    # 누가 먼저 할 것인지를 결정하는 구문
    print('The %s will go first.' % turn)
    game_is_playing = True

    while game_is_playing:
        if turn == 'player':                            # 사용자 턴이라면?
            draw_board(the_board)                           # 일단, 현재 판을 출력한다.
            move = get_player_move(the_board)               # 사용자로부터 두고 싶은 곳을 입력 받는다. (둘수 있는 곳인지 검증 하고 옴)
            make_move(the_board, player_letter, move)       # 실제 판에 둔다.

            if is_winner(the_board, player_letter):         # 승리 했는지 확인해서
                draw_board(the_board)                           # 판을 출력하고
                print('Hooray! You have won the game!')
                game_is_playing = False                         # 게임 진행을 멈춤
            else:                                           # 승리하지 않았다면
                if is_board_full(the_board):                    # 판이 다 찼는지 확인
                    draw_board(the_board)                       # 판을 그려서 다 찾는지 알려준다.
                    print('The game is a tie!')
                    break
                else:
                    turn = 'computer'

        else:                                           # 컴퓨터 턴이라면?
            move = get_computer_move(the_board, computer_letter)    # weak AI 에 의한 둘 위치 결정
            make_move(the_board, computer_letter, move)

            if is_winner(the_board, computer_letter):
                draw_board(the_board)
                print('The computer has beaten you! You lose.')
                game_is_playing = False
            else:
                if is_board_full(the_board):
                    draw_board(the_board)
                    print('The game is a tie!')
                    break
                else:
                    turn = 'player'

    if not play_again():
        break
