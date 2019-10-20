import copy
import random  # 랜덤으로 순서를 정하기 위해서

arr = [[' ', ' ', ' '], [' ', ' ', ' '], [' ', ' ', ' ']]  # 게임이 이루어질 배열 형성


def select_turn():
    """
    순서를 랜덤으로 결정하는 함수
    사용자 먼저:True
    컴퓨터 먼저:False
    """
    list_1 = [0, 1]
    random.shuffle(list_1)  # [0,1]을 섞는다
    if list_1[0] == 0:  # 첫 원소가 0이면 True, 1이면 False
        return True
    return False


def play(num, char_any):
    """
    말을 둘 수 있는지 판별하고 말을 두는 함수
    :param num:두고자 하는 칸의 숫자
    :param char_any:칸을 채우는 문자
    :return 공백에 두려하면 True, 채워진 칸에 두려하면 False
    """
    if arr[(num - 1) // 3][num % 3 - 1] == ' ':
        arr[(num - 1) // 3][num % 3 - 1] = char_any
        return True
    return False


def check_win():
    """
    승리조건에 맞는지 판별해주는 함수
    가로, 세로 , 대각선 순으로 판별한다.
    :return:이기면 True, 지면 False를 리턴한다.
    """
    for i in range(3):
        if arr[i][0] == arr[i][1] and arr[i][1] == arr[i][2] and arr[i][0] != ' ':  # 가로 판별
            return True
        if arr[0][i] == arr[1][i] and arr[1][i] == arr[2][i] and arr[0][i] != ' ':  # 세로 판별
            return True
    if arr[0][0] == arr[1][1] and arr[1][1] == arr[2][2] and arr[0][0] != ' ':  # 대각선 판별
        return True
    elif arr[0][2] == arr[1][1] and arr[1][1] == arr[2][0] and arr[0][2] != ' ':  # 다른 대각선 판별
        return True
    return False


def printscreen():
    """
    현재 게임이 진행되고 있는 판의 상태를 출력해주는 함수
    """
    print('-' * 13)
    print('  ' + arr[0][0] + ' | ' + arr[0][1] + ' | ' + arr[0][2] + '  ')
    print('-' * 13)
    print('  ' + arr[1][0] + ' | ' + arr[1][1] + ' | ' + arr[1][2] + '  ')
    print('-' * 13)
    print('  ' + arr[2][0] + ' | ' + arr[2][1] + ' | ' + arr[2][2] + '  ')
    print('-' * 13)


def play_pc():
    """
    컴퓨터가 두어야 할 위치를 찾는다.
    컴퓨터의 승리, 사용자의 승리 방해, 모서리 칸, 꼭짓점 칸, 중심 순서대로 둘 칸 판별
    :return: 컴퓨터가 두어야 할 칸의 위치
    """
    for k in range(3):  # 컴퓨터의 승리 조건 판별
        if arr[k][0] == arr[k][1] and arr[k][1] == char_com and arr[k][2] == ' ':
            return 3 * k + 3
        if arr[k][0] == arr[k][2] and arr[k][2] == char_com and arr[k][1] == ' ':
            return 3 * k + 2
        if arr[k][1] == arr[k][2] and arr[k][2] == char_com and arr[k][0] == ' ':
            return 3 * k + 1
        if arr[0][k] == arr[1][k] and arr[1][k] == char_com and arr[2][k] == ' ':
            return 7 + k
        if arr[0][k] == arr[2][k] and arr[2][k] == char_com and arr[1][k] == ' ':
            return 4 + k
        if arr[1][k] == arr[2][k] and arr[2][k] == char_com and arr[0][k] == ' ':
            return 1 + k
    if arr[0][0] == arr[1][1] and arr[1][1] == char_com and arr[2][2] == ' ':
        return 9
    if arr[0][0] == arr[2][2] and arr[2][2] == char_com and arr[1][1] == ' ':
        return 5
    if arr[2][2] == arr[1][1] and arr[1][1] == char_com and arr[0][0] == ' ':
        return 1
    if arr[0][2] == arr[1][1] and arr[1][1] == char_com and arr[2][0] == ' ':
        return 7
    if arr[0][2] == arr[2][0] and arr[2][0] == char_com and arr[1][1] == ' ':
        return 5
    if arr[2][0] == arr[1][1] and arr[1][1] == char_com and arr[0][2] == ' ':
        return 3
    for k in range(3):  # 사용자의 승리 방해
        if arr[k][0] == arr[k][1] and arr[k][1] == char_play and arr[k][2] == ' ':
            return 3 * k + 3
        if arr[k][0] == arr[k][2] and arr[k][2] == char_play and arr[k][1] == ' ':
            return 3 * k + 2
        if arr[k][1] == arr[k][2] and arr[k][2] == char_play and arr[k][0] == ' ':
            return 3 * k + 1
        if arr[0][k] == arr[1][k] and arr[1][k] == char_play and arr[2][k] == ' ':
            return 7 + k
        if arr[0][k] == arr[2][k] and arr[2][k] == char_play and arr[1][k] == ' ':
            return 4 + k
        if arr[1][k] == arr[2][k] and arr[2][k] == char_play and arr[0][k] == ' ':
            return 1 + k
    if arr[0][0] == arr[1][1] and arr[1][1] == char_play and arr[2][2] == ' ':
        return 9
    if arr[0][0] == arr[2][2] and arr[2][2] == char_play and arr[1][1] == ' ':
        return 5
    if arr[2][2] == arr[1][1] and arr[1][1] == char_play and arr[0][0] == ' ':
        return 1
    if arr[0][2] == arr[1][1] and arr[1][1] == char_play and arr[2][0] == ' ':
        return 7
    if arr[0][2] == arr[2][0] and arr[2][0] == char_play and arr[1][1] == ' ':
        return 5
    if arr[2][0] == arr[1][1] and arr[1][1] == char_play and arr[0][2] == ' ':
        return 3
    if arr[0][1] == ' ':  # 모서리 칸
        return 2
    if arr[1][0] == ' ':
        return 4
    if arr[1][2] == ' ':
        return 6
    if arr[2][1] == ' ':
        return 8
    if arr[0][0] == ' ':  # 꼭짓점 칸
        return 1
    if arr[0][2] == ' ':
        return 3
    if arr[2][0] == ' ':
        return 7
    if arr[2][2] == ' ':
        return 9
    if arr[1][1] == ' ':  # 중심
        return 5


def end():
    """
    게임판에 공백이 없을 때 게임을 끝내는 함수
    :return: 게임판에 공백이 없으면 True, 있으면 False
    """
    for k in range(3):
        for l in range(3):
            if arr[k][l] == ' ':
                return False
    return True


def playagain(char_player):
    """
    사용자의 재사용 여부를 판단하는 함수
    :param char_player:재시작 물음에 사용자가 대답한 답변
    :return:다시 할 것이면 True, 그만할 것이면 False
    """
    if char_player in ['Y', 'y', 'yes', 'Yes']:
        return True
    return False


def boardclear():
    """
    게임판을 모두 공백으로 만드는 함수
    """
    for k in range(3):
        for l in range(3):
            arr[k][l] = ' '


def winrate():
    """
    사용자의 승률을 기록하여 출력하는 함수
    """
    winrate_play = win_play / all_games * 100
    print("Winrate: %d" % (winrate_play), end='%')
    print()


win_play = 0  # 사용자의 승리 수
all_games = 0  # 게임한 총 횟수

while True:
    while True:  # O, X 중 말을 선택할 수 있게 하고 다른 것이 입력될 시 제대로 입력을 받을 수 있도록 유도한다.
        mal = input("Please enter your sign(O or X):")
        if mal == 'X':
            char_play = 'X'
            char_com = 'O'
            break
        elif mal == "O":
            char_play = 'O'
            char_com = 'X'
            break
        print("Please type O or X")

    all_games += 1  # 게임한 횟수 1 증가
    printscreen()  # 게임판 출력

    for j in range(9):  # 플레이 순서를 무작위로 정하여 번갈아가면서 게임 시작
        if select_turn() or j:
            print("It's your turn!")
            while True:  # 빈 곳의 수를 입력받아 사용자의 말을 둠
                num_play = input("Enter your number(1~9):")  # 사용자가 두고자 하는 칸 입력받음
                if num_play in ['1', '2', '3', '4', '5', '6', '7', '8', '9']:  # 입력값이 1~9사이 자연수인지 판별
                    if play(int(num_play), char_play):
                        break
                print("Wrong typing!")
            printscreen()  # 게임판 출력
            if check_win():  # 사용자의 승리여부 확인
                print("Congratulation! You win!")
                win_play += 1  # 사용자의 승리 수 1 증가
                break
            if end():  # 게임이 비겼는지 판단
                print("Draw!")
                break
        print("It's pc's turn!")
        play(play_pc(), char_com)  # PC의 착수
        printscreen()  # 게임판 출력
        if check_win():  # PC의 승리여부 확인
            print("Oh! pc win!")
            break
        if end():  # 게임이 비겼는지 판단
            print("Draw!")
            break
    boardclear()  # 게임판 비우기
    winrate()  # 플레이어의 승률 출력
    if not playagain(input("Will you try again?(yes or no):")):  # 사용자의 재시작 여부 확인
        break
