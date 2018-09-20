# -*- coding: utf-8 -*-
"""
Title       Tic Tac Toe
Author      ITSC (Taewon Kang)
Date        2018.09.05
"""

import random

def draw_board(board):  # tictactoe 현황 표시
    print(board[1] + '|' + board[2] + '|' + board[3])
    print(board[4] + '|' + board[5] + '|' + board[6])
    print(board[7] + '|' + board[8] + '|' + board[9])

def free_space(board, move):
    return board[move] == ' '  # 두고자 하는 곳이 비어 있는지 확인

def make_move(board, letter, move):  # 판 정보와, 'O'/'X' 구분, 말을 놓을 위치 (1~9) 를 입력받는다
    board[move] = letter  # 판의 말을 놓을 위치에 O 또는 X를 저장한다.

def winner_check(board, letter):
    win = [[1,2,3],[4,5,6],[7,8,9],[1,4,7],[2,5,8],[3,6,9],[1,5,9],[3,5,7]]  # 가로, 세로 대각선 승리조건을 win 리스트로 제작

    for i in win:  # win에서 값을 하나씩 꺼내 i에 넣는다.
        tmp = 0  # 일치 개수 저장
        for j in i:  # 리스트에서 값을 한개씩 꺼내와 j에 저장
            if board[j] == letter:  # 일치여부 확인
                tmp += 1  # count 증가
                if tmp == 3:  # 3개를 채웠다면 승리로 True 반환
                    return True

def is_vaild_char(letter):  # 사용자가 입력한 문자가 O 또는 X인지 검사
    result = None
    if letter == 'X' or letter == 'O':
        result = True
    else:
        result = False
    return result

def is_digit(user_input_number):  # 문자열 값을 입력받아 정수로 변환 가능할 경우에는 True, 그렇지 않다면 False로 변환해줌
    result = user_input_number.isdigit()
    return result

def is_vaild_num(num):  # 사용자가 입력한 숫자가 1부터 9 사이인지 검사
    if int(num) > 9 or int(num) < 1:
        return False
    else:
        return True

def is_yes(letter):  # 문자열값이 대소문자에 관계 없이 Y인지 감지
    result = None
    if letter == 'Y' or letter == 'y':
        result = True
    else:
        result = False
    return result


def is_no(letter):  # 문자열값이 대소문자에 관계 없이 N인지 감지
    result = None
    if letter == 'N' or letter == 'n':
        result = True
    else:
        result = False
    return result

def get_board_copy(board):  # 컴퓨터가 말을 둘 곳을 결정하기 위해서 임시로 판을 복제함.
    new_board = []  # 복사할 빈 list 선언
    for i in board:  # list에서 값을 하나씩 꺼냄
        new_board.append(i)  # list에 값 추가
    return new_board  # 만든 new_board 반환

def get_turn():  # 차례가 컴퓨터인지 사람인지를 구함
    return 'computer' if random.randint(0, 1) == 0 else 'human'

def board_full(board):  # 판에 더 둘 곳이 있는지 확인
    for i in range(1, 10):
        if free_space(board, i):
            return False
    return True

def getPlayermove():  # 플레이어가 둘 수를 입력받음
    playermove = ' '
    while True:
        playermove = input('What is your next move? (1~9): ')  # 1부터 9까지 수 입력
        if is_digit(playermove):  # 입력한 숫자가 정수인가? (알파벳 등 안됨)
            if int(playermove) > 9 or int(playermove) < 1:  # 입력한 숫자가 1부터 9 사이인가?
                print("Wrong Input, Input again (1~9)")
            else:
                return int(playermove)
                break
        else:
            print("Wrong Input, Input again (number only)")

def random_list(board, moves_list):  # 둘 수 있는 곳의 목록 반환
    possible = []
    for i in moves_list:
        if free_space(board, i):  # 놓고 싶은 곳이 비어 있는지 확인
            possible.append(i)  # 비어 있다면 저장

    if len(possible) != 0:
        return random.choice(possible)
    else:
        return None


def getComMove(board, c_letter):  # 알고리즘 Github 참조
    p_letter2 = 'O' if c_letter == 'X' else 'X'  # 플레이어의 수식 확인

    # tic-tae-toe AI
    for i in [c_letter, p_letter2]:  # 컴퓨터 플레이어 순으로 승리하는 수가 있는지 확인
        for j in range(1, 10):
            board2 = get_board_copy(board)  # 임시의 판을 만들어 확인에 사용
            if free_space(board2, j):  # 비어 있는지 확인
                make_move(board2, i, j)  # 특정 공간에 말을 임시로 둠
                if winner_check(board2, i):  # 승리 조건 확인
                    return j  # 특정 위치 반환 (승리인 경우)

    rand_mv = random_list(board, [1, 3, 7, 9])  # 가장자리가 비어 있다면 랜덤으로 선점
    if rand_mv is not None:
        return rand_mv

    if free_space(board, 5):  # 중앙을 택할 수 있다면, 가져간다.
        return 5

    return random_list(board, [2, 4, 6, 8])  # 2,4,6,8번을 택할 수 있다면 가져간다.


def input_letter():
    while True:
        letter = input('Do you want to be X or O? :').upper()  # X, O 말을 입력받는다
        if is_vaild_char(letter) == True:  # 입력된 문자가 X나 O인지 검사
            return ['X', 'O'] if letter == 'X' else ['O', 'X']
        else:
            print('Wrong Input, Try again.')

def main():
    # Main 함수, 프로그램 시작
    print('Welcome to TicTacToe!')

    while True:
        find = 0
        board = [' '] * 10  # 1~9 Index 생성
        p_letter, c_letter = input_letter()  # 사용자가 선택한 말, 컴퓨터가 택해야 하는 말을 지정

        turn = get_turn()  # 누가 먼저인가 결정
        print('The ' + turn +' will go first.')

        while True:
            if turn == 'human':  # 사용자의 턴
                draw_board(board)  # 현재 판 출력
                move = getPlayermove()  # 사용자에게 말을 놓고 싶은 곳을 입력받음
                make_move(board, p_letter, move)  # 실제 판에 말을 둠

                if winner_check(board, p_letter):  # 승리했다면?
                    draw_board(board)
                    print('You win!') # 판 출력, 승리 출력
                    while True:
                        chk = input('one more(Y/N) ?')  # 다시 플레이할지 여부
                        if is_no(chk) == True:  # No
                            print("Thank you for using this program")
                            print("End of the Game")
                            exit()
                        if is_yes(chk) == True:  # Yes
                            find = 1
                            break
                        else:
                            print("Wrong Input, Input again")

                else:  # 승리하지 않았다면
                    if board_full(board):
                        draw_board(board)
                        print('the game is a tie!')
                        break
                    else:
                        turn = 'computer'

                if find == 1:  # 다시 하겠다는 의사를 밝히면 초기로 돌아감
                    break


            else:  # 컴퓨터의 턴
                move = getComMove(board, c_letter)
                make_move(board, c_letter, move)
                
                if winner_check(board, c_letter):  # 컴퓨터가 승리했다면?
                    draw_board(board)
                    print('The computer has beaten you! You lose.') # 실패 출력
                    while True:
                        chk = input('one more(Y/N) ?')  #Play again?
                        if is_no(chk) == True:  # No
                            print("Thank you for using this program")
                            print("End of the Game")
                            exit()
                        if is_yes(chk) == True:  # Yes
                            find = 1
                            break
                        else:
                            print("Wrong Input, Input again")

                else:  # 승리하지 않았다면
                    if board_full(board):
                        draw_board(board)
                        print('The game is a tie!')
                        break
                    else:
                        turn = 'human'

                if find == 1:
                    break

                # 승리 후 다시 플레이할지 여부에 대한 코드는 human과 동일

if __name__ == "__main__":
    main()