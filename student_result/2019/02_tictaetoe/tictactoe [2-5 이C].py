"""
<tic-tac-toe>
1. 사용자가 x 또는 o 선택 -> 제대로 입력 안하면 다시 하도록 함
2. 컴퓨터는 멍청하지 않음
3. 다시 플레이할지 입력받는다
4. 승률을 기록하고 출력
5. 현재 상태, 컴퓨터가 다음 둘 곳 판단, 다시 플레이, 승률 기록은 함수로 작성
"""

import random
import time

winning = 0


def shape_choice():
    """
    사용자와 컴퓨터가 게임을 할 모양을 선택하는 함수
    :return: 사용자와 컴퓨터의 모양
    """

    print('\n말 모양을 골라보자~')

    while True:
        print('x 와 o 중 하나만 선택해!')
        user_shape = input()

        if user_shape == 'x':
            print('네 모양은 이제 x 야!')
            com_shape = 'o'
            break

        elif user_shape == 'o':
            print('네 모양은 이제 o 야!')
            com_shape = 'x'
            break

        else:
            print('제대로', end=' ')

    return user_shape, com_shape


def state_now(user_num, com_num, user_shape, com_shape):
    """
    :param user_num: 사용자가 선택한 번호 리스트
    :param com_num: 컴퓨터가 선택한 번호 리스트
    :param user_shape: 사용자의 번호 모양
    :param com_shape: 컴퓨터의 번호 모양
    :param num: 각 위치의 상태를 나타내는 문자들이 차례로 저장되어 있는 리스트
    :return:
    """
    shape = []  # 출력할 모양 리스트

    # 1~9의 번호가 택해졌다면 택한 사람에 맞는 모양, 선택되지 않았다면 '-' 저장
    for i in range(1, 10):
        if i in user_num:
            shape.append(user_shape)
        elif i in com_num:
            shape.append(com_shape)
        else:
            shape.append('-')

    j = 0
    print('*현재 상태*')
    print('-' * 19)
    for i in shape:
        j = j + 1
        print('|  ', end='')
        print(i, end='')
        print('  ', end='')
        if j % 3 == 0:
            print('|')
            print('-' * 19)

    print('')


def computer_choice(num, com_num, user_num):
    """
    :param num: 남은 번호 리스트
    :param com_num: 지금까지 컴퓨터가 선택한 번호 리스트
    :param user_num: 지금까지 사용자가 선택한 번호 리스트
    :return: 컴퓨터가 총 선택한 번호 리스트
    """

    correct = [[1, 2, 3], [4, 5, 6], [7, 8, 9], [1, 4, 7], [2, 5, 8], [3, 6, 9], [1, 5, 9], [3, 5, 7]]
    set1 = set(user_num)
    set2 = set(com_num)

    # 한줄에 컴퓨터의 말이 두개 이상 있는 경우 승리하도록 하는 코드
    for i in correct:

        set3 = set(i)  # 현재 검사할 correct 안 리스트 원소 집합
        num_set = set(num)

        if len(set2.intersection(set3)) == 2:  # 컴퓨터가 한 줄에 두개를 이미 놓아둔 경우
            # 남은 줄에 놓아야 이길 수 있음
            choice = set3.difference(set2)  # 놓아야 하는 위치. 완성하고자 하는 직선의 집합과의 차집합으로 계산
            if choice.intersection(num_set) == choice:
                temp = choice.pop()
                num.remove(temp)
                com_num.append(temp)
                return num, com_num

            else:
                continue

    # 한줄에 사용자의 말이 두개 있는 경우 패배하지 않기 위한 코드
    for i in correct:
        set3 = set(i)  # 현재 검사할 correct 안 리스트 원소 집합
        num_set = set(num)

        if len(set1.intersection(set3)) == 2:  # 한 줄에 두개를 사용자가 입력해놓은 경우
            # 사용자가 이기지 못하도록 한 줄의 남은 곳에 놓아야 함
            choice = set3.difference(set1)
            if choice.intersection(num_set) == choice:
                temp = choice.pop()
                num.remove(temp)
                com_num.append(temp)
                return num, com_num

            else:
                continue

    # 연속으로 있는 말이 없어 승패가 확정되지 않았을 때 랜덤으로 고르는 코드

    choice = random.choice(num)
    num.remove(choice)
    com_num.append(choice)

    return num, com_num


def user_choice(num, user_num):
    """
    :param num: 남아 있는 칸 번호 리스트
    :param user_num: 지금까지 사용자가 선택한 번호 리스트
    :return: 사용자가 선택하고 난 후, 남은 칸 번호 리스트
    """

    # 사용자에게서 칸 번호를 입력받아 제대로 되었는지 확인
    print('칸 번호를 입력해!')
    while True:
        try:
            choice = int(input())

            li = list(range(10))
            if choice not in li:
                print('번호를 제대로 입력해..')

            else:
                if choice not in num:
                    print('비어있는 칸 번호를 입력해..')

                else:
                    user_num.append(choice)
                    num.remove(choice)
                    break

        except ValueError:
            print('숫자를 입력해..')

    return num, user_num


def game_end(user_num, com_num):
    """.
    사용자 또는 컴퓨터의 일렬의 세 숫자가 완성되었지 판별한다.
    칸이 다 찼는지 확인해 게임이 끝났는지 계속되는지 판별한다.
    :return: True(계속) or False(게임 끝)
    """

    correct = [[1, 2, 3], [4, 5, 6], [7, 8, 9], [1, 4, 7], [2, 5, 8], [3, 6, 9], [1, 5, 9], [3, 5, 7]]
    for i in correct:

        set1 = set(user_num)
        set2 = set(com_num)
        set3 = set(i)
        if len(set1.intersection(set3)) == 3:
            print('우와!!!!! 승리!!!!!')
            global winning
            winning = winning + 1
            print('내가 이긴 횟수 : %d회' % winning)
            return True

        if len(set2.intersection(set3)) == 3:
            print('아쉽지만 패배ㅠㅜㅠㅜㅠㅜ')
            # print('내가 이긴 횟수 : %d회' % winning)
            return True

    if len(user_num) + len(com_num) == 9:
        print('칸이 다 찼어! 비겼네 @^^@')
        return True

    return False


def play_game(game_cnt):
    """
    게임을 진행하는 함수.
    :param game_cnt: 게임을 한 횟수
    :return:
    """
    print('*' * 50)
    print('%d round Tic_tac_toe 게임 시작!!!' % game_cnt)
    print("*" * 50)
    user_shape, com_shape = shape_choice()  # 각자의 말 선택
    print('말을 놓을 칸의 번호는 다음과 같아.')
    print("""
    -------------------
    |  1  |  2  |  3  |
    -------------------
    |  4  |  5  |  6  |
    -------------------
    |  7  |  8  |  9  |
    -------------------
        
    """)
    num = list(range(1, 10))  # 선택할 수 있는 번호 리스트
    com_num = []  # 컴퓨터가 선택한 번호 리스트
    user_num = []  # 사용자가 선택한 번호 리스트

    # 순서를 랜덤으로 결정
    first = random.randrange(1, 3)
    time.sleep(1)
    print('순서는 랜덤이야..! 과연 첫 번째 순서는?')
    time.sleep(1)
    print('...\n...\n...')
    time.sleep(1)

    if first == 1:
        print('아쉽게도 내가 먼저 *^^*')
        while True:
            print('*' * 50)
            print('나 : %s, 컴퓨터 : %s' % (user_shape, com_shape))
            print("computer's turn")
            time.sleep(1)
            num, com_num = computer_choice(num, com_num, user_num)
            state_now(user_num, com_num, user_shape, com_shape)
            if game_end(user_num, com_num):
                break
            print('*' * 50)
            print('나 : %s, 컴퓨터 : %s' % (user_shape, com_shape))
            print("user's turn")
            num, user_num = user_choice(num, user_num)
            state_now(user_num, com_num, user_shape, com_shape)
            if game_end(user_num, com_num):
                break
            # 사용자 또는 컴퓨터가 입력할 때마다 게임이 끝났는지 game_continue 로 검사한다.
    else:
        print('너가 첫 번째야 >ㅡ<')
        while True:
            print('*' * 50)
            print('나 : %s, 컴퓨터 : %s' % (user_shape, com_shape))
            print("user's turn")
            num, user_num = user_choice(num, user_num)
            state_now(user_num, com_num, user_shape, com_shape)
            if game_end(user_num, com_num):
                break
            print('*' * 50)
            print('나 : %s, 컴퓨터 : %s' % (user_shape, com_shape))
            print("computer's turn")
            time.sleep(1)
            num, com_num = computer_choice(num, com_num, user_num)
            state_now(user_num, com_num, user_shape, com_shape)
            if game_end(user_num, com_num):
                break


cnt = 0

while True:
    cnt = cnt + 1
    play_game(cnt)
    print('게임 다시 할거야? (answer yes or no)')
    answer = input()
    if answer == 'no':
        print('전체 %d게임 중 %d번 승리' % (cnt, winning))
        print('승률 : %f' % (winning / cnt))
        print('!!!게임끝!!!')
        time.sleep(2.5)
        break
