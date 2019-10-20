import random

win = 0  # 이긴 횟수
game = 0  # 총 게임 횟수
list = [['1', '2', '3'], ['4', '5', '6'], ['7', '8', '9']]  # 처음 판의 모습


def print_list():
    """
    현재 판 위의 상태를 리스트에서 판 모양으로 바꾸어 출력해줌
    :return: 없음
    """

    print("""
    ┌──┬──┬──┐
    │ %c  │ %c  │ %c  │
    ├──┼──┼──┤
    │ %c  │ %c  │ %c  │
    ├──┼──┼──┤
    │ %c  │ %c  │ %c  │
    └──┴──┴──┘
    """ % (list[0][0], list[0][1], list[0][2], list[1][0], list[1][1], list[1][2], list[2][0], list[2][1],
           list[2][2]))  # 리스트 형태의 판을 실제 판의 모양으로 출력해줌


def explain_rule():
    """
    틱택토 게임에 대해서 규칙을 설명함
    :return: 없음
    """

    print(""" 
    TIC-TAC-TOE는 3X3 판 위에서 서로 번갈아가며 말을 놓아 먼저 가로, 세로, 대각선 중 한 줄을 완성시키면 이기는 게임입니다.
    선공/후공은 랜덤으로 결정되며, 판 위의 번호를 입력하여 어디에 놓을지 결정할 수 있습니다.
    판의 모양은 다음과 같습니다.""")

    print_list()  # 초기 판의 모습을 출력

    print("""    완벽한 인공지능 "B-Siri"는 당신이 이기지 못하도록 노력할 것입니다.
    컴퓨터를 이기고 진정한 승자로 거듭나세요.
    """)


def can_win(com):
    """
    컴퓨터나 플레이어가 놓아서 바로 이길 수 있는 자리가 있는지 확인함
    :param com: 확인하려고 하는 문자
    :return: 만약 그러한 자리가 없다면 -1, 있다면 그 자리의 위치
    """

    isok = -1  # 만약 이길 수 있는 경우가 없다면 -1을 출력하여 알려줌
    for i in range(3):
        if list[i][0] is com and list[i][1] is com and '1' <= list[i][2] <= '9':
            isok = 3 * i + 2
            break
        if list[i][0] is com and list[i][2] is com and '1' <= list[i][1] <= '9':
            isok = 3 * i + 1
            break
        if list[i][1] is com and list[i][2] is com and '1' <= list[i][0] <= '9':
            isok = 3 * i + 0
            break
        if list[0][i] is com and list[1][i] is com and '1' <= list[2][i] <= '9':
            isok = 6 + i
            break
        if list[0][i] is com and list[2][i] is com and '1' <= list[1][i] <= '9':
            isok = 3 + i
            break
        if list[2][i] is com and list[1][i] is com and '1' <= list[0][i] <= '9':
            isok = i
            break
    if list[0][0] is com and list[1][1] is com and '1' <= list[2][2] <= '9':
        return 8
    if list[0][0] is com and list[2][2] is com and '1' <= list[1][1] <= '9':
        return 4
    if list[2][2] is com and list[1][1] is com and '1' <= list[0][0] <= '9':
        return 0
    if list[0][2] is com and list[1][1] is com and '1' <= list[2][0] <= '9':
        return 6
    if list[0][2] is com and list[2][0] is com and '1' <= list[1][1] <= '9':
        return 4
    if list[2][0] is com and list[1][1] is com and '1' <= list[0][2] <= '9':
        return 2
    return isok


def act_com(cnt, com):
    """
    컴퓨터가 어디에 둘지 결정함
    만약 이길 수 있는 자리가 있다면 최우선적으로 두고, 없다면 상대가 다음 차례에 이길 수 있는 자리에 둠
    그것도 없다면 임의의 자리에 둠
    컴퓨터가 행동한 이후 이겼는지 또한 확인하여 줌
    :param cnt: 몇 번째 수인지 표시
    :param com: 컴퓨터가 사용하는 문자
    :return: 컴퓨터가 승리하였는지의 여부
    """

    if com == 'O':
        player = 'X'
    else:
        player = 'O'

    if cnt == 0:  # 컴퓨터가 선공일 시 조금 더 이길 확률이 높은 가장자리에 수를 두도록 함
        tmp_list = [[0, 0], [0, 2], [2, 0], [2, 2]]
        random.shuffle(tmp_list)
        list[tmp_list[0][0]][tmp_list[0][1]] = com

    else:
        x = can_win(com)
        y = can_win(player)

        if x is not -1:  # 컴퓨터가 바로 이길 수 있는 경우가 존재하는지 확인함
            list[x // 3][x % 3] = com
            return True

        elif y is not -1:  # 사용자가 바로 이길 수 있는 경우가 존재하는지 확인하고 방지함
            list[y // 3][y % 3] = com
            return False

        else:  # 위의 두 경우가 존재하지 않을 시 빈 칸에 랜덤으로 둠
            rand_num = random.randint(0, 8)
            while not '1' <= list[rand_num // 3][rand_num % 3] <= '9':
                rand_num = random.randint(0, 8)
            list[rand_num // 3][rand_num % 3] = com
            return False


def if_win(player):
    """
    현재 상태에서 플레이어가 이겼는지 확인해줌
    :param player: 플레이어가 사용하는 문자
    :return:
    """
    win = False  # 일단 졌다고 가정하고 이긴 경우를 확인한다.
    for i in range(3):  # 가로 또는 세로로 이긴 경우
        if list[0][i] is player and list[1][i] is player and list[2][i] is player:
            win = True
            break
        if list[i][0] is player and list[i][1] is player and list[i][2] is player:
            win = True
            break
    if list[0][0] is player and list[1][1] is player and list[2][2] is player:
        win = True
    if list[0][2] is player and list[1][1] is player and list[2][0] is player:
        win = True  # 대각선으로 이기는 경우

    return win


def yesorno():
    """
    사용자에게 y 또는 n의 선택지를 만들었을 때 올바른 입력이 들어올 때까지 처리해줌
    :return: y인지 n인지의 여부
    """

    ok = False
    while True:  # 올바른 입력값이 들어올 때까지
        again = input()
        if again is 'y' or again is 'Y':
            ok = True
            break
        elif again is 'n' or again is 'N':
            break
        else:  # 제대로된 입력이 들어오지 않은 경우
            print("y 또는 n 으로 대답해 주십시오.")
    return ok


def win_per():
    """
    승률을 계산하고 출력해주는 함수
    :return:
    """
    print("""
총 게임 횟수 : %d
이긴 횟수 : %d
승률 : %.2f percent
    """ % (game, win, win / game * 100))


def play_again():
    """
    사용자에게 다시 플레이 할 것인지 물어봄
    :return: 만약 그만한다면, 게임을 종료하도록 한다.
    """

    print("다시 하시겠습니까?(y/n)")

    if yesorno() is False:  # 더 이상 실행하지 않음
        print("게임을 종료합니다.")
        return False
    else:  # 게임을 반복함
        print("""게임을 다시 시작합니다 



                """)
        return True


while True:

    list = [['1', '2', '3'], ['4', '5', '6'], ['7', '8', '9']]
    print("틱택토 게임에 참여하시게 된 것을 환영합니다.")
    print("게임 설명을 들으시겠습니까? (y/n)")

    if yesorno() is True:
        explain_rule()  # y로 대답하면 규칙을 설명해준다.

    print("O와 X 중 사용할 것을 고르세요.")

    while True:  # 올바른 입력값이 들어올 때까지
        again = input()
        if again is 'o' or again is 'O':
            com = 'X'
            player = 'O'
            break
        elif again is 'x' or again is 'X':
            com = 'O'
            player = 'X'
            break
        else:
            print("O 또는 X로 대답해 주십시오.")  # 제대로된 입력이 들어오지 않은 경우

    cnt = 0  # 몇 번째 수인지 판단하는 변수
    order = ['first', 'second']
    random.shuffle(order)

    if order[0] == 'second':  # 랜덤으로 리스트를 섞어 나온 순서를 바탕으로 판단한다.
        print("컴퓨터가 선공입니다.")
        act_com(cnt, com)
        print_list()
        cnt += 1
    else:
        print("당신이 선공입니다.")
        print_list()

    now = 'player'  # 지금 플레이어의 차례임을 의미함
    while cnt < 9:  # 판이 꽉 차기 전까지
        if now == 'player':  # 플레이어의 차례일 경우
            print("어디에 둘지 정하십시오.(1~9)")

            while True:
                where = input()
                if len(where) != 1:  # 한 자리 정수로 입력을 받아야 함
                    print("1에서 9까지의 숫자로 입력해주십시오.")
                    continue
                if not '1' <= where <= '9':
                    print("1에서 9까지의 숫자로 입력해주십시오.")
                    continue
                elif not '1' <= list[(int(where) - 1) // 3][(int(where) - 1) % 3] <= '9':  # 빈 칸인지 확인
                    print("이미 다른 말이 놓여져 있는 칸입니다.")
                    continue
                else:
                    list[(int(where) - 1) // 3][(int(where) - 1) % 3] = player
                    break
            print()
            print("플레이어:")
            print_list()
            player_win = if_win(player)  # 플레이어가 이겼는지 확인함
            if player_win is True:  # 플레이어가 승리한 상황
                win += 1  # 이긴 횟수 증가
                game += 1  # 총 게임 횟수 증가
                print("당신이 이겼습니다!")
                break
            cnt += 1
            now = 'com'  # 다음 차례는 컴퓨터의 차례이므로 바꾸어 줌

        else:
            com_win = act_com(cnt, com)  # 컴퓨터가 수를 놓도록 하고 이겼는지를 리턴해서 받음
            print()
            print("컴퓨터:")
            print_list()
            if com_win is True:  # 컴퓨터가 이긴 경우
                game += 1
                print("컴퓨터가 이겼습니다!")
                break
            cnt += 1
            now = 'player'  # 다음 차례는 플레이어의 차례이므로 바꾸어 줌

    if cnt == 9:  # 판이 가득 찼음을 의미함 즉 비긴 경우
        print("비겼습니다!")
        game += 1

    win_per()  # 승률을 표시

    if play_again() is False:  # 다시 플레이 하지 않는다면 종료
        break
