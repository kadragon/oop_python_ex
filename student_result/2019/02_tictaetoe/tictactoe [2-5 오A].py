import random

gameboard = []  # 게임 판
for i in range(9):
    gameboard.append('-')  # - 로 초기화

win = 0  # 승률 체크를 위한 승리 횟수 저장
lose = 0  # 승률 체크를 위한 패배 횟수 저장
cal = [2, 3, 5, 7, 11, 13, 17, 19, 23]
ans = [30, 1001, 7429, 238, 627, 1495, 506, 935]

"""
기본적인 정답 체크 알고리즘

<cal 리스트>
2   3   5 
7   11  13
17  19  23

열의 곱, 행의 곱, 대각선의 곱을 계산하여 ans 리스트에 저장
Com와 player를 위한 변수를 하나씩 정의하여 선택한 위치의 값들의 곱을 계산
    ps) 이 계산 값들은 player_ans, com_ans 변수에 저장 되어 있음
만약 그 곱이 ans 내부의 리스트 안의 어떤 값의 배수라면 승리!
이는 소수의 성질을 이용한 것임
"""


def intro():
    """
    인트로 부분
    :return: 플레이어의 마크 설정, 선공 후공은 자동 결정됨
    """
    print('This game is Tic Tac Toe.')
    marker = input('what do you want? O or X')
    while True:
        if marker == 'O' or marker == 'X':
            break
        marker = input('what do you want? O or X')
    return marker


def example():
    """
    플레이어의 입력 위치를 알려주기 위한 예시
    :return:
    """
    exgameboard = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
    printgameboard(exgameboard)


def input_player(gb, player_ans):
    """
    플레이어의 입력을 받고, 이를 게임판에 적용

    :param gb: 게임판을 받기
    :param player_ans: 플레이어의 마크가 올라간 위치에 해당되는 소수들의 곱
    :return: player_ans 의 값에 새로 받은 input 값에 해당된 소수까지 곱하여 리턴
    """

    num = input('표시할 위치를 입력하세요. 입력은 1~9의 정수로 이루어집니다.\n입력 : ')
    while True:
        if num == 'LOCATION':
            example()  # 입력하는 방법, 마크를 놓기 위한 입력 위치 보여주기
        if num == 'BOARD':
            printgameboard(gb)  # 현재 게임판 보여주기
        if num.isdigit():  # 입력된 스트링이 숫자로 이루어져있는지 확인
            if 1 <= int(num) <= 9 and gb[int(num) - 1] == '-':  # 그 수는 1에서 9사이이고, 그 수에 해당된 위치는 이미 마크가 올라간 곳이 아닌지 확인
                gb[int(num) - 1] = player  # 플레이어의 마크 올리기
                player_ans *= cal[int(num) - 1]  # player_ans 새로 계산
                print('<PLAYER>')
                printgameboard(gb)  # 게임판 보여주기
                return player_ans
        num = input('비어있는 공간인지, 제대로 입력했는지 확인하세요.\n게임 판을 보려면 BOARD를, 입력 방법을 보려면 LOCATION을 입력하세요')


def input_COM(gb, com_ans, player_ans):
    """
    컴퓨터의 입력 위치를 계산 하는 함수
    :param gb: 현재 게임판
    :param com_ans: 컴퓨터의 마크가 올라간 위치에 해당되는 소수들의 곱
    :param player_ans: 플레이어의 마크가 올라간 위치에 해당되는 소수들의 곱
    :return: com_ans 의 값에 새로 받은 input 값에 해당된 소수까지 곱하여 리턴
    """
    chk = 0  # chk는 차후 입력할 위치를 잠시 저장하는 변수임

    for i in range(9):
        if gb[i] == '-':
            for j in range(8):
                if not (com_ans * cal[i]) % ans[j]:  # 이런 상황이면 컴퓨터의 승리
                    chk = i  # 따라서 이 경우를 chk 변수에 저장
                    break  # 찾자마자 종료

    if not chk:  # 현재 턴에 승리가 불가능할 경우, 방어
        for i in range(9):
            if gb[i] == '-':
                for j in range(8):
                    if not ((player_ans * cal[i]) % ans[j]):  # 이런 상황이면 플레이어의 승리
                        chk = i  # 따라서 이경우를 chk 변수에 저장
                        break  # 찾자마자 종료

    if not chk:  # 현재 턴에 승리, 패배 할 경우 없으면 랜덤히 값을 잡자
        while gb[chk] != '-':  # 빈 곳을 찾을 때까지 계속
            chk = random.randrange(0, 9)  # 0 ~ 8 까지의 값을 계속 랜덤히 입력 받기

    gb[chk] = com  # 이렇게 계산한 값을 넣고
    print('<COM>')
    printgameboard(gb)  # 게임 판 출력
    return com_ans * cal[chk]  # 새로운 com_ans 리턴


def checkcom(com_ans):
    """
    컴퓨터의 승리 확인
    :param com_ans: 컴퓨터의 마크가 올라간 위치에 해당되는 소수들의 곱
    :return: 1이면 승리, 0이면 아직 확인 불가
    """

    for i in range(8):
        if not (com_ans % ans[i]):
            return 1
    return 0


def checkplayer(player_ans):
    """
    플레이어의 승리 확인
    :param player_ans: 플레이어의 마크가 올라간 위치에 해당되는 소수들의 곱
    :return: 1이면 승리, 0이면 아직 확인 불가
    """
    for i in range(8):
        if not (player_ans % ans[i]):
            return 1
    return 0


def drawcheck(gb):
    """
    비긴 판인지 확인
    :param gb: 현재 게임 판
    :return: 1이면 비김, 0이면 아직 확인 불가
    """
    ch = 0

    for i in range(9):  # 판을 돌며
        if gb[i] == '-':  # - 체크
            ch += 1

    if not ch:  # 없으면 1을 리턴
        return 1
    else:  # 한 개 이상이면 0을 리턴
        return 0


def printgameboard(gb):
    """
    현재의 게임판 출력 함수
    :param gb: 현재 게임 판
    """
    # 아름답게 보이기 위한 노력
    print('-' * 16)
    for i in range(9):
        print('  ' + gb[i] + '  ', end='')
        if i % 3 == 2:
            print('\n' + '-' * 16)


def playagain():
    """
    한 판 더할지 결정하는 함수 (baseball 에서 살짝..)
    :return: 1또는 0으로 리턴
    """
    a = input('Play again? Yes or No')
    while 1:
        if a == 'Yes':  # Yes 에서만 1로!
            ag = 1
            break
        elif a == 'No':  # No 에서만 0으로!
            ag = 0
            break
        else:  # 다른 경우 다시 입력받기!
            a = input('Just say Yes or No')
    return ag


def maindish():
    """
    함수의 몸체 부분
    게임의 운영
    :return: 누가 승리자인지 혹은 비겼는지 알 수 있는 변수
    """
    winner = 0  # 승리자가 누구인지 확인
    com_ans = 1  # 컴퓨터의 마크가 올라간 위치에 해당되는 소수들의 곱
    player_ans = 1  # 플레이어의 마크가 올라간 위치에 해당되는 소수들의 곱
    while True:
        if player == 'O':  # 컴퓨터의 선공
            com_ans = input_COM(gameboard, com_ans, player_ans)  # 컴퓨터의 입력
            if checkcom(com_ans):  # 컴퓨터 승리 확인
                winner = 1  # 승리 시, winner에 1을 저장 후, break
                break
            if drawcheck(gameboard):  # 비기는 경우 체크
                winner = 2  # 비겼을 시, winner에 2를 저장후, break
                break
            player_ans = input_player(gameboard, player_ans)  # 플레이어의 입력
            if checkplayer(player_ans):  # 플레이어의 승리 확인
                break  # 승리 시, winner는 여전히 0, break

        else:  # 모두 동일하나, 플레이어의 선공
            player_ans = input_player(gameboard, player_ans)
            if checkplayer(player_ans):
                break
            if drawcheck(gameboard):
                winner = 2
                break
            com_ans = input_COM(gameboard, com_ans, player_ans)
            if checkcom(com_ans):
                winner = 1
                break

    return winner  # winner 변수 리턴


player = intro()

# 플레이어의 반대로 컴퓨터의 마크 결정

if player == 'O':
    com = 'X'
else:
    com = 'O'

while True:
    if player == 'X':
        printgameboard(gameboard)
    whowin = maindish()  # 누구의 승리인지, 비긴 건지 확인
    if whowin == 0:  # 0에서 플레이어의 승리
        print("YOU WIN!!!")
        win += 1
    elif whowin == 1:  # 1에서 컴퓨터의 승리
        print("YOU LOSE!!")
        lose += 1
    else:  # 2에서 비김
        print("DRAW!!")
        win += 1
        lose += 1

    print("승률: %2f %%" % ((win / (win + lose)) * 100))  # 승률 계산

    if not playagain():  # 게임 더 할지 결정
        break

    # 게임 판 다시 초기화

    gameboard = []

    for i in range(9):
        gameboard.append('-')
