import random


def get_user():  # 사용자가 선공할지 후공할지 입력한 값이 올바른지 판단하고 반환
    print('Choose x/o (x:선공, o:후공): ', end='')
    get = input()

    if get == 'o':
        return 'o'
    elif get == 'x':
        return 'x'
    else:
        return get_user()


def user_play(user_mark):  # 사용자가 입력한 위치에 사용자 마크를 표시
    print("위치를 입력하세요 >> ", end='')

    full = loc = 0
    while full != 1:
        loc = int(get_loc())
        if chk[loc - 1] == 0:
            full = 1
    chk[loc - 1] = 1  # 사용자가 놓은 곳에 1을 표시

    print_board(loc - 1, user_mark)


def com_play(com_mark):  # 컴퓨터가 질 수 있는 위치를 판단하고 그 위치에 마크를 표시
    import time

    print("컴퓨터 공격...")
    time.sleep(1)

    full = loc = 0

    for i in range(9):  # 다음 차례에 사용자가 놓았을 때 게임이 끝나는 위치를 찾는다
        if chk[i] == 0:
            chk[i] = 1
            if game_over() == 1:
                loc = i
                full = 1
                break
            chk[i] = 0

    while full != 1:
        loc = random.choice(range(9))
        if chk[loc] == 0:
            full = 1

    chk[loc] = 2  # 컴퓨터가 놓은 곳에 2를 표시

    print_board(loc, com_mark)


def print_board(loc, mark):  # 현재 보드 상황 출력
    global a

    a = a[:loc] + mark + a[loc + 1:]

    print("-----------")
    for i in range(3):
        print(" %s | %s | %s " % (a[3 * i], a[3 * i + 1], a[3 * i + 2]))
        print("-----------")


def get_loc():  # 사용자가 입력한 위치가 올바른 값인지 판단하고 반환
    while 1:
        num = input()
        try:
            int(num)
        except ValueError:
            print("1~9 중 하나를 입력해주세요 >> ", end='')
            continue

        if len(num) != 1:
            print("1~9 중 하나를 입력해주세요 >> ", end='')
        else:
            if chk[int(num) - 1] != 0:
                print("놓을 수 없는 자리입니다..")
                return get_loc()
            else:
                return num


def game_over():  # 각 줄을 확인하여 승부가 결정됬을 때 승리한 대상을 반환
    win = 0
    for i in range(3):
        if chk[3 * i] == chk[3 * i + 1] == chk[3 * i + 2] != 0:
            win = chk[3 * i]
        elif chk[i] == chk[i + 3] == chk[i + 6] != 0:
            win = chk[i]
    if chk[0] == chk[4] == chk[8] != 0:
        win = chk[4]
    elif chk[2] == chk[4] == chk[6] != 0:
        win = chk[4]

    return win  # 사용자가 이겼다면 1, 컴퓨터는 2, 승부가 결정되지 않았을 때는 0을 반환


def reset():  # 게임을 다시 시작하기 위해 초기화
    global chk, a

    a = "123456789"
    chk = [0] * 9


def play_again():  # 게임을 다시할지 여부 조사
    print('다시 할래요? 다시 하려면 y / 끝내려면 n : ', end=' ')
    answer = input()
    if answer == 'y':
        reset()
        return 1
    elif answer == 'n':
        return 0
    else:
        return play_again()


def winning_rate():  # 승률을 계산하여 반환
    return win_count / total_count


a = "123456789"
chk = [0] * 9
win_count = total_count = 0

while 1:
    user = get_user()
    time = winner = 0

    if user == 'o':
        com = 'x'
        com_play(com)
        time += 1
    else:
        com = 'o'
        print_board(9, '0')

    while 1:
        user_play(user)
        time += 1

        if time == 9:
            break
        winner = game_over()
        if winner != 0:
            break

        com_play(com)
        time += 1

        if time == 9:
            break
        winner = game_over()
        if winner != 0:
            break

    # 승자 파악
    if winner == 0:
        print("ㅡ무승부ㅡ")
    elif winner == 1:
        win_count += 1
        print("W 승리 W")
    else:
        print("L 패배 L")

    total_count += 1

    print("승리:%d / 전체:%d >> 현재 승률: %.2f %%\n" % (win_count, total_count, winning_rate() * 100))

    if not play_again():
        break
    else:
        print()
