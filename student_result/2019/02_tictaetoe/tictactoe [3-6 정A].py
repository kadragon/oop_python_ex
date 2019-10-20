# 랜덤으로 순서를 결정하기 위해 random 을 import 한다.
import random
from time import sleep

arr = [" ", " ", " ", " ", " ", " ", " ", " ", " ", " "]  # O 또는 X 가 표시된다.
number = list(range(1, 10))  # 1부터 9의 값을 저장해 놓은 리스트
user = 'OX'  # 사용자의 모양을 저장해놓는 변수
com = 'XO'  # 컴퓨터의 모양을 저장해놓는 변수
flag = False  # 게임 전체를 반복하는 while 문을 탈출하기 위한 변수
next = True  # 다음 차례가 누구인지 구별하기 위한 변수
flag2 = True  # 게임이 한 차례 끝나면 반복되는 while 문을 탈출하기 위한 변수
count = 0  # 총 플레이한 횟수
win = 0  # 승리한 횟수


# winrate 함수 : 게임 플레이 횟수와 승리한 횟수를 기록한다.
def winrate(result):
    global win, count
    if result:
        win += 1
        count += 1
    else:
        count += 1


# select 함수 : 사용자로부터 O or X 의 표식을 선택할 수 있게 한다.
def select():
    global user
    global com
    user = input()
    user = user.upper()
    if user == 'O':
        print("You select O")
        com = 'X'
    elif user == 'X':
        print("You select X")
        com = 'O'
    else:
        print("You must select O or X\nPlease select again!")
        select()


# board 함수 : 게임판을 출력한다.
def board():
    global arr
    for i in range(3):
        print("|", end='')
        for j in range(3):
            print(" %s |" % arr[i * 3 + j + 1], end='')
        print()
    print("=" * 25)


# playmore 함수 : 다시 플레이 할지를 물어본다.
def playmore():
    print("Want to play more? Y/N")
    global flag
    ans = input()
    ans = ans.upper()
    if ans == 'Y':  # 다시 플레이 하는 경우 게임에 필요한 리스트와 배열들을 초기화 한다.
        global number, arr
        arr = []
        for _ in range(10):
            arr.append(" ")
        number = list(range(1, 10))
        flag = False
    elif ans == 'N':
        flag = True
    else:
        print("Please Type Y / N")
        playmore()


# check 함수 : 보드판이 승리조건을 만족했는지 매번 확인한다.
# 게임이 끝났다고 판단되면 다시 할 것인지를 묻는 playmore 함수를 호출한다.
def check():
    global flag2, win
    for i in range(1, 4):
        if arr[i] == arr[i + 3] and arr[i + 3] == arr[i + 6] and arr[i] in ['O', 'X']:
            print("Game End")
            if user == arr[i]:
                print("You Win")
                winrate(True)
            else:
                print("You Lose")
                winrate(False)
            flag2 = False
            break
        elif arr[3 * i - 2] == arr[3 * i - 1] and arr[3 * i - 1] == arr[3 * i] and arr[3 * i - 2] in ['O', 'X']:
            print("Game End")
            if user == arr[3 * i - 2]:
                print("You Win")
                winrate(True)
            else:
                print("You Lose")
                winrate(False)
            flag2 = False
            break
        elif arr[1] == arr[5] and arr[5] == arr[9] and arr[1] in ['O', 'X']:
            print("Game End")
            if user == arr[1]:
                print("You Win")
                winrate(True)
            else:
                print("You Lose")
                winrate(False)
            flag2 = False
            break
        elif arr[3] == arr[5] and arr[5] == arr[7] and arr[3] in ['O', 'X']:
            print("Game End")
            if user == arr[2 * i + 1]:
                print("You Win")
                winrate(True)
            else:
                print("You Lose")
                winrate(False)
            flag2 = False
            break


# 사용자가 게임판에 입력할 수 있게 해주는 함수
def userappend():
    global user, arr, number, next
    print("선택 가능한 번호")
    print(number)
    try:
        tmp1 = int(input())
        if tmp1 in number:
            number.remove(tmp1)
            print(number)
            print(user)
            arr[tmp1] = user
            board()
            check()  # 게임이 끝났다면 playmore 함수를 호출한다.
            next = True
        else:
            print("You can't select there!\nPlease select again...")
            userappend()

    except Exception:
        print("You must select number!")
        userappend()


# 컴퓨터가 게임을 진행하는 함수
# 우선 게임을 종료시킬 수 있는 수가 있는지를 살피고, 없으면 랜덤으로 선택한다.
def comappend():
    global com, arr, number, next
    print("제 차례네요!")
    sleep(1)

    # 가로 승리조건 보기
    if arr[1] == arr[2] and arr[1] in ['O', 'X'] and 3 in number:
        arr[3] = com
        number.remove(3)
    elif arr[2] == arr[3] and arr[2] in ['O', 'X'] and 1 in number:
        arr[1] = com
        number.remove(1)
    elif arr[4] == arr[5] and arr[4] in ['O', 'X'] and 6 in number:
        arr[6] = com
        number.remove(6)
    elif arr[5] == arr[6] and arr[5] in ['O', 'X'] and 4 in number:
        arr[4] = com
        number.remove(4)
    elif arr[7] == arr[8] and arr[7] in ['O', 'X'] and 9 in number:
        arr[9] = com
        number.remove(9)
    elif arr[8] == arr[9] and arr[8] in ['O', 'X'] and 7 in number:
        arr[7] = com
        number.remove(7)
    elif arr[1] == arr[3] and arr[1] in ['O', 'X'] and 2 in number:
        arr[2] = com
        number.remove(2)
    elif arr[4] == arr[6] and arr[4] in ['O', 'X'] and 5 in number:
        arr[5] = com
        number.remove(5)
    elif arr[7] == arr[9] and arr[7] in ['O', 'X'] and 8 in number:
        arr[8] = com
        number.remove(8)
    # 세로 승리조건 보기
    elif arr[1] == arr[4] and arr[1] in ['O', 'X'] and 7 in number:
        arr[7] = com
        number.remove(7)
    elif arr[4] == arr[7] and arr[4] in ['O', 'X'] and 1 in number:
        arr[1] = com
        number.remove(1)
    elif arr[2] == arr[5] and arr[2] in ['O', 'X'] and 8 in number:
        arr[8] = com
        number.remove(8)
    elif arr[5] == arr[8] and arr[5] in ['O', 'X'] and 2 in number:
        arr[2] = com
        number.remove(2)
    elif arr[3] == arr[6] and arr[3] in ['O', 'X'] and 9 in number:
        arr[9] = com
        number.remove(9)
    elif arr[6] == arr[9] and arr[6] in ['O', 'X'] and 3 in number:
        arr[3] = com
        number.remove(3)
    elif arr[1] == arr[7] and arr[1] in ['O', 'X'] and 4 in number:
        arr[4] = com
        number.remove(4)
    elif arr[2] == arr[8] and arr[2] in ['O', 'X'] and 8 in number:
        arr[5] = com
        number.remove(5)
    elif arr[3] == arr[9] and arr[3] in ['O', 'X'] and 6 in number:
        arr[6] = com
        number.remove(6)
    # 대각선 승리조건 보기
    elif arr[1] == arr[5] and arr[1] in ['O', 'X'] and 9 in number:
        arr[9] = com
        number.remove(9)
    elif arr[5] == arr[9] and arr[5] in ['O', 'X'] and 1 in number:
        arr[1] = com
        number.remove(1)
    elif arr[3] == arr[5] and arr[3] in ['O', 'X'] and 7 in number:
        arr[7] = com
        number.remove(7)
    elif arr[5] == arr[7] and arr[5] in ['O', 'X'] and 3 in number:
        arr[3] = com
        number.remove(3)
    elif arr[1] == arr[9] and arr[1] in ['O', 'X'] and 5 in number:
        arr[5] = com
        number.remove(5)
    elif arr[3] == arr[7] and arr[3] in ['O', 'X'] and 5 in number:
        arr[5] = com
        number.remove(5)
    else:
        i = number[random.randrange(len(number))]
        arr[i] = com
        number.remove(i)

    board()
    check()  # 게임이 끝났다면 playmore 함수를 호출한다.
    next = False


# turn 함수 : 랜덤으로 순서를 결정해준다.
def turn():
    i = random.randrange(2)
    if i == 0:
        print("먼저 시작하세요!")
        board()
        print("1~9의 번호를 입력하면 됩니다.")
        userappend()
    else:
        print("제가 먼저 시작하겠습니다!")
        board()
        comappend()


while True:
    print("TicTacToe Game Start!\nPlease select O / X\n")
    select()
    print("Game Start!")
    turn()
    flag2 = True
    while flag2:
        if len(number) == 0:
            print("비겼네요!")
            winrate(False)
            break
        elif next:
            comappend()
        else:
            userappend()
    print("당신의 승률은 %.2f%%입니다." % ((win / count) * 100))
    playmore()
    if flag:
        exit()
