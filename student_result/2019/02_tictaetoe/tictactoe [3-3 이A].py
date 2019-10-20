import random

board = [[' ', ' ', ' '], [' ', ' ', ' '], [' ', ' ', ' ']]
program = 'O'
player = 'X'
play_check = True

program_score = 0
player_score = 0


def program_check():  # 컴퓨터가 이길 수 있는 자리 찾아서 공격

    for i in range(3):  # 가로 경우의 수 3가지 확인
        if board[i][0] == board[i][1] and board[i][1] == program:
            if board[i][2] == ' ':  # 둘자리에 비어있는지 확인
                board[i][2] = program  # 비어있으면 넣고
                return True  # True반환하기
        if board[i][1] == board[i][2] and board[i][2] == program:
            if board[i][0] == ' ':
                board[i][0] = program
                return True
        if board[i][0] == board[i][2] and board[i][2] == program:
            if board[i][1] == ' ':
                board[i][1] = program
                return True

    for i in range(3):  # 세로 경우의 수 3가지 확인
        if board[0][i] == board[1][i] and board[1][i] == program:
            if board[2][i] == ' ':
                board[2][i] = program
                return True
        if board[1][i] == board[2][i] and board[2][i] == program:
            if board[0][i] == ' ':
                board[0][i] = program
                return True
        if board[0][i] == board[2][i] and board[2][i] == program:
            if board[1][i] == ' ':
                board[1][i] = program
                return True

    # 대각선 경우의 수 2가지 확인
    if board[0][0] == board[1][1] and board[1][1] == program:  # 왼위-오른아래 대각선
        if board[2][2] == ' ':
            board[2][2] = program
            return True
    if board[1][1] == board[2][2] and board[2][2] == program:
        if board[0][0] == ' ':
            board[0][0] = program
            return True
    if board[0][0] == board[2][2] and board[2][2] == program:
        if board[1][1] == ' ':
            board[1][1] = program
            return True

    if board[2][0] == board[1][1] and board[1][1] == program:  # 왼아래-오른위 대각선
        if board[0][2] == ' ':
            board[0][2] = program
            return True
    if board[2][0] == board[0][2] and board[0][2] == program:
        if board[1][1] == ' ':
            board[1][1] = program
            return True
    if board[1][1] == board[0][2] and board[0][2] == program:
        if board[2][0] == ' ':
            board[2][0] = program
            return True

    return False  # 컴퓨터가 이길 수 있는 자리가 없으면 false반환


def user_check():  # 사용자가 이길 수 있는 자리 찾아서 방어

    for i in range(3):  # 가로 경우의 수 3가지 확인
        if board[i][0] == board[i][1] and board[i][1] == player:
            if board[i][2] == ' ':  # 둘자리에 비어있는지 확인
                board[i][2] = program  # 비어있으면 넣고
                return True  # True반환하기
        if board[i][1] == board[i][2] and board[i][2] == player:
            if board[i][0] == ' ':
                board[i][0] = program
                return True
        if board[i][0] == board[i][2] and board[i][2] == player:
            if board[i][1] == ' ':
                board[i][1] = program
                return True

    for i in range(3):  # 세로 경우의 수 3가지 확인
        if board[0][i] == board[1][i] and board[1][i] == player:
            if board[2][i] == ' ':
                board[2][i] = program
                return True
        if board[1][i] == board[2][i] and board[2][i] == player:
            if board[0][i] == ' ':
                board[0][i] = program
                return True
        if board[0][i] == board[2][i] and board[2][i] == player:
            if board[1][i] == ' ':
                board[1][i] = program
                return True

    # 대각선 경우의 수 2가지 확인
    if board[0][0] == board[1][1] and board[1][1] == player:  # 왼위-오른아래 대각선
        if board[2][2] == ' ':
            board[2][2] = program
            return True
    if board[1][1] == board[2][2] and board[2][2] == player:
        if board[0][0] == ' ':
            board[0][0] = program
            return True
    if board[0][0] == board[2][2] and board[2][2] == player:
        if board[1][1] == ' ':
            board[1][1] = program
            return True

    if board[2][0] == board[1][1] and board[1][1] == player:  # 왼아래-오른위 대각선
        if board[0][2] == ' ':
            board[0][2] = program
            return True
    if board[2][0] == board[0][2] and board[0][2] == player:
        if board[1][1] == ' ':
            board[1][1] = program
            return True
    if board[1][1] == board[0][2] and board[0][2] == player:
        if board[2][0] == ' ':
            board[2][0] = program
            return True

    return False  # 사용자가 이길 수 있는 자리가 없으면 false반환


def random_choose():  # 컴퓨터가 랜덤하게 둘 자리 찾아서 비어있으면 넣기

    while True:
        list = [0, 0], [0, 1], [0, 2], [1, 0], [1, 1], [1, 2], [2, 0], [2, 1], [2, 2]
        i, j = random.choice(list)
        if board[i][j] == ' ':
            board[i][j] = program
            return True  # 랜덤하게 둘 자리 찾으면 넣고 True반환하여 함수 종료 아니면 계속 반복


def success_check():  # 성공하면 True반환, 성공한 값 없으면 False반환

    global player_score, program_score
    winner = ' '

    if (board[0][0] == board[0][1] and board[0][1] == board[0][2]):  # 8가지의 성공 경우의 수 확인 후 성공하면 winner에 성공자의 기호 저장
        winner = board[0][0]
    elif (board[1][0] == board[1][1] and board[1][1] == board[1][2]):
        winner = board[1][0]
    elif (board[2][0] == board[2][1] and board[2][1] == board[2][2]):
        winner = board[2][0]
    elif (board[0][0] == board[1][0] and board[1][0] == board[2][0]):
        winner = board[0][0]
    elif (board[0][1] == board[1][1] and board[1][1] == board[2][1]):
        winner = board[0][1]
    elif (board[0][2] == board[1][2] and board[1][2] == board[2][2]):
        winner = board[0][2]
    elif (board[0][0] == board[1][1] and board[1][1] == board[2][2]):
        winner = board[0][0]
    elif (board[0][2] == board[1][1] and board[1][1] == board[2][0]):
        winner = board[0][2]

    if winner == player:  # 성공자가 플레이어이면
        print("플레이어가 우승하였습니다.")
        player_score = player_score + 1
        return True
    elif winner == program:  # 성공자가 프로그램이면
        print("프로그램이 우승하였습니다.")
        program_score = program_score + 1
        return True
    # 성공자가 공백이면 check는 그대로 False값 유지

    for i in range(3):
        for j in range(3):
            if board[i][j] == ' ':  # 보드에 공백이 존재하면 False 반환
                return False

    program_score = program_score + 1
    player_score = player_score + 1
    print("비겼습니다")  # 우승자도 없고 보드가 꽉차있으면 비김
    return True


def play_again():  # 다시 할건지 확인하는 함수

    global board, program, player, play_check, program_score, player_score

    win_rate = player_score / (program_score + player_score) * 100
    print("플레이어 승률 %0.2f %%" % win_rate)

    print("한번 더 하시겠습니까? Y or N")
    while True:
        answer = input()
        if answer.upper() == 'Y':  # 다시 하겠다고하면 전역변수 값 초기화 시키기
            board = [[' ', ' ', ' '], [' ', ' ', ' '], [' ', ' ', ' ']]
            program = 'O'
            player = 'X'
            break
        elif answer.upper() == 'N':  # 다시 안할거면 play_check값에 False저장
            play_check = not play_check
            break
        else:  # 제대로 입력하지 않았을 때
            print("똑바로 입력해!!")


def print_board():  # 보드 출력하는 함수

    board_line = ['┏', '┳', '┳', '┓', '┣', '╋', '╋', '┫', '┗', '┻', '┻', '┛']
    for i in range(3):
        for j in range(3):
            print(board_line[i * 4 + j], end=" ")
            print(board[i][j], end=" ")
        print(board_line[(i + 1) * 4 - 1], end="")
        print("\n")


def game_start():  # 플레이어 선택 함수

    print("TIC!TAC!TOE!")
    print("플레이어를 선택해 주세요 O/X")
    while True:
        play = input()
        if play.upper() == 'O':
            print("당신은 O, 프로그램은 X")
            return (["O", "X"])  # 플레이어가 왼쪽, 프로그램이 오른쪽에 오는 리스트 반환
        elif play.upper() == 'X':
            print("당신은 X, 프로그램은 O")
            return (["X", "O"])  # 플레이어가 왼쪽, 프로그램이 오른쪽에 오는 리스트 반환
        else:
            print("똑바로 입력해!!")


def first_choose():  # 순서 정하는 함수

    ran = random.choice(['O', 'X'])
    if ran == player:  # 랜덤으로 정한 값이 플레이어와 동일하면 사용자 먼저 시작
        print("먼저 시작하세요!")
        user_turn()  # 사용자 먼저 시작
    else:  # 랜덤으로 정한 값이 플레이어와 동일하지 않으면 프로그램 먼저 시작
        print("프로그램이 먼저 시작합니다!")
        program_turn()  # 프로그램 먼저 시작


def user_turn():  # 사용자 차례

    print("1~9까지의 수를 입력하세요!")
    while True:
        num_list = map(str, range(10))
        num = input()
        if num not in num_list or num == '0':  # 제대로 입력했는지 확인하기
            print("다시 입력하세요")
        elif board[int((int(num) - 1) / 3)][(int(num) - 1) % 3] == program or board[int((int(num) - 1) / 3)][
            (int(num) - 1) % 3] == player:  # 둘 수 있는 곳인지 확인하기
            print("이미 차있는 자리 입니다")
        else:
            break
    board[int((int(num) - 1) / 3)][(int(num) - 1) % 3] = player  # 둘 수 있는 곳이면 보드에 player채우기

    if success_check():  # 성공 하면 게임 종료, 성공 안하면 프로그램 차례
        print_board()
        play_again()
    else:
        program_turn()


def program_turn():
    first_time = 1

    for i in range(3):
        for j in range(3):
            if board[i][j] != ' ':  # 첫번째 놓는게 아니면
                first_time = 0
                break

    if first_time:  # 첫번째 놓는 경우, 가운데와 모서리중에 랜덤하게 선택
        list = [0, 0], [2, 2], [0, 2], [2, 0], [1, 1]
        i, j = random.choice(list)
        board[i][j] = program

    else:
        if not program_check():  # 컴퓨터가 이길 수 있는 자리 찾아서 공격/ 공격시 True반환-> if문 실행x / 공격할 자리 없으면 False반환-> if문 실행
            if not user_check():  # 사용자가 이길 수 있는 자리 찾아서 방어/ 방어시 True반환-> if문 실행x / 방어할 자리 없으면 False반환-> if문 실행
                random_choose()  # 공격방어 할자리 없으면 랜덤하게 넣기

    if success_check():  # 성공 하면 게임 종료, 성공 안하면 사용자 차례
        print_board()  # 보드 출력하기
        play_again()
    else:
        print_board()  # 보드 출력하기
        user_turn()


while play_check:  # 나중에 다시 할건지 확인하기 위해 ( 다시 안할경우 play_check에 false저장, 프로그램 전체 종료 )
    print_board()  # 게임시작
    list = game_start()  # 플레이어가 왼쪽, 프로그램이 오른쪽에 오는 리스트 반환
    program = list[1]
    player = list[0]
    first_choose()  # 순서 정하면서 게임시작
