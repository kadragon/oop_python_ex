import copy  # 보드를 카피하여 이길 수 있는 곳인지 체크하기 위해
import random  # 컴퓨터와 사용자 중 누가 먼저 시작할지 결정하기 위해


def print_state(Game):  # 보드의 상태를 출력하는 함수
    print("\n-----------")
    print(" %s | %s | %s" % (Game[1], Game[2], Game[3]))
    print(" %s | %s | %s" % (Game[4], Game[5], Game[6]))
    print(" %s | %s | %s" % (Game[7], Game[8], Game[9]))
    print("-----------\n")


def right_place(place, Game):  # 1~9까지의 숫자가 든 문자열과 보드를 입력받아 가능한 곳인지 판정하는 함수
    place = int(place)  # 문자열을 숫자로 변경
    if place > 0 and place < 10 and Game[place] == ' ':  # 범위에 맞고 보드가 비었다면 가능한 곳
        return True
    return False


def only_integer(num):  # 입력된 값이 '1'~'9'까지인지를 판별하는 함수
    for i in range(1, 10):
        if str(i) == num:  # '1'부터 '9'까지 중 같은 것이 있다면 True
            return True
    return False


def user_places(user, Game):  # 사용자가 입력한 위치에 따라 보드에 입력하는 함수
    print_state(Game)  # 게임판 출력
    print("What is your next move? (1-9):", end=' ')
    user_p = input()  # 입력받음
    while not only_integer(user_p) or not right_place(user_p, Game):
        user_p = input("(1-9) 중 둘 수 있는 곳의 위치를 입력하세요.")  # 범위에 없거나 둘 수 없으면 다시 입력받음
    Game[int(user_p)] = user


def iswin(player, Game):  # player와 보드판을 받아 player가 승리했는지 판정하는 함수
    win = [[1, 2, 3], [4, 5, 6], [7, 8, 9], [1, 4, 7], [2, 5, 8], [3, 6, 9], [1, 5, 9], [3, 5, 7]]  # 이것들이 다 같으면 승리한 것임
    for i in range(8):  # win배열의 구성요소들에 대해
        cnt = 0
        for j in range(3):
            if Game[win[i][j]] == player:
                cnt += 1
        if cnt == 3:  # 세 개의 구성요소가 모두 player 였다면 player의 승리
            return True
        cnt = 0
    return False


def win_place(player, Game):  # player가 이길 수 있는 곳을 찾는 함수
    for i in range(1, 10):
        if right_place(i, Game):  # 가능한 모든 곳에 대해
            tmp = copy.deepcopy(Game)
            tmp[i] = player  # 보드판을 복사해서 채워넣기
            if iswin(player, tmp):  # 이겼다면 승리의 수가 존재한 것이브로 그곳을 반환
                return i
    return -1


def next_places(user, com, Game):  # 컴퓨터가 다음 둘 곳을 결정하는 함수
    now = win_place(com, Game)
    if now != -1:
        Game[now] = com  # 컴퓨터가 이길 수 있는 수가 있다면 그곳을 둠
        return
    now = win_place(user, Game)
    if now != -1:
        Game[now] = com  # 사용자가 이길 수 있는 수가 있다면 그곳을 막음
        return
    for i in range(1, 10):
        if right_place(i, Game):
            Game[i] = com  # 아니라면 그냥 가능한 곳에 둔다
            return


def play_again():  # 사용자에게 다시 플레이할 것인지 물어보는 함수
    print("Do you want to play again? (yes or no): ", end='')
    again = input()
    while again != "yes" and again != "no":
        again = input("yes나 no를 입력하세요.")  # yes나 no가 아니면 다시 입력받음
    if again == "yes":
        return True
    else:
        return False


def Odds(win, lose, tie):  # 승률을 출력하는 함수
    print("당신의 승률은 %.2f %% 입니다." % (win / (win + lose + tie) * 100))
    return


print("Welcome to Tic Tac Toe!")
Win = 0
Lose = 0
Tie = 0  # 승률 계산을 위한 변수

while True:
    board = [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']  # 보드 생성
    print("Do you want to be X or O? :", end=' ')
    user_pos = input()
    while user_pos not in "XO" or user_pos == '':  # 유저의 포지션을 입력받음, X나 O가 아니면 다시 입력
        user_pos = input("X나 O를 입력하세요.")
    if user_pos == 'O':
        com_pos = 'X'
    else:
        com_pos = 'O'

    first = random.randrange(0, 2)  # 첫번째에 누가 시작할지 랜덤으로 결정
    if first == 1:
        print("The player will go first.")  # 사용자가 먼저라면 사용자가 두게 함
        user_places(user_pos, board)
    else:
        print("The computer will go first.")
    cnt = 0
    while True:
        next_places(user_pos, com_pos, board)  # 컴퓨터의 차례
        if iswin(com_pos, board):  # 컴퓨터가 이겼다면 게임판을 출력하고 졌음을 알려줌
            print_state(board)
            print("You lose...")
            Lose += 1
            break
        cnt += 1  # 컴퓨터가 둔 후 시행횟수 +1
        if cnt >= 9:  # 컴퓨터가 둔 후 판이 다 찼다면 무승부를 출력
            print_state(board)
            print("The game is a tie!")
            Tie += 1
            break
        user_places(user_pos, board)  # 사용자의 차례
        if iswin(user_pos, board):  # 사용자가 이겼다면 게임판을 출력하고 이겼음을 알려줌
            print_state(board)
            print("Hooray! You have won the game!")
            Win += 1
            break
        cnt += 1  # 사용자가 둔 후 시행횟수 +1
        if cnt >= 9:  # 사용자가 둔 후 판이 다 찼다면 무승부를 출력
            print_state(board)
            print("The game is Tie!")
            break
    Odds(Win, Lose, Tie)  # 게임이 끝난 후 승률을 출력
    if not play_again():  # 다시 플레이할지 물어봄
        break
