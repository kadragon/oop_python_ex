import random
import sys

line_list = [[0, 1, 2], [3, 4, 5], [6, 7, 8], [0, 3, 6], [1, 4, 7], [2, 5, 8], [0, 4, 8], [2, 4, 6]]  # 승리하는 8개의 조건
comment = ["축하드립니다, 승리하셨습니다!", "패배하셨습니다.", "비기셨습니다"]  # 게임의 세 가지 결과
role = ['O', 'X']  # 게임의 두 가지 역할
turn = 0  # 먼저 시작할 사람 정하기
loc = [' '] * 9  # 틱택토 경기판
win = 0  # 이긴 경기의 수
total = 0  # 총 경기 수
percent = 0  # 승률
player_char = 0  # 사용자의 역할
end = False  # 게임이 끝나는지 체크


def intro():
    global end, player_char, loc
    loc = [' '] * 9
    print("Tic-Tac-Toe 게임입니다!")
    print("가로, 세로, 대각선으로 한 줄을 완성하시면 이깁니다.")
    print("X와 O 중 하나를 골라주세요!")
    global first
    flag = 1
    player_ans = []
    while flag:
        flag = 0
        player_ans = list(input())
        if len(player_ans[0]) != 1:  # 한 글자 이상 입력한다면 출력.
            print("한 자리로 입력해주세요!")
            flag = 1  # 사용자가 다시 입력해야 하는 경우 flag=1
        elif player_ans[0] == 'x' or player_ans[0] == 'X':
            player_char = 1  # x나 X로 대답한다면 player_char을 1로 설정.
            print("X로 게임을 시작합니다!")
        elif player_ans[0] == 'o' or player_ans[0] == 'O':
            player_char = 0  # o나 O로 대답한다면 player_char을 0으로 설정.
            print("O로 게임을 시작합니다!")
        else:
            print("X나 O를 입력해주세요!")
            flag = 1  # 사용자가 다시 입력해야 하는 경우 flag=1
    turn = random.randint(0, 1)
    while end is False:
        if turn == 0:
            print("먼저 시작하세요!")
            while True:
                user_play()  # 사용자가 먼저 시작.
        else:
            print("컴퓨터가 먼저 시작합니다!")
            while True:
                computer_play()  # 컴퓨터가 먼저 시작.
        turn = (turn - 1) ** 2  # turn이 0이라면 1로, 1이라면 0으로 바꿈.


def display():
    print('-' * 11)
    for j in range(3):
        for i in range(j * 3, (j + 1) * 3):
            print(loc[i] + '.', end='')  # loc에 저장된 값을 출력
        print(' ')


def user_play():
    user()
    display()
    result()
    loc[computer()] = role[(player_char - 1) ** 2]  # computer() 함수의 리턴값을 이용하여 loc 배열 채움.
    display()
    result()


def computer_play():
    global role, player_char, loc
    loc[computer()] = role[(player_char - 1) ** 2]
    display()
    result()
    user()
    display()
    result()


def user():
    global role, player_char, loc
    inp = list(input())
    if len(inp) != 1:
        print("1부터 9 사이의 한자리 정수로 입력해주세요!")
        user()
    elif not inp[0].isdecimal():  # inp가 정수가 아니라면
        print("정수를 입력해주세요!")
        user()
    elif 1 <= int(inp[0]) and int(inp[0]) <= 9 and loc[int(inp[0]) - 1] == ' ':
        loc[int(inp[0]) - 1] = role[player_char]
    else:
        print("1부터 9 사이의 비어있는 정수를 입력해주세요!")
        user()


def computer():
    global role, r, player_char
    for line in line_list:
        chk_cnt = 0
        for num in line:
            if loc[num] == role[player_char]:
                chk_cnt += 1  # 승리 조건 중 사용자가 놓은 말의 수를 센다.
            if loc[num] == role[(player_char - 1) ** 2]:
                chk_cnt -= 1  # 승리 조건 중 컴퓨터가 놓은 말의 수를 센다.
        if chk_cnt == 2:  # 사용자가 한 줄의 두 칸 이상을 채웠다면
            for num in line:
                if loc[num] != role[player_char]:  # 사용자의 두 칸을 제외한 나머지 칸이 빈칸이라면
                    return num  # 칸 번호 리턴.

    rand_num = random.randint(0, 8)
    while loc[rand_num] != ' ':
        rand_num = random.randint(0, 8)  # 사용자를 방어하지 않아도 된다면 랜덤한 자리에 말 두기.
    return rand_num


def result():
    for line in line_list:
        chk_cnt = 0
        for num in line:
            if loc[num] == role[player_char]:
                chk_cnt += 1
            if loc[num] == role[(player_char - 1) ** 2]:
                chk_cnt -= 1
        if chk_cnt == 3:  # 사용자가 승리 조건을 만족했다면
            game_end(0)
        if chk_cnt == -3:  # 컴퓨터가 승리 조건을 만족했다면
            game_end(1)

    kan_cnt = 0
    for kan in range(9):
        if loc[kan] != ' ':
            kan_cnt += 1
    if kan_cnt == 9:  # 누구도 승리하지 않고 판이 모두 채워졌다면
        game_end(2)


def game_end(did_win):
    global win, total, percent, end
    print("%s" % comment[did_win])  # 결과 메세지 출력
    if did_win == 0:  # 사용자가 승리했다면 승리한 판 수 1 증가.
        win = win + 1
    total = total + 1
    percent = float(100 * (win / total))  # float 형으로 퍼센트 단위로 승률 계산
    percent = str(percent)  # 출력을 위해서 승률을 string 형으로 형변환
    print("승률은" + percent + '%' + "입니다!")
    end = True  # 게임이 끝났음을 나타내기 위해서 end=True로 변경.
    restart()


def restart():
    print("다시 플레이하시겠습니까?(y/n)")
    answer = []
    answer = list(input())
    while ' ' in answer:  # 사용자 입력 공백 제거
        answer.remove(' ')
    if len(answer) == 1:
        if ord(answer[0]) == 121 or ord(answer[0]) == 89:  # y나 Y가 입력되었을 때 재실행
            loc = [' '] * 9
            intro()
        elif ord(answer[0]) == 110 or ord(answer[0]) == 78:  # n이나 N이 입력되었을 때 종료
            print("안녕히 가세요!")
            sys.exit()
        else:
            print("y나 n을 입력해주세요!")
            restart()
    elif len(answer) == 3:
        if (ord(answer[0]) == 121 or ord(answer[0]) == 89) and (ord(answer[1]) == 101 or ord(answer[1]) == 69) and (
                ord(answer[2]) == 115 or ord(answer[2]) == 83):  # yes, Yes, yEs, yeS, YEs, YeS, YEs, YES가 입력되었을 때 재실행
            loc = [' '] * 9
            intro()
        else:
            print("y나 n을 입력해주세요!")
            restart()
    elif len(answer) == 2:
        if (ord(answer[0]) == 110 or ord(answer[0]) == 78) and (
                ord(answer[1]) == 111 or ord(answer[1]) == 79):  # no, No, nO, NO가 입력되었을 때 종료
            print("안녕히 가세요!")
            sys.exit()
        else:
            print("y나 n을 입력해주세요!")
            restart()
    else:
        print("y나 n을 입력해주세요!")
        restart()


intro()
