import random
print("-TicTacToe-")#게임의 시작을 알립니다.
#게임 판을 저장합니다.
game_map = [[' ']*4 for i in range(4)]#4*4의 이차원 배열 game_map을 선언합니다.

#놓아도 되는 곳인지를 확인해주는 함수입니다.
def is_it_ok(x, y):
    space = 0#빈 공간의 수를 저장하는 변수입니다.
    for i in range(0, 4):
        for j in range(0, 4):
            if game_map[i][j] != ' ':
                space = space+1#채워져있는 칸의 수를 샙니다.
    if space == 9:#만약 칸이 모두 다 채워졌으면 0을 반환합니다.
        return 0
    elif game_map[x][y] !=' ':#만약 넣으려는 자리에 이미 수가 있으면 -1을 반환합니다.
        return -1
    else:#문제가 없어 넣어도 되는 칸이면 1을 반환합니다.
        return 1

#매번 변화하는 판을 출력하는 함수입니다.
def printer(x, y, v):#놓을 위치, 놓을 알파벳을 받습니다.
    ok = is_it_ok(x, y)#놓아도 되는 곳인지 확인합니다.
    if ok == -1:#사용자가 놓으려는 칸이 만약 이미 놓아진 칸이라면 반환합니다.
        print("\n-이미 놓여진 칸입니다. 다시 입력하세요-\n")
        user_turn()#다시 입력을 받습니다.
    elif ok == 1:#아니라면
        if v == 1:#알파벳에 따라 구분하여 놓습니다.
            game_map[x][y] = 'X'
        elif v== -1:
            game_map[x][y] = 'O'
        #변화한 판을 출력합니다.
        print("[%c|%c|%c]" %(game_map[0][0], game_map[0][1], game_map[0][2]))
        print("[%c|%c|%c]" %(game_map[1][0], game_map[1][1], game_map[1][2]))
        print("[%c|%c|%c]" %(game_map[2][0], game_map[2][1], game_map[2][2]))
    #승리 여부를 확인합니다.
    winnie = win()#win()은 승리 여부를 확인하는 함수입니다.
    if winnie !=0:#만약 누군가 승리 했다면
        print("경기 종료!!")#경기 종료를 외치고
        game_end()#게임을 끝내주는 함수로 갑니다.
        return

# 사용자의 알파벳 선택을 저장하는 변수입니다.
a = 0
#사용자의 알파벳 선택을 받는 함수입니다. 만약 X를 선택하면 1을, 아니면 -1을 반환합니다.
def input_from_player():
    global play
    play =1#려빈 이거 하나 추가했어 그러니까 되더라
    print("X 와 O중 하나를 선택하세요.")
    wrong = 1  # 문자 선택과 관련된 사용자의 잘못된 입력을 배제하기 위한 변수입니다.
    # 사용자가 사용할 문자를 받는 함수입니다.
    while wrong == 1:
        turn = input()  #사용자가 자신의 문자를 입력합니다.
        if (turn != 'X') and (turn != 'O') and (turn != 'x') and (turn != 'o'):  # 잘못된 입력을 배제하기 위한 부분입니다.
            print("다시 입력하십시오, 제대로된 입력값은 X, O, x, o 중 하나입니다.")
        else:
            wrong = 0
            if (turn == 'X') or (turn == 'x'):#사용자의 입력에 따라 값을 반환합니다.
                return 1
            else:
                return -1

#게임 순서를 정하는 함수입니다.
def dice():
    print("주사위를 굴려 순서를 정합니다.\n데굴데굴......\n데굴데굴......\n")
    start = random.randint(0, 2)  #시작 순서를 랜덤으로 결정합니다.
    if start == 0:#만약, 컴퓨터가 먼저 시작하면
        print("컴퓨터가 먼저 시작합니다!!")
        computer_turn()#컴퓨터의 턴으로 넘어갑니다.
    else:
        print("사용자가 먼저 시작합니다!!")
        user_turn()#아니면, 사용자의 턴으로 넘어갑니다.

#사용자의 차례에 실행되는 함수입니다.
def user_turn():
    global play#게임이 끝났을 경우 추가적인 호출을 방지 하기 위한 부분입니다.
    if play != 1:
        return
    ok_user = is_it_ok(3, 3)  # 판이 다 차있는지 확인하는 과정입니다. is_it_ok()를 이용하여 확인합니다.
    if ok_user == 0:#만약 다 차있을 경우
        game_end()#게임을 끝내주는 함수로 갑니다.
        return
    print("(||사용자의 차례||)")
    wrong_position = 1  # position 과 관련된 잘못된 입력을 배제하기 위한 변수입니다.
    # 사용자가 놓을 position 을 받는 부분입니다.
    while wrong_position == 1:
        print("어디에 놓으실건가요? 놓으실 위치는 1에서 3사이의 정수 2개를 받습니다. 이를 공백으로 구분하여 입력하십시오.")
        position = (input().split())
        #잘못된 입력을 배제하기 위한 부분입니다.
        if ((position[0] != '1') and (position[0] != '2') and (position[0] != '3')) or (
                (position[1] != '1') and (position[1] != '2') and (position[1] != '3')):
            print("다시 입력하세요. 올바른 입력값은 1에서 3사이의 정수 2개를 공백으로 입력하는 것 입니다.")
        else:
            wrong_position = 0
            print("입력하신 값의 첫 두 숫자가", position, "이기에", position, "에 두겠습니다.")
            x = int(position[0])-1#문자형이기에 정수형으로 바꿉니다.
            y = int(position[1])-1
            #출력해주는 함수로 위치, 알파벳을 보냅니다.
            printer(x, y, a)
    computer_turn()#컴퓨터의 턴을 호출합니다.

#컴퓨터의 턴에 실행되는 함수입니다.
def computer_turn():
    emergencyx = -1#컴퓨터가 필수적으로 놓아야 할 곳을 저장하는 변수들입니다.
    emergencyy = -1
    character_user = ' '#사용자와 컴퓨터의 알파벳을 저장하는 변수로 프로그래밍의 용이함을 위한 변수입니다. 큰 의미는 없습니다.
    computer_user = ' '
    #게임이 끝난 이후의 호출을 막기 위한 장치입니다.
    global play
    if play != 1:
        return
    ok_computer = is_it_ok(3, 3)  # 판이 다 차있는지 확인하는 과정입니다.
    if ok_computer == 0:#만약 다 차있다면
        game_end()#게임을 끝내주는 함수로 갑니다.
        return
    print("(||컴퓨터의 차례||)\n")
    if a == 1:#사용자와 컴퓨터의 알파벳을 저장합니다.
        character_user = 'X'
        computer_user = 'O'
    elif a== -1:
        character_user = 'O'
        computer_user = 'X'
    #공격하는 함수입니다.
    for i in range(0, 3):#모든 경우를 탐색하여 공격가능한 곳을 찾습니다.
        if (game_map[i][0] == game_map[i][1] == computer_user) and (game_map[i][2] == ' '):
            emergencyx = i
            emergencyy = 2
            break
        elif (game_map[i][0] == game_map[i][2] == computer_user) and (game_map[i][1] == ' '):
            emergencyx = i
            emergencyy = 1
            break
        elif (game_map[i][1] == game_map[i][2] == computer_user) and (game_map[i][0] == ' '):
            emergencyx = i
            emergencyy = 0
            break
        elif (game_map[0][i] == game_map[1][i] == computer_user) and (game_map[2][i] == ' '):
            emergencyx = 2
            emergencyy = i
            break
        elif (game_map[0][i] == game_map[2][i] == computer_user) and (game_map[1][i] == ' '):
            emergencyx = 1
            emergencyy = i
            break
        elif (game_map[1][i] == game_map[2][i] == computer_user) and (game_map[0][i] == ' '):
            emergencyx = 0
            emergencyy = i
            break
    if (game_map[0][0] == game_map[1][1] == computer_user) and (game_map[2][2] == ' '):
        emergencyx = 2
        emergencyy = 2
    elif (game_map[0][0] == game_map[2][2] == computer_user) and (game_map[1][1] == ' '):
        emergencyx = 1
        emergencyy = 1
    elif (game_map[1][1] == game_map[2][2] == computer_user) and (game_map[0][0] == ' '):
        emergencyx = 0
        emergencyy = 0
    elif (game_map[2][0] == game_map[1][1] == computer_user) and (game_map[0][2] == ' '):
        emergencyx = 0
        emergencyy = 2
    elif (game_map[2][0] == game_map[0][2] == computer_user) and (game_map[1][1] == ' '):
        emergencyx = 1
        emergencyy = 1
    elif (game_map[1][1] == game_map[0][2] == computer_user) and (game_map[2][0] == ' '):
        emergencyx = 2
        emergencyy = 0
    if (emergencyx != -1) and a == 1:  # 만약 공격 가능한 곳이 있다면
        print("공격입니다!! 컴퓨터가 놓을 곳은...", "X=", emergencyx + 1, "Y=", emergencyy + 1, "입니다!")
        printer(emergencyx, emergencyy, -1)#출력한 뒤
        user_turn()#사용자에게 턴을 넘깁니다.
        return
    elif (emergencyx != -1) and a == -1:
        print("공격입니다!! 컴퓨터가 놓을 곳은...", "X=", emergencyx + 1, "Y=", emergencyy + 1, "입니다!")
        printer(emergencyx, emergencyy, 1)
        user_turn()
        return
    else:#공격 할 곳이 없다면
        for i in range(0, 3):#막아야 하는 곳을 찾습니다.
            if (game_map[i][0] == game_map[i][1] == character_user) and (game_map[i][2] == ' '):
                emergencyx = i
                emergencyy = 2
                break
            elif (game_map[i][0] == game_map[i][2] == character_user) and (game_map[i][1] == ' '):
                emergencyx = i
                emergencyy = 1
                break
            elif (game_map[i][1] == game_map[i][2] == character_user) and (game_map[i][0] == ' '):
                emergencyx = i
                emergencyy = 0
                break
            elif (game_map[0][i] == game_map[1][i] == character_user) and (game_map[2][i] == ' '):
                emergencyx = 2
                emergencyy = i
                break
            elif (game_map[0][i] == game_map[2][i] == character_user) and (game_map[1][i] == ' '):
                emergencyx = 1
                emergencyy = i
                break
            elif (game_map[1][i] == game_map[2][i] == character_user) and (game_map[0][i] == ' '):
                emergencyx = 0
                emergencyy = i
                break
        if (game_map[0][0] == game_map[1][1] == character_user) and (game_map[2][2] == ' '):
            emergencyx = 2
            emergencyy = 2
        elif (game_map[0][0] == game_map[2][2] == character_user) and (game_map[1][1] == ' '):
            emergencyx = 1
            emergencyy = 1
        elif (game_map[1][1] == game_map[2][2] == character_user) and (game_map[0][0] == ' '):
            emergencyx = 0
            emergencyy = 0
        elif (game_map[2][0] == game_map[1][1] == character_user) and (game_map[0][2] == ' '):
            emergencyx = 0
            emergencyy = 2
        elif (game_map[2][0] == game_map[0][2] == character_user) and (game_map[1][1] == ' '):
            emergencyx = 1
            emergencyy = 1
        elif (game_map[1][1] == game_map[0][2] == character_user) and (game_map[2][0] == ' '):
            emergencyx = 2
            emergencyy = 0

        if (emergencyx != -1) and a == 1:  # 만약 막아야 할 곳이 있다면
            print("막겠습니다!! 컴퓨터가 놓을 곳은...", "X=", emergencyx + 1, "Y=", emergencyy + 1, "입니다!")
            printer(emergencyx, emergencyy, -1)#출력한 뒤
            user_turn()#사용자에게 턴을 넘깁니다.
            return
        elif (emergencyx != -1) and a == -1:
            print("막겠습니다!! 컴퓨터가 놓을 곳은...", "X=", emergencyx + 1, "Y=", emergencyy + 1, "입니다!")
            printer(emergencyx, emergencyy, 1)
            user_turn()
            return
    t=1#for문애서 빠져나올 때 쓰는 변수입니다.
    for i in range(0, 3):
        for j in range(0, 3):
            if game_map[i][j] == ' ' :#앞부터 탐색하다 빈칸이 있으면 그 곳에 채웁니다.
                if a ==1:
                    print("할게 없군요...컴퓨터가 놓을 곳은...", "X=", i+1, "Y=", j+1, "입니다!")
                    printer(i, j, -1)
                    t=0
                    break
                elif a == -1:
                    print("할게 없군요...컴퓨터가 놓을 곳은...", "X=", i + 1, "Y=", j + 1, "입니다!")
                    printer(i, j, 1)
                    t=0
                    break
            if t == 0:
                break
        if t == 0:
            break

    user_turn()#사용자에게 턴을 넘깁니다.

#다시 플레이 할지 묻는 함수입니다.
def play_more():
    wrong_input = 1#잘못된 입력을 배제하기 위한 함수입니다.
    while wrong_input == 1:
        print("다시 플레이하시겠습니까? Yes 또는 No 로 답하세요.")
        r = input()
        if r == 'Yes':
            return -1
        elif r == 'No':
            return 0
        else:
            print("잘못된 입력입니다. 다시 입력해 주세요.")
    return -1

#승리를 검증해주는 함수입니다. 머리를 쓰는 대신 노가다로 대신했습니다......
def win():
    #각 세로줄 3개, 가로줄 3개, 대각선 2개를 검증합니다.
    if (game_map[0][0] == game_map[0][1]) and (game_map[0][1] == game_map[0][2]) and (game_map[0][0] == 'X'):
        return 11
    elif (game_map[1][0] == game_map[1][1]) and (game_map[1][1] == game_map[1][2]) and (game_map[1][0] == 'X'):
        return 11
    elif (game_map[2][0] == game_map[2][1]) and (game_map[2][1] == game_map[2][2]) and (game_map[2][0] == 'X'):
        return 11
    elif (game_map[0][0] == game_map[1][0]) and (game_map[1][0] == game_map[2][0]) and (game_map[0][0] == 'X'):
        return 11
    elif (game_map[0][1] == game_map[1][1]) and (game_map[1][1] == game_map[2][1]) and (game_map[0][1] == 'X'):
        return 11
    elif (game_map[0][2] == game_map[1][2]) and (game_map[1][2] == game_map[2][2]) and (game_map[0][2] == 'X'):
        return 11
    elif (game_map[0][0] == game_map[1][1]) and (game_map[1][1] == game_map[2][2]) and (game_map[0][0] == 'X'):
        return 11
    elif (game_map[0][2] == game_map[1][1]) and (game_map[1][1] == game_map[2][0]) and (game_map[0][2] == 'X'):
        return 11

    elif (game_map[0][0] == game_map[0][1]) and (game_map[0][1] == game_map[0][2]) and (game_map[0][0] == 'O'):
        return 21
    elif (game_map[1][0] == game_map[1][1]) and (game_map[1][1] == game_map[1][2]) and (game_map[1][0] == 'O'):
        return 21
    elif (game_map[2][0] == game_map[2][1]) and (game_map[2][1] == game_map[2][2]) and (game_map[2][0] == 'O'):
        return 21
    elif (game_map[0][0] == game_map[1][0]) and (game_map[1][0] == game_map[2][0]) and (game_map[0][0] == 'O'):
        return 21
    elif (game_map[0][1] == game_map[1][1]) and (game_map[1][1] == game_map[2][1]) and (game_map[0][1] == 'O'):
        return 21
    elif (game_map[0][2] == game_map[1][2]) and (game_map[1][2] == game_map[2][2]) and (game_map[0][2] == 'O'):
        return 21
    elif (game_map[0][0] == game_map[1][1]) and (game_map[1][1] == game_map[2][2]) and (game_map[0][0] == 'O'):
        return 21
    elif (game_map[0][2] == game_map[1][1]) and (game_map[1][1] == game_map[2][0]) and (game_map[1][1] == 'O'):
        return 21
    else:
        return 0

play = 1
#다시 플레이하기 위한 변수입니다.

#'게임을' "끝내주는 함수입니다.".
def game_end():
    winner=win()#누가 이겼는지 확인합니다.
    #print(winner) 제작 당시 디버깅 용으로 사용한 문입니다.
    if winner % 10 == 1:#승자를 출력합니다.
        if winner == 11:
            print("X가 이겼습니다!!! Win")
        else:
            print("O가 이겼습니다!!! Win")
    else:
        print("Draw, Good game(무승부입니다...)")
    global play#다시 플레이 할지에 대한 답변을 저장하는 변수입니다.
    play = play_more()#다시 플레이할지 묻습니다.
   # print(play) 제작 당시 디버깅 용으로 사용한 문
    return

while play == 1:#play가 1인 동안
    printer(3, 3, '0')#처음 판을 출력합니다.
    a = input_from_player()#사용자에게 알파벳을 선택하게 합니다.
    dice()#주사위를 굴려 순서를 정하는 것으로 게임을 시작합니다.
    #게임이 끝나면 play 가 -1또는 0으로 바뀌므로 while 문 밖으로 나옵니다.

if play == -1:# 리플레이
    while play == -1:
        for i in range(0, 4):# 초기화
            for j in range(0, 4):
                game_map[i][j] = ' '
        print("재시작입니다.")
        printer(3, 3, '0')
        a = input_from_player()
        dice()
