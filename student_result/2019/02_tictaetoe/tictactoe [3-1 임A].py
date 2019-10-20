board = []
user = ''
computer = ''
endans = 'Yes'
check = ''
lane = [[0, 1, 2], [3, 4, 5], [6, 7, 8], [0, 3, 6], [1, 4, 7], [2, 5, 8], [0, 4, 8], [2, 4, 6]]
u_s = 0
c_s = 0


def first():  # 처음에 user가 o를 선택하smswl x를 선택하는지에 따라 이를 인식하고 선공 후공을 지정해주는 역할을 하는 함수이다.
    global user, computer, check
    print("O와 X중 하나를 선택하세요.(O가 선공, X가 후공입니다.)")
    ans = input().upper()
    if (ans == 'O'):
        user = 'O'
        check = 0
        computer = 'X'
    elif (ans == 'X'):
        user = 'X'
        check = 1
        computer = 'O'
    else:  # O와 x가 아닌 다른 수를 입력하였을때 재입력해달라는 메시지를 띄운다.
        print("O와 X중 하나만 가능합니다. 다시 입력해주세요.")
        return first()


def reset():  # 보드판을 리셋하는, 다시 게임을 시작하였을 때를 위한 함수.
    global board
    board = ['.', '.', '.', '.', '.', '.', '.', '.', '.']


def usernumber():  # user가 입력한 숫자가 보드판에 적합한 함수인지 체크해주는 함수
    u_n = input()
    if (not u_n.isdecimal()):  # 입력한 수가 정수인지 판단.
        print("0 1 2 / 3 4 5 / 6 7 8 가 보드 위치에 따른 숫자입니다. 자기 차례에 원하는 위치의 숫자를 입력해주세요.")
        return usernumber()
    if (int(u_n) < 0 or int(u_n) >= 9):  # 입력한 수가 0부터 8까지인지 판단.
        print("0 1 2 / 3 4 5 / 6 7 8 가 보드 위치에 따른 숫자입니다. 자기 차례에 원하는 위치의 숫자를 입력해주세요.")
        return usernumber()
    u_n = int(u_n)
    if (board[u_n] == 'X' or board[u_n] == 'O'):  # 이미 놓여진 곳이라면 재입력하라는 메시지를 띄운다.
        print("이미 놓여진 곳입니다. 다른 곳을 선택해 주세요.")
        return usernumber()
    return u_n


def computernumber():  # computer가 숫자를 놓는데에 지시를 내리는 함수
    global board
    k = abletowin()
    if k >= 0:
        return k
    k = danger()
    if k >= 0:
        return k
    for i in range(9):
        if board[i] == '.':
            return i


def abletowin():  # computer가 이기기 위해 count라는 변수를 두어 각 칸마다의 computer의 o또는 x의 갯수를 세어
    # lane(이기기 위한 배치)별로 count를 세었을 때 2가 나오면 lane의 남은 한자리에 놓아 이길 수 있도록 한다.
    global lane, computer
    for i in lane:
        count = 0
        for j in i:
            if board[j] == computer:
                count += 1
        if count == 2:
            if board[i[0]] == '.': return i[0]
            if board[i[1]] == '.': return i[1]
            if board[i[2]] == '.': return i[2]
    else:
        return -1


def danger():  # user가 놓는 곳을 위의 ablewin의 함수와 같은 방식으로 세어 user가 이길 수 있는경우를 막기 위해 남은 lane자리를 computer가 놓게 하는 함수
    global lane, user
    for i in lane:
        count = 0
        for j in i:
            if board[j] == user:
                count += 1
        if count == 2:
            if board[i[0]] == '.': return i[0]
            if board[i[1]] == '.': return i[1]
            if board[i[2]] == '.': return i[2]
    else:
        return -1


def board_print():  # 매 tur마다 board의 상태를 출력해주는 함수
    for i in range(9):
        print("[", board[i], "]", end="")
        if (i + 1) % 3 == 0:
            print("")


def game():  # game을 진행하는 함수이고 check라는 변수를 두어 0일때는 user가, 1일때는 computer가 게임을 하도록 turn을 교체해준다.
    global board, check
    while True:
        if check == 0:
            board_print()
            board[usernumber()] = user
            check += 1
        else:
            board[computernumber()] = computer
            check -= 1
        if game_ended():
            board_print()
            break


def game_ended():  # 보드가 꽉찼을 때, 승패가 결정난 상황이 되었을 때 게임을 끝내는 함수
    global board, lane

    if board.count('.') == 0:
        return True

    for i in lane:
        if board[i[0]] == board[i[1]] and board[i[1]] == board[i[2]] and board[i[0]] != '.':
            return True

    return False


def end():  # 게임이 끝나고 난 뒤 누가 승리하였는지, 현재스코어가 어떻게 되는지 알려주는 함수
    global lane, user, u_s, c_s
    for i in lane:
        count = 0
        for j in i:  # 보드를 lane대로 세는 for문
            if board[j] == user:
                count += 1
        if count == 3:
            u_s += 1  # 보드의 칸을 일일이 lane(일열로 되는 배열)대로 세었을 때 같은 user의 문자가 3번 나오면 u_s 변수를 +1 한다.
            print("user가 승리했습니다.")
            print('[computer]' + str(c_s) + ' : ' + str(u_s) + '[user]')
            return
    for i in lane:
        count = 0
        for j in i:  # 보드를 lane대로 세는 for문
            if board[j] == computer:
                count += 1
        if count == 3:
            c_s += 1  # 보드의 칸을 일일이 lane(일열로 되는 배열)대로 세었을 때 같은 computer의 문자가 3번 나오면 c_s 변수를 +1 한다.
            print("computer가 승리했습니다.")
            print('[computer]' + str(c_s) + ' : ' + str(u_s) + '[user]')
            return
    print("무승부!")  # 그 외의 경우는 무승부로 판단한다.
    print('[computer]' + str(c_s) + ' : ' + str(u_s) + '[user]')


while (endans == 'Yes'):  # 모든 게임을 진행하는 함수라고 볼수 있다.
    first()  # user의 o,x를 고르는 함수를 부르고
    reset()  # board판을 리셋시켜준다.
    print("0 1 2 / 3 4 5 / 6 7 8 가 보드 위치에 따른 숫자입니다. 자기 차례에 원하는 위치의 숫자를 입력해주세요.")
    # 보드판 사용법을 출력하고
    game()  # game을 진행하는 함수를 호출
    end()  # game의 결과와 현재까지의 score를 출력해준다.
    print("게임을 한 번 더 하시려면 Yes를 입력해주세요")  # 게임을 다시 시작할 것인지 물어본다
    endans = input()  # 대답을 변수에 저장하고 대답이Yes일 경우 게임을 다시 시작한다.
