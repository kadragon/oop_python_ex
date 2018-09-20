# coding: utf-8

# In[3]:


# Tic Tac Toe _ protype 
import copy
import random

MAP = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]  # tic Tac Toe map
match = {1: [0, 0], 2: [0, 1], 3: [0, 2], 4: [1, 0], 5: [1, 1], 6: [1, 2], 7: [2, 0], 8: [2, 1],
         9: [2, 2]}  # 숫자와 접근하고자 하는 맵의 좌표 매칭
AI_set_1 = [1, 3, 7, 9]
AI_set_2 = [2, 4, 6, 8]
AI_set_3 = [5]


def choose_icon():  # 유져의 아이콘 정하기

    repeat_icon = 1

    while repeat_icon == 1:  # 원하는 형식의 문자를 입력할 때 때 까지 반복
        u_icon = input("Choose the icon X or @: ").upper()
        if u_icon == '@' or u_icon == 'X':
            repeat_icon = 0
        else:
            print("It's wrong form, input again")

    if u_icon == '@':
        A_icon = 'X'
    else:
        A_icon = '@'

    return [u_icon, A_icon]


def make_interface():  # 인터페이스 로딩
    print("""TIC TAC TOE!!!!
    @or X를 선택하고 번갈아가면서 3x3 칸에서 @,X를 두게 됩니다. 이때 먼저 빙고를 맞추면 승리입니다
    =============
    = 1 = 2 = 3 =
    =============
    = 4 = 5 = 6 =
    =============
    = 7 = 8 = 9 =
    =============
    각 숫자가 써있는 위치에 말을 놓기위해선 각 위치에 맞는 숫자를 입력하시면 됩니다! \n""")


def draw_map():
    print("=" * 13)
    print("= " + (MAP[0][0] if MAP[0][0] != 0 else " ") + " = " + (MAP[0][1] if MAP[0][1] != 0 else " ") + " = " + (
        MAP[0][2] if MAP[0][2] != 0 else " ") + " =")
    print("=" * 13)
    print("= " + (MAP[1][0] if MAP[1][0] != 0 else " ") + " = " + (MAP[1][1] if MAP[1][1] != 0 else " ") + " = " + (
        MAP[1][2] if MAP[1][2] != 0 else " ") + " =")
    print("=" * 13)
    print("= " + (MAP[2][0] if MAP[2][0] != 0 else " ") + " = " + (MAP[2][1] if MAP[2][1] != 0 else " ") + " = " + (
        MAP[2][2] if MAP[2][2] != 0 else " ") + " =")
    print("=" * 13)


def choose_u_number(number_list):  # 유져의 숫자 선택

    repeat_number = 1
    while repeat_number == 1:
        u_num = int(input("choose the number that you want to set the icon: "))

        if u_num in number_list:  # 입력 가능한 숫자인지 확인
            repeat_number = 0
        else:
            print("you can't set the icon in that block, try again!")

    return u_num


def choose_A_number(number_list, user_icon, AI_icon):
    for i in number_list:  # i 는 놓을 수 있는 공간의 숫자(놓을 수 없는 자리는 이미 걸러짐)
        new_map = copy.deepcopy(MAP)  # 시험 해 볼 맵을 로드함
        temp = match[i]
        new_map[temp[0]][temp[1]] = AI_icon
        if judge_win(new_map):
            return i

    for i in number_list:  # i 는 놓을 수 있는 공간의 숫자(놓을 수 없는 자리는 이미 걸러짐)
        new_map = copy.deepcopy(MAP)  # 시험 해 볼 맵을 로드함
        temp = match[i]
        new_map[temp[0]][temp[1]] = user_icon
        if judge_win(new_map):
            return i

    random.shuffle(AI_set_1)
    random.shuffle(AI_set_2)

    for i in AI_set_1:
        if i in number_list:
            return i

    for i in AI_set_2:
        if i in number_list:
            return i

    for i in AI_set_1:
        if i in number_list:
            return i


def Draw(input_num, input_icon):
    Temp = match[input_num]  # 좌표를 임시로 Temp에 지정
    MAP[Temp[0]][Temp[1]] = input_icon  # 아이콘을 맵에 저장


def judge_win(Map):
    if (Map[0][0] == Map[0][1] == Map[0][2] != 0) or (Map[1][0] == Map[1][1] == Map[1][2] != 0) or (
            Map[2][0] == Map[2][1] == Map[2][2] != 0) or (Map[0][0] == Map[1][0] == Map[2][0] != 0) or (
            Map[0][1] == Map[1][1] == Map[2][1] != 0) or (Map[0][2] == Map[1][2] == Map[2][2] != 0) or (
            Map[0][0] == Map[1][1] == Map[2][2] != 0) or (Map[2][0] == Map[1][1] == Map[0][2] != 0):
        return 1
    else:
        return 0


play_again = 'yes'
while play_again == 'yes' or play_again == 'y':

    make_interface()

    icon = choose_icon()  # 유져와 AI 아이콘 정하기
    user_icon = icon[0]
    AI_icon = icon[1]

    number_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]  # 입력할 수 있는 자리의 숫자

    end = 0  # 틱택토가 끝나면 end = 1로 바꿈
    while end == 0:

        draw_map()

        if number_list == []:  # 무승부인지 판단
            end = 1
            print("DRAW!!")
            draw_map()
            continue

        user_num = choose_u_number(number_list)  # 유져의 숫자 선택
        number_list.remove(user_num)  # 유져가 선택한 숫자 배열에서 제거
        Draw(user_num, user_icon)  # 맵과 유져가 선택한 숫자 매칭
        end = judge_win(MAP)  # 이겼으면 판별하고 함수를 끝내줌
        if end == 1:
            print("You win!!")
            draw_map()
            continue

        if number_list == []:  # 무승부인지 판단
            end = 1
            print("DRAW!!")
            draw_map()
            continue

        AI_num = choose_A_number(number_list, user_icon, AI_icon)  # AI 숫자 선택
        number_list.remove(AI_num)  # AI가 선택한 숫자 배열에서 제거
        Draw(AI_num, AI_icon)  # 맵과 유져가 선택한 숫자 매칭
        end = judge_win(MAP)  # 이겼으면 판별하고 함수를 끝내줌
        if end == 1:
            print("You lose!!")
            draw_map()

    # for row in MAP:
    #    print(row)

    MAP = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]  # 맵 리셋

    play_again = input("Do you want to play again? (yes or no): ")
