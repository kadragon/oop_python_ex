import random
import sys
import time


class GameBoard(object):
    def __init__(self, usr, com):
        # 유저와 컴퓨터의 문양을 지정하고 게임보드 클래스 생성
        # usr : 보드상에 나타날 유저의 문양 / com : 보드상에 나타날 컴퓨터의 문양

        self.board = []
        # 3 by 3 board
        # 0 : nobody / 1 : com / 2 : usr
        for _ in range(3):
            tmp = []
            for _ in range(3):
                tmp.append(0)
            self.board.append(tmp)
            self.user_code = usr
            self.com_code = com

        self.line = {}
        # i 번째 줄에 속한 칸을 기록
        """
                7
              / 
        _ _ _ - 6
        _ _ _ - 5
        _ _ _ - 4
        | | | N
        0 1 2   3
        """

        # 각 라인에 속한 좌표 기록
        for i in range(3):
            self.line[i] = []
            for j in range(3):
                self.line[i].append([j, i])

            self.line[i + 4] = []
            for j in range(3):
                self.line[i + 4].append([i, j])

        self.line[7] = []
        for j in range(3):
            self.line[7].append([j, 2 - j])

        self.line[3] = []
        for j in range(3):
            self.line[3].append([j, j])

        # 이미 자리가 찬 위치 기록
        self.filled = []

    def input(self, inp, key):
        # 보드의 해당 위치에 표시하는 함수
        # key : 누구의 input? / 'com' or 'usr'
        # inp : 수를 둘 위치
        self.filled.append(inp)
        idx = inp - 1
        if key is 'com':
            self.board[idx // 3][idx % 3] = 1
        elif key is 'usr':
            self.board[idx // 3][idx % 3] = 2

    def display(self):
        # 현재 보드 상태 출력
        print("=" * 13)
        for i in self.board:
            print('|', end='')
            for j in i:
                if j == 0:
                    j = ' '
                elif j == 1:
                    j = self.com_code
                else:
                    j = self.user_code
                print(" %c |" % j, end='')
            print("")
        print("=" * 13)

    def is_player_win(self, key):
        # key 가 이겼는지 판단
        # key : 'com' or 'usr'
        # 이겼으면 True, 이기지 않았으면 False
        if key is 'com':
            for i in range(8):
                cnt = 0
                for j in self.line[i]:
                    if self.board[j[0]][j[1]] is 1:
                        cnt += 1
                if cnt == 3:
                    return True
        elif key is 'usr':
            for i in range(8):
                cnt = 0
                for j in self.line[i]:
                    if self.board[j[0]][j[1]] is 2:
                        cnt += 1
                if cnt == 3:
                    return True
        return False

    def is_full(self):
        # 꽉 찼으면 True 아니면 False
        # draw 판정용
        a = True
        for i in range(3):
            for j in range(3):
                if self.board[i][j] == 0:
                    a = False
        return a


class ScoreBoard(object):
    def __init__(self, name):
        # name(str) : 유저이름
        self.user_name = name
        self.win = 0
        self.lose = 0
        self.draw = 0

    def display(self):
        # 스코어 상태 출력
        winning_rate = 0
        tot = self.lose + self.win + self.draw
        if tot > 0:
            winning_rate = self.win / tot
        print(f"""
{self.user_name}'s record :
win  : {self.win}
lose : {self.lose}
draw : {self.draw}
winning rate : {winning_rate}
""")


def chk_input(game_board, string):
    # 올바른 입력이면 True, 아니면 False
    try:
        inp = int(string)
    except ValueError:
        return False
    if inp < 1:
        return False
    if inp > 9:
        return False
    if inp in game_board.filled:
        return False
    return True


def com_turn(game_board):
    # 컴퓨터차례 진행하는 함수
    # 컴퓨터가 다음에 둘 곳 판단 후 입력
    time.sleep(1)
    print(f"\n\n{com_name}'s turn")
    time.sleep(2)

    where_com_should_put = [1, 1]  # 노란줄 보기 싫어서 생성
    mode = [-2]
    chk = True

    # 헬모드
    if com_name == "Chara":
        mode = [-2, 2]

    # 막아야 할 수 탐색
    for i in range(8):
        cnt = 0
        for j in game_board.line[i]:
            if game_board.board[j[0]][j[1]] == 1:
                cnt += 1
            elif game_board.board[j[0]][j[1]] == 2:
                cnt -= 1
            else:
                where_com_should_put = j
        if cnt in mode:
            chk = False
            break

    # 막을 필요가 있는 위치가 없는데 헬모드가 아니면 위치 랜덤
    if chk and (com_name != "Chara"):
        empty_list = []
        for i in range(3):
            for j in range(3):
                if game_board.board[i][j] == 0:
                    empty_list.append([i, j])
        random.shuffle(empty_list)
        where_com_should_put = empty_list[0]

    # [x, y]형태의 좌표를 1부터 9까지의 숫자로 변환
    where_com_should_put = where_com_should_put[0] * 3 + where_com_should_put[1] + 1
    game_board.input(where_com_should_put, 'com')


def user_turn(game_board):
    # user 차례 진행하는 함수
    time.sleep(2)
    while True:
        usr_input = input(f"\n\n{user_id}'s turn \n[1~9]: ")
        if usr_input == "quit":
            return "quit"
        if usr_input == "Kill me" and com_name == "Chara":
            return "kill"
        if chk_input(game_board, usr_input):
            usr_input = int(usr_input)
            game_board.input(usr_input, 'usr')
            break
        else:
            print("Wrong input.\nI need one digit of number between 1 to 9.")


def start_game(score_board):
    # 게임을 하나 진행하는 함수
    # score_board : 유저의 전적을 기록할 ScoreBoard 클래스

    first_move = random.randrange(1, 3)
    # 자신의 문양 지정
    while True:
        user_cod = input("What is your pattern? (in one letter) : ")
        if len(user_cod) != 1:
            print("It is not one letter \n\n")
        else:
            break
    # 컴퓨터의 문양 지정
    while True:
        comp_cod = input(f"What is {com_name}'s pattern? (in one letter) : ")
        if com_name == "Chara":
            if score_dict[com_name].win + score_dict[com_name].draw > 0:
                print("As you know, ")
            else:
                print("wait!")
            time.sleep(1)
            print("I'll choose myself!!!")
            comp_cod = user_cod
            time.sleep(1)
            print('\n')
            break
        elif len(comp_cod) != 1:
            print("it is not one letter \n\n")
        else:
            break
    game_board = GameBoard(usr=user_cod, com=comp_cod)

    print(f"{score_board.user_name} : '{game_board.user_code}' \n{com_name} : '{game_board.com_code}'\n")
    game_board.display()

    time.sleep(1)
    print("Choosing who will go first...")
    time.sleep(random.randrange(1, 4))

    # 유저 먼저
    if first_move == 2:
        print(f"{score_board.user_name} get first move")
        time.sleep(1)
        while True:
            # 유저 차례
            macro = user_turn(game_board)
            if macro == 'quit':
                score_board.lose += 1
                score_dict[com_name].win += 1
                print(f"{score_board} resigned")
                break
            if macro == "kill":
                print('No Problem')
                time.sleep(1)
                print('-' + '9' * 99999)
                sys.exit()

            game_board.display()
            if game_board.is_player_win('usr'):
                score_board.win += 1
                score_dict[com_name].lose += 1
                print(f"{score_board.user_name} is win!")
                break
            elif game_board.is_full():
                print("draw")
                score_board.draw += 1
                score_dict[com_name].draw += 1
                break

            # com 차례
            com_turn(game_board)
            game_board.display()
            if game_board.is_player_win('com'):
                score_board.lose += 1
                score_dict[com_name].win += 1
                print(f"{score_board.user_name} is lose!")
                break
            elif game_board.is_full():
                print("draw")
                score_board.draw += 1
                score_dict[com_name].draw += 1
                break
    # 컴 먼저
    else:
        print(f"{com_name} get first move")
        time.sleep(1)
        while True:
            # computer 차례
            com_turn(game_board)
            game_board.display()
            if game_board.is_player_win('com'):  # 이겼니?
                score_board.lose += 1
                score_dict[com_name].win += 1
                print(f"{score_board.user_name} is lose!")
                break
            elif game_board.is_full():  # 비겼어?
                print("draw")
                score_board.draw += 1
                score_dict[com_name].draw += 1
                break

            # user 차례
            macro = user_turn(game_board)
            if macro == 'quit':
                score_board.lose += 1
                score_dict[com_name].win += 1
                print(f"{score_board} resigned")
                break
            if macro == "kill":
                print('No Problem')
                time.sleep(1)
                print('-' + '9' * 999)
                for _ in range(80):
                    print('9' * 999)
                sys.exit()
            game_board.display()
            if game_board.is_player_win('usr'):  # 이겼니?
                score_board.win += 1
                score_board[com_name].lose += 1
                print(f"{score_board.user_name} is win!")
                break
            elif game_board.is_full():  # 비겼어?
                print("draw")
                score_board.draw += 1
                score_dict[com_name].draw += 1
                break


def restart():
    # 게임 재시작 함수
    if com_name == "Chara":
        re = input("""Do you want to play new game?
if you want to do again, enter any key
no other choice
[(y)]: """)
        print("\n" * 40)
    else:
        re = input("""Do you want to play new game?
if you want to do again, enter y
else, enter any other key
[y/(n)]: """)
        if re != "y":
            return 'no'
        print("\n" * 40)
    return 'yes'


com_name = "Computer"
score_dict = {"Computer": ScoreBoard("Computer")}

# 시작멘트
time.sleep(1)
print("""
Hello,
it's Dracul's TicTacToe.""")
time.sleep(3)
print("""You can make your id.
We will record your score with it.""")
time.sleep(5)
print("""You can choose you and computer's pattern on board too !
If you want, they can be same letter.
Also, you can make it ' '(emptyspace)!!!""")
time.sleep(7)
print("""
Enjoy the game
""")
time.sleep(4)
print("\n" * 40)
time.sleep(2)
print("Ummmm....")
time.sleep(2)
print("One thing, that I want to say before you start the game,")
time.sleep(3)
print("Don't write 'Chara' for your id.")
time.sleep(2)
print("\n\n\n\n\n\n\n" * 6)

# 게임 시작
while True:
    while True:
        user_id = input("Give me your id(in 12 letters)\n: ")
        if len(user_id) <= 12:
            break
        else:
            print("over 12 letters")
        if user_id is "computer":
            print("Hey, human. Are you serious?")

    if "Frisk" in score_dict:
        if user_id in ["Chara", "Frisk"]:
            print("Go, Go, Go !!!!!!!!!!!11")
        else:
            print("NONONO, ")
            time.sleep(2)
            print("You should play with me, Frisk. Don't be shy.")
            user_id = "Frisk"
            time.sleep(2)
    elif user_id == "Chara":
        score_dict[user_id] = ScoreBoard(user_id)
        time.sleep(3)
        print("Oh")
        time.sleep(3)
        print("really?")
        time.sleep(1)
        for _ in range(5):
            print('.')
            time.sleep(1)
        time.sleep(5)
        print('hmmmmmm')
        time.sleep(5)
        print("...")
        time.sleep(5)
        print("OK")
        time.sleep(3)
        print("But,")
        time.sleep(2)
        print("as I said")
        time.sleep(2)
        print("you can't use that name for your id")
        time.sleep(2)
        print("\nBecause,")
        time.sleep(3)
        print("It is my name!")
        time.sleep(2)
        print("\n\nuser_id : Frisk")
        time.sleep(4)
        print("\n\nPlay with me!")
        time.sleep(2)
        print("\n")
        user_id = "Frisk"
        com_name = "Chara"
        score_dict[user_id] = ScoreBoard(user_id)
    elif user_id not in score_dict:
        score_dict[user_id] = ScoreBoard(user_id)
        print("hello noob\n")

    # 게임 진행
    user_score = score_dict[user_id]
    start_game(user_score)

    # 전적 출력
    print('-' * 20)
    user_score.display()
    print('-' * 20)
    score_dict[com_name].display()

    # 다시시작 여부
    # 헬모드는 그런거 없다
    if restart() == 'no':
        break
