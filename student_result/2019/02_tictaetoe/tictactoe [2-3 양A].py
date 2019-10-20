"""
틱택토 게임 2019. 09. 25
made by 2309 양현서
"""

import random
import time

MARKER_PLAYER = ''  # 플레이어의 말의 종류를 나타내는 변수
MARKER_COM = ''  # 컴퓨터의 말의 종류를 나타내는 변수
BOARD = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]  # 보드판의 상태, (처음 설명을 위해 자리 번호로 선언.)
TURN_TYPE = 0  # 선공 대상을 나타내는 변수 (0이면 플레이어, 1이면 컴퓨터가 선공.)


def start_notification():
    """
    틱택토 게임을 시작하기 전에 실행되는 함수로서, 플레이어의 요구에 따라 틱택토의 규칙에 대해 설명하는 함수.
    :return: 없음.
    """
    print('=' * 100)
    print("<틱택토 게임>이 시작되었습니다.")
    print("┻┳|\n"
          "┳┻|__∧   ...틱택토?\n"
          "┻┳|•﹃•)\n"
          "┳┻|⊂ﾉ\n"
          "┻┳|Ｊ\n")
    rule = input("<틱택토 게임>의 규칙 설명을 들으시겠습니까? (y/(n)) ")  # 규칙 설명을 들을 것인지 질문 및 대답 입력.

    if rule in ["y", "yes"]:  # y 또는 yes 가 입력될 경우,
        rule_explain()  # 규칙에 대한 설명 제공.

    time.sleep(0.5)
    print('\n' + '-' * 100)
    input("Enter 를 누르면 시작합니다! ")  # Enter 입력 후 게임이 시작되도록 임의의 입력을 받음.


def rule_explain():
    """
    틱택토 게임의 규칙을 출력하는 함수.
    :return: 없음.
    """
    print('\n' + '=' * 100)
    print("|틱택토 게임 규칙|")
    print("틱택토는 우리나라의 오목과 비슷한 게임으로, 쉽게 말하면 3×3 말판에서 이루어지는 삼목 게임입니다.\n"
          "플레이어와 컴퓨터는 3×3 말판에서 O 또는 X 의 게임말을 번갈아가며 놓습니다.\n"
          "먼저 가로 또는 세로 또는 대각선으로 3개 이상의 말을 일직선에 놓은 사람이 승리합니다.\n"
          "말을 놓을 때는 1~9의 번호 중, 놓고 싶은 자리의 번호를 입력하시면 됩니다.")

    time.sleep(1)
    print_board()
    print("\n틱택토 게임의 자리 번호는 이와 같습니다.\n"
          "말의 종류는 랜덤으로 정해집니다.")


def print_board():
    """
    BOARD 배열에 저장되어 있는 현재 보드 상태를 격자에 넣어 출력하는 함수.
    :return: 없음.
    """
    global BOARD

    print("\n┏━━━┯━━━┯━━━┓")
    print("┃ %s │ %s │ %s ┃" % (BOARD[0][0], BOARD[0][1], BOARD[0][2]))
    print("┠───┼───┼───┨")
    print("┃ %s │ %s │ %s ┃" % (BOARD[1][0], BOARD[1][1], BOARD[1][2]))
    print("┠───┼───┼───┨")
    print("┃ %s │ %s │ %s ┃" % (BOARD[2][0], BOARD[2][1], BOARD[2][2]))
    print("┗━━━┷━━━┷━━━┛")


def is_right_input(position):
    """
    플레이어가 입력한 문자열이 옳은 형식인지 여부를 리턴하는 함수.
    입력 문자열이 옳지 않은 형식일 경우, 옳은 입력을 유도하는 문구를 출력.
    :param position: 플레이어가 입력한 문자열.
    :return: 옳은 형식의 입력인 경우 True, 옳지 않은 형식의 입력일 경우 False를 반환.
    """
    natural_num = "123456789"  # 1~9 범위의 자연수로 이루어진 문자열. 입력된 문자가 자연수 문자인지 판단하는 데 이용.

    for i in position:  # 입력된 문자열의 모든 문자에 대해 확인.
        if i not in natural_num:  # 입력된 문자열에 자연수가 아닌 문자가 포함되어 있을 때,
            print("1~9 범위의 정수 이외의 문자는 입력할 수 없습니다.\n")  # 입력 오류 안내.
            return False  # 옳지 않은 입력이므로 False 반환.

    if len(position) != 1:  # 입력된 문자열의 길이가 1이 아닐 때,
        print("1개의 숫자를 입력해주십시오.\n")  # 입력 오류 안내.
        return False  # 옳지 않은 입력이므로 False 반환.

    pos = int(position) - 1  # 자연수로 확인된 문자열을 정수형으로 변환, BOARD 리스트의 인덱스로 변환용이하도록 1 빼기.
    if BOARD[pos // 3][pos % 3] != ' ':  # 입력된 위치에 이미 말이 놓여 있을 때,
        print("이미 말이 놓인 자리는 놓을 수 없습니다.\n")  # 입력 오류 안내.
        return False  # 옳지 않은 입력이므로 False 반환.

    return True  # 위의 모든 경우에 해당하지 않는 경우 옳은 입력이므로 True 반환.


def count_marker(marker, line, idx):
    """
    보드에서 행 또는 열 또는 대각선의 특정 말 개수와 빈칸의 위치를 반환하는 함수.
    :param marker: 개수를 셀 말의 종류를 나타내는 변수.
    :param line: 'row', 'col', 'dia' 중의 하나로, 탐색할 줄의 종류(행 또는 열 또는 대각선)를 나타내는 변수.
    :param idx: 몇 번째 줄(행: 0~2번째, 열: 0~2번째, 대각선 0~1번째)에서 탐색할지 지정하는 변수.
    :return: 주어진 줄에서, 주어진 말의 수와 빈칸의 위치를 dictionary 형태로 반환.
    """
    global BOARD

    info = {'cnt': 0, 'blank_point': [-1, -1]}  # 탐색할 줄에 대한 정보를 선언 및 초기화. 함수의 끝에서 이를 반환.

    if line == "row":  # 탐색할 줄의 종류가 '행'인 경우,
        points = [[idx, i] for i in range(3)]  # 탐색할 점의 좌표 지정.
    elif line == "col":  # 탐색할 줄의 종류가 '열'인 경우,
        points = [[i, idx] for i in range(3)]  # 탐색할 점의 좌표 지정.
    elif line == "dia":  # 탐색할 줄의 종류가 '대각선'인 경우,
        if idx == 0:  # 탐색할 대각선 위의 점들의 x,y 좌표의 차가 일정한 경우,
            points = [[i, i] for i in range(3)]  # 탐색할 점의 좌표 지정.
        elif idx == 1:  # 탐색할 대각선 위의 점들의 x,y 좌표의 합이 일정한 경우,
            points = [[i, 2 - i] for i in range(3)]  # 탐색할 점의 좌표 지정.

    for point in points:  # 주어진 줄 위에 있는 모든 점들에 대하여,
        r = point[0]
        c = point[1]
        if BOARD[r][c] == marker:  # 점에 탐색 목표 말이 올려져 있으면,
            info['cnt'] += 1  # 줄 위의 탐색 목표 말의 개수 정보를 1 증가.
        if BOARD[r][c] == ' ':  # 점에 아무 말도 없으면,
            info.update({'blank_point': [r, c]})  # 줄 위의 빈칸 정보에 좌표 추가.

    return info  # 탐색 정보를 반환.


def put_player():
    """
    플레이어에게 문자열을 입력받아 그에 따른 동작을 하는 함수.
    exit 가 입력되면, False 를 반환함으로써 play_game 함수에 종료 명령을 전달.
    1~9 범위의 자연수가 입력되면, 보드의 그 자리 번호에 플레이어의 말을 놓음.
    :return: exit 가 입력될 경우, 게임의 종료를 의미하는 False 를 반환하고, 그 이외의 경우 True 반환.
    """
    print("당신의 차례입니다. 당신의 말은 '%s' 입니다." % MARKER_PLAYER)

    while True:  # 옳은 형식의 문자열이 입력될 때까지 반복.
        position = input("말을 놓을 위치를 입력하세요: ")

        if position == "exit":  # 만약 exit 가 입력되면, 게임을 중도 종료.
            print('\n' + "=" * 100)
            print("게임을 종료합니다.")
            return False  # False 를 리턴함으로써 게임 종료 명령을 play_game 함수에 전달.

        if is_right_input(position):  # 옳은 형식의 문자열이 입력되면, 반복문 탈출
            break

    pos = int(position) - 1  # 입력 문자열을 정수형으로 변환, BOARD 리스트의 인덱스로 변환용이하도록 1 빼기.

    BOARD[pos // 3][pos % 3] = MARKER_PLAYER  # 입력 자연수가 의미하는 자리 번호에 컴퓨터의 말 배치.

    return True  # exit 가 입력되지 않아 모든 동작을 수행한 경우, True 반환.


def put_com():
    """
    컴퓨터가 말을 놓는 동작을 하는 함수.
    말을 놓음으로써 컴퓨터가 승리할 수 있는 자리가 있으면 그 자리에 말을 놓아 승리.
    컴퓨터가 승리할 수 있는 자리는 없지만, 다음 턴에 플레이어가 말을 놓음으로써 승리할 수 있는 자리가 있으면 그 자리에 말을 놓아 방어.
    컴퓨터와 플레이어 모두 승리할 수 있는 자리가 없으면, 랜덤하게 말을 배치.
    :return: 없음.
    """
    print("컴퓨터의 차례입니다. 컴퓨터가 '%s' 말을 놓겠습니다." % MARKER_COM)
    time.sleep(1.5)

    while True:  # 비어 있는 자리를 찾을 때까지,
        pos = [random.randrange(0, 3), random.randrange(0, 3)]  # 0~2 범위의 난수를 발생시킴으로써 자리를 랜덤하게 선택.
        if BOARD[pos[0]][pos[1]] == ' ':  # 랜덤하게 선택한 자리에 말이 놓여있지 않은 경우,
            break  # 반복문 탈출.

    lose_point = {'marker': MARKER_PLAYER, 'point': []}  # 플레이어가 다음 턴에 말을 놓음으로써 승리할 수 있는 자리에 관한 정보.
    win_point = {'marker': MARKER_COM, 'point': []}  # 컴퓨터가 말을 놓음으로써 승리할 수 있는 자리에 관한 정보.

    lines = {'row': 3, 'col': 3, 'dia': 2}  # 각 종류의 줄이 몇 개씩 있는지 나타내는 사전 자료형 변수.

    for special_point in [lose_point, win_point]:  # 플레이어가 승리할 수 있는 자리와 컴퓨터가 승리할 수 있는 자리를 조사.
        for line in lines:  # 모든 줄의 종류에 대하여,
            for i in range(lines[line]):  # 특정 종류의 모든 줄에 대하여,
                mark_info = count_marker(special_point['marker'], line, i)  # 탐색 줄과 목표 말에 관한 정보 반환 받음.
                if mark_info['cnt'] == 2:  # 탐색한 줄 위에 특정 말이 2개 존재할 때,
                    if mark_info['blank_point'] != [-1, -1]:  # 탐색한 줄 위에 빈칸이 존재하면,
                        special_point['point'].append(mark_info['blank_point'])  # 빈칸의 좌표를 승리 가능 자리에 정보에 추가.
        if len(special_point['point']) > 0:  # 플레이어 또는 컴퓨터가 승리할 수 있는 자리가 존재하면,
            pos = special_point['point'][
                random.randrange(0, len(special_point['point']))]  # 그중 하나를 랜덤으로 선택해 말을 놓을 자리로 지정.

    BOARD[pos[0]][pos[1]] = MARKER_COM  # 지정된 자리에 컴퓨터의 말을 배치.


def is_win(marker):
    """
    특정한 말 3개가 보드 위에 일직선으로 있는지 판단함으로써 승리 여부를 반환하는 함수.
    :param marker: 승리 여부를 조사할 말의 종류를 나타내는 변수.
    :return: marker 말 3개가 보드 위에 일직선으로 있어 승리한 경우 True, 그렇지 않은 경우 False 를 반환.
    """
    lines = {'row': 3, 'col': 3, 'dia': 2}  # 각 종류의 줄이 몇 개씩 있는지 나타내는 사전 자료형 변수.

    for line in lines:  # 모든 줄의 종류에 대하여,
        for i in range(lines[line]):  # 특정 종류의 모든 줄에 대하여,
            mark = count_marker(marker, line, i)  # 줄과 목표 말의 개수에 대한 정보를 반환 받음.
            if mark['cnt'] == 3:  # 탐색한 줄 위의 목표 말의 개수가 3개일 때,
                return True  # 승리를 의미하는 True 반환.

    return False  # 모든 줄에 대해 탐색했음에도 불구하고 위의 조건을 만족하지 않아 반환되지 않은 경우, False 반환.


def win():
    """
    틱택토 게임에서 플레이어가 승리한 경우(컴퓨터가 패배한 경우), 승리 문구를 출력하는 함수.
    :return: 없음.
    """
    global win_count
    win_count += 1  # 승리 횟수 1 증가. 승률 계산에 이용.

    time.sleep(1)
    print('\n' + '-' * 100)
    print("...Λ＿Λ\n"
          "（ㆍωㆍ)つ━☆*。\n"
          "⊂　　 ノ 　　　.승\n"
          "　し-Ｊ　　　°。리 *´¨)\n"
          "　　　　　　..　.· ´¸.·했*´¨) ¸.·*¨)\n"
          "　　　　　　　　　　(¸.·´ (어요!¸.'*\n")
    print("승리하셨습니다!")


def lose():
    """
    틱택토 게임에서 플레이어가 패배한 경우(컴퓨터가 승리한 경우), 패배 문구를 출력하는 함수.
    :return: 없음.
    """
    time.sleep(1)
    print('\n' + '-' * 100)
    print("╭┈┈┈┈╯   ╰┈┈┈╮\n\n"
          " ╰┳┳╯    ╰┳┳╯\n\n"
          "  N 　    N\n\n"
          " ○  　     ○\n"
          "    ╰┈┈╯\n"
          "  O  ╭━━━━━╮　 O\n"
          "     ┈┈┈┈\n"
          "　　o     　　 o\n")
    print("패배하셨습니다...")


def draw():
    """
    틱택토 게임에서 플레이어와 컴퓨터가 비긴 경우, 무승부 문구를 출력하는 함수.
    :return: 없음.
    """
    time.sleep(1)
    print('\n' + '-' * 100)
    print("　　　　　／＞　　フ\n"
          "　　　　　| 　_　 _ l\n"
          "　 　　　／` ミ＿Yノ\n"
          "　　 　 /　　　 　 |\n"
          "　　　 /　 ヽ　　 ﾉ\n"
          "　 　 │　　|　|　|\n"
          "　／￣|　　 |　|　|\n"
          "　| (￣ヽ＿_ヽ_)__)\n"
          "　＼二つ\n")
    print("비기셨습니다.")


def play_game():
    """
    한 판의 게임을 실행하는 함수.
    :return: 없음.
    """
    global MARKER_COM, MARKER_PLAYER, BOARD, TURN_TYPE  # 전역 변수 사용을 위한 선언.

    print('\n' + '=' * 100)

    while True:  # 옳은 형식의 입력이 들어올 때까지 반복.
        marker_type = input("'O'와 'X' 중 어느 말을 사용하시겠습니까? ")  # 플레이어가 사용할 말을 입력받음.
        if marker_type in ['O', 'o']:  # 'O' 또는 'o'가 입력된 경우,
            MARKER_PLAYER = 'O'  # 플레이어의 말을 'O'로 설정.
            MARKER_COM = 'X'  # 컴퓨터의 말을 'X'로 설정.
            break
        if marker_type in ['X', 'x']:  # 'O' 또는 'o'가 입력된 경우,
            MARKER_PLAYER = 'X'  # 플레이어의 말을 'X'로 설정.
            MARKER_COM = 'O'  # 컴퓨터의 말을 'O'로 설정.
            break
        print("O(o)나 X(x) 중 하나를 입력하세요.\n")
    time.sleep(1)

    print('\n' + '-' * 100)
    print("당신의 말은 '%s' 입니다." % MARKER_PLAYER)  # 설정된 말에 대한 안내.

    TURN_TYPE = random.randrange(0, 2)  # 0~1 범위에서 난수를 발생시킴으로써 선공 대상을 랜덤으로 정함.
    time.sleep(1)
    if TURN_TYPE == 0:  # 생성된 난수가 1인 경우, 플레이어를 선공으로 설정함.
        print("당신이 선공입니다!")  # 선공 대상에 대한 안내.
    else:  # 생성된 난수가 0인 경우, 컴퓨터를 선공으로 설정함.
        print("컴퓨터가 선공입니다.")  # # 선공 대상에 대한 안내.

    BOARD = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    time.sleep(1)
    print_board()  # 보드의 자리 번호를 출력.
    BOARD = [[' '] * 3 for i in range(3)]  # 보드 초기화.

    for turn in range(9):  # 플레이어와 컴퓨터를 합해 최대 9회 말을 놓는 동작을 진행.
        time.sleep(0.5)
        print('\n' + '-' * 100)

        if turn % 2 == TURN_TYPE:  # TURN_TYPE 에 따라 플레이어 또는 컴퓨터의 차례임을 판단.
            marker = MARKER_PLAYER
            if not put_player():  # 플레이어의 입력을 받고, 그에 따라 말을 배치. 만약 종료 명령이 들어온 경우(False 가 반환된 경우),
                return  # 함수를 반환시킴으로써 게임 종료.
        else:
            marker = MARKER_COM
            put_com()  # 컴퓨터가 판단하여 말을 배치.

        print_board()  # 보드의 현재 상태를 출력.

        if is_win(marker):  # marker 를 이용하는 대상이 승리한 경우,
            if marker == MARKER_PLAYER:  # 플레이어가 승리한 경우, 승리 문구 출력.
                win()
            else:  # 컴퓨터가 승리한 경우, 패배 문구 출력.
                lose()
            return

    draw()  # 9번 말을 놓는 동작이 이루어진 후에도 승패가 결정되지 않은 경우, 무승부로 판단 후 무승부 문구 출력.


def play_again():
    """
    게임을 다시 플레이할지 물어보고, 플레이어의 대답에 따라 재시작 여부를 반환하는 함수.
    :return: 플레이어가 게임을 다시 플레이 하겠다고 답하면 True, 그렇지 않다면 False 를 반환.
    """
    print('\n' + '-' * 100)
    replay = input("다시 플레이 하시겠습니까? (y/(n)) ")  # 재시작 여부에 대한 대답 입력.

    if replay in ["y", "yes"]:  # y 또는 yes 가 입력된 경우, 플레이어가 재시작을 원한다는 의미의 True 반환.
        return True
    else:  # 그렇지 않은 경우, 플레이어가 재시작을 원하지 않는다는 의미의 False 리턴.
        return False


def print_winning_rate(play_count, win_count):
    print("플레이 횟수 %d회 중, 승리 횟수 %d회로, 당신의 승률은 %.2f%%입니다." % (play_count, win_count, (win_count / play_count) * 100))


start_notification()  # 틱택토 게임에 대한 설명을 제공함으로써 게임의 시작을 알림.

play_count = 0  # 플레이한 횟수를 저장하는 변수.
win_count = 0  # 플레이어가 이긴 횟수를 저장하는 변수.

while True:  # 사용자가 재시작을 원하지 않을 때까지,
    play_count += 1
    play_game()  # 게임을 시작.
    print_winning_rate(play_count, win_count)

    if not play_again():  # 게임이 끝나면 재시작 여부에 관해 질문, 플레이어가 재시작을 원하지 않는다고 답하면 프로그램을 종료.
        print_winning_rate(play_count, win_count)
        break
