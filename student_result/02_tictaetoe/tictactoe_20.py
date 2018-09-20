import random
import copy
import time


def printline(gamenow):
    #틱택토 배열을 출력한다.
    print()
    print("-----------------")
    print(" %2s  | %2s  | %2s" % (gamenow[0][0],gamenow[0][1],gamenow[0][2]))
    print("-----------------")
    print(" %2s  | %2s  | %2s" % (gamenow[1][0], gamenow[1][1], gamenow[1][2]))
    print("-----------------")
    print(" %2s  | %2s  | %2s" % (gamenow[2][0], gamenow[2][1], gamenow[2][2]))
    print("-----------------")
    print()

def clearmatrix(matrix):
    #틱택토 배열을 초기화한다.
    for i in range(3):
        for j in range(3):
            matrix[i][j] = ' '

def checkwin(arr):
    #경기가 종료되었는지 확인한다. 모든 경우 탐색
    win='n'
    cnt=0
    for i in range(0,9):
        if matrix[i // 3][i % 3]!=' ':
            cnt+=1
    if cnt==9 and matrix[1][1]!=' ':
        win='f'
    for i in range(0,3):
        if arr[i][1]==arr[i][2] and arr[i][0]==arr[i][1] and arr[i][0]!=' ':
            win=arr[i][0]
        if arr[1][i]==arr[2][i] and arr[0][i]==arr[1][i] and arr[0][i]!=' ':
            win=arr[0][i]
    if arr[0][0]==arr[1][1] and arr[0][0]==arr[2][2] and arr[0][0]!=' ':
        win=arr[1][1]
    if arr[2][0]==arr[1][1] and arr[1][1]==arr[0][2] and arr[1][1]!=' ':
        win=arr[1][1]
    return win

def emptycheck(matrix,i):
    #그 자리에 수를 놓을 수 있는가?에 대해 탐색한다.
    if matrix[i//3][i%3]==' ':
        return True
    else:
        return False

def playcom(arr, player):
    #컴퓨터 차례를 진행한다
    ans=100
    for i in range(0,9): #이길 수 있는 수를 찾는다 // 이길 수 있는 최선의 수로 가져간다.
        temp = copy.deepcopy(arr)
        if emptycheck(temp,i):
            temp[i // 3][i % 3] = com
            if checkwin(temp)=='X' or checkwin(temp)=='O':
                print("Maybe I won!")
                time.sleep(1)
                ans=i
                break
    for i in range(0,9): #방어의 수를 찾는다
        temp = copy.deepcopy(arr)
        if emptycheck(temp,i):
            temp[i // 3][i % 3] = player
            if checkwin(temp)=='X' or checkwin(temp)=='O':
                if ans==100:
                    print("Hmmm. Defense")
                    time.sleep(1)
                    ans=i
    if ans==100: #두 수가 없으면 아무거나 선택!
        ans=random.randrange(0,9)
    return ans #반환

name="TicTacToe"# 시작 세팅
matrix = [[0]*3 for i in range(3)]
for i in range(0,9):
    matrix[i//3][i%3]=name[i]
print("Welcome to Tic-Tac-Toe game")
printline(matrix)
input("Press enter to start!\n")

#게임 시작 : 좌표 안내
for i in range(0,9):
    matrix[i//3][i%3]=i
printline(matrix)
print("It's coordinate!\nGood Luck!\n")

#배열 초기화
clearmatrix(matrix)

#약간의 기다림...
time.sleep(1)
print("Loading....\n")
time.sleep(2)

#게임의 루프
while(True):
    player=random.randrange(0,2) #먼저 시작 결정
    turn=player
    if player==1:
        player='X'
        com='O'
    else:
        player='O'
        com='X'
    if player=='X':
        print("You start first!")
        print("You are 'X'")
    else:
        print("Computer starts first.")
        print("You are 'O'")
    printline(matrix) #현 상황 보여주기

    while(True): #본 게임 시작        
        
        if turn == 1:
            while (True):#사용자 턴
                where = input("What's your choice? : ")
                if where.isdigit() and len(where) == 1:
                    where = int(where)
                    if where != 9 and emptycheck(matrix,where):
                        matrix[where // 3][where % 3] = player
                        turn = 0
                        break
                print("Wrong Input! Retry!")

        elif turn == 0:
            print("Computer's turn, Wait for a While.....")
            time.sleep(1)
            while(True):#컴퓨터 턴
                where=playcom(matrix,player)
                if emptycheck(matrix,where):
                    matrix[where // 3][where % 3] = com
                    turn = 1
                    break
                
        printline(matrix) #현 상황 보여주기
        
        time.sleep(0.5)
        print("Game Checking.....\n")
        time.sleep(0.8)
        
        if checkwin(matrix) != 'n':# 경기 종료
            printline(matrix)
            win = checkwin(matrix)
            if win == player:
                print("%c Won! Congratulations" % player)
            elif win == 'f':
                print("Draw, nobody won")
            else:
                print("%c Won! You Loser!" % com)
            break
        
    print("Press 1 to play again. Else to quit") # 재시작
    re=input()
    if re=='1':
        print("Game Reset.... Wait for a while......\n")
        time.sleep(1)
        clearmatrix(matrix) #배열 초기화
    else:
        break
