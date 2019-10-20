import time
import random

status = [' ', ' ', ' ',
          ' ', ' ', ' ',
          ' ', ' ', ' ']
# status 는 틱택토 플레이 판이다. 처음에는 모든 칸이 비어 있는 상태이다.

line = ['012', '345', '678', '036', '147', '258', '048', '246']
# 한 줄에 해당되는 index 들을 적어놓은 것이다.
# 이해를 돕기 위한 주석:
#  0 1 2  |  . . .  |  . . .  |  0 . .  |  . 1 .  |  . . 2  |  0 . .  |  . . 2
#  . . .  |  3 4 5  |  . . .  |  3 . .  |  . 4 .  |  . . 5  |  . 4 .  |  . 4 .
#  . . .  |  . . .  |  6 7 8  |  6 . .  |  . 7 .  |  . . 8  |  . . 8  |  6 . .

status_checked = [False, False, False,
                  False, False, False,
                  False, False, False]
# 판에 O 또는 X의 말이 표시되어 있는지 체크한 list 이다. 처음에는 모두 False 로 초기화되어있다.

entire_game = True  # 전체 게임을 플레이할 것인지 여부. 이후 want_replay 함수에 의해 True 혹은 False 로 바뀐다.
game_finished = False  # 현재 게임이 끝났는지 아닌지 여부. 누군가 승리했거나 비겼으면 True 로 바뀐다.
player = ' '  # 플레이어의 말. 'O' 또는 'X'가 된다.
computer = ' '  # 컴퓨터의 말. 'O' 또는 'X'가 된다.
player_win = 0  # 플레이어의 승리 회수
computer_win = 0  # 컴퓨터의 승리 회수


# 함수 선언
def reset_setup():  # 게임 시작 시 설정을 초기화하는 함수.
    global status, status_checked, game_finished, player, computer
    # 게임 판, 게임 체크 판, 게임 종료 여부, 플레이어의 말, 컴퓨터의 말을 전역변수로 하여 초기화한다.
    # 초기화 값은 위에서 설명한 것과 같다.
    status = [' ', ' ', ' ',
              ' ', ' ', ' ',
              ' ', ' ', ' ']
    status_checked = [False, False, False,
                      False, False, False,
                      False, False, False]
    game_finished = False
    player = ' '
    computer = ' '


def print_status():  # 게임 판을 출력하는 함수이다.
    print("                   -------------")
    print("                   | %s | %s | %s |" % (status[0], status[1], status[2]))
    print("                   -------------")
    print("                   | %s | %s | %s |" % (status[3], status[4], status[5]))
    print("                   -------------")
    print("                   | %s | %s | %s |" % (status[6], status[7], status[8]))
    print("                   -------------")


def check_input(input_str):  # 플레이어의 입력을 확인하는 함수이다. 잘못된 입력의 경우 False 를 반환한다.
    try:
        int(input_str)  # 플레이어가 입력한 문자열이 정수가 아니면 오류가 발생한다.
        if int(input_str) not in range(1, 10):  # 플레이어가 입력한 수가 범위를 벗어나는 경우
            print("1부터 9 사이의 정수를 입력해 주세요.")
            return False
        elif status_checked[int(input_str) - 1]:  # 플레이어가 선택한 칸에 이미 말이 놓여 있는 경우
            print("이미 차 있는 칸입니다. 다른 위치를 선택해주세요.")
        else:
            global player
            status_checked[int(input_str) - 1] = True  # 플레이어가 선택한 칸에 '선택되었음' 이라고 표시한다.
            status[int(input_str) - 1] = player.upper()  # 해당 칸을 공란(' ')에서 플레이어의 말 (O 또는 X) 로 변경한다.
            return True  # 제대로 된 입력이었으므로 True 를 반환한다.
    except ValueError:
        print("올바른 입력을 해 주세요.")
        return False


def check_winner():
    # 승리한 사람이 있는지, 아님 비겼는지 (승리/비긴 경우 True 반환)
    # 아님 아직 게임이 안 끝났는지 (안 끝난 경우 False 반환) 확인하는 함수이다.
    global player, computer, player_win, computer_win
    for i in line:  # 8개의 줄을 확인한다.
        string = ''
        for j in range(3):
            string += str(status[int(i[j])])  # 그 줄에 채워진 말을 일렬로 나열
        if (string == "XXX") | (string == 'OOO'):  # 한 줄이 같은 말 3개로 채워진 경우
            winner = string[0]  # 그 말을 winner 에 저장
    try:
        if winner == player.upper():  # 플레이어의 말이 한 줄에 3개인 경우
            player_win += 1  # 플레이어의 승리 회수 1 증가
            print("당신이 이겼습니다! 축하합니다!")
            return True
        else:  # 컴퓨터의 말이 한 줄에 3개인 경우
            computer_win += 1  # 컴퓨터 승리 회수 1 증가
            print("컴퓨터가 이겼습니다.")
            return True
    except UnboundLocalError:  # 승리자가 없는 경우 winner 이 없어서 if 문에서 error 발생
        for i in status:
            if i not in "XO":  # 칸에 빈칸이 있는 경우
                return False  # 게임이 안 끝났으므로 False 반환
        print("비겼습니다.")  # 칸에 빈칸이 없으므로 비긴 게임임
        return True


def player_turn():  # 플레이어의 차례에 작동하는 함수이다.
    print("당신의 차례입니다.")
    right_input = False
    while not right_input:  # 올바른 입력이 주어질 때까지 while 문이 실행된다.
        print("다음 위치를 선택해 주세요: (1 ~ 9)", end=' ')
        player_input = input()
        right_input = check_input(player_input)
    print_status()  # (칸은 check_input 함수가 채웠으므로) 현재 게임판을 출력한다.


def cpu_turn():  # 컴퓨터 차례에 작동하는 함수이다.
    print("컴퓨터 선택중 ... ")
    global computer
    time.sleep(1)  # 컴퓨터의 차례라는 효과를 주기 위해 1초 휴식을 줌
    if two_selected():  # two_selected 함수가 True 를 반환한 경우, 그 함수가 칸을 채웠으므로 게임판을 출력하고 턴을 마친다.
        print_status()
    else:
        # 0~8 중 임의의 수를 선택해, 그 수에 해당하는 칸이 비어 있으면 컴퓨터의 말을 놓은 뒤, 게임판을 출력한다..
        cpu_select = list(range(9))
        random.shuffle(cpu_select)
        for i in cpu_select:
            if status[i] not in "XO":
                status[i] = computer
                status_checked[i] = True
                print_status()
                return


def two_selected():  # 한 줄에 2개가 선택되어 있고, 나머지 칸이 비어있는 경우를 체크하는 함수이다.
    global player, computer
    need_to_place = 10
    for i in line:
        # 각 if 문에서, 한 줄에 2개가 선택되어 있고 나머지 칸이 비어있는지 여부를 확인한다.
        # 컴퓨터의 말이 2칸을 채우고 있는 경우, 즉시 나머지 칸을 채우고 True 를 반환하며 종료한다.
        # 플레이어의 말이 2칸을 채우고 있는 경우, 이후에 나머지 칸을 채울 수 있도록 need_to_place 를 갱신해 둔다.
        # 플레이어의 경우를 나중에 채우는 이유: 컴퓨터가 바로 승리할 수 있는 경우(컴퓨터가 2칸 차지)를 먼저 처리하기 위해서.
        if (status[int(i[1])] == status[int(i[2])]) & (status[int(i[0])] not in "XO"):
            if status[int(i[1])] == computer:
                status[int(i[0])] = computer
                status_checked[int(i[0])] = True
                return True
            elif status[int(i[1])] == player.upper():
                need_to_place = int(i[0])
        elif (status[int(i[0])] == status[int(i[2])]) & (status[int(i[1])] not in "XO"):
            if status[int(i[0])] == computer:
                status[int(i[1])] = computer
                status_checked[int(i[1])] = True
                return True
            elif status[int(i[0])] == player.upper():
                need_to_place = int(i[1])
        elif (status[int(i[0])] == status[int(i[1])]) & (status[int(i[2])] not in "XO"):
            if status[int(i[0])] == computer:
                status[int(i[2])] = computer
                status_checked[int(i[2])] = True
                return True
            elif status[int(i[0])] == player.upper():
                need_to_place = int(i[2])
    if need_to_place in range(9):  # 플레이어가 2칸을 차지하고 있는 경우
        status[need_to_place] = computer  # 나머지 칸을 채우고, True 를 반환한다.
        status_checked[need_to_place] = True
        return True
    else:  # 플레이어도, 컴퓨터도 2칸을 차지하고 있지 않은 경우이다. 즉, 다음 턴에 바로 게임이 안 끝나는 경우.
        return False  # 이후 cpu_turn 함수에서 랜덤으로 칸을 채우게 된다.


def want_replay():  # 게임 재시작 여부를 확인하는 함수이다.
    while True:
        print("다시 플레이하시겠습니까? (Y/N)", end=' ')
        reply = input()
        if reply.upper() == 'Y':  # 새로운 게임 시작
            reset_setup()
            print('=' * 60)
            print("게임 재시작 중...")
            print('=' * 60)
            time.sleep(1)
            return True
        elif reply.upper() == 'N':  # 게임 종료
            print("안녕히 가세요!", end='')
            return False
        else:  # 다시 질문한다.
            print("'Y' 또는 'N'으로 대답해주세요.")


def win_rate():  # 승률을 출력하는 함수. 소수점 아래 첫째 자리까지만 출력한다.
    global entire_game, player_win, computer_win
    print("현재 스코어는 플레이어 %d : 컴퓨터 %d 입니다." % (player_win, computer_win))
    try:
        print("현재 승률은 " + str(round(100 * player_win / (player_win + computer_win), 1)) + "%입니다.")
    except ZeroDivisionError:
        # 플레이어와 컴퓨터 모두 이긴 적이 없는 경우, 승률 계산식에서 0으로 나누는 오류가 발생한다.
        # 이 경우 그냥 승률은 0.0% 라고 출력한다. (어쨌거나 아직 플레이어가 이기지는 않았으니...)
        print("현재 승률은 0.0% 입니다.")


def player_first():  # 선공을 결정하는 함수
    return_value = [True, False]  # True 와 False 로 이루어진 list 를 섞는다.
    random.shuffle(return_value)
    return return_value[0]  # 섞었을 때 True 가 앞에 있었으면 True 가, False 가 앞에 있었으면 False 가 반환된다.


# 게임 플레이
print("즐거운 틱택토 게임!")
print("각 칸은 다음과 같습니다.")
print("                   -------------")
print("                   | 1 | 2 | 3 |")
print("                   -------------")
print("                   | 4 | 5 | 6 |")
print("                   -------------")
print("                   | 7 | 8 | 9 |")
print("                   -------------")

while entire_game:
    while (player.upper() != 'X') & (player.upper() != 'O'):
        print("X, O 중 하나를 선택하세요:", end=' ')
        player = input()
        if (player.upper() != 'X') & (player.upper() != 'O'):
            print("올바른 입력을 해 주세요.")
    if player.upper() == 'X':
        computer = 'O'  # 플레이어의 말이 X 니까 컴퓨터의 말은 O
    else:
        computer = 'X'  # 플레이어의 말이 O 니까 컴퓨터의 말은 X
    print("게임을 시작합니다!")
    if player_first():
        print("당신이 선공입니다.")
        print_status()
        # 게임이 끝났는지 아닌지 턴이 끝날 때마다 확인한다.
        while not game_finished:
            player_turn()
            game_finished = check_winner()
            if not game_finished:
                cpu_turn()
                game_finished = check_winner()
    else:
        print("컴퓨터가 선공입니다.")
        print_status()
        # 마찬가지로, 턴이 끝날 때마다 게임이 끝났는지 아닌지 확인한다.
        while not game_finished:
            cpu_turn()
            game_finished = check_winner()
            if not game_finished:
                player_turn()
                game_finished = check_winner()
    win_rate()  # 게임이 종료되었으므로 승률을 출력한다.
    entire_game = want_replay()  # 다시 플레이할지 확인하고, 이에 따라 entire_game 의 값을 갱신한다.
