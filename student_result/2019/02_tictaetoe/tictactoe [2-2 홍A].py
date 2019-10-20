import random
import time

"""
line_list : 틱택토에서 승리 조건을 저장해놓은 리스트입니다. 리스트에 들어 있는 8개의 리스트들은 각각 세로,가로,대각선 중 한 줄을 나타냅니다.
end_saying : end의 값에 따라, 즉 끝난 조건에 따라 다르게 출력하게 하는 리스트입니다.
boardprint_list : 나와 컴퓨터의 말 모양을 정합니다.
comment : 나의 승률을 평가합니다.
board : 현재 틱택토 판의 상태를 저장합니다.
"""
line_list = [[1, 2, 3], [4, 5, 6], [7, 8, 9], [1, 4, 7], [2, 5, 8], [3, 6, 9], [1, 5, 9], [3, 5, 7]]
end_saying = ["와!! 플레이어님이 이기셨어요!!", "컴퓨터의 승리입니다.", "비겼습니다!"]
boardprint_list = ['X', 'O']
comment = ["ㅋㅋㅋㅋㅋ 컴퓨터한테 못 이긴다고?", "진짜 엄청 못하네", "당신은 랜덤함수를 돌리는 컴퓨터보다 못합니다", "당신은 랜덤함수를 돌리는 컴퓨터와 비슷한 실력입니다.",
           "참 참 참 참 참 참",
           "완벽주의자시군요! 한 판 더 어떠신가요?"]
player_win, computer_win, tie, troll_flag, start_flag = 0, 0, 0, 0, 1
troll_comment = ["싫어 아무도 나한테 못이겨 아무도!", "비겼어? 비겼으면 진거야"]
board = [0] * 10


# eq_print : 서로 다른 출력들을 구분해주는 선을 출력해주는 함수입니다.
def eq_print():
    print("=" * 60)


# boardlist_select : 말의 모양을 정하는 함수입니다.
def boardlist_select():
    # temp_char1, temp_char2는 각각 사용자와 컴퓨터의 말 모양을 저장합니다.
    # 한 글자이고, 혼동되지 않게 숫자가 아닌 모양을 선택합니다.
    global troll_flag
    temp_char1, temp_char2 = 0, 0
    eq_print()
    print("말 모양은 뭐로 하고 싶으세요? 숫자만 빼고 입력해주세요.")
    char_flag = True
    while char_flag:
        char_flag = False
        char_input = input("입력 : ").strip(' ')
        if len(char_input) != 1:
            print("제가 설명을 제대로 하지 않았네요.한 글자만 입력이 가능합니다.")
            char_flag = True
        elif '0' <= char_input <= '9':
            print("숫자는 안됩니다.")
            char_flag = True
        else:
            print("당신의 말 모양은 '%s'입니다! 흥미롭네요..." % char_input)
            temp_char1 = char_input
    comp_char = chr(random.randint(1000, 3000))
    while '0' <= comp_char <= '9':
        comp_char = chr(random.randint(1000, 3000))
    temp_char2 = comp_char
    if troll_flag:
        temp_char2 = 'ࠃ'
    print("저는 그러면 '%s'로 두겠습니다!" % temp_char2)
    return temp_char1, temp_char2


# player_input : 사용자의 입력을 받는 함수입니다.
def player_input():
    """
    flag : 사용자가 입력을 정상적으로 하지 않으면 True값으로 설정되어 다시 입력받습니다.
    str_input : 사용자의 입력을 받는 곳입니다.
    """
    flag = True
    while flag:
        flag = False
        eq_print()
        print("보드에서 놓을 칸을 입력해주세요. 1~9까지 입력이 가능합니다.\n입력 : ", end='')
        str_input = input().strip(' ')
        """
        사용자의 입력이
        1) 1글자이며
        2) 글자 값이 1~9 사이의 값이며 (선생님께 질문)
        3) 틱택토 판에 아직 놓아져있지 않으면
        올바른 입력으로 받아들입니다.
        """
        if len(str_input) == 1 and '1' <= str_input[0] <= '9' and board[int(str_input)] == 0:
            return int(str_input)
        else:
            eq_print()
            print("다시 입력해주세요. 입력 조건을 무시했거나 이미 놓아진 곳입니다.")
            flag = True


# start : 맨 처음 함수입니다. 틱택토에 대한 간단한 설명과 누가 먼저 할지를 결정합니다.
def start():
    """
    turn : 누가 먼저 할지를 결정하는 변수로, True라면 내가, False라면 컴퓨터가 먼저 시작합니다.
    """
    eq_print()
    print("""TIC-TAC-TOE
컴퓨터와 대결합니다.
서로 번갈아가며 3*3칸 안에 자신의 말을 놓습니다.
가로, 세로, 대각선으로 3개를 연속으로 놓는 경우 승리합니다.""")
    boardprint_list[0], boardprint_list[1] = boardlist_select()

    turn = random.choice([True, False])
    board_print()
    eq_print()
    if turn is False:
        print("제가 먼저 시작할게요!")
    else:
        print("먼저 시작하세요!")
    return turn


# com_do: 컴퓨터가 어디 둘 지를 선택하게 되는 함수입니다.
def com_do():
    """
    첫 번째 for문은 '자기가 이길 수 있는 곳이 있는지'를 판별합니다.
    line_list에 있는 리스트 하나하나마다 틱택토 판을 검사하면서
    만약 자신의 말이 두 개 있고 나머지 한 칸이 비어 있다면 그 칸을 선택합니다.
    """
    for line in line_list:
        cnt = 0
        for num in line:
            if board[num]:
                cnt += (10 ** board[num])
        if cnt == 200:
            for num in line:
                if not board[num]:
                    return num
    """
    두 번째 for문은 '상대가 이길수 있는 곳이 있는지'를 판별합니다.
    line_list에 있는 리스트 하나하나마다 틱택토 판을 검사하면서 
    만약 상대의 말이 두 개 있고 나머지 한 칸이 비어 있다면 그 칸을 선택합니다. 
    """
    for line in line_list:
        cnt = 0
        for num in line:
            if board[num]:
                cnt += (10 ** board[num])
        if cnt == 20:
            for num in line:
                if not board[num]:
                    return num
    """
    위의 for문에서 아무런 위치도 선택되지 않았다면,
    지금 남아있는 칸들 중 하나를 무작위로 선택합니다.
    """
    res = random.randint(1, 9)
    while board[res]:
        res = random.randint(1, 9)
    return res


# game_ended : 게임이 끝났는지를 판별하는 동시에, 어떻게 끝났는지도 판별하는 함수입니다.
def game_ended(cnt):
    """
    1 : 사용자가 이겼을 때
    2 : 컴퓨터가 이겼을 때
    3 : cnt가 9일 때(판이 모두 채워졌을 때
    0 : 아직 끝나지 않았을 때
    1과 2는 각각 line_list를 이용하여 확인합니다.
    이후 cnt를 이용하여 3을 체크한 후,
    끝나지 않았다면 0을 return합니다.
    """
    global player_win, computer_win, tie
    for line in line_list:
        chksum = 0
        for num in line:
            if board[num]:
                chksum += (10 ** board[num])
        if chksum == 30:
            player_win += 1
            return 1
        if chksum == 300:
            computer_win += 1
            return 2
    if cnt == 9:
        tie += 1
        return 3
    return 0


# retry_ans : 사용자가 다시 하고싶은지를 묻는 함수입니다. 대답을 받고, 재시작 여부를 판별합니다.
def retry_ans():
    """
    hope : 사용자의 대답을 입력받습니다.
    troll_flag : 다른 것을 입력해도 게임을 종료하지 못하게 합니다. 평상시에는 False입니다.
    yes를 입력하면 다시 시작합니다.
    no나 다른 것을 입력하면 게임이 끝나게 됩니다.
    """
    global troll_flag
    eq_print()
    print("다시하시겠습니까? yes 또는 no로 입력하세요.")
    hope = input()
    if hope == 'yes' or hope == 'ㅛㄷㄴ':
        eq_print()
        print("좋습니다.")
        return 1
    if troll_flag:
        print("넌 못나가!")
        return 1
    elif hope == 'no' or hope == 'ㅜㅐ':
        print("즐거웠어요.")
        return 0
    elif hope == '참':
        print("이 게임에서 유일한 이스터에그입니다. 그러면 좀 재미있게 가보죠.")
        troll_flag = 1
        return 1
    else:
        print("나중에 보죠.")
        return 0


# board_print : 게임판을 출력해주는 함수입니다. 아직 말이 놓여있지 않은 곳은 1~9로, 놓여있는 곳은 O나 X로 표현합니다.
def board_print():
    global board
    eq_print()
    for i in range(0, 3):
        print(' ' * 20, '=' * 16, '\n', '>>', ' ' * 18, end='')
        for j in range(1, 4):
            if board[i * 3 + j] == 0:
                print("| %d |" % (i * 3 + j), end='')
            else:
                print("| %s |" % boardprint_list[board[i * 3 + j] - 1], end='')
        print(' ' * 20)
    print(' ' * 20, '=' * 16)


# winrate_print : 승률을 출력해주는 함수입니다. 승/(승+패)를 출력합니다. 만약 0승 0패일때는 승률을 따지지 않습니다.
def winrate_print():
    global player_win, computer_win, tie
    if computer_win == 0 and player_win == 0:
        winrate = 0
    else:
        winrate = player_win / (player_win + computer_win)
    print("%d승 %d패 %d무, 현재 승률 %.2f입니다. %s" % (player_win, computer_win, tie, winrate, comment[int(winrate * 5)]))


# troll... : 만약 다시 하고 싶냐고 물어볼 때 '참'을 입력하면 진행되는 이스터에그입니다.
def troll_as_much_as_u_can(end):
    """
    게임판의 말들을 모두 O로 바꿔버리고,
    컴퓨터의 승리마냥 출력하는 함수입니다.
    troll_flag가 true일 때 진행됩니다.
    """
    global board
    eq_print()
    print("%s" % troll_comment[int((end + 1) / 2 - 1)])
    for i in range(1, 10):
        board[i] = 2
    board_print()


# com_play : 컴퓨터가 둘 곳을 찾은 뒤 두는 함수입니다. 별 거 없습니다.
def com_play(com_p, cnt, troll_ing):
    """
    생각하는 척 하려고 time.sleep을 넣었습니다.
    """
    if troll_ing:
        eq_print()
        print("나 또 할꺼야! 메롱메롱메롱")
    elif cnt != 0:
        eq_print()
        print("제 차례에요! 저 둘게요! 생각할 시간 조금만요...")
    time.sleep(random.randint(1, 2))
    board[com_p] = 2


# playing : 거의 틱택토 게임의 메인 틀입니다. turn에 따라 누가 둘지를 결정하고, 이를 실행합니다.
def playing(cnt, turn, troll_t):
    global board, troll_flag
    if turn:
        board[player_input()] = 1
    else:
        com_num = com_do()
        com_play(com_num, cnt, False)
        """
        troll_flag가 True일때 발동하는 이스터에그입니다.
        단 한 번, 1/5의 확률로 컴퓨터가 한 번 더 두게 됩니다.
        """
        if cnt < 8 and troll_flag and random.randint(0, 4) == 1 and troll_t is False:
            troll_t = True
            com_num = com_do()
            com_play(com_num, cnt, True)
            cnt += 1
    cnt += 1
    return cnt, troll_t


# board_init() : 판을 초기화하는 함수입니다.
def board_init():
    global board
    for i in range(1, 10):
        board[i] = 0


# turn_change : 순서를 넘겨주는 함수입니다.
def turn_change(turn):
    return not turn


# end_game : 만약 끝났다면, 결과 출력 및 후처리를 하는 함수입니다.
def end_game(end):
    """
    승률 출력 및 재시작 여부를 물어보는 함수입니다.
    평가도 해줘요!
    """
    global troll_flag, end_saying;
    if end:
        if (end == 1 or end == 3) and troll_flag == 1:
            troll_as_much_as_u_can(end)
            end = 2
        winrate_print()
        eq_print()
        print(end_saying[end - 1])
        return retry_ans()
    return 1


# The Game Starts!
# 게임을 실행하는 메인 코드입니다.
while start_flag:
    board_init()  # 판을 초기화합니다.
    end, start_flag, cnt, troll_twice = 0, 0, 0, False
    turn = start()  # 누가 먼저 시작할지를 정합니다.
    while end == 0:
        cnt, troll_twice = playing(cnt, turn, troll_twice)  # 현재 순서가 말을 놓습니다.
        board_print()  # 이에 따른 게임판을 출력합니다.
        end = game_ended(cnt)  # 게임이 끝났는지 판별합니다.
        start_flag = end_game(end)  # 끝났다면 평가 및 결과를 출력하고, 아니라면 반복합니다.
        turn = turn_change(turn)  # 끝나지 않았다면 순서를 바꿉니다.

# 게임이 끝났을 때, 일정 시간 후 꺼집니다.
time.sleep(2)
