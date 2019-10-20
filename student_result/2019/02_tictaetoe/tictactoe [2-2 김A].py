# 소과제 2 - Tic Tac Toe

import random

text_welcome = """
----------------------윤종's Tic-Tac-Toe----------------------
환영합니다! 
틱택토는 3 x 3 칸에서 돌아가면서 한 칸을 가져가고, 
결국 1 줄을 얻는 사람이 이기는 게임이에요!
저를 이겨보세요! 
"""

text_square = """
자리는 아래와 같습니다. 
-----------
 1 | 2 | 3
 4 | 5 | 6
 7 | 8 | 9
-----------
"""
text_input = """
입력은 1 ~ 9 로 해주세요 
"""
text_start = """
누가 먼저 시작할지 정할께요...
"""
text_win = """
축하합니다! 승리하셨어요! 
"""
text_lose = """
아쉽네요, 패배하셨어요. 
"""
text_tie = """
무승부네요, 다음 번엔 이겨보세요!"""


def print_info(data):
    """
    :param data: list 형식으로 출력할 격자판의 정보를 입력받음.
    :return: 없음. 출력함.
    """
    print("============")
    print(" %c | %c | %c " % (data[0], data[1], data[2]))
    print(" %c | %c | %c " % (data[3], data[4], data[5]))
    print(" %c | %c | %c " % (data[6], data[7], data[8]))
    print("============")


def choose_side():
    """
    플레이어가 X, O를 정하는 함수
    :return: list 로  [플레이어의 기호, 컴퓨터의 기호]를 반환.
    """
    side = input("X, O 무엇을 선택하시겠어요? (X / O로 입력)")
    while side != 'X' and side != 'O':  # 'X', 'O' 가 아니면 다시 입력받음.
        print('잘못입력하셨습니다.')
        print('영글자 X 혹은 O을 입력해주세요')
        side = input("X, O 무엇을 선택하시겠어요? (X / O로 입력)")
    if side is 'X':
        n_side = 'O'
    else:
        n_side = 'X'
    return [side] + [n_side]


def retry():
    """
    재도전 여부를 확인하는 함수
    :return:  다시 도전한다면 1 return, 아니라면 0 return
    """
    again = input('한판 더?? (Y / N)')  # 재도전 여부 입력
    while again != 'N' and again != 'Y':  # 재도전 입력이 이상한지 검사
        print('잘못 입력하셨습니다.')
        print('영글자 Y 혹은 N를 입력해주세요')
        again = input('다시 도전하시겠습니까? (Y / N)')
    if again is 'N':
        return 1
    else:
        return 0


def result(win, lose, tie):
    """
    게임이 끝나고 최종 결과를 출력
    :param win: 이긴 경기 수
    :param lose: 진 경기 수
    :param tie: 무승부 경기 수
    :return: 없음
    """
    print("Result- Win:%d | Lose:%d | Tie:%d | Win Ratio: %2d %%" % (win, lose, tie, 100 * win / (win + lose + tie)))


def valid(n):
    """
    사용자가 선택한 숫자가 유효한지 ( 1 ~ 9로 입력했는지 확인)
    :param n: 사용자의 입력
    :return: 1 ~ 9가 임력되었으면 1 반환
    """
    if len(n) != 1 or (ord(n) < ord('1') or ord(n) > ord('9')):
        return 1


def repeated(n, stat):
    """
    사용자가 입력한 숫자의 중복 여부 확인
    :param n: 사용자의 선택
    :param stat: 현재 3 x 3 게임판 상황을 9칸 리스트로 입력받음
    :return: 중복되었으면 1 반환
    """
    if stat[int(n) - 1] != ' ':
        return 1


def pick(stat):
    """
    사용자가 수를 두는 차례
    :param stat: 현재 게임판의 상황 (9칸 리스트)
    :return: 입력이 올바를때, 사용자가 입력한 수를  반환 함.
    """
    p = input("당신의 차례입니다")
    while valid(p) or repeated(p, stat):
        print("잘못 입력하셨습니다.")
        if valid(p):  # 1~9가 아닌 경우
            p = input("1~9로 재입력")
        elif repeated(p, stat):  # 이미 자리에 수가 있는 경우
            print("중복되었습니다.")
            p = input("빈 자리를 택하세요")
    return p


lines = [[0, 1, 2], [3, 4, 5], [6, 7, 8], [0, 3, 6], [1, 4, 7], [2, 5, 8], [0, 4, 8], [2, 4, 6]]  # 3x3 칸에서 가능한 선의 집합.
n_win = 0  # 이긴, 진, 무승부한 횟수를 기록하는 전역변수
n_lose = 0
n_tie = 0


def com(stat):
    """
    컴퓨터가 수를 두는 차례
    :param stat: 현재 게임판 상황 ( 9칸 리스트)
    :return: 컴퓨터가 선택한 자리를 반환
    """
    c_win = []  # Computer 가 이길 수 있는 자리를 append 한다
    c_lose = []  # Computer 가 막아야 하는 자리를 append 한다
    for i in lines:  # 8 가지의 선을 모두 분석
        line = []

        for t in range(3):  # 지금 분석하는 선의 정보를 line 에 복사해 놓음, line 에 있는 자리에 놓을 수 있다.
            line.append(i[t])

        p_cnt = []  # Player 가 차지한 자리를 append 한다
        c_cnt = []  # Computer 가 차지한 자리를 append 한다

        for t in range(3):  # 한 선에 대한 정보를 파악

            if stat[i[t]] is Player:  # 분석하는 줄에서 player 가 놓은 자리는 p_cnt 에 추가하고, line 에선 지운다
                p_cnt.append(i[t])
                line.remove(i[t])

            elif stat[i[t]] is Computer:  # 분석하는 줄에서 컴퓨터가 놓은 자리는 c_cnt 에 추가하고, line 에선 지운다
                c_cnt.append(i[t])
                line.remove(i[t])

        if len(c_cnt) + len(p_cnt) is 3:  # line 이 꽉찬 경우
            continue
        if len(c_cnt) is 2 and len(p_cnt) is 0:  # 컴퓨터가 승리할 수 있는 경우
            c_win.append(line[0])
        if len(c_cnt) is 0 and len(p_cnt) is 2:  # 플레이어가 이기는 것을 막는 경우
            c_lose.append(line[0])

    if len(c_win):  # 8개의 선을 전부 탐색한 후, 반드시 이기는 곳을 택함
        return c_win[0]

    if len(c_lose):  # 8개의 선을 전부 탐색후, 반드시 막아야 하는 곳을 택함
        return c_lose[0]

    empty = []  # 반드시 놓아야 하는 점이 없다면, 빈 곳을 찾아 random 으로 골라서 선택함
    for i in range(9):
        if stat[i] is ' ':
            empty.append(i)
    random.shuffle(empty)
    return empty[0]


def check(stat, num, player, computer):
    """

    :param stat: 현재 게임판 상황
    :param num: 게임 진행 상황 (1 ~ 9번째 차례)
    :param player:  player 가 선택한 문자
    :param computer: computer 가 선택한 문자
    :return: 승부 / 무승부 : return  1 , 아직 게임 진행중이면 return 0
    """
    global n_win, n_lose, n_tie  # 전역변수 사용
    for i in lines:
        if stat[i[0]] == stat[i[1]] == stat[i[2]]:  # 한 줄이 같은 문자로 찼을 경우,
            if stat[i[0]] is ' ':  # 문자가 공백이면 그대로 진행
                continue
            if stat[i[0]] is player:  # 문자가 player 이면 플레이어 승
                print(text_win)
                n_win += 1
                return 1

            elif stat[i[0]] is computer:  # 문자가 computer 이면 컴퓨터 승
                print(text_lose)
                n_lose += 1
                return 1

    if num is 9:  # 9회를 진행했는데 승부가 나지 않았으면 무승부
        print(text_tie)
        n_tie += 1
        return 1
    return 0


# STARTS HERE ====================================================================

print(text_welcome)
print(text_square)

game_is_on = 1  # 게임이 진행되고 있으면 1
while game_is_on is 1:
    Player, Computer = choose_side()  # 문자를 정함
    print(text_start)
    P_first = random.randint(0, 1)  # 순서를 정함

    if P_first is 1:
        print("플레이어가 먼저!\n")
    else:
        print("제가 먼저네요 ^^\n")
    game = 1  # 한 판에서 게임이 진행된 수
    Status = [' '] * 9  # 게임판 현황
    while game <= 9:
        if P_first is 1:  # 플레이어 선공인 경우

            Status[int(pick(Status)) - 1] = Player  # 플레이어가 수를 놓음
            print_info(Status)  # 게임판 출력
            if check(Status, game, Player, Computer):  # 게임판 상황 판단
                if retry():
                    game_is_on = 0
                break
            game += 1

        Status[int(com(Status))] = Computer  # 컴퓨터가 수를 놓음
        print_info(Status)  # 게임판 출력
        if check(Status, game, Player, Computer):  # 게임판 상황 판단
            if retry():
                game_is_on = 0
            break
        game += 1
        P_first = 1

result(n_win, n_lose, n_tie)  # 결과, 승률 출력
