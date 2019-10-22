'''
Title:tictactoe
객체지향프로그래밍 2차 과제 | 틱택토를 만들어 보자
제작자 240* 유**
날짜: 2019.9.28
'''

import random
import copy


def setting():  # 플레이어와 컴퓨터의 아이콘을 지정해주는 함수
    usericon = ''  # 유저의 아이콘을 선언
    count = 1  # 카운트는 유저가 아이콘을 계속해서 잘못 입력할경우 대비하는 상수값
    while usericon != 'O' and usericon != 'X':  # 아이콘 입력이 올바를 때까지
        if count > 10:  # 계속해서 오류형태로 칠경우
            print("그냥 제가 지정해드릴게요;;")  # 임의로 지정
            usericon = random.choice('OX')  # 유저의 아리콘은 O또는 X가 된다.
            break  # 올바르게 지정되었으니 반복문을 나간다.
        if count > 0:  # 일반적으로 입력을 받을 경우
            print("Welcome to Tic Tac Toe!\nDo you want to be X or O?")  # 안내문
            usericon = input().upper()  # 입력값는 값을 대문자로 바꾸어 소문자로 입력하여도 올바르게 처리되도록 함
            count += 1  # 실수하는 정도를 카운트 상수에 저장

    if usericon == 'O':  # 유저의 아이콘이 O인 경우
        return ['O', 'X']  # 항상 유저 아이콘이 리스트의 앞에 있도록 리턴
    else:  # 유저 아이콘이 X라면
        return ['X', 'O']  # X가 리스트 앞에 가도록 하고 리턴


def setboard(board):  # 게임보드의 상태를 보여주는 함수
    print('|' + board[1] + '|' + board[2] + '|' + board[3] + '|')
    print("-------")
    print('|' + board[4] + '|' + board[5] + '|' + board[6] + '|')
    print("-------")
    print('|' + board[7] + '|' + board[8] + '|' + board[9] + '|' + '\n')
    # 보드[1]부터 보드[9]까지 보드 상태를 보여줌


def setfirst():  # 게임 플레이 순서를 정하는 함수)
    first = random.randint(1, 2)  # 이는 setting함수에서 리턴된 리스트를 인덱스로 접근하게함.
    return first  # 인덱스값은 0,1이니 후에 이를 -1처리해줌


def boardisfull(board):  # 게임 보드가 꽉찼는지 확인하는 함수
    for i in range(1, 10):
        if board[i] == ' ':
            return False  # 하나라도 빈칸이 있다면 거짓
    return True  # 꽉 찼다면 참


def loccheck(board, x):  # 현 위치에 아이콘을 놓아도 되는지 판별
    if x < 1 or x > 9:  # 보드 안에 들어가는지 확인
        return False
    elif board[x] != ' ':  # 그 위치에 이미 아이콘이 있는지 확인
        return False  # 있으면 거짓 리턴
    return True  # 그 외에 가능한 경우이니 참값 리턴


def boardcopy(board):  # 게임보드를 복사하는 용도
    return copy.copy(board)  # copy 모듈 사용


def winnercheck(board, icon):  # 현재 보드에서 누가 승자인지 판단하는 함수
    AcroTop = (board[1] == icon and board[2] == icon and board[3] == icon)  # 맨위 가로줄
    AcroMid = (board[4] == icon and board[5] == icon and board[6] == icon)  # 중간 가로줄
    AcroBot = (board[7] == icon and board[8] == icon and board[9] == icon)  # 맨 아래 가로줄
    DownLef = (board[1] == icon and board[4] == icon and board[7] == icon)  # 왼쪽 세로줄
    DownMid = (board[2] == icon and board[5] == icon and board[8] == icon)  # 중간 세로줄
    DownRig = (board[3] == icon and board[6] == icon and board[9] == icon)  # 오른쪽 세로줄
    Diagonal1 = (board[1] == icon and board[5] == icon and board[9] == icon)  # 왼쪽위-오른쪽아래 대각선
    Diagonal2 = (board[3] == icon and board[5] == icon and board[7] == icon)  # 왼쪽아래-오른쪽위 대각선
    return AcroTop or AcroMid or AcroBot or DownLef or DownMid or DownRig or Diagonal1 or Diagonal2
    # 위 경우 중 하나라도 만족한다면 게임 종료 조건에 부합하니 참 값 출력, 그렇지 않으면 거짓 값 출력


def chooseRandomloc(board, moveList):  # 랜덤 위치를 이동하고자 하는 위치에서 뽑아주는 함수
    Moves = []  # 움직일 수 있는 곳
    for i in moveList:  # 움직이고 싶은 곳에 대해 탐색
        if loccheck(board, i):  # 만약 i가 표시사능한 위치이면
            Moves.append(i)  # 움직일 수 있는 곳을 저장하는 리스트에 더함
    if len(Moves) != 0:  # 움직일 수 있는 곳이 있으면
        return random.choice(Moves)  # 그 중 랜덤으로 위치값 리턴
    else:  # 원하는 곳으로 움직일 수 없으면
        return None  # None 리턴


def computer(computericon, board):  # 컴퓨터가 동작하게 하는 함수
    if computericon == 'X':  # 플레이어와 컴퓨터 아이콘 구별 작업
        playericon = 'O'
    else:
        playericon = 'X'
    for i in range(1, 10):  # 게임보드를 탐색
        copiedboard = boardcopy(board)  # 게임보드를 복사하고
        if loccheck(copiedboard, i):  # 복사된 보드에서 임의 위치에 컴퓨터의 아이콘을 표시해도 된다면
            copiedboard[i] = computericon  # 복사된 보드에 컴퓨터의 아이콘을 둬봄
        if winnercheck(copiedboard, computericon):  # 만약 컴퓨터가 이길 수 있는 경우가 있다면
            return i  # 그 위치값을 리턴

    for i in range(1, 10):  # 게임보드를 탐색
        copiedboard = boardcopy(board)  # 게임보드를 복사하고
        if loccheck(copiedboard, i):  # 복사된 보드에서 임의 위치에 플레이어의 아이콘을 표시해도 된다면
            copiedboard[i] = playericon  # 복사된 보드에 플레이어의 아이콘을 둬봄
        if winnercheck(copiedboard, playericon):  # 플레이어가 이기는 수가 있다면
            return i  # 그 경우를 방어하도록 위치값 리턴
    # 한번의 수로 끝날 경우가 아니라면
    move = chooseRandomloc(board, [1, 3, 7, 9])  # 우선적으로 대각선 모서리에 두고자 함
    if move != None:  # 랜덤위치로 움직일 수 있다면
        return move  # 랜덤 위치 리턴
    if loccheck(board, 5):  # 중앙에 둘 수 있다면
        return 5  # 중앙 위치 리턴
    return chooseRandomloc(board, [2, 4, 6, 8])  # 나머지는 2,4,6,8 위치이고 이 중 둘 수 있는 경우가 항상 있으니 랜점함수로 랜덤위치를 리턴


def player(icon, board):  # 플레이어의 동작을 받고 위치값을 리턴하는 함수
    print("어디에 둘까요?")
    flag = True  # 사용자가 올바른 위치값을 두는지 확인하기 위한 부울 값
    while (flag):
        try:  # 우선 입력을 받음
            loc = int(input())
        except Exception:  # 입력 오류가 발생할 셩우 경고문 출력
            print("입력값이 이상합니다! 다시 입력해주세요. 입력값은 1부터 9까지의 자연수중 하나여야 합니다,빈 공간이어야 합니다.")
        else:  # 입력이 올바르면
            if loccheck(board, loc):  # 입력위치에 아이콘을 둘 수 있는지 확인
                flag = False  # 둘 수 있으면 반복문을 나가게끔 부울값 수정
            else:  # 그외는 다시 경고문 출력
                print("입력값이 이상합니다! 다시 입력해주세요. 입력값은 1부터 9까지의 자연수중 하나여야 하며,빈 공간이어야 합니다.")
    return loc


def tutorial():  # 위치정보를 제공함(보드의 인덱스 값)
    print("위치 정보")
    print("-------")
    print("|1|2|3|")
    print("-------")
    print("|4|5|6|")
    print("-------")
    print("|7|8|9|\n")


def regame():  # 게임을 다시할 건지 판단하는 함수
    print("다시 하시겠어요?[Y/N(혹은 아무거나)]")
    ans = input()
    if ans in ['y', 'Y', 'Yes', 'yes']:  # 이 중 한가지 대답일 경우 다시 게임을 플레이하게 함
        return False
    else:  # 그외의 경우 게임을 종료하도록 부울값 리턴
        print("SEE YOU!")
        return True


def WinRate(roundcount, wincount, losecount, drawcount):  # 승률 출력하는 함수
    print('당신의 승률: %.3f' % (wincount / roundcount))  # 승률 출력
    print('전적:%d전 %d승 %d패 %d무' % (roundcount, wincount, losecount, drawcount))  # 전적 출력


# 메인코드
roundcount = 0  # 전체 판수
wincount = 0  # 이긴 횟수
losecount = 0  # 진 횟수
drawcount = 0  # 비긴 횟수

while True:
    roundcount += 1  # 판 횟수추가
    isplayingGame = True  # 한 판의 게임에 대한 부울값
    board = [' ' for i in range(10)]  # 보드 초기화
    iconset = setting()  # 아이콘을 setting함수로 지정
    playericon = iconset[0]  # 항상 사용자 아이콘이 앞이니 다음과 같이 선언가능
    computericon = iconset[1]  # 마찬가지로 컴퓨터 아이콘 선언
    print("플레이어:" + playericon)  # 아이콘 정보 안내
    print("컴퓨터:" + computericon)
    tutorial()  # 보드 위치 정보 출력
    first = setfirst() - 1  # 1혹은 2로 값이 리턴되니 인덱스 범위에 맞게 -1
    Whosturn = False  # 누구의 차례인지 구분하는 부울값
    print(iconset[first] + '이 먼저 시작합니다!')  # 차례 안내

    if iconset[first] == playericon:  # 플레이어 아이콘이 먼저일 경우
        Whosturn = True  # 부울값 수정

    while isplayingGame:
        if Whosturn:  # 플레이어가 먼저일 때
            board[player(playericon, board)] = playericon  # 플레이어에게 위치 입력받고 보드 수정
            Whosturn = False  # 컴퓨터 차례로 전환
        else:  # 컴퓨터 차례
            board[computer(computericon, board)] = computericon  # 컴퓨터가 보드에 아이콘 표시
            Whosturn = True  # 플레이어 차례로 전환
        setboard(board)  # 수정된 게임보드 매턴마다 보여줌
        if winnercheck(board, playericon):  # 플레이어가 이긴 경우
            print("You Win!")
            wincount += 1  # 승리 기록
            isplayingGame = False  # 이번 판은 종료되었기에 부울값 수정
        elif winnercheck(board, computericon):  # 컴퓨터가 이긴경우
            print("You Lose!")
            losecount += 1  # 패배 기록
            isplayingGame = False  # 이번 판은 종료되었기에 부울값 수정
        elif boardisfull(board):  # 비긴 경우
            print("DRAW!")
            drawcount += 1  # 무승부 기록
            isplayingGame = False  # 이번 판은 종료되었기에 부울값 수정
    WinRate(roundcount, wincount, losecount, drawcount)  # 승률 출력
    if regame():  # 판 종료후 다시 게임할 것인지 물어보고 다시할 경우 반복문 계속되며 아닐 경우 반복문 종료
        break
