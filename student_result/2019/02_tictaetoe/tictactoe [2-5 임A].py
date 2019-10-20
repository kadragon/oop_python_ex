import random  # 컴퓨터 AI가 랜덤으로 수를 둘 때 사용되는 랜덤 모듈입니다.

board = [[0, 0, 0, 0],  # 게임 보드는 인덱스 (0, 0) 부터 (2, 2) 까지를 사용하며 4*4로 선언한 이유는 (-1, -1)의 좌표를 초기값 저장으로 사용하기 위해서입니다.
         [0, 0, 0, 0],
         [0, 0, 0, 0],
         [0, 0, 0, 0]]

intro = """
어서 오세요! 틱택토 게임에 오신 것을 환영합니다.
틱택토 게임은 두 플레이어가 번갈아 가면서 3 x 3 판에 O 또는 X의 말을 놓고
만약 O나 X가 가로, 세로 또는 대각선에서 3개가 일렬로 놓인다면 그 플레이어의 승리입니다!
┌───┬───┬───┐
│ 1 │ 2 │ 3 │
├───┼───┼───┤
│ 4 │ 5 │ 6 │
├───┼───┼───┤
│ 7 │ 8 │ 9 │
└───┴───┴───┘
과 같이 번호를 입력하면 그 자리에 놓을 수 있습니다.
      
그럼 틱택토 게임을 시작하겠습니다!
"""
# 첫 플레이 시 출력될 게임의 규칙 설명 인트로입니다.

game_result = []  # 게임 결과를 'com'(컴퓨터 승리), 'user'(사용자 승리), 'tie'(무승부)로 저장해 이후 승률을 계산할 수 있도록 합니다.


def find_coord(num):
    return [(int(num) - 1) // 3, (int(num) - 1) % 3]  # 1~9의 번호를 입력받아 이 숫자를 각각에 대응하는 좌표로 바꾸어 크기 2의 리스트로 리턴합니다.


def choose_mark():  # O와 X 중에서 무엇으로 입력받을지 정하는 함수입니다.
    input_mark = 0  # 사용자 입력 표식을 정의합니다.
    while input_mark != 'O' and input_mark != 'X':  # 사용자의 입력값이 'O(o)'나 'X(x)'가 아닌 동안
        print('무엇으로 플레이할래요?(O / X): ', end='')  # 무엇으로 플레이 할지 물어본 뒤
        input_mark = input().upper()
    return [input_mark, chr(ord('O') + ord('X') - ord(input_mark))]
    # 만약 입력이 'O'라면 ['O', 'X']를, 'X'라면 ['X', 'O']를 리턴합니다.


"""
아래 함수들은 컴퓨터 AI의 구동을 위한 함수들입니다.
┌───┬───┬───┐ 컴퓨터 AI는 각각 줄을 다음과 같이 번호로 계산합니다. 다음 0~7의 숫자를 idx 라고 부르겠습니다.
│ 1 │ 2 │ 3 │ 가로줄: (1, 2, 3) -> 0, (4, 5, 6) -> 1, (7, 8, 9) -> 2
├───┼───┼───┤ 세로줄: (1, 4, 7) -> 3, (2, 5, 8) -> 4, (3, 6, 9) -> 5
│ 4 │ 5 │ 6 │ 대각선: (1, 5, 9) -> 6, (7, 5, 3) -> 7
├───┼───┼───┤
│ 7 │ 8 │ 9 │
└───┴───┴───┘
"""


def find_loc(idx):  # 이 함수에 들어오는 idx는 두 칸이 같은 표식으로 이루어져 있고 남은 한 칸은 비어있습니다.
    # idx 를 전달받아서 그 idx 에 대해서 빈 자리의 좌표를 [x, y]로 리턴하는 함수입니다.
    if 0 <= idx <= 2:  # 가로줄 idx 가 전달될 경우
        for i in range(0, 3):  # 그 가로줄 안에서 가로로 이동하면서
            if board[idx % 3][i] == 0:  # 만약 그 칸이 비어있다면
                return [idx % 3, i]  # 그 칸의 좌표를 리턴합니다.
    if 3 <= idx <= 5:  # 세로줄 idx 가 전달될 경우
        for i in range(0, 3):  # 그 세로줄 안에서 세로로 이동하면서
            if board[i][idx % 3] == 0:  # 만약 그 칸이 비어있다면
                return [i, idx % 3]  # 그 칸의 좌표를 리턴합니다.
    if idx == 6:  # 오른쪽 아래로 향하는 대각선 idx 가 전달될 경우
        for i in range(0, 3):  # 그 대각선 안에서 오른쪽 아래로 이동하면서
            if board[i][i] == 0:  # 만약 그 칸이 비어있다면
                return [i, i]  # 그 칸의 좌표를 리턴합니다.
    if idx == 7:  # 오른쪽 위로 향하는 대각선 idx 가 전달될 경우
        for i in range(0, 3):  # 그 대각선 안에서 오른쪽 위로 이동하면서
            if board[i][2 - i] == 0:  # 만약 그 칸이 비어있다면
                return [i, 2 - i]  # 그 칸의 좌표를 리턴합니다.


def cur():  # 현재 게임판의 상태를 리턴하는 함수입니다.
    # 아래 네 개의 리스트 sum_x, sum_y, sum_d, sum_u의 [0]에는 그 줄의 컴퓨터 표식의 개수를, [1]에는 사용자 표식의 개수를 저장합니다.
    sum_x = [[0, 0, 0], [0, 0, 0]]
    # 0~2 idx 에 대해서 그 줄의 표식의 개수를 저장합니다.
    sum_y = [[0, 0, 0], [0, 0, 0]]
    # 3~5 idx 에 대해서 그 줄의 표식의 개수를 저장합니다.
    sum_d = [[0], [0]]
    # 6 idx 에 대해서 그 줄의 표식의 개수를 저장합니다.
    sum_u = [[0], [0]]
    # 7 idx 에 대해서 그 줄의 표식의 개수를 저장합니다.
    for i in range(0, 3):
        for j in range(0, 3):
            if board[i][j]:  # 보드를 가로줄 우선으로 탐색하면서 만약 그 칸이 비어있지 않다면
                sum_x[bool(com_mark != board[i][j])][i] += 1
                # 컴퓨터 표식과 그 칸의 표식이 같으면 sum_x[0]에 1을 더하고 다르면 sum_x[1]에 1을 더합니다.
            if board[j][i]:  # 보드를 세로줄 우선으로 탐색하면서 만약 그 칸이 비어있지 않다면
                sum_y[bool(com_mark != board[j][i])][i] += 1
                # 컴퓨터 표식과 그 칸의 표식이 같으면 sum_y[0]에 1을 더하고 다르면 sum_y[1]에 1을 더합니다.
        if board[i][i]:  # 보드를 오른쪽 아래로 탐색하면서 만약 그 칸이 비어있지 않다면
            sum_d[bool(com_mark != board[i][i])][0] += 1
            # 컴퓨터 표식과 그 칸의 표식이 같으면 sum_d[0]에 1을 더하고 다르면 sum_d[1]에 1을 더합니다.
        if board[i][2 - i]:  # 보드를 오른쪽 위로 탐색하면서 만약 그 칸이 비어있지 않다면
            sum_u[bool(com_mark != board[i][2 - i])][0] += 1
            # 컴퓨터 표식과 그 칸의 표식이 같으면 sum_u[0]에 1을 더하고 다르면 sum_u[1]에 1을 더합니다.

    list_com = sum_x[0] + sum_y[0] + sum_d[0] + sum_u[0]  # 이 4개의 리스트의 [0] 인덱스만을 합쳐 크기 8의 리스트로 만듭니다.
    list_user = sum_x[1] + sum_y[1] + sum_d[1] + sum_u[1]  # 이 4개의 리스트의 [1] 인덱스만을 합쳐 크기 8의 리스트로 만듭니다.

    return [list_com, list_user]  # 이 두 리스트를 리턴합니다.


def com_act():  # 컴퓨터의 행동 함수입니다. 최종적으로 표식을 보드에 입력하는 역할을 합니다.
    list_com, list_user = cur()  # cur 함수를 통해서 현재 각각 idx 의 상태를 리스트로 전달받습니다.
    list_can = []  # 표식을 그려야 하는(또는 그릴 수 있는) 후보 idx 들을 저장해두는 candidate 리스트입니다.

    for i in range(0, 8):
        if list_com[i] == 2 and list_user[i] == 0:  # 만약 그 idx 에 컴퓨터의 표식이 2개고 사용자의 표식이 0개라면
            list_can.append(i)  # '승리 가능 idx' 후보에 넣습니다.

    if len(list_can):  # '승리 가능 idx' 안에 값이 있다면 (이 곳에 놓으면 컴퓨터의 승리가 확정되는 idx 가 있다면)
        cho = random.choice(list_can)  # '승리 가능 idx' 후보 중에서 하나를 랜덤으로 고른 뒤
        tx, ty = find_loc(cho)  # 그 idx 에서 빈 좌표를 찾아내 tx, ty 에 저장하고
        board[tx][ty] = com_mark  # 보드의 그 x, y 좌표에 컴퓨터의 표식을 둡니다.
        return

    list_can = []  # 리스트를 초기화합니다.
    for i in range(0, 8):
        if list_com[i] == 0 and list_user[i] == 2:  # 만약 그 idx 에 컴퓨터의 표식이 0개고 사용자의 표식이 2개라면
            list_can.append(i)  # '위험 지역 idx' 후보에 넣습니다.

    if len(list_can):  # '위험 지역 idx' 안에 값이 있다면 (이 곳에 놓으면 사용자의 승리가 확정되는 idx 가 있다면)
        cho = random.choice(list_can)  # '위험 지역 idx' 후보 중에서 하나를 랜덤으로 고른 뒤
        tx, ty = find_loc(cho)  # 그 idx 에서 빈 좌표를 찾아내 tx, ty 에 저장하고
        board[tx][ty] = com_mark  # 보드의 그 x, y 좌표에 컴퓨터의 표식을 둡니다.
        return

    list_can = []  # 리스트를 초기화합니다.
    for i in range(1, 10):  # 만약 사용자의 승리 위험이나 컴퓨터의 승리 기회 상황이 아니라면
        tx, ty = find_coord(i)
        if not board[tx][ty]:  # 1~9 까지의 모든 칸에 대해서 그 좌표에 값이 없다면
            list_can.append(i)  # '랜덤 위치' 후보에 넣습니다.

    cho = random.choice(list_can)  # '랜덤 위치' 후보 중에서 하나를 고른 뒤
    tx, ty = find_coord(cho)  # 그 숫자에 대한 좌표를 찾아내
    board[tx][ty] = com_mark  # 보드의 그 x, y 좌표에 컴퓨터의 표식을 둡니다.
    return


def loc_chk(input_list):  # 사용자의 위치 입력 값을 리스트로 전달받아 [(입력 값이 옳은가?(0/1), x좌표, y좌표)]를 리턴하는 함수입니다.
    tx = -1  # 입력 값이 옳지 않아도 리턴 값의 크기 3 리스트를 맞추기 위해 기본 x, y 좌표 값은 -1, -1로 정해두었습니다.
    ty = -1
    if len(input_list) == 0:  # 사용자 입력 리스트의 크기가 1일때
        print('값을 입력해주세요.')
        return [0, tx, ty]  # [0, -1, -1]을 리턴한다.
    for i in input_list:  # 사용자 입력 리스트 안에
        if not '1' <= i <= '9':  # 1부터 9 사이의 정수가 아닌 것이 있다면
            print('1과 9 사이의 정수만 입력해주세요.')
            return [0, tx, ty]  # [0, -1, -1]을 리턴한다.
    if len(input_list) != 1:  # 사용자 입력 리스트의 크기가 2 이상이면
        print('1과 9 사이에서 입력해주세요.')
        return [0, tx, ty]  # [0, -1, -1]을 리턴한다.
    tx, ty = find_coord(input_list[0])  # 이제 사용자 입력 리스트는 1~9의 정수이므로 놓을 수 있는 위치인지 판단하기 위해 그 숫자의 좌표를 가져온다.
    if board[tx][ty] != 0:  # 그 좌표에 0이 아닌 값이 들어있다면
        print('이미 둔 곳입니다.')
        return [0, tx, ty]  # [0, -1, -1]을 리턴한다.
    return [1, tx, ty]  # 값을 놓을 수 있으므로 [1, tx, ty]를 리턴한다.


def win_chk():  # 매 턴이 끝날 때 마다 승, 패, 비김 여부를 체크해 리턴하는 함수입니다.
    list_com, list_user = cur()  # 현재 각 idx 의 상황을 cur()함수로 불러옵니다.
    tie = 1  # 기본적으로 비겼다고 해 놓습니다.
    for i in range(0, 8):
        if list_com[i] == 3:  # 만약 컴퓨터의 표식 3개로 차 있는 idx 가 있다면
            return 'com'  # 'com'을 리턴합니다.
        if list_user[i] == 3:  # 만약 사용자의 표식 3개로 차 있는 idx 가 있다면
            return 'user'  # 'user'를 리턴합니다.
        if list_com[i] + list_user[i] != 3:  # 만약 세 칸이 모두 꽉 차지 않은 idx 가 존재한다면
            tie = 0  # 비김 여부를 0으로 만듭니다.
    if tie:  # 비김 여부가 1이라면
        return 'tie'  # 'tie'를 리턴합니다.
    else:  # 아무 상황도 아니라면
        return 'none'  # 'none'를 리턴합니다.


def print_board():  # 현재 게임 보드의 상태를 출력하는 함수입니다.
    print('┌───┬───┬───┐')
    for i in range(0, 3):
        print('│ %c │ %c │ %c │' % (board[i][0], board[i][1], board[i][2]))
        if i != 2:
            print('├───┼───┼───┤')
    print('└───┴───┴───┘')


def rep_chk():  # 다시 플레이할지 입력받는 함수입니다.
    input_rep = 0  # 다시 플레이할지 물어본 뒤 입력값을 저장합니다.
    print('다시 플레이할래요?(Y / N): ', end='')
    while input_rep != 'Y' and input_rep != 'N':  # 입력값이 'Y(y)'또는 'N(n)'이 아닌 동안
        input_rep = input().upper()  # 입력값을 저장하고
        if input_rep == 'Y':  # 입력값이 'Y(y)'라면
            return 1  # 1을 리턴합니다.
        if input_rep == 'N':  # 입력값이 'X(x)'라면
            print('=' * 80)
            print('게임 종료')  # 전체 게임이 종료되었다고 출력한 뒤
            print('=' * 80)
            return 0  # 0을 리턴합니다.
        print('Y 또는 N으로 입력해주세요.')  # 'Y(y)'또는 'N(n)'이 아니라면 입력 조건을 다시 출력합니다.


def win_rate():  # 승률을 기록하는 함수입니다.
    rate = game_result.count('user') / len(game_result)  # 승률을 (사용자가 승리한 게임의 수)/(전체 게임의 수)로 정합니다.
    print('승률은 %f%%입니다' % (rate * 100))
    print('%d승 %d무 %d패' % (game_result.count('user'), game_result.count('tie'), game_result.count('com')))
    print('=' * 80)


replay = 1  # 다시 플레이할지의 여부를 저장하는 변수로 초기에는 1로 정해져 있습니다.
play_time = 0  # 플레이 횟수를 저장합니다.

while replay:
    board = [[0, 0, 0, 0],
             [0, 0, 0, 0],
             [0, 0, 0, 0],
             [0, 0, 0, 0]]  # 게임 보드를 초기화 합니다.
    user_mark, com_mark = 0, 0  # 사용자와 컴퓨터의 표식을 초기화합니다.
    play_time += 1  # 게임을 플레이한 횟수를 1 늘립니다.
    if play_time == 1:  # 만약 게임을 처음 플레이하는 것이라면
        print(intro)  # 게임 설명을 출력합니다.
    user_mark, com_mark = choose_mark()  # 사용자의 표식과 컴퓨터의 표식을 정합니다.
    user_turn = random.randrange(0, 2)  # user_turn 이 1이면 사용자의 턴이고 0이면 컴퓨터의 턴입니다. 초깃값(선공)은 0, 1 중에서 랜덤으로 정해집니다.
    if user_turn == 0:
        print('컴퓨터가 먼저 시작합니다.')
    else:
        print('당신이 먼저 시작합니다.')
    game_end = 0  # 게임이 끝났는지(사용자 승, 컴퓨터 승, 판이 꽉차서 비김)를 저장하는 변수입니다.
    print('=' * 80)

    chk = 'none'  # win_chk 함수를 통해서 게임의 현재 상황을 문자열로 저장해두는 변수입니다.
    while not game_end:  # 게임 종료 조건이 아닌 동안
        if user_turn:  # 만약 사용자의 차례라면
            input_loc = 0  # 표식을 놓을 위치 입력값, input_loc
            loc_ok = 0  # 사용자가 입력한 표식을 놓을 위치가 '표식 위치 입력 조건(1~9 사이의 정수이고 해당 자리에 표식 없음)'에 맞는지저장하는 변수입니다.
            x, y = -1, -1  # 사용자가 입력한 값에 해당하는 좌표를 저장할 두 변수를 저장합니다.
            while not loc_ok:  # 입력값이 '표식 위치 입력 조건'에 맞지 않는 동안
                print('당신(%c)의 차례입니다! 표식을 놓을 위치를 정하세요(1 ~ 9): ' % user_mark, end='')
                input_loc = list(input())  # 사용자의 입력값을 리스트로 변환해
                loc_ok, x, y = loc_chk(input_loc)  # '표식 위치 입력 조건' 체크 함수에 저장한 뒤
                # 조건에 옳은지와 옳다면 사용할 그에 해당하는 x, y 좌표값을 리턴합니다.
            board[x][y] = user_mark  # 보드의 (x, y) 위치에 사용자의 표식을 입력합니다.
            user_turn = 1 - user_turn  # 다음 턴은 컴퓨터의 턴입니다.
        else:  # 만약 컴퓨터의 차례라면
            print('컴퓨터(%c)의 차례입니다!' % com_mark)
            com_act()  # 컴퓨터는 조건을 판단해 표식을 입력하는 행동을 수행합니다.
            user_turn = 1 - user_turn  # 다음 턴은 사용자의 턴입니다.
        print_board()  # 현재 보드의 상태를 출력합니다.
        print('=' * 80)
        chk = win_chk()  # 현재 게임의 상태를 'com', 'user', 'tie', 'none' 넷 중 하나로 저장합니다.
        if chk == 'com':  # 만약 컴퓨터가 승리했다면
            print('컴퓨터 승리!')
            game_end = 1  # 이번 게임이 끝나게 됩니다.
        if chk == 'user':  # 만약 사용자가 승리했다면
            print('당신의 승리!')
            game_end = 1  # 이번 게임이 끝나게 됩니다.
        if chk == 'tie':  # 만약 비겼다면
            print('비겼습니다!')
            game_end = 1  # 이번 게임이 끝나게 됩니다.

    game_result.append(chk)  # 이번 게임의 결과를 승리자, 또는 비겼다는 것을 'com', 'user', 'tie'로 저장합니다.
    replay = rep_chk()  # 다시 플레이할지 입력받아 1 또는 0으로 저장합니다.

win_rate()
