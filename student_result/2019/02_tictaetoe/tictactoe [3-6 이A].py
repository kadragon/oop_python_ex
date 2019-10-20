import random
import copy

numbers = list(range(2))


def make_board(board):  # 판을 그리는 함수
    print()
    print('-' * 11)
    print(' %s | %s | %s ' % (board[1], board[2], board[3]))
    print('-' * 11)
    print(' %s | %s | %s ' % (board[4], board[5], board[6]))
    print('-' * 11)
    print(' %s | %s | %s ' % (board[7], board[8], board[9]))
    print('-' * 11)
    print()


def play_again():
    # 다시 한번 플레이 할 것인가?
    return input('Are you going to play again? (yes or no): ').lower().startswith('y')


def is_able(board, target):
    # 두고자 하는 곳이 비어있는 곳인가?
    return board[target] == ' '


def get_player_move(board):  # 놓을 곳을 입력받는 함수

    player_move = ' '
    while player_move not in '1 2 3 4 5 6 7 8 9'.split() or not is_able(board, int(player_move)):
        player_move = input('What is your next move? (1-9): ')
    return int(player_move)


def choose_random(board, moves_list):  # Thx, Kadragon for idea
    # 둘 수 있는 곳을 확인 및 반환
    possible_moves = []
    for i in moves_list:
        if is_able(board, i):  # 둘 수 있는지 확인
            possible_moves.append(i)  # 가능하다면 옮기기
    if len(possible_moves) != 0:
        return random.choice(possible_moves)
    else:
        return None


def make_move(board, computer_letter):  # Thx, Kadragon for idea
    # 필승위치 방지 함수
    player_letter = 'O' if computer_letter == 'X' else 'X'  # player_letter 불러오기

    for check_letter in [computer_letter, player_letter]:  # 우승 가능 여부 확인
        for j in range(1, 10):
            copy_board = copy.copy(board)  # 판을 복사해서 확인에 사용
            if is_able(copy_board, j):
                do(copy_board, check_letter, j)  # 특정 공간에 말을 임시로 두기
                if win(copy_board, check_letter):  # 승리조건 확인
                    return j  # 승리위치라면  그 위치 반환

    return choose_random(board, range(1, 10))  # 아니면 랜덤적으로 놓기


def ask_free(board, target):  # 놓을 수 있는 곳인지 확인
    return board[target] == ' '


def ask_done(board):  # 판이 가득 찼는지 확인
    for i in range(1, 10):
        if ask_free(board, i):
            return False

    return True


def do(board, letter, target):  # 판에다가 놓기
    board[target] = letter


def input_letter():
    letter = ' '
    while not (letter == 'O' or letter == 'X'):
        print("Select O / X")
        letter = input().upper()
    return 'X' if letter == 'X' else 'O'


def bring_c_letter(temp):  # player글자 받아서 computer글자 정하기
    if (temp == 'X'):
        return 'O'
    else:
        return 'X'


def with_random():  # 랜덤적으로 숫자를 골라 0 index에 있는 걸로 선택
    random.shuffle(numbers)
    return numbers[0]


def is_able(board, to):
    return board[to] == ' '


def get_input(board):
    player_move = ' '
    while player_move not in '1 2 3 4 5 6 7 8 9'.split() or not is_able(board, int(player_move)):
        player_move = input('Where do you want to place? (1-9): ')

    return int(player_move)


def win(board, letter):  # 우승조건
    winning = [[1, 2, 3], [1, 4, 7], [1, 5, 9], [2, 5, 8], [3, 5, 7], [3, 6, 9], [4, 5, 6], [7, 8, 9]]
    for i in winning:
        count = 0
        for j in i:
            if board[j] == letter:
                count += 1
                if count == 3:
                    return True
            else:
                continue


def turn_conversion():  # 0, 1을 플레이어로 변환
    if numbers[0] == 0:
        return 'player'
    else:
        return 'computer'


def inform(temp):
    if temp == 0:
        print("You Start First.")
    else:
        print("I Will Start.")


print("=" * 50)
print("Let's Play Tic-Tac-Toe!")
print("If you don't know the rules, visit https://ko.wikipedia.org/wiki/틱택토")
print("")
print("=" * 50)

while True:  # break 만들기
    real_board = [' '] * 10
    player_letter = input_letter()  # letter 받기
    computer_letter = bring_c_letter(player_letter)  # player이 입력하지 않은 문자로 선택하기
    inform(with_random())  # 랜덤적으로 결정해서 순서 알려주기
    turn = turn_conversion()  # 0, 1을 O, X로 순서에 맞게 변환하기
    game_flag = True  # 게임 중간에 끊을 수 있게 만든 flag

    while game_flag:
        if turn == 'computer':
            move = make_move(real_board, computer_letter)  # 컴퓨터가 움직이기
            do(real_board, computer_letter, move)

            if win(real_board, computer_letter):  # 컴퓨터가 이겼으면
                print('You losed. HAHA')  # 끝내고
                make_board(real_board)  # 그려주고
                game_flag = False
            else:
                if ask_done(real_board):
                    make_board(real_board)
                    print('Well, it was a Tie')
                    break
                else:
                    turn = 'player'

        else:
            make_board(real_board)  # board 그려주기
            move = get_input(real_board)  # 입력받기
            do(real_board, player_letter, move)  # 그 위치에 말 놓기

            if win(real_board, player_letter):  # 이겼다면
                make_board(real_board)  # 그려주기
                print('You won! Congratulations')  # 축하해주기
                game_flag = False  # 게임 종료시키기

            else:
                if ask_done(real_board):  # 가득 찼다면
                    print('Well, it was a Tie')  # 무승부라고 안내하기
                    make_board(real_board)  # 그려주기
                    break  # 게임 종료
                else:
                    turn = 'computer'  # computer 턴으로 넘기기

    if not play_again():  # 다시 게임을 진행할 것인가?
        break
