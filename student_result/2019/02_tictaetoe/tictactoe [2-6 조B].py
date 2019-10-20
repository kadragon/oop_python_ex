import random
import time
import sys

winner = [[1, 2, 3], [4, 5, 6], [7, 8, 9], [1, 4, 7], [2, 5, 8], [3, 6, 9], [1, 5, 9], [3, 5, 7]]
win = 0  # 승리 횟수
lose = 0  # 패배 횟수
draw = 0  # 무승부 횟수
round = 0  # 라운드 수

length_of_board = 9  # 판의 길이(판을 1차원 배열로 만듬)
board = [0] * length_of_board  # 판 초기화


# 판을 출력하는 함수
def print_board(board_in_func):
    print("┌───────┬───────┬───────┐")
    print("│   %c   │   %c   │   %c   │" % (board_in_func[0], board_in_func[1], board_in_func[2]))  # 첫 줄
    print("├───────┼───────┼───────┤")
    print("│   %c   │   %c   │   %c   │" % (board_in_func[3], board_in_func[4], board_in_func[5]))  # 두번째 줄
    print("├───────┼───────┼───────┤")
    print("│   %c   │   %c   │   %c   │" % (board_in_func[6], board_in_func[7], board_in_func[8]))  # 세번째 줄
    print("└───────┴───────┴───────┘")


# 사용자의 입력을 받는 함수
def user_input(board_in_func):
    while True:
        print("Type a number from 1 ~ 9")
        user_input_number = input()  # user_input_number 에 사용자가 입력한 수를 넣는다.
        if '1' <= user_input_number <= '9':  # 1 부터 9 까지의 숫자가 입력으로 들어올 때는 정수형으로 변환 해준다.
            user_input_number = int(user_input_number)
            break
        else:  # 1 부터 9 까지의 숫자가 없으면 다시 입력받는다.
            print("Wrong Input. Type again")

    if board_in_func[user_input_number - 1] != 'X' and board_in_func[user_input_number - 1] != 'O':  # 놓으려고 하는 자리가 비었다면
        board_in_func[user_input_number - 1] = user_side  # 표시한다
    else:  # 차있다면
        print("Wrong Input. Type again")
        user_input(board_in_func)  # 다시 놓는다


# 컴퓨터가 수비하는 함수
def com_defence(board_in_func):
    for x in range(len(winner)):
        user_number = 0
        com_number = 0

        for y in range(3):
            if board_in_func[winner[x][y] - 1] == user_side:
                user_number += 1
            elif board_in_func[winner[x][y] - 1] == com_side:
                com_number += 1

        if user_number == 2:  # 사용자의 돌 중에서 두개 연속된 것이 있으면
            for y in range(3):
                if '1' <= board_in_func[winner[x][y] - 1] <= '9':
                    return winner[x][y] - 1

        elif com_number == 2:  # 컴퓨터의 돌 중에서 두개 연속된 것이 있으면
            for y in range(3):
                if '1' <= board_in_func[winner[x][y] - 1] <= '9':
                    return winner[x][y] - 1

    return -1


# 최소의 자리를 반환해준다
def min_pos(board_in_func):
    for x in range(len(board_in_func)):
        if '1' <= board_in_func[x] <= '9':
            return x
    return -2


# 컴퓨터가 입력하는 함수
def com_input(board_in_func):
    print("Computer is thinking..... This could take a few seconds.")
    for x in range(3):
        print('.')
        time.sleep(0.5)
    com_input_number = min_pos(board_in_func)  # 남은 최소 자리에 넣어준다
    if com_defence(board_in_func) != -1:  # 방어하거나 공격할 수 있다면
        com_input_number = com_defence(board_in_func)  # 그 자리에 놓는다
    board_in_func[com_input_number] = com_side  # 그 자리에 놓는다


# 우승자를 찾는 함수
def find_winner(board_in_func):
    global win, lose
    for x in range(len(winner)):
        user_number = 0
        com_number = 0

        for y in range(3):
            if board_in_func[winner[x][y] - 1] == user_side:
                user_number += 1
            elif board_in_func[winner[x][y] - 1] == com_side:
                com_number += 1

        if user_number == 3:  # 사용자의 돌 중에서 연속된 3개가 있다면
            print("User Win")  # 사용자 승리 출력
            win += 1  # 승리 횟수 1 추가
            return True  # 참 반환

        if com_number == 3:  # 컴퓨터 돌 중에서 연속된 3개가 있다면
            print("Com Win")  # 컴퓨터 승리
            lose += 1  # 패배 횟수 1 추가
            return True  # 참 반환

    return False  # 거짓 반환


# 다시 할 건지 물어보는 함수
def play_again():
    global play
    print("Do you want to play again? Type (Yes) or (No)")
    play_again_input = input()  # yes or no 를 입력받는다

    play_again_input = play_again_input.lower()

    if play_again_input == "yes":
        play = True
    elif play_again_input == "no":
        print("Bye Bye")
        sys.exit()  # 종료
    else:
        print("Type correctly")
        play_again()  # 다시 입력하도록 유도


# 판의 모든 원소를 삭제
def delete_board(board_in_func):
    for x in range(1, 10):
        board_in_func[x - 1] = str(x)


# 비길 때 상황
def tie(board_in_func):
    global draw
    flag = 0
    for x in range(len(board_in_func)):
        if board_in_func[x] == 'O' or board_in_func[x] == 'X':
            flag += 1

    if flag == 9:  # 판이 꽉 차있다면
        print("You Tie")
        draw += 1  # 비긴 횟수 1 추가
        return True  # 참 반환

    else:
        return False


# 승률 구하는 함수
def win_rate():
    global win, lose, draw, round
    print("%d Round Result: %d W %d L %d D" % (round, win, lose, draw))
    print("Your winning rate is %f(percent)" % ((win / round) * 100))


type_well = True

# 편을 입력 받는 함수
while type_well:
    print("Please Choose your Side(O / X)")
    user_side = input()
    user_side = user_side.upper()

    if user_side == 'O':
        com_side = 'X'
        type_well = False
    elif user_side == 'X':
        com_side = 'O'
        type_well = False
    else:
        print("Type Correctly!!")
        type_well = True

print("Your Side is %c" % user_side)

play = True

while play:
    flag_main = 0
    for i in range(len(board)):
        if board[i] == 'O' or board[i] == 'X':
            flag_main = 1

    if flag_main == 0:
        user_order = random.randrange(1, 3)  # 랜덤으로 순서 정하기

        if user_order == 1:
            print("You will go First")
        else:
            print("Computer will go First")

        for i in range(1, 10):
            board[i - 1] = str(i)
        print_board(board)

    # 사용자가 처음 시작할 때
    if user_order == 1:
        user_input(board)  # 사용자가 먼저 판 입력 받음
        print_board(board)  # 판 출력 받음
        if find_winner(board) or tie(board):  # 우승자가 있거나 비겼을 때
            round += 1  # 라운드 횟수 1 증가
            win_rate()  # 승률 출력
            play_again()  # 다시 플레이할 건지 물어봄
            delete_board(board)  # 판 초기화

        com_input(board)  # 컴퓨터가 후공
        print_board(board)
        if find_winner(board) or tie(board):
            round += 1
            win_rate()
            play_again()
            delete_board(board)

    if user_order == 2:  # 사용자가 후공일 때
        com_input(board)  # 컴퓨터 먼저 선공
        print_board(board)
        if find_winner(board) or tie(board):
            round += 1
            win_rate()
            play_again()
            delete_board(board)

        user_input(board)  # 사용자 후공
        print_board(board)
        if find_winner(board) or tie(board):
            round += 1
            win_rate()
            play_again()
            delete_board(board)
