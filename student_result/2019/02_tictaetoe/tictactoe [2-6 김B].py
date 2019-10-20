import random

# 이기는 경우들
winners = ((0, 1, 2), (3, 4, 5), (6, 7, 8), (0, 3, 6), (1, 4, 7), (2, 5, 8), (0, 4, 8), (2, 4, 6))

table = range(1, 10)
player_win = 0  # 사용자가 이긴 횟수
computer_win = 0  # 컴퓨터가 이긴 횟수


def print_board():  # 화면에 현재 상태를 출력하는 기능
    print("---------")
    x = 1
    for i in board:
        end = ' | '
        if x % 3 == 0:
            end = ' \n'
            if i is not 1:
                end += '---------\n'
        char = ' '
        if i in ('O', 'X'):
            char = i
        x += 1
        print(char, end=end)


def can_move(board, move):  # 범위 내이며 이미 O/X가 있는지 확인, 문제 없으면 True 리턴
    if move in table and board[move - 1] == move - 1:
        return True
    return False


def is_win(board, player):  # 위의 winners 튜플 경우인지 확인
    places = []
    x = 0
    for i in board:
        if i == player:
            places.append(x)
        x += 1
    win = False
    for i in winners:
        cnt = 0
        win = False
        for j in i:
            if board[j] == player:
                cnt += 1
        if cnt == 3:
            win = True
            break
    return win


def movement(board, player, move, undo=False):  # 자리에 변화가 생기고 이기는 경우인지 확인하여 리스트형으로 리턴
    if can_move(board, move):
        board[move - 1] = player
        win = is_win(board, player)
        if undo:  # 실제로 그 자리에 O/X를 두지 않고 경우 확인만 할 경우 다시 원래대로 되돌리기
            board[move - 1] = move - 1
        return [True, win]
    return [False, False]


def computer_move():  # 컴퓨터가 다음 둘 곳을 판단하는 기능
    move = -1
    for i in table:
        # computer가 바로 이길 수 있는 경우를 탐색한다.
        if movement(board, computer, i, True)[1]:
            move = i
            break
    if move == -1:
        # computer가 이번 턴에 이길 수 없다면 player가 이기게 될 경우를 방어한다.
        for i in table:
            if movement(board, player, i, True)[1]:
                move = i
                break
    if move == -1:
        # player가 이길 경우가 없다면 아무 곳에 둔다.
        k = random.randrange(1, 10)
        while not can_move(board, k):
            k = random.randrange(1, 10)
        move = k
    return movement(board, computer, move)


def is_full():  # 모든 칸이 차는 경우
    return board.count('O') + board.count('X') == 9


def right_input():  # input의 형식이 올바른지(정수형) 확인 후 input 값 리턴
    while True:
        try:
            move = int(input("\n# 어디에 두실래요? [1~9]: "))
        except:
            print("잘못 입력했잖아요. 다시.")
        else:
            return move


def get_order():  # 랜덤으로 순서를 결정하는 함수
    ord = random.randrange(0, 2)
    if ord == 0:
        print("컴퓨터가 선공이에요")
    else:
        print("당신이 선공이에요")
    return ord


def onemore():  # 사용자에게 다시 플레이할 것인지 물어보는 함수
    s = input("한 번 더? Y/N >>> ").upper()
    while (s != 'Y' and s != 'YES') and (s != 'N' and s != 'NO'):
        s = input("제대로 입력하세요! Y/N >>> ").upper()
    if s == 'Y' or s == 'YES':
        ok = True
    elif s == 'N' or s == 'NO':
        ok = False
    return ok


def print_winning_rate(win, lose):  # 승률을 기록하는 함수
    if win + lose == 0:
        winning_rate = 0
    else:
        winning_rate = (win / (win + lose)) * 100
    print("승률: ", winning_rate, "%\n")


ing = True
print("틱택토!!")
while ing:
    result = '비겼어요!'  # reult의 default값
    board = [0, 1, 2, 3, 4, 5, 6, 7, 8]
    player = input("O/X 중 하나를 고르세요 : ").upper()
    while player != 'O' and player != 'X':
        player = input("올바른 형식으로 고르세요 [O/X] : ").upper()
    if player == 'O':
        computer = 'X'
    else:
        computer = 'O'

    ord = get_order()
    while not is_full():
        # 사용자 선공일 경우 아래 코드부터 시작
        if ord == 1:
            print_board()
            move = right_input()
            moved, won = movement(board, player, move)
            if not moved:
                print("둘 수 없는 칸을 입력했어요. 다시.")
                continue
            if won:
                result = '당신이 이겼어요!'
                player_win += 1
                break
        # 컴퓨터 선공일 경우 아래 코드부터 시작
        ord = 1
        if (not is_full()) and computer_move()[1]:  # 모든 칸이 차지 않았으면 컴퓨터가 둠. 이후 컴퓨터가 이겼는지 판단
            result = '컴퓨터가 이겼어요!'
            computer_win += 1
            break
        if is_full():  # 사용자, 컴퓨터 둘 다 이기지 않았는데 꽉 차면 'result=비김' 변화 없이 break
            break

    print_board()
    print(result)
    print_winning_rate(player_win, computer_win)  # 사용자가 이기고 진 횟수 각각 전달하여 승률 출력
    ing = onemore()
