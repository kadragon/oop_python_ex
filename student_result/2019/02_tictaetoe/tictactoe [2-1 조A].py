import random


def print_board(data):
    print("-------------")
    print(" %c : %c : %c " % (data[0], data[1], data[2]))
    print(" %c : %c : %c " % (data[3], data[4], data[5]))
    print(" %c : %c : %c " % (data[6], data[7], data[8]))
    print("-------------")


def choose_pattern():
    side = input("패턴 입력[X/O]")
    while side != 'X' and side != 'O':
        print('wrong input')
        side = input("패턴 입력[X/O]")
    if side is 'X':
        n_side = 'O'
    else:
        n_side = 'X'
    return [side] + [n_side]


def restart():
    again = input('replay? [Y/N]')
    if again is 'N':
        return 1
    else:
        return 0


def result(win, lose, draw):
    print("Win:%d   Lose:%d   Draw:%d   Ratio: %2d %%" % (win, lose, draw, 100 * win / (win + lose + draw)))


def valid(n):
    if len(n) != 1 or (ord(n) < ord('1') or ord(n) > ord('9')):
        return 1


def repeated(n, stat):
    if stat[int(n) - 1] != ' ':
        return 1


def pick(stat):
    p = input("your turn")
    while valid(p) or repeated(p, stat):
        print("wrong input")
        if valid(p):
            p = input("wrong input")
        elif repeated(p, stat):
            print("wrong input")
            p = input()
    return p


lines = [[0, 1, 2], [3, 4, 5], [6, 7, 8], [0, 3, 6], [1, 4, 7], [2, 5, 8], [0, 4, 8], [2, 4, 6]]
win = 0
lose = 0
draw = 0


def computer_turn(stat):
    win = []
    lose = []
    for i in lines:
        line = []
        for t in range(3):
            line.append(i[t])
        p_cnt = []
        cnt = []
        for t in range(3):
            if stat[i[t]] is Player:
                p_cnt.append(i[t])
                line.remove(i[t])
            elif stat[i[t]] is Computer:
                cnt.append(i[t])
                line.remove(i[t])
        if len(cnt) + len(p_cnt) is 3:
            continue
        if len(cnt) is 2 and len(p_cnt) is 0:
            win.append(line[0])
        if len(cnt) is 0 and len(p_cnt) is 2:
            lose.append(line[0])
    if len(win):
        return win[0]
    if len(lose):
        return lose[0]
    empty = []
    for i in range(9):
        if stat[i] is ' ':
            empty.append(i)
    random.shuffle(empty)
    return empty[0]


def check(stat, num, player, computer):
    global win, lose, draw
    for i in lines:
        if stat[i[0]] == stat[i[1]] == stat[i[2]]:
            if stat[i[0]] is ' ':
                continue
            if stat[i[0]] is player:
                print("이겼습니다")
                win += 1
                return 1

            elif stat[i[0]] is computer:
                print("졌습니다")
                lose += 1
                return 1
    if num is 9:
        print("비겼습니다")
        draw += 1
        return 1
    return 0


print("""Tic Tac Toe 게임을 시작합니다!

게임은 3*3 격자판에서 진행됩니다.
당신은 컴퓨터와 번갈아가며 게임을 하게 됩니다.
선공과 후공은 랜덤으로 결정됩니다.
가로, 세로 대각선으로 같은 표시(O/X)가 놓인다면, 해당 표시의 플레이어가 승리합니다!

Game Start!
""")

ingame = 1
while ingame is 1:
    Player, Computer = choose_pattern()
    print("선공/후공을 정합니다")
    first = random.randint(0, 1)

    if first is 1:
        print("player first")
    else:
        print("computer first")
    game = 1
    status = [' '] * 9
    while game <= 9:
        if first is 1:
            status[int(pick(status)) - 1] = Player
            print_board(status)
            if check(status, game, Player, Computer):
                if restart():
                    ingame = 0
                break
            game += 1

        status[int(computer_turn(status))] = Computer
        print_board(status)
        if check(status, game, Player, Computer):
            if restart():
                ingame = 0
            break
        game += 1
        first = 1

result(win, lose, draw)
