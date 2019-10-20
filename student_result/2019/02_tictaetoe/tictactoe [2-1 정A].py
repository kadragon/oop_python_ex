"""
user_input : 유저가 자신의 캐릭터를 옳게 선택하도록 한다
print_screen : 화면의 현재 상태를 출력
computer : 컴퓨터가 다음 둘 곳을 판단
user : 유저가 둘 곳을 받음
play_again : 게임을 다시 플레이할 지 결정
match_number : 승률을 기록
user_win : 유저가 승리했는지를 리턴
"""
import random  # 선공, 후공을 랜덤으로 뽑기 위해서
from time import sleep  # 컴퓨터가 놓을 때 쉬어주기 위해서
import copy  # deepcopy 를 활용하기 위해서

win = 0
same = 0
lose = 0


def user_choose():
    """
    유저가 자신의 캐릭터를 잘 선택하도록 돕는다
    :return: 유저의 캐릭터 O 또는 X string
    """
    while True:
        print("캐릭터 선택 O = 1, X= 2를 입력하시오 : ")
        a = input()
        if a != '1' and a != '2':
            print("1, 2 중 하나의 숫자로 다시 입력해 주세요")
        elif a == '1':
            return 'O'
        else:
            return 'X'


def print_screen(screen):
    """
    화면의 현재 상태를 출력하는 기능
    :param screen: 현재 상태를 0:빈공간, 1:O, 2:X 로 저장해 놓은 리스트
    :return: none
    """
    a = copy.deepcopy(screen)
    print("-" * 15)
    for i in range(0, 3):
        for j in range(0, 3):
            num = i * 3 + j
            if a[num] == 0:
                a[num] = ' '
            elif a[num] == 1:
                a[num] = 'O'
            else:
                a[num] = 'X'
            print(' |' + a[i * 3 + j] + '|', end=' ')
        print(' ')
        print('-' * 15)
    return


def computer(cha_com, cha_usr, screen):
    """

    :param cha_com: 컴퓨터의 캐릭터
    :param cha-usr: 유저의 캐릭터
    :param screen: 기존의 screen 상태
    :return: [새로 넣을 칸. 컴퓨터 승리 여부]
    """
    # 1. 컴퓨터가 승리할 곳이 있는가
    # 가로, 세로줄 세기
    for i in range(0, 3):
        raw_cnt = 0  # 가로 줄 카운트
        col_cnt = 0  # 세로 줄 카운트
        for j in range(0, 3):
            if cha_com == screen[3 * i + j]:
                raw_cnt += 1
            if cha_com == screen[3 * j + i]:
                col_cnt += 1
        if raw_cnt == 2:
            for j in range(0, 3):
                if screen[3 * i + j] == 0:
                    return [3 * i + j, True]
        if col_cnt == 2:
            for j in range(0, 3):
                if screen[3 * j + i] == 0:
                    return [3 * j + i, True]
    # 대각선 세기
    r_cnt = 0
    l_cnt = 0
    for i in range(0, 3):
        if screen[4 * i] == cha_com:
            r_cnt += 1
        if screen[2 * i + 2] == cha_com:
            l_cnt += 1
    if r_cnt == 2:
        for i in [0, 4, 8]:
            if screen[i] == 0:
                return [i, True]
    if l_cnt == 2:
        for i in [2, 4, 6]:
            if screen[i] == 0:
                return [i, True]

    # 2. 유저가 승리할 곳이 있는가
    # 가로, 세로줄 세기
    for i in range(0, 3):
        raw_cnt = 0  # 가로 줄 카운트
        col_cnt = 0  # 세로 줄 카운트
        for j in range(0, 3):
            if cha_usr == screen[3 * i + j]:
                raw_cnt += 1
            if cha_usr == screen[3 * j + i]:
                col_cnt += 1
        if raw_cnt == 2:
            for j in range(0, 3):
                if screen[3 * i + j] == 0:
                    return [3 * i + j, False]
        if col_cnt == 2:
            for j in range(0, 3):
                if screen[3 * j + i] == 0:
                    return [3 * j + i, False]
    # 대각선 세기
    r_cnt = 0
    l_cnt = 0
    for i in range(0, 3):
        if screen[4 * i] == cha_usr:
            r_cnt += 1
        if screen[2 * i + 2] == cha_usr:
            l_cnt += 1
    if r_cnt == 2:
        for i in [0, 4, 8]:
            if screen[i] == 0:
                return [i, False]
    if l_cnt == 2:
        for i in [2, 4, 6]:
            if screen[i] == 0:
                return [i, False]

    # 3. 빈 공간 랜덤으로 채워주기
    space = []
    for i in range(0, 9):
        if screen[i] == 0:
            space.append(i)
    random.shuffle(space)
    return [space[0], False]


def user(screen):
    """
    유저가 둘 곳을 받음
    :param screen: 기존의 screen 상태
    :return: 유저가 말을 놓을 인덱스
    """
    ok = []

    for i in range(0, 9):
        if screen[i] == 0:
            ok.append(i)
    print("당신의 차례입니다. 말을 놓고 싶은 칸을 입력하시오.")
    while True:
        print("왼쪽 위부터 오른쪽, 아래로 내려가면서 1~9를 뜻합니다.")
        want = input()
        if want not in ['1', '2', '3', '4', '5', '6', '7', '8', '9']:
            print("입력 형식이 잘못되었습니다! 다시 입력하세요.")
        elif int(want) - 1 not in ok:
            print("이미 말이 놓여 있는 곳입니다! 다시 입력하세요.")
        else:
            break
    return int(want) - 1


def play_again():
    """
    유저가 게임을 다시 시작할지 결정
    :return: 재시작 여부를 True 혹은 False 로 리턴
    """
    command = str(input("다시 시작하려면 re를 입력하세요. 끝내려면 아무 키나 눌러주세요."))
    if command == "re":
        print("=" * 80)
        return True
    return False


def match_number():
    print('=' * 20)
    print("@@@승률@@@ = ", win / (win + same + lose))
    print("승리 : ", win)
    print("비김 : ", same)
    print("짐 : ", lose)
    print('=' * 20)
    return


def user_win(cha, screen):
    """
    유저가 이겼는지를 판단하고
    유저가 이기지 않았다면 False
    유저가 이겼다면 True 를 리턴
    :param cha: 유저의 캐릭터
    :param screen: 현재 상태를 저장해 놓은 리스트
    :return: 게임의 끝남 여부를 True 혹은 False 로 리턴
    """
    for i in range(0, 3):
        raw_cnt = 0  # 가로 줄 카운트
        col_cnt = 0  # 세로 줄 카운트
        for j in range(0, 3):
            if cha == screen[3 * i + j]:
                raw_cnt += 1
            if cha == screen[3 * j + i]:
                col_cnt += 1
        if raw_cnt == 3:
            return True
        if col_cnt == 3:
            return True
    # 대각선 세기
    r_cnt = 0
    l_cnt = 0
    for i in range(0, 3):
        if screen[4 * i] == cha:
            r_cnt += 1
        if screen[2 * i + 2] == cha:
            l_cnt += 1
    if r_cnt == 3:
        return True
    if l_cnt == 3:
        return True
    return False


print("Tic Tac Toe 게임을 시작합니다")
print("사용자는 O 혹은 X 중 자신의 캐릭터를 선택할 수 있습니다")
user_character = user_choose()
if user_character == 'O':
    user_character = 1
    com_character = 2
else:
    user_character = 2
    com_character = 1

while True:
    Game = [0] * 9
    print("선공 후공이 랜덤으로 정해집니다")
    print("...선택중...")
    sleep(0.5)
    sleep(1)
    if random.randint(1, 2) == 1:
        print("당신은 선공입니다!")
        sleep(1)
        print_screen(Game)
        Game[user(Game)] = user_character  # user's turn
        print_screen(Game)
    else:
        print("당신은 후공입니다!")
    while True:
        sleep(1)
        x = computer(com_character, user_character, Game)  # computer's turn
        Game[x[0]] = com_character
        print_screen(Game)
        if x[1]:  # computer win
            lose += 1
            match_number()
            break
        if 0 not in Game:  # same
            same += 1
            match_number()
            break
        Game[user(Game)] = user_character  # user's turn
        print_screen(Game)
        if user_win(user_character, Game):
            win += 1
            match_number()
            break
        if 0 not in Game:  # same
            same += 1
            match_number()
            break
    if not play_again():
        break
