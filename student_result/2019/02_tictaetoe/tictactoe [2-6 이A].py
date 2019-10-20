import random
import time

game_map = [' '] * 10
win = 0
lose = 0
draw = 0


def reset_map():  # 게임을 시작할 때마다 맵을 초기화하는 함수
    global game_map
    game_map = [' '] * 10


def win_rate():  # 현재까지의 승률을 출력하는 함수
    print('현재 승률 : %.2f %%' % (100 * win / (win + lose + draw)))


def print_map(map):  # 현재 맵의 상태를 보여주는 함수
    print('┌───┬───┬───┐')
    print('│ %c │ %c │ %c │' % (map[1], map[2], map[3]))
    print('├───┼───┼───┤')
    print('│ %c │ %c │ %c │' % (map[4], map[5], map[6]))
    print('├───┼───┼───┤')
    print('│ %c │ %c │ %c │' % (map[7], map[8], map[9]))
    print('└───┴───┴───┘')


def print_rules():  # 부가적인 규칙을 설명하는 함수
    temp_map = '0123456789'
    print('X 가 선공, O 가 후공입니다.')
    print('각 자리의 번호는 다음과 같습니다.')
    print_map(temp_map)


def winner(who):  # 매개 변수 who는 player 또는 computer둥 하나로, who가 승리 조건을 만족하면 1, 아니면 0을 리턴
    if game_map[1] == game_map[2] == game_map[3] == who:
        return 1
    elif game_map[4] == game_map[5] == game_map[6] == who:
        return 1
    elif game_map[7] == game_map[8] == game_map[9] == who:
        return 1
    elif game_map[1] == game_map[4] == game_map[7] == who:
        return 1
    elif game_map[2] == game_map[5] == game_map[8] == who:
        return 1
    elif game_map[3] == game_map[6] == game_map[9] == who:
        return 1
    elif game_map[1] == game_map[5] == game_map[9] == who:
        return 1
    elif game_map[3] == game_map[5] == game_map[7] == who:
        return 1
    else:
        return 0


def turn_player(turn):  # 사용자의 차례에 실행되는 함수, 현재 몇 번째 턴인지 저장
    global win
    global draw
    if turn >= 10:  # turn이 10 이상 넘어가면 승자가 나오지 않은 것으로 간주하여 무승부로 판단 후 게임 종료(리턴)
        draw += 1
        print('비겼습니다.')
        return

    print('-' * 50)
    print('놓을 위치를 입력하세요')
    pos = input('>> ')
    while len(pos) != 1 or pos not in '123456789' or game_map[int(pos)] != ' ':
        print('잘못된 입력 또는 이미 놓여있는 위치입니다. 놓을 위치를 입력하세요')
        pos = input('>> ')

    game_map[int(pos)] = player
    print_map(game_map)  # 사용자의 입력 후 맵의 상태 출력
    if winner(player):  # 사용자가 이겼다면 승리 판정 후 게임 종료(리턴)
        win += 1
        print('이겼습니다.')
        return
    turn_computer(turn + 1)  # 턴을 증가시켜 컴퓨터로 턴을 넘김


def turn_computer(turn):  # 컴퓨터의 턴에 실행되는 함수
    global lose
    global draw
    if turn >= 10:  # turn이 10 이상 넘어가면 승자가 나오지 않은 것으로 판단하여 무승부
        draw += 1
        print('비겼습니다.')
        return

    print('-' * 50)
    print('컴퓨터의 차례입니다.')  # (line 84 ~ 138) 다음 턴에 사용자가 이길 수 있는 상황이라면 그것을 막는 수를 둔다.
    if game_map[1] == player and game_map[2] == player and game_map[3] == ' ':
        game_map[3] = computer
    elif game_map[2] == player and game_map[3] == player and game_map[1] == ' ':
        game_map[1] = computer
    elif game_map[3] == player and game_map[1] == player and game_map[2] == ' ':
        game_map[2] = computer

    elif game_map[4] == player and game_map[5] == player and game_map[6] == ' ':
        game_map[6] = computer
    elif game_map[5] == player and game_map[6] == player and game_map[4] == ' ':
        game_map[4] = computer
    elif game_map[6] == player and game_map[4] == player and game_map[5] == ' ':
        game_map[5] = computer

    elif game_map[7] == player and game_map[8] == player and game_map[9] == ' ':
        game_map[9] = computer
    elif game_map[8] == player and game_map[9] == player and game_map[7] == ' ':
        game_map[7] = computer
    elif game_map[9] == player and game_map[7] == player and game_map[8] == ' ':
        game_map[8] = computer

    elif game_map[1] == player and game_map[4] == player and game_map[7] == ' ':
        game_map[7] = computer
    elif game_map[4] == player and game_map[7] == player and game_map[1] == ' ':
        game_map[1] = computer
    elif game_map[7] == player and game_map[1] == player and game_map[4] == ' ':
        game_map[4] = computer

    elif game_map[2] == player and game_map[5] == player and game_map[8] == ' ':
        game_map[8] = computer
    elif game_map[5] == player and game_map[8] == player and game_map[2] == ' ':
        game_map[2] = computer
    elif game_map[8] == player and game_map[2] == player and game_map[5] == ' ':
        game_map[5] = computer

    elif game_map[3] == player and game_map[6] == player and game_map[9] == ' ':
        game_map[9] = computer
    elif game_map[6] == player and game_map[9] == player and game_map[3] == ' ':
        game_map[3] = computer
    elif game_map[9] == player and game_map[3] == player and game_map[6] == ' ':
        game_map[6] = computer

    elif game_map[1] == player and game_map[5] == player and game_map[9] == ' ':
        game_map[9] = computer
    elif game_map[5] == player and game_map[9] == player and game_map[1] == ' ':
        game_map[1] = computer
    elif game_map[9] == player and game_map[1] == player and game_map[5] == ' ':
        game_map[5] = computer

    elif game_map[3] == player and game_map[5] == player and game_map[7] == ' ':
        game_map[7] = computer
    elif game_map[5] == player and game_map[7] == player and game_map[3] == ' ':
        game_map[3] = computer
    elif game_map[7] == player and game_map[3] == player and game_map[5] == ' ':
        game_map[5] = computer

    else:  # 다음 턴에 사용자가 이길 수 있는 상황이 아니라면 빈 곳 중 랜덤으로 선택
        pos = random.randint(1, 9)
        while game_map[pos] != ' ':
            pos = random.randint(1, 9)
        game_map[pos] = computer

    time.sleep(1)
    print_map(game_map)  # 컴퓨터의 선택 후 맵의 상태 출력
    if winner(computer):  # 컴퓨터가 이겼다면 패배 판정 후 게임 종료(리턴)
        print('졌습니다.')
        lose += 1
        return
    turn_player(turn + 1)


def play_game():  # 한번의 게임을 진행하는 함수
    print('X 또는 O 를 선택하세요')
    global player
    global computer
    player = input('>> ').upper()
    while len(player) != 1 or player not in 'OX':
        print('잘못된 입력입니다. X 또는 O 를 선택하세요')
        player = input('>> ').upper()

    if player == 'X':
        computer = 'O'
        turn_player(1)
    elif player == 'O':
        player = 'X'
        turn_computer(1)

    win_rate()  # 한 번의 게임이 끝난 후 승률을 출력


def start_game():  # 게임 시작, 다시 시작을 결정하는 함수
    reset_map()
    print('게임을 시작합니다.')
    play_game()

    print('다시 시작하시겠습니까? (y/n)')
    check = input('>> ')
    while len(check) != 1 or check not in 'yn':
        print('y/n 으로 입력해주세요')
        check = input('>> ')
    if check == 'y':
        start_game()  # 사용자가 다시 시작을 입력하면 다시 시작
    elif check == 'n':
        print('게임을 종료합니다.')
        return


print_rules()
start_game()
