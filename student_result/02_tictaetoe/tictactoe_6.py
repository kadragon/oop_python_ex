'''
Title Tic-Tac-Toe
Made by Choi ho young
'''
import random

board=[]
turn=True
def intro(): # 시작할 때만 동작, 게임 설명
    print("Tic-Tac-Toe is a game for two players, X and O\n")
    print("You take turns marking the spaces in a 3*3 grid\n")
    print("If you succeed in placing three of your marks in a horizontal, vertical, or diagonal rows,\n")
    print("You win the game!\n")
    print("Now let's begin!\n")

def now(board): # 현재 보드 상태 출력
    print("| %c | %c | %c |\n"%(board[0], board[1], board[2]))
    print("| %c | %c | %c |\n"%(board[3], board[4], board[5]))
    print("| %c | %c | %c |\n"%(board[6], board[7], board[8]))

def clear_settings(board): # 전체 보드를 놓여지지 않은 상태로 초기화
    for i in range(9):
        board.append(' ')

def choose_pick(): # 플레이어가 O와 X 중 무엇을 택할 지 결정 (기본 설정은 X)
    global turn
    turn=input('Choose Your Side (O or X) : ').upper().startswith('O')

def choose_first(): # 어느 쪽이 먼저 공격할 지 결정, 0이면 플레이어가, 1이면 컴퓨터가 먼저 공격
    setting=list(range(0, 2))
    random.shuffle(setting)
    return setting[0]

def input_stone(): # 놓을 위치 확인
    global board
    if board_full():
        return False
    while True:
        tmp = int(input('Choose where to put your stone (1~9) : '))
        if tmp>9 or tmp<1:
            print('Re-enter your choice')
            continue
        if board[tmp-1]==' ':
            if turn:
                board[tmp-1]='O'
            else:
                board[tmp-1]='X'
            break
        else:
            print('Where you want to put your stone is not empty. Re-enter your choice.')
            continue

def check_probability(board, side): # 놓았을 때 이길 수 있는 곳이 있는 지 확인
    if (board[4]==board[0] and board[0]==board[8]) or (board[4]==board[1] and board[1]==board[7]) or (board[4]==board[3] and board[3]==board[5]) or (board[4]==board[2] and board[2]==board[6]):
        if board[4]==side:
            return True
    if (board[0]==board[1] and board[1]==board[2]) or (board[0]==board[3] and board[3]==board[6]):
        if board[0]==side:
            return True
    if (board[8]==board[2] and board[2]==board[5]) or (board[8]==board[6] and board[6]==board[7]):
        if board[8]==side:
            return True

def check_win(board): # 승리/패배 확인
    if (board[4]==board[0] and board[0]==board[8]) or (board[4]==board[1] and board[1]==board[7]) or (board[4]==board[3] and board[3]==board[5]) or (board[4]==board[2] and board[2]==board[6]):
        if board[4]=='O':
            if turn:
                print('You Win!')
            else:
                print('You Lose...')
            return True
        if board[4] == 'X':
            if turn:
                print('You Lose...')
            else:
                print('You Win!')
            return True
    if (board[0]==board[1] and board[1]==board[2]) or (board[0]==board[3] and board[3]==board[6]):
        if board[0]=='O':
            if turn:
                print('You Win!')
            else:
                print('You Lose...')
            return True
        if board[0] == 'X':
            if turn:
                print('You Lose...')
            else:
                print('You Win!')
            return True
    if (board[8]==board[2] and board[2]==board[5]) or (board[8]==board[6] and board[6]==board[7]):
        if board[8]=='O':
            if turn:
                print('You Win!')
            else:
                print('You Lose...')
            return True
        if board[8] == 'X':
            if turn:
                print('You Lose...')
            else:
                print('You Win!')
            return True

def board_full(): # 보드에 놓을 곳이 있는 지를 판별하여 없다면 무승부라는 멘트와 함께 True를 반환
    chk=1
    for i in range(9):
        if board[i]==' ':
            chk=0
    if chk==1:
        print("It's a Draw.")
        return True
    else:
        return False

def copy_board(board): # 보드를 복사하여 임시 보드 만들기
    global board_copy
    board_copy=[]
    for i in board:
        board_copy.append(i)
    return board_copy

def put_stone(): #컴퓨터가 어디에 놓을 지 결정
    global board
    if board_full():
        return False
    if turn: # 놓아서 이길 수 있는 곳에 놓기
        for i in range(8):
            board_copy=copy_board(board)
            if board_copy[i]==' ':
                board_copy[i]='X'
                if check_probability(board_copy, 'X'):
                    board[i]='X'
                    return True
    else:
        for i in range(8):
            board_copy=copy_board(board)
            if board_copy[i]==' ':
                board_copy[i]='O'
                if check_probability(board_copy, 'O'):
                    board[i]='O'
                    return True
    if turn: # 놓지 않았을 때 질 위치에 놓기
        for i in range(8):
            board_copy=copy_board(board)
            if board_copy[i]==' ':
                board_copy[i]='O'
                if check_probability(board_copy, 'O'):
                    board[i]='X'
                    return True
    else:
        for i in range(8):
            board_copy=copy_board(board)
            if board_copy[i]==' ':
                board_copy[i]='X'
                if check_probability(board_copy, 'X'):
                    board[i]='O'
                    return True
    if board[0]==' ' or board[2]==' ' or board[6]==' ' or board[8]== ' ': # 확률 높은 가장자리에 랜덤으로 놓기
        chk=[]
        for i in [0, 2, 6, 8]:
            if board[i]==' ':
                chk.append(i)
        random.shuffle(chk)
        if turn:
            board[chk[0]]='X'
            return True
        else:
            board[chk[0]]='O'
            return True
    if board[4]==' ': # 가운데에 놓기
        if turn:
            board[4]='X'
            return True
        else:
            board[4]='O'
            return True
    if board[1]==' ' or board[3]==' ' or board[5]==' ' or board[7]== ' ': # 십자 위치에 놓기
        chk=[]
        for i in [1, 3, 5, 7]:
            if board[i]==' ':
                chk.append(i)
        tmp=random.shuffle(chk)
        if turn:
            board[tmp[0]]='X'
            return True
        else:
            board[tmp[0]]='O'
            return True

def play_again(): # 게임 종료 후 다시 플레이할 지를 물어보는 함수
    return input('Do you want to play again? (Press Y to play again) ').lower().startswith('y')


intro()
while True:
    board=[]
    clear_settings(board)
    choose_pick()
    if_first=choose_first()
    while True:
        if if_first==0:
            now(board)
            input_stone()
            if check_win(board):
                now(board)
                break
            if board_full():
                now(board)
                break
            put_stone()
            if check_win(board):
                now(board)
                break
            if board_full():
                now(board)
                break
        else:
            put_stone()
            if check_win(board):
                now(board)
                break
            if board_full():
                now(board)
                break
            now(board)
            input_stone()
            if check_win(board):
                now(board)
                break
            if board_full():
                now(board)
                break
    if play_again():
        continue
    else:
        break
print('Thank You For Playing!')



