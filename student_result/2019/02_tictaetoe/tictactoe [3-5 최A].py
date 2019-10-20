import random
import copy

SCORE = [0, 0, 0]


def play_again():
    """
    게임 재시도 여부를 질문
    :return: 재시도하지 않는 경우 True
    """
    print("한 판 더?[Y/N]\n", end=">>> ")
    ans = input().upper()
    while ans != "Y" and ans != "N":  # 다른 답변을 입력한 경우
        print("한 판 더 할거냐고;;;\n", end=">>> ")
        ans = input().upper()
    if ans == "N":
        return True


def choose_OX():
    """
    사용자가 사용할 문자를 선택하는 함수
    :return: O/X 중 사용자가 선택한 문자
    """
    print("O/X 중에서 선택하세요. X가 먼저 시작합니다.\n", end=">>> ")
    char = input().upper()
    while char != "O" and char != "X":  # O/X가 아닌 값을 입력한 경우
        print("O.X. 중에서 선택하라고;;;\n", end=">>> ")
        char = input().upper()
    return char


def show_board(map_list):
    """
    사용자에게 게임판 보여주기
    :param map_list: 게임판을 저장한 list
    """
    print(map_list[1] + ' | ' + map_list[2] + ' | ' + map_list[3])
    print(map_list[4] + ' | ' + map_list[5] + ' | ' + map_list[6])
    print(map_list[7] + ' | ' + map_list[8] + ' | ' + map_list[9])


def player_choose(map_list):
    """
    사용자가 빈칸 중 하나 선택.
    :param map_list: 현재 게임판 상태
    :return: 사용자가 선택한 칸
    """
    show_board(map_list)
    print("빈칸 중 하나를 선택하세요\n", end=">>> ")
    site = input()
    while site not in map_list:  # 빈칸을 선택하지 않은 경우
        print("빈.칸. 중에서 하나 선택하라고;;;\n", end=">>> ")
        site = input()
    return int(site)


def board_check(map_list):
    """
    게임판에 우승자가 있는지 확인해보자
    :param map_list: 현재 게임판 상태
    :return: 우승자 있는 경우 우승한 문자를 return
    """
    if map_list[1] == map_list[2] and map_list[2] == map_list[3]:
        return map_list[1]
    elif map_list[4] == map_list[5] and map_list[5] == map_list[6]:
        return map_list[4]
    elif map_list[7] == map_list[8] and map_list[8] == map_list[9]:
        return map_list[7]
    elif map_list[1] == map_list[4] and map_list[4] == map_list[7]:
        return map_list[1]
    elif map_list[2] == map_list[5] and map_list[5] == map_list[8]:
        return map_list[2]
    elif map_list[3] == map_list[6] and map_list[6] == map_list[9]:
        return map_list[3]
    elif map_list[1] == map_list[5] and map_list[5] == map_list[9]:
        return map_list[1]
    elif map_list[3] == map_list[5] and map_list[5] == map_list[7]:
        return map_list[3]


def record_score(winner, player, computer):
    """
    사용자의 승/무/패를 기록하자
    :param winner: 승리한 문자(O/X)
    :param player: 사용자의 문자
    :param computer: 컴퓨터의 문자
    """
    if winner == player:
        SCORE[0] += 1
    elif winner == computer:
        SCORE[2] += 1
    else:
        SCORE[1] += 1


def com_choose(map_list, player):
    """
    컴퓨터가 고를 칸을 선택한다.
    :param map_list: 현재 게임판의 상태
    :param player: 사용자의 문자
    :return: 컴퓨터가 선택한 칸의 숫자, 빈칸이 없는 경우 0
    """
    possible_site = []  # 입력 가능한 자리
    for i in [1, 2, 3, 4, 5, 6, 7, 8, 9]:
        if map_list[i] != "O" and map_list[i] != "X":
            possible_site.append(i)
    for i in possible_site:  # 입력 가능한 자리 중에서 사용자를 방어할 수 있는 자리
        fake_map = copy.copy(map_list)
        fake_map[i] = player
        if board_check(fake_map) == player:
            return i
    if len(possible_site) != 0:  # 방어할 필요 없는 경우에는 랜덤
        return random.choice(possible_site)


while True:
    Game_Board = [' ', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    Player = choose_OX()  # 사용자의 문자
    if Player == "X":
        Computer = "O"  # 컴퓨터의 문자
        turn = 0  # 0이면 사용자 차례, 1이면 컴퓨터 차례
    else:
        Computer = "X"
        turn = 1
    time = 9  # 게임을 주고받는 횟수, 0이 되면 게임을 무조건 종료

    while True:
        if turn == 0:  # 사용자 차례
            pick = player_choose(Game_Board)  # 사용자가 선택한 위치
            Game_Board[pick] = Player  # 선택한 위치에 사용자의 문자 입력
            time -= 1
            if board_check(Game_Board) == Player:  # 사용자가 승리한 경우
                record_score(Player, Player, Computer)
                show_board(Game_Board)
                print("승리!!!")
                print("%d승 %d무 %d 패" % (SCORE[0], SCORE[1], SCORE[2]))
                break
            elif time == 0:  # 무승부인 경우
                record_score(' ', Player, Computer)
                show_board(Game_Board)
                print("무승부!!!")
                print("%d승 %d무 %d 패" % (SCORE[0], SCORE[1], SCORE[2]))
                break
            else:
                turn = 1  # 컴퓨터의 차례

        else:
            pick2 = com_choose(Game_Board, Player)  # 컴퓨터가 선택한 위치
            Game_Board[pick2] = Computer  # 선택한 위치에 컴퓨터의 문자 입력
            time -= 1
            if board_check(Game_Board) == Computer:  # 컴퓨터가 승리한 경우
                record_score(Computer, Player, Computer)
                show_board(Game_Board)
                print("패배!!!")
                print("%d승 %d무 %d 패" % (SCORE[0], SCORE[1], SCORE[2]))
                break
            elif time == 0:  # 무승부인 경우
                record_score(' ', Player, Computer)
                show_board(Game_Board)
                print("무승부!!!")
                print("%d승 %d무 %d 패" % (SCORE[0], SCORE[1], SCORE[2]))
                break
            else:
                turn = 0  # 사용자의 차례

    if play_again():  # 게임을 재도전하지 않는 경우
        break

print("Bye~!")
