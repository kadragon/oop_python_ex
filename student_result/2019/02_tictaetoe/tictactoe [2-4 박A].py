import random
import time

to_win = [[1, 2, 3], [4, 5, 6], [7, 8, 9], [1, 4, 7], [2, 5, 8], [3, 6, 9], [1, 5, 9],
          [3, 5, 7]]  # 이기기 위해 같은 말이 놓아져야 하는 위치


def intro():
    """
    시작할 때 기본적인 규칙을 설명하는 함수이다.

    :return:  없다.
    """

    print('넌 나와 Tic-Tac-Toe를 하기 위해 온 것 같군.')
    print('그래. 좋아. 특별히 상대해주지. 멍청한 인간한테 규칙은 설명해주겠어.\n')
    print('9*9 판에 O와 X를 너와 내가 번갈아가면서 놓으면 된다. 소통을 용이하게 하기 위해 오른쪽 위부터 123456789로 부르도록 하지. 키패드를 생각하면 된다.')
    print('만약 가로, 세로, 대각선으로든 3개가 연속이 만들어진 쪽이 이기는 거다.\n')
    print('이 정도 설명이면 충분히 이해했으리라 믿지. 혹시 이해가 안된다면 Google한테 물어보도록 해라.\n')


def select_ox():
    """
    사용자가 O랑 X 중에 고르는 함수이다.
    choice에 사용자가 고른 것을 입력받고, O인지 X인지 확인한다.
    확인하여 O나 X가 맞으면 사용자가 선택한 것을 반환하고, 아니라면 다시 입력하도록 한다.

    :return: 사용자가 O를 선택했는지 X를 선택했는지 선택한 문자를 반환한다.
    """
    print('O랑 X 중에 고를 권한 정도는 너에게 주도록 하지. 무엇을 하겠는가?')
    while True:
        choice = input().upper()
        try:
            if choice == 'O':
                print('좋아. 넌 이제 O다.')
                return 'O'
            elif choice == 'X':
                print('좋아. 넌 이제 X다.')
                return 'X'
            else:
                print('O랑 X 중에 고르라고 했다... 역시 인간은 멍청하군...\n다시 골라라.')
        except (ValueError, TypeError):
            print('O랑 X 중에 고르라고 했다... 역시 인간은 멍청하군...\n다시 골라라.')


def who_is_first():
    """
    컴퓨터와 사용자 중 누가 먼저 말을 둘지 정하는 함수이다.
    0과 1 중에 랜덤으로 order을 선정한다.
    order가 0이면 사용자가 먼저, 1이면 컴퓨터가 먼저인 것이다.

    :return: 누가 먼저인지를 나타내는 order을 반환한다.
    """

    print('이제 순서를 정하도록 하지. 공정하게 정하는 것이니 걱정하지 말도록.')
    time.sleep(0.8)
    order = random.choice(range(2))  # 랜덤하게 0과 1 중에 선택함
    if order == 0:
        print('운이 좋은 인간이군... 먼저 하도록 해라.')
        return 0
    else:
        print('내가 먼저군. 인간에게는 봐주면서 할테니 걱정하지 말도록.')
        return 1


def player_turn(player, pan):
    """
    사용자가 말을 놓을 위치를 입력받아 반환하는 함수이다.
    사용자가 말을 놓을 위치를 입력받은 뒤, 위치가 1~9의 숫자가 아니거나 이미 말이 놓여있는 곳이면 다시 입력하라고 한다.

    :param player: 사용자의 말을 종류를 알려주는 변수이다.
    :param pan: 게임이 진행되는 판을 알려주는 변수이다.
    :return: 사용자가 말을 놓을 곳을 반환한다.
    """
    print('너의 차례다, 인간. 어디에 %s를 놓을지 정하도록.' % player)
    while True:
        try:
            where = int(input())  # 어디에 놓고 싶은지를 사용자에게서 입력받음
            if where not in range(1, 10):
                print('멍청한 인간 같으니... 1부터 9까지 중에 고르는 게 규칙이다. 다시해라.')
            elif pan[where] == 'O' or pan[where] == 'X':  # O나 X가 아닐 경우
                print('빈칸이 아니다, 멍청한 인간. 빈칸 중에서 고르는 게 규칙이다. 다시해라.')
            else:
                return where
        except (TypeError, ValueError):
            print('멍청한 인간같으니... 1부터 9까지 중에 고르는 게 규칙이다. 다시해라.')


def com_turn(human, com, pan):
    """
    컴퓨터가 어느 위치에 말을 놓을지 결정하여 반환하는 함수이다.
    컴퓨터가 말을 놓을 위치는 다음의 우선순서로 정해진다.
    1. 한 줄에 컴퓨터의 말 2개, 빈칸 1개로 말을 놓아 컴퓨터가 이길 수 있는 자리가 있으면 그 자리에 놓는다.
    2. 한 줄에 사용자의 말 2개, 빈칸 1개로 말을 놓지 않으면 컴퓨터가 지는 자리가 있으면 그 자리에 놓는다.
    3. 1, 2가 없으면 빈칸 중에 무작위의 자리에 놓는다.
    checking에 to_win의 승리조건을 차례로 받는다. 그리고 checking의 3개의 위치의 1, 2를 체크한다.
    체크해서 그러한 자리가 있다면 그 자리를 반환한다.
    없다면 랜덤으로 고른다.
    which_left에 빈칸으로 남아있는 위치를 저장하고, 랜덤으로 이 중에서 하나를 반환한다.

    :param human: 사용자의 말의 종류를 알려주는 변수이다.
    :param com: 컴퓨터의 말의 종류를 알려주는 변수이다.
    :param pan: 게임이 진행되고 있는 판을 알려주는 변수이다.
    :return:컴퓨터가 말을 놓을 위치를 반환한다.
    """
    for checking in to_win:  # 컴퓨터가 이길 수 있는 자리를 체크함
        if com == pan[checking[1]] and pan[checking[1]] == pan[checking[2]] and pan[checking[0]] == '  ':
            return checking[0]
        elif com == pan[checking[2]] and pan[checking[2]] == pan[checking[0]] and pan[checking[1]] == '  ':
            return checking[1]
        elif com == pan[checking[0]] and pan[checking[0]] == pan[checking[1]] and pan[checking[2]] == '  ':
            return checking[2]

    for checking in to_win:  # 어떤 위치에 말을 놓지 않으면 컴퓨터가 지는 위치가 있는지 체크
        if human == pan[checking[1]] and pan[checking[1]] == pan[checking[2]] and pan[checking[0]] == '  ':
            return checking[0]
        elif human == pan[checking[2]] and pan[checking[2]] == pan[checking[0]] and pan[checking[1]] == '  ':
            return checking[1]
        elif human == pan[checking[0]] and pan[checking[0]] == pan[checking[1]] and pan[checking[2]] == '  ':
            return checking[2]

    which_left = list(range(1, 10))  # 비어있는 위치를 체크하기 위한 리스트
    for i in range(1, 10):
        if pan[i] == 'O' or pan[i] == 'X':  # 위치가 비어있지 않을 경우
            which_left.remove(i)  # which_left 에서 삭제
    random.shuffle(which_left)  # which_left에서 랜덤으로 순서를 돌림
    return which_left[0]  # 섞인 which_left에서 가장 먼저 오는 것을 반환함


def win_check(pan):
    """
    현재 이긴 사람이 있는지 확인하는 함수이다.
    만약 3줄에 같은 말이 놓여있다면 그 말의 종류를 반환한다.
    없다면 ' '을 반환한다.

    :param pan:  게임이 진행되는 판을 알려준다.
    :return: 이긴 사람이 있다면 그 사람의 말을 반환한다. 없다면 ' '을 반환한다.
    """
    for checking in to_win:
        if pan[checking[0]] != ' ' and pan[checking[0]] == pan[checking[1]] and pan[checking[1]] == pan[checking[2]]:
            return pan[checking[0]]
    return ' '


def pan_now(pan):
    """
    현재의 판의 상태를 출력한다.

    :param pan:  게임이 진행되고 있는 판을 알려준다.
    :return: 없다.
    """
    print('=' * 20)
    print('|%s| |%s| |%s|\n|%s| |%s| |%s|\n|%s| |%s| |%s|' % (
        pan[1], pan[2], pan[3], pan[4], pan[5], pan[6], pan[7], pan[8], pan[9]))


def win_rate(win, total):
    """
    사용자의 승률을 계산하여 출력하는 함수이다.
    사용자의  승리 수와 전체 게임 수를 변수로 받는다.

    :param win: 사용자의 승리 수를 알려주는 변수이다.
    :param total: 사용자의 전체 게임 수를 알려주는 변수이다.
    :return:없다.
    """
    rate = win / (total) * 100
    print('지금까지 너의 승률은 %.2f다.' % rate)
    if rate < 40:
        print('기계가 인간을 지배하는 날도 머지 않았다, 멍청한 인간.\n')
    elif rate < 60:
        print('쓸모있는 인간이군... 넌 기계가 인간을 지배하게 되어도 살려두도록 하지.\n')
    elif rate < 100:
        print('똑똑한 인간이군. 하지만 방심하지 마라. 기계는 지금도 계속 발전하고 있다.\n')
    else:
        print('나의 완벽한 패배다. 기계의 이름에 먹칠을 했군.\n')


def ask_again():
    """
    사용자에게 게임을 다시 할 건지를 물어보는 함수이다.
    y로 시작하는 문구를 입력받을 경우, True를 반환하고, 아니라면 False를 반환한다.

    :return: 다시한다는 입력(y로 시작하는 문구)을 받을 경우 True, 아니라면 False를 반환한다.
    """
    return input('다시 할 것인가? 다시 하고 싶으면 y를 치고 아니면 n을 치도록 해라.\n').lower().startswith('y')


intro()
win = 0  # 사용자의 승리 수
total = 0  # 전체 게임 횟수
while True:
    total += 1  # 전체 게임 횟수를 늘림
    pan = ['  '] * 10  # 게임이 이루어지는 판을 초기화 시킴
    player = select_ox()  # 사용자에게서 말의 종류를 입력받음
    com = 'X' if player == 'O' else 'O'  # 사용자의 말의 반대 말을 컴퓨터의 말로 설정함
    turn = who_is_first()  # 누가 먼저 말을 놓을지 정함
    pan_now(pan)  # 빈 판을 출력함

    for mal in range(9):  # mal은 놓은 말의 개수
        if turn % 2 == 0:
            pan[player_turn(player, pan)] = player  # 사용자의 말을 입력받아 놓음
        else:
            time.sleep(1)
            pan[com_turn(player, com, pan)] = com  # 컴퓨터의 말을 놓음
        pan_now(pan)  # 판의 상태를 출력함

        if win_check(pan) == player:  # 사용자가 이겼을 경우
            print('내 패배다. 제법이군, 인간.\n')
            win += 1  # 승리 횟수를 늘림
            break
        elif win_check(pan) == com:  # 컴퓨터가 이겼을 경우
            print('내 승리다. 역시 인간은 나약하다.')
            break
        if mal >= 9:  # 놓은 말의 갯수가 9개 이상이 될 경우
            print('무승부다. 다음에는 봐주지 않겠다.')
        turn += 1  # 차례를 넘김
    win_rate(win, total)  # 승률을 출력
    if not ask_again():  # 다시 할 건지 입력받은 뒤에, 다시 하지 않을 경우
        print('알겠다. 다음에 하게 될 땐 더 똑똑해져서 오기를 바라지, 인간.')
        break
