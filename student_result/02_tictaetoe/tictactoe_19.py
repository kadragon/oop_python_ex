# WWAAAAAAAA THIS IS ME
# making tictactoe game!
# 201080905 Object-Oriented Programming class
#

import random


def draw_map(map_string):
    """
    map_string, 즉 현재 게임 상황 문자열을 받아
    게임 맵 상태를 출력해준다.

    """
    print('123'
          '456'
          '789')
    print(map_string[1] + '|' + map_string[2] + '|' + map_string[3])
    print('-----')
    print(map_string[4] + '|' + map_string[5] + '|' + map_string[6])
    print('-----')
    print(map_string[7] + '|' + map_string[8] + '|' + map_string[9])


def choose_character():
    """
    사용자가 X또는 O를 고르도록 하는 함수
    :return: 사용자가 고른 캐릭터를 반환
    """
    print('Choose X/O. X goes first.')
    player_character = input().upper()
    while(player_character != 'X' and player_character != 'O'):
        print('please type X, or O')
        player_character = input().upper()

    return player_character


def check_who_won(map_string):
    """
    혹시 누가 이겼나 확인하고 이긴 사람이 있으면 return
    :param map_string: current 게임판
    :return: 누가 이겼는지 X/O, 아무도 이기지 않았다면 ' '(blank)
    """
    if map_string[1] == map_string[2] and map_string[2] == map_string[3]:
        return map_string[1]
    elif map_string[4] == map_string[5] and map_string[5] == map_string[6]:
        return map_string[4]
    elif map_string[7] == map_string[8] and map_string[8] == map_string[9]:
        return map_string[7]
    elif map_string[1] == map_string[4] and map_string[4] == map_string[7]:
        return map_string[1]
    elif map_string[2] == map_string[5] and map_string[5] == map_string[8]:
        return map_string[2]
    elif map_string[3] == map_string[6] and map_string[6] == map_string[9]:
        return map_string[3]
    elif map_string[1] == map_string[5] and map_string[5] == map_string[9]:
        return map_string[1]
    elif map_string[3] == map_string[5] and map_string[5] == map_string[7]:
        return map_string[3]
    else:
        return ' '


def game_over(winner):
    """
    게임 종료 시 실행되어 게임결과를 알려주고,
    재실행 여부를 묻는다.
    :param winner: 이긴 사람. 0이면 플레이어, 1이면 컴퓨터
    :return: 재실행 여부. True or False.
    """
    if winner == 0:
        print("You Won!")
    else:
        print("You Lost.")

    print("Play again?[Y/N]")
    if input().upper() == 'Y':
        print('Restarting the Game...')
        return True
    else:
        print('Game Over. Thanks for playing.')
        return False


def players_turn(map_string):
    """
    플레이어의 차례일 때 실행되는 함수

    :param map_string: 현재 게임 상황_빈칸 확인하려고
    :return: 플레이어가 선정한 숫자 반환
    """
    print('Your Turn. Choose a number to go')
    turn = input()

    while turn not in '1 2 3 4 5 6 7 8 9'.split() or map_string[int(turn)] != ' ':
        print("Please type a number in blank [1~9]")
        turn = input()

    return int(turn)


def computer_go(map_string, moveList):
    """
    컴퓨터가 놓을 수 있는 자리인지 확인하고 그 중에 하나 랜덤으로 리턴
    :param map_string:
    :param moveList:
    :return:
    """
    possibleMoves = []

    for i in moveList:
        if map_string[i] == ' ':
            possibleMoves.append(i)
    if len(possibleMoves) != 0:
        return random.choice(possibleMoves)
    else:
        return 0


def computers_turn(map_string, computer_character):
    """
    컴퓨터 차례에 실행되는 함수
    :param map_string: 게임 상황
    :param computer_character: 컴퓨터 캐릭터가 뭔지 받음
    :return: 컴퓨터가 놓은 자리의 숫자를 반환
    """

    for i in range(1, 10, 1):
        if map_string[i] == ' ':
            map_string[i] = computer_character
            if check_who_won(map_string) != ' ':
                return i
            map_string[i] = ' '

    # 4귀
    move = computer_go(map_string, [1, 3, 7, 9])
    if move != 0:
        return move

    # 4변
    move = computer_go(map_string, [2, 4, 6, 8])
    if move != 0:
        return move

    # 안 되면 중앙을 마지막에
    return 5


while True:     # 무한반복하게 while true
    map_string = [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']
    if choose_character() == 'X':
        player_character = 'X'
        computer_character = 'O'
        turn = 0
    else:
        player_character = 'O'
        computer_character = 'X'
        turn = 1

    game_keep_going = True
    replay = False

    while game_keep_going:
        # 참고로 turn의 값에서 0은 사용자 차례, 1은 컴퓨터 차례임
        if turn == 0:
            # 플레이어 차례
            draw_map(map_string)
            move = players_turn(map_string)
            map_string[move] = player_character

            if check_who_won(map_string) == player_character:
                draw_map(map_string)
                replay = game_over(0)
                game_keep_going = False
                break
            elif check_who_won(map_string) == computer_character:
                draw_map(map_string)
                replay = game_over(1)
                game_keep_going = False
            else:
                turn = 1

        else:
            # 컴퓨터 차례
            move = computers_turn(map_string, computer_character)
            map_string[move] = computer_character

            if check_who_won(map_string) == player_character:
                draw_map(map_string)
                replay = game_over(0)
                game_keep_going = False
                break
            elif check_who_won(map_string) == computer_character:
                draw_map(map_string)
                replay = game_over(1)
                game_keep_going = False
            else:
                turn = 0

        if replay == True:
            break

    if replay == False:
        break