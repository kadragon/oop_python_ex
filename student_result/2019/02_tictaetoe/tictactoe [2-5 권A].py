# tic-tac-toe game 2502 권태희

import random
import copy


def opening():
    # 게임 시작 멘트
    print("=" * 40)
    print("Tic-Tac-Toe 게임에 오신 것을 환영합니다!")
    print("가로, 세로, 대각선 중 한 줄을 자신의 캐릭터(O 혹은 X)로 채우면 승리하게 됩니다")
    print("자신의 캐릭터를 놓을 칸은 아래와 같은 한 자리 숫자로 입력하시면 됩니다:")
    print("1 | 2 | 3")
    print("4 | 5 | 6")
    print("7 | 8 | 9")
    print("=" * 40)


def choosecharacter():
    # O로 플레이할지, X로 플레이할지 선택하게 하는 함수(0 입력 -> O, 1입력 -> X)
    # 사용자가 이상한 값을 입력하면 다시 입력하도록 함
    # 입력받은 값을 숫자 그대로 리턴함(0또는 1로)
    global character
    print("O로 플레이하실지, X로 플레이할지 선택해주세요")
    try:
        character = int(input("O로 플레이(먼저 플레이): 0 // X로 플레이(늦게 플레이): 1 >>>  "))
    except(TypeError, ValueError, KeyboardInterrupt):
        print("다시 입력해주세요")
        choosecharacter()
    if character == 0:
        print("O를 선택하셨습니다! 컴퓨터보다 먼저 플레이하게 됩니다")
        print("=" * 40)
    elif character == 1:
        print("X를 선택하셨습니다! 컴퓨터보나 늦게 플레이하게 됩니다")
        print("=" * 40)
    else:
        print("다시 입력해주세요")
        choosecharacter()


def show_gameboard():
    # 현재 상태를 출력해주는 함수
    # 전달받는 인자, 반환하는 인자 모두 없음
    print("현재 상황입니다")
    for i in range(3):
        for j in range(1, 3):
            if gameboard[3 * i + j] == 1:
                print("  X  |", end='')
            elif gameboard[3 * i + j] == 0:
                print("  O  |", end='')
            else:
                print("     |", end='')
        if gameboard[3 * i + 3] == 1:
            print("  X")
        elif gameboard[3 * i + 3] == 0:
            print("  O")
        else:
            print(" ")
    print("=" * 40)


def play_player():
    # 플레이어의 입력을 담당하는 함수
    # 플레이어가 입력하는 숫자에 플레이어의 말을 놓음(놓을 수 없는 경우 재입력 유도)
    # 함수에 전달되는 값과 함수가 반환하는 값은 없음
    print("플레이하실 차례입니다! 표시할 칸을 1부터 9까지의 숫자로 입력해주세요")
    try:
        location = int(input("내 말을 놓을 위치 >>>  "))
    except(TypeError, ValueError, KeyboardInterrupt):
        print("다시 입력해주세요")
        play_player()
    else:
        if type(location) != int:
            print("다시 입력해주세요")
            play_player()
            return
        elif location < 1 or location > 9:
            print("말을 놓을 수 없는 위치입니다")
            play_player()
            return
        elif gameboard[location] != -1:
            print("말을 놓을 수 없는 위치입니다")
            play_player()
            return
        if character == 0:
            gameboard[location] = 0
            return
        else:
            gameboard[location] = 1
            return


def play_computer():
    # 컴퓨터의 플레이를 담당하는 함수
    # 플레이어의 다음 차례 승리 조건이 있는지 탐색한 후, 있다면 플레이어의 승리를 방지
    # 승리 조건이 없는 경우 랜덤한 위치에 말을 놓음
    print("컴퓨터의 차례입니다!")
    not_filled_yet = []
    for i in range(1, 10):
        if gameboard[i] == -1:
            not_filled_yet.append(i)
            # 아직 말을 놓지 않은 위치를 리스트에 저장
    if character == 1:
        for i in not_filled_yet:
            nextgameboard = copy.copy(gameboard)
            nextgameboard[i] = 1
            can_player_win = is_game_over(nextgameboard)
            if can_player_win == 1:
                gameboard[i] = 0
                return
                # 플레이이어의 승리 조건이 있다면 승리를 방지
        # 플레이어의 말이 X인 경우
    else:
        for i in not_filled_yet:
            nextgameboard = copy.copy(gameboard)
            nextgameboard[i] = 0
            can_player_win = is_game_over(nextgameboard)
            if can_player_win == 1:
                gameboard[i] = 1
                return
                # 플레이어의 승리 조건이 있다면 승리를 방지
        # 플레이어의 말이 O인 경우
    random.shuffle(not_filled_yet)
    if character == 1:
        gameboard[not_filled_yet[0]] = 0
    else:
        gameboard[not_filled_yet[0]] = 1


def is_game_over(board):
    # 게임이 종료되었는지를 판단하는 함수
    # 함수에 전달되는 값은 판단할 대상인 게임판 리스트
    # 한 쪽의 승리로 게임이 종료되면 1을, 무승부로 게임이 종료되면 0을, 아직 게임이 끝나지 않았으면 -1을 반환
    for i in range(0, 3):
        if board[3 * i + 1] == board[3 * i + 2] and board[3 * i + 2] == board[3 * i + 3] and board[3 * i + 3] != -1:
            return 1
    for i in range(1, 4):
        if board[i] == board[3 + i] and board[3 + i] == board[6 + i] and board[6 + i] != -1:
            return 1
    if board[1] == board[5] and board[5] == board[9] and board[9] != -1:
        return 1
    if board[3] == board[5] and board[5] == board[7] and board[7] != -1:
        return 1
    for i in range(1, 10):
        if board[i] == -1:
            return -1
    return 0


def play_again():
    # 한 번 더 플레이할지를 물어보는 함수
    # 함수에 전달되는 인자와 함수가 반환하는 인자 모두 없음
    # 플레이어가 1을 입력하면 한 번 더 플레이, 0을 입력하면 플레이 종료
    print("한 번 더 플레이하시겠습니까?")
    try:
        end = int(input("한 번 더 플레이: 1 플레이 종료: 0 >>>  "))
    except(TypeError, ValueError, KeyboardInterrupt):
        print("다시 입력해주세요")
        play_again()
    else:
        if end == 1:
            print("좋은 선택이에요!")
            return True
        elif end == 0:
            print("언젠가 다시 만나요!")
            return False
        else:
            print("다시 입력해주세요")
            play_again()


def print_win_rate(did_you_win):
    # 승률을 출력하는 함수: 이때까지 이기고 비기고 진 횟수와 승률을 모두 출력
    # 승리, 패배, 무승부의 횟수는 전역변수로 선언되어있음
    # 함수에 전달되는 값 'did_you_win'이 1이면 플레이어의 승리, 0이면 무승부, -1이면 패배
    # 함수가 반환하는 값이 없음
    global win, tie, lose
    if did_you_win == 1:
        print("축하합니다! 이겼습니다!!")
        win += 1
    elif did_you_win == 0:
        print("비겼습니다!")
        tie += 1
    else:
        lose += 1
        print("아쉽지만 다음에는 승리하기를 바래요!")
    print("")
    print("현재까지 당신의 승률은 다음과 같습니다")
    print("총 플레이 횟수: %d" % (win + lose + tie))
    print("이긴 횟수: %d" % win, end=' ')
    print("진 횟수: %d" % lose, end=' ')
    print("비긴 횟수: %d" % tie)
    print("당신의 승률: %f" % (win / (win + lose + tie)))
    print("")


win = 0
lose = 0
tie = 0

while True:
    # 게임의 전체적인 흐름. 사용자가 플레이를 그만둘 때까지 무한 반복 시행
    opening()
    # 오프닝 멘트
    choosecharacter()
    # 사용자가 어떤 캐릭터로 플레이할지 선택
    # 전역변수 character 가 0이면 플레이어가 먼저 플레이, 1이면 컴퓨터가 먼저 플레이
    global gameboard
    gameboard = [0, -1, -1, -1, -1, -1, -1, -1, -1, -1]
    show_gameboard()
    if character == 0:
        play_player()
        show_gameboard()
    for i in range(5):
        play_computer()
        show_gameboard()
        chkgameover = is_game_over(gameboard)
        if chkgameover == 1:
            print_win_rate(-1)
            break
        if chkgameover == 0:
            print_win_rate(0)
            break
        play_player()
        show_gameboard()
        chkgameover = is_game_over(gameboard)
        if chkgameover == 1:
            print_win_rate(1)
            break
        if chkgameover == 0:
            print_win_rate(0)
            break
        # 사용자와 컴퓨터가 번갈아서 플레이 진행, 한 번 말을 둘 때마다 현재 상황을 출력하고 게임이 끝났는지 판단

    if not play_again():
        break
