# 컴퓨터가 순서를 랜덤으로 설정하기 위해 random 을 import 해줍니다
import random
import time

list = ['   ', '   ', '   ', '   ', '   ', '   ', '   ', '   ', '   ', '   ']  # 3X3 판에 적힌 수를 일차원 배열로 나타냅니다
com = 'c'  # 컴퓨터가 사용할 문자를 저장하는 변수입니다
user = 'u'  # 사용자가 사용할 문자를 저장하는 변수입니다
win = 0  # 사용자가 승리한 횟수를 저장하는 변수입니다
lose = 0  # 사용자가 패배한 횟수를 저장하는 변수입니다
tie = 0  # 사용자가 비긴 횟수를 저장하는 변수입니다
count = 0  # 사용자가 경기를 시행한 횟수를 저장하는 변수입니다


def print_list():
    """
    현재 3X3 판의 어느 위치에 어느 문자가 채워져있는지 출력하는 함수입니다
    """

    print("%s | %s | %s\n%s | %s | %s\n%s | %s | %s" % (
    list[1], list[2], list[3], list[4], list[5], list[6], list[7], list[8],
    list[9]))  # 리스트의 인덱스를 1, 2, 3/ 4, 5, 6/ 7, 8, 9로 나누어 출력합니다


def random_order():
    """
    컴퓨터와 사용자 중 누가 먼저 수를 놓을지 순서를 정하는 함수입니다
    """
    ran_list = [0, 1]  # 0과 1로 이루어진 리스트를 생성합니다
    random.shuffle(ran_list)  # ran_list 의 값을 무작위로 섞어줍니다
    if ran_list[0] == 0:
        print("The player goes first")  # ran_list 에서 0이 앞에 오면 사용자가 먼저 수를 놓습니다
    else:
        print("The computer goes first")  # ran_list 에서 1이 앞에 오면 컴퓨터가 먼저 수를 놓습니다
        list[5] = com  # 중앙 5번 위치에 컴퓨터가 수를 놓습니다
        print_list()  # 리스트에 채워진 현황을 출력합니다
    return


def user_right_place(insert):
    """
    사용자가 입력한 자리가 조건을 만족하는지, 수를 놓을 수 있는 자리인지 판별합니다
    """
    if insert == '':  # insert 의 default 값인 공백이 입력되면 false 를 반환합니다
        return False

    for i in insert:
        if not i.isdigit():  # 사용자가 입력한 값 중 하나라도 숫자가 아니라면 false 를 반환합니다
            print("Please insert an integer in range 1 ~ 9")
            return False

    for i in insert:
        if i.isdigit():
            if int(insert) < 1 or int(insert) > 9:  # 사용자가 입력한 값이 자연수가 아니면 false 를 반환합니다
                print("Please insert an integer in range 1 ~ 9")
                return False
        else:
            return False

    if list[int(insert)] != '   ':  # 사용자가 입력한 값에 해당하는 자리가 이미 채워져있다면 다시 선택하라는 말과 함께 false 를 반환합니다
        print("The place '%s'  is already occupied, select again" % insert)
        return False

    return True


def computer_can_win():
    """
    컴퓨터가 승리할 수 있는 수가 있는지 판별하고, 있다면 그 자리를 반환하는 함수입니다
    승리할 수 있는 경우가 존재한다면, 그 자리에 수를 놓습니다
    """

    check = [-1, 0, 0, 0, 0, 0, 0, 0, 0, 0]  # 1 ~ 9 까지의 자리 번호 중 컴퓨터가 채운 번호를 1로, 사용자가 채운 번호를 -10으로 저장하는 리스트입니다
    check_list = [[1, 2, 3], [4, 5, 6], [7, 8, 9], [1, 4, 7], [2, 5, 8], [3, 6, 9], [1, 5, 9],
                  [3, 5, 7]]  # 가로, 세로, 대각선에 해당하는 자리번호를 묶어놓은 리스트입니다

    for i in range(1, 10):
        if list[i] == com:  # 컴퓨터가 채운 자리를 찾아 check 리스트에 1을 저장합니다
            check[i] = 1
        elif list[i] == user:  # 사용자가 채운 자리를 찾아 check 리스트에 -10을 저장합니다
            check[i] = -10

    for i in check_list:
        if check[i[0]] + check[i[1]] + check[i[2]] == 2:  # 가로, 세로, 대각선에 저장되어있는 값의 합이 2인 경우를 탐색합니다
            for j in i:
                if check[j] == 0:  # 세 자리 중 빈 자리를 찾아 반환합니다
                    return j

    return 0  # 컴퓨터가 승리할 수 있는 경우가 없다면 0을 반환합니다


def user_can_win():
    """
    사용자가 승리할 수 있는 수가 있는지 판별하고, 있다면 그 자리를 반환하는 함수입니다
    승리할 수 있는 경우가 존재한다면, 그 자리를 막아줍니다
    """

    check = [-1, 0, 0, 0, 0, 0, 0, 0, 0, 0]  # 1 ~ 9 까지의 자리 번호 중 사용자가 채운 번호를 1로, 컴퓨터가 채운 번호를 -10으로 저장하는 리스트입니다
    check_list = [[1, 2, 3], [4, 5, 6], [7, 8, 9], [1, 4, 7], [2, 5, 8], [3, 6, 9], [1, 5, 9],
                  [3, 5, 7]]  # 가로, 세로, 대각선에 해당하는 자리번호를 묶어놓은 리스트입니다

    for i in range(1, 10):
        if list[i] == user:  # 사용자가 채운 자리를 찾아 check 리스트에 1을 저장합니다
            check[i] = 1
        elif list[i] == com:  # 컴퓨터가 채운 자리를 찾아 check 리스트에 -10을 저장합니다
            check[i] = -10
    for i in check_list:
        if check[i[0]] + check[i[1]] + check[i[2]] == 2:  # 가로, 세로, 대각선에 저장되어있는 값의 합이 2인 경우를 탐색합니다
            for j in i:
                if check[j] == 0:  # 세 자리 중 빈 자리를 찾아 반환합니다
                    return j

    return 0  # 사용자가 승리할 수 있는 경우가 없다면 0을 반환합니다


def com_place():
    """
    컴퓨터가 놓을 수 있는 자리를 판별합니다
    """
    x1 = computer_can_win()  # computer_can_win 의 반환값을 저장하는 변수입니다
    x2 = user_can_win()  # user_can_win 의 반환값을 저장하는 변수입니다
    listi = []  # 컴퓨터가 우선적으로 놓아야 할 수가 없다면 랜덤으로 자리를 설정하기 위한 리스트입니다

    if x1 != 0:  # 컴퓨터가 이길 수 있는 수가 있다면, 그 자리에 해당하는 번호를 반환합니다
        return x1
    elif x2 != 0:  # 사용자가 이길 수 있는 수가 있어 막아야 한다면, 그 자리에 해당하는 번호를 반환합니다
        return x2
    else:
        for i in range(1, 10):  # 우선적으로 놓아야 할 수가 없다면 빈 공간중 랜덤으로 한 자리를 반환합니다
            if list[i] == '   ':  # 아직 채워지지 않은 공간의 번호를 탐색합니다
                listi.append(i)  # 그 번호를 listi 에 저장합니다
        random.shuffle(listi)  # listi 를 랜덤으로 섞습니다
        if len(listi) != 0:
            return listi[0]  # listi 가 비어있지 않다면 listi 에 저장된 값 중 첫번째 값을 반환합니다
    return -1


def check_if_over():
    """
    경기의 종료 여부를 판단하는 함수입니다
    """

    check = [-1, 0, 0, 0, 0, 0, 0, 0, 0, 0]  # 1 ~ 9 까지의 자리 번호 중 사용자가 채운 번호를 10으로, 컴퓨터가 채운 번호를 -10으로 저장하는 리스트입니다
    check_list = [[1, 2, 3], [4, 5, 6], [7, 8, 9], [1, 4, 7], [2, 5, 8], [3, 6, 9], [1, 5, 9],
                  [3, 5, 7]]  # 가로, 세로, 대각선에 해당하는 자리번호를 묶어놓은 리스트입니다

    global win, lose, tie

    for i in range(1, 10):
        global list
        if list[i] == user:  # 사용자가 채운 자리를 찾아 check 리스트에 10을 저장합니다
            check[i] = 10
        elif list[i] == com:  # 컴퓨터가 채운 자리를 찾아 check 리스트에 -10을 저장합니다
            check[i] = -10
    for i in check_list:
        if check[i[0]] + check[i[1]] + check[i[2]] == 30:  # 가로, 세로, 대각선에 저장되어있는 값의 합이 30인 경우를 탐색하여 사용자가 승리하였다고 출력합니다
            print("\nYou won the game")
            list = ['   ', '   ', '   ', '   ', '   ', '   ', '   ', '   ', '   ', '   ']  # list를 초기화 시킵니다
            win += 1  # 승리 횟수에 1을 더하여 저장합니다
            return True
    for i in check_list:
        if check[i[0]] + check[i[1]] + check[i[2]] == -30:  # 가로, 세로, 대각선에 저장되어있는 값의 합이 -30인 경우를 탐색하여 사용자가 패배하였다고 출력합니다
            print("\nComputer won the game")
            list = ['   ', '   ', '   ', '   ', '   ', '   ', '   ', '   ', '   ', '   ']  # list를 초기화 시킵니다
            lose += 1  # 패배 횟수에 1을 더하여 저장합니다
            return True

    cnt = 0  # 위에서 경기가 이미 종료되었는지 판별하는 변수입니다

    for i in range(1, 10):
        if list[i] == '   ':  # 위에서 경기가 이미 종료되어 리스트가 초기화 되었다면 cnt 를 1로 바꾸어줍니다
            cnt = 1
    if cnt == 0:  # 위에서 리스트의 모든 값이 채워져있다면 비겼다고 출력합니다
        print("\nGame tied")
        list = ['   ', '   ', '   ', '   ', '   ', '   ', '   ', '   ', '   ', '   ']  # list를 초기화 시킵니다
        tie += 1
        return True

    return False  # 경기가 끝나지 않았다면 fasle 를 반환합니다


def win_stats():
    """
    사용자의 승률을 출력하는 함수입니다
    """
    a = str((win / count) * 100)  # 승리 횟수를 전체 횟수로 나눈 후 퍼센테이지로 저장한 변수입니다
    print("win stats : %s%%\n" % (a[0:6]))  # 승률을 출력합니다


def play_again():
    """
    사용자가 게임을 다시 플레이할 것인지 의사를 묻는 함수입니다
    """
    return input('\nDo you want to play again? \n(yes / no)\n>').lower().startswith(
        'y')  # y 로 시작하는 yes를 출력하면 게임을 한 번 더 진행합니다


print("=" * 70)
print("Welcome to the TIC-TAC-TOE GAME!")

while True:
    count += 1  # 게임 실행 횟수를 1 증가시킵니다
    print("Choose which marker you will play as\n(O / X)\n>", end=' ')  # 사용자가 사용할 말을 정합니다

    while 1:  # 말을 'O', 'o', 'X', 'x' 이외에는 입력받지 않습니다
        a = input()
        if a == 'O' or a == 'o':
            print("The player will play as 'O' ")
            user = 'O'
            com = 'X'
            break
        elif a == 'X' or a == 'x':
            print("The player will play as 'X' ")
            user = 'X'
            com = 'O'
            break
        else:
            print("Only choose 'O' or 'X'")
    print("=" * 70)
    random_order()  # 랜덤으로 순서를 정합니다
    time.sleep(1)

    while not check_if_over():  # 시도 횟수가 10번을 초과하지 않도록 설정합니다
        place = ''

        # 사용자 입력한 값을 저장하는 변수입니다
        while not user_right_place(place):  # 입력한 값이 1 ~ 9 범위 내의 자연수인지, 비어있는 공간인지 확인합니다
            print('\nWhich place do you want to mark?')
            print('1 | 2 | 3\n4 | 5 | 6\n7 | 8 | 9')
            place = input('>')  # 사용자가 수를 놓을 곳을 입력받습니다

        list[int(place)] = user  # 해당하는 자리에 사용자의 말을 놓습니다
        print_list()  # 현재 3X3 판의 어느 위치에 어느 문자가 채워져있는지 출력합니다
        if check_if_over():  # 게임이 종료되었는지 확인합니다
            break

        print()
        time.sleep(1)

        cp = com_place()  # 컴퓨터가 수를 놓을 수 있는 자리를 탐색하여 저장하는 변수입니다
        list[int(cp)] = com  # 해당하는 자리에 컴포터의 말을 놓습니다
        print_list()  # 현재 3X3 판의 어느 위치에 어느 문자가 채워져있는지 출력합니다
        if check_if_over():  # 게임이 종료되었는지 확인합니다
            break

    if not play_again():
        print("=" * 70)
        print("\nTIC -TAC -TOE  GAME OVER\n")
        print("games played =  %d" % count)  # 총 플레이 횟수를 출력합니다
        time.sleep(1)
        print("games won =  %d" % win)  # 총 승리 횟수를 출력합니다
        time.sleep(1)
        print("games lost =  %d" % lose)  # 총 패배 횟수를 출력합니다
        time.sleep(1)
        print("games tied =  %d" % tie)  # 총 비긴 횟수를 출력합니다
        time.sleep(1)
        win_stats()  # 사용자의 승률을 출력합니다
        print("=" * 70)
        break
