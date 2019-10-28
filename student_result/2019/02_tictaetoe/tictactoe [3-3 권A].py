import random
import copy

w = 0
t = 0
l = 0

print("Let's play Tic Tac Toe!")
print("X goes first! O goes last!")


def printpresent(alist):  # 화면에 현재 상태를 출력하는 기능
    for i in [0, 3, 6]:
        for j in [0, 1, 2]:
            if j != 0:
                print(" |", end='')
            print(' ' + alist[i + j], end='')
        print()
        print('-' * 12)


def compter(alist, struse, strcom):  # 컴퓨터가 다음 둘 곳을 판단하는 기능
    a = list(range(0, 9))  # a = [ 0, 1, 2, 3, 4, 5, 6, 7 ,8 ]
    random.shuffle(a)  # a를 랜덤하게 배열
    t = 10
    cp = copy.copy(alist)  # 현 게임판 복사
    for i in range(0, 9):
        if cp[i] == ' ':
            cp = copy.copy(alist)  # cp를 현 게임판으로 초기화
            cp[i] = strcom
            if win(cp, struse, strcom) == 0:  # 컴퓨터가 승리할 수 있는 자리 계산
                t = i
    for i in range(0, 9):
        if cp[i] == ' ':
            cp = copy.copy(alist)
            cp[i] = struse
            if win(cp, struse, strcom) == 1:  # 사용자가 승리할 수 있는 자리 계산
                t = i
    if t == 10:  # 컴퓨터나 사용자가 승리할 수 있는 자리가 없으면 랜덤으로 자리 배치
        for i in a:
            if alist[i] == ' ':
                t = i
    alist[t] = strcom


def check(alist, str):  # 사용자의 위치를 입력 받고 공간을 확인하는 함수
    try:
        print("What is your next move? (1-9)")
        t = int(input())

        while t not in [1, 2, 3, 4, 5, 6, 7, 8, 9]:  # 1~9 제외 다른 숫자 입력 시 재입력
            print("Try again")
            t = int(input())

        while alist[t - 1] != ' ':  # 이미 선택된 자리 입력 시 재입력
            print("Can not be placed")
            print("What is your next move? (1-9)")
            t = int(input())
        alist[t - 1] = str
    except ValueError:  # 사용자가 숫자가 아닌 다른 문자를 입력했을 떄
        print("Try again")
        check(alist, str)


def win(alist, struse, strcom):
    row1 = alist[0:3]
    row2 = alist[3:6]
    row3 = alist[6:9]
    col1 = alist[0:9:3]
    col2 = alist[1:9:3]
    col3 = alist[2:9:3]
    rit = alist[0:9:4]
    lit = alist[2:8:2]

    if row1.count(struse) == 3 or row2.count(struse) == 3 or row3.count(struse) == 3:  # 사용자 가로줄 확인
        return 1
    if col1.count(struse) == 3 or col2.count(struse) == 3 or col3.count(struse) == 3:  # 사용자 세로줄 확인
        return 1
    if rit.count(struse) == 3 or lit.count(struse) == 3:  # 사용자 대각선 확인
        return 1
    if row1.count(strcom) == 3 or row2.count(strcom) == 3 or row3.count(strcom) == 3:  # 컴퓨터 가로줄 확인
        return 0
    if col1.count(strcom) == 3 or col2.count(strcom) == 3 or col3.count(strcom) == 3:  # 컴퓨터 세로줄 확인
        return 0
    if rit.count(strcom) == 3 or lit.count(strcom) == 3:  # 컴퓨터 대각선 확인
        return 0
    else:
        return 2


def again():  # 사용자에게 다시 플레이 할 것인지 물어보는 함수
    print("One more try? Y/N")
    ans = str(input()).upper()
    if ans == 'YES' or ans == 'Y':  # 재시작
        ttt()
    else:  # 끝
        exit()


def report(a, b, c):  # 승률을 기록하는 함수
    global w
    global t
    global l
    w += a  # 승리횟수
    t += b  # 비긴 횟수
    l += c  # 진 횟수
    print("Win : %d Tie : %d Lose %d" % (w, t, l))


def ttt():
    alist = [' '] * 9  # 게임 판
    print("Do you want to be X or O?")  # 사용자의 패 선택
    a = str(input()).upper()
    while a not in ['X', 'O']:  # O, X가 아닌 다른 패를 선택했을 때 재입력
        print("Try again")
        a = str(input()).upper()
    if a == 'X':
        print("--------You go first-------- ")
        b = 'O'
    else:
        b = 'X'
        print("--------Computer goes first-------- ")

    for i in range(0, 9):
        if a == 'X' and i % 2 == 0:  # X가 선, 사용자 입력
            check(alist, a)
        elif a == 'O' and i % 2 == 1:  # O가 후, 사용자 입력
            check(alist, a)
        elif a == 'X' and i % 2 == 1:  # X가 선, 컴퓨터 입력 및 게임 현황 출력
            compter(alist, a, b)
            printpresent(alist)
        elif a == 'O' and i % 2 == 0:  # O가 후, 컴퓨터 입력 및 게임 현황 출력
            compter(alist, a, b)
            printpresent(alist)
        if win(alist, a, b) == 1:  # 사용자 승리
            printpresent(alist)
            print("You win!")
            report(1, 0, 0)  # 승 추가
            again()
        elif win(alist, a, b) == 0:  # 컴퓨터 승리
            print("You lose!")
            report(0, 0, 1)  # 패 추가
            again()

    if a == 'X':
        printpresent(alist)
    print("The game is tie!")  # 비김
    report(0, 1, 0)  # 비김 추가
    again()  # 다시 할 지 묻기


ttt()
