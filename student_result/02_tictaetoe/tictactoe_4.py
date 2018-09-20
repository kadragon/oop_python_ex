
import random   #ai가 임의의 자리를 선택
import copy     #ai가 ai 나 user의 승리시행을 판단
import time     #딜레이 함수 사용

def user_choice():                                          #시작시 user 선택 함수
    chosen=input("Choose your letter: O / X ").upper()   #user 문자 입력
    while not (chosen=='X' or chosen=='O'):               #O(o) 또는 X(x) 가 아니면 재입력
        chosen=input("You choose wrong letter. Choose again. ").upper()
    return chosen                                           #user 문자 반환

def ai_choice(user):    #ai 문자 선택 함수
    if user=='X':       #user의 반대 문자를 반환
        return 'O'
    else:
        return 'X'

def print_board(board):                                         #보드를 출력하는 함수
    print("%s | %s | %s" %(board[1], board[2], board[3]))      #1~9번까지 3열 3행으로 출력
    print("%s | %s | %s" %(board[4], board[5], board[6]))
    print("%s | %s | %s" %(board[7], board[8], board[9]))
    print('')

def right_place(place, board):                           #둘 수 있는 위치인지 확인하는 함수
    place=int(place)                                     #입력을 문자형으로 받으므로 정수형으로 변환
    if (place>0 and place<10 and board[place]==' '):    #1~9 범위 내이고, 빈칸(' ')이라면 참을 반환, 아니면 거짓을 반환
        return True
    return False

def winner(now, board):                                                             #승리하였는지 판단하는 함수
    win_list=[[1,2,3],[4,5,6],[7,8,9],[1,4,7],[2,5,8],[3,6,9],[1,5,9],[3,5,7]]       #이기는 조건 가로(1,2,3), 세로(1,2,3), 대각선(1->9, 3->7)
    for i in range(0,8):                                                            #승리 조건 내에서 now와 해당 좌표의 보드가 같으면 cnt 증가
        cnt=0                                                                        #cnt=3 이면(=3개가 같다면) 참을 반환, 아니면 거짓을 반환
        for j in range(0,3):
            if now==board[win_list[i][j]]:
                cnt+=1
        if cnt==3:
            return True
        cnt=0
    return False

def find_place(now, board):                 #ai가 다음 두는 수가 승리인지를 판단하는 함수
    for i in range(1,10):                   #1~9까지 둘 수 있는 위치이면
        if right_place(i, board):
            temp_board=copy.copy(board)     #보드를 복사한 임시 보드의 i에 두어
            temp_board[i]=now               #승리인지 판단
            if winner(now, temp_board):     #승리한다면 i(=이기는 위치)를 반환
                return i
    return 0

def user_turn(user, board):                                                 #user의 입력을 받아 보드에 두는 함수
    print("Your turn:\n")
    print_board(board)                                                       #보드를 출력
    user_place=input("Where you will put? ")                              #user가 둘 위치를 입력
    while not (user_place.isdigit() and right_place(user_place, board)):   #만약 정수가 아니거나, 둘 수 있는 위치가 아니라면
        user_place=input("It is an invalid value. Try again. ")         #다시 입력을 받는다
    board[int(user_place)]=user                                              #자료형이 문자형이므로 정수형으로 변환하여 보드에 user 문자를 입력

def ai_turn(user, ai, board):       #ai가 보드에 두는 함수
    print("ai turn:", end='')      #'...'을 0.5 초 딜레이를 주면서 출력
    for i in range(0,3):
        print(". ", end='')
        time.sleep(0.5)
    print("\n", end='')
    now=find_place(ai, board)       #ai가 이길 수 있는 위치를 탐색
    if now:                         #만약 now가 0 이 아니라면(=ai가 이길 수 있는 위치가 있다면)
        board[now]=ai               #now 위치에 두고 리턴
        return
    now=find_place(user, board)     #user가 이길 수 있는 위치를 탐색
    if now:                         #만약 now가 0 이 아니라면(=user가 이길 수 있는 위치가 있다면)
        board[now]=ai               #now 위치에 두고 리턴
        return
    rand_index=[]                   #위 두 상황이 아니면
    for i in range(1,10):           #1~9 에서 비어있는 위치를 리스트에 저장
        if right_place(i, board):
            rand_index.append(i)
    rand=random.choice(rand_index)  #리스트에서 랜덤값을 뽑아 보드에 두기
    board[rand]=ai


print("Tic Tac Toe")
print("You can choose X or O")
print("You can put your letter in 1~9 on the board.")
print("If you choose X and put on 4, then")
print("The board will be like this.")
print(" | | ")
print("X| | ")
print(" | | ")
print("If you put 3letter on a line, you win a game.\n")

while True:                                                 #실행부, yes가 아닐 때까지 반복
    board=[' ',' ',' ',' ',' ',' ',' ',' ',' ',' ']      #빈 보드를 리스트로 선언
    user=user_choice()                                       #user가 문자를 선택
    ai=ai_choice(user)                                       #ai가 문자를 선택
    cnt=0                                                    #draw를 위해 cnt 변수 선언
    if user=='X':                                            #'X'가 먼저 시작하므로, user가 X면
        print("You go first!")                              #user가 먼저 시작 후 cnt+1
        time.sleep(0.5)
        user_turn(user, board)
        cnt+=1
    else:                                                    #ai 가 X면 반복문 실행
        print("ai go first!")
        time.sleep(0.5)
    while True:                                              #승리자가 나오거나 draw 전까지 반복
        ai_turn(user, ai, board)                              #ai의 차례
        if winner(ai, board):                                 #만약 ai가 승리하면
            print_board(board)                                #보드를 출력하고, 반복문 탈출
            print("You lose the game")
            break
        cnt+=1                                                #ai 차례 후 cnt+1
        if cnt>=9:                                            #만약 cnt=9 이면(=앞에서 승리하지 않았고, 모든 수를 보드에 두면)
            print("draw")                                     #무승부를 출력, 반복문 탈출
            break
        user_turn(user, board)                                 #user의 차례
        if winner(user, board):                                #만약 user가 승리하면
            print_board(board)                                 #보드를 출력하고, 반복문 탈촐
            print("You win the game!")
            break
        cnt+=1                                                 #user 차례 후 cnt+1
        if cnt>=9:                                             #만약 cnt=9 이면(=앞에서 승리하지 않았고, 모든 수를 보드에 두면)
            print("draw")                                      #무승부를 출력, 반복문 탈출
            break
    re=input("Will you play again? yes / no ")             #게임이 끝나면 게임을 다시할지 입력
    if not re=='yes':                                         #yes를 입력하지 않으면 게임을 종료
        print('')
        break
print("\nGame Over")
