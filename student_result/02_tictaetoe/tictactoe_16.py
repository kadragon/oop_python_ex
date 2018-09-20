import random

# 처음 시작 화면 출력하기(각 위치는 1~9의 숫자로 지정)
def display_intro():
    print('\n'*15)
    print('-'*50)
    print("""
        Let's Tic-Tac-Toe Game!
    Enter the coordinate with number.
    <The Coordinate of Each position> 
              1  |  2  |  3  
            -----------------
              4  |  5  |  6 
            -----------------
              7  |  8  |  9  
    """)
    print('-'*50)

# 현재 보드판 상황 출력하기
def display_board():
    print("""
      %c  |  %c  |  %c  
    ------------------
      %c  |  %c  |  %c  
    ------------------
      %c  |  %c  |  %c 
    """ %(pos[1], pos[2], pos[3], pos[4], pos[5], pos[6], pos[7], pos[8], pos[9]))

# 플레이어가 선택한 표식 입력받기
def player_Mark():
    m = input('Choose your marker, O or X : ')   # 입력한 표식을 m에 저장하기
    if m == 'O' or m == 'o':                        # O 또는 o 입력시 플레이어 마커는 O, Com 마커는 X
        print("You : O , Com : X")
        return 'O','X'
    elif m == 'X' or m == 'x':                      # X 또는 x 입력시 플레이어 마커는 X, Com 마커는 O
        print("You : X , Com : O")
        return 'X','O'
    else:                                            # 잘못 입력했을 때 재귀적으로 호출하여 다시 입력받기
        print("Something wrong. Enter again.")
        return player_Mark()

# 플레이어가 표식을 놓을 위치 입력받기
def get_value():
    try:
        a = int(input('Enter the position number: '))
        if a < 1 or a > 9:                                                  # 위치는 1~9의 숫자로 지정되어 있음
            print("Hey, you entered the wrong value! enter again!")
            return get_value()
        elif pos[a] != ' ':                                                 # 이미 표식이 있는 곳에 또 놓을 수 없도록 하기
            print("Hey, you can't put your marker there. enter again!")
            return get_value()
        else:
            return a
    except TypeError as e:                                                  # TypeError 발생시 e로 저장한 뒤 값 다시 받기
        print("Hey, you entered the wrong value! enter again!")
        return get_value()
    except ValueError as e:                                                 # ValueError 발생시 e로 저장한 뒤 값 다시 받기
        print("Hey, you entered the wrong value! enter again!")
        return get_value()

# 결과 판정하기
def ending(mark, mark_Com):
    # 가운데 5 위치를 기준으로 상하좌우 대각선 중 3개 모두 일치한 것이 있는지 판별하기(1,5,9 / 2,5,8 / 3,5,7 / 4,5,6)
    for i in range(1,5):
        if pos[5] == mark_Com and pos[5+i] == mark_Com and pos[5-i] == mark_Com:
            print('\nHAHAHA! You lose!')
            return 0
        elif pos[5+i] == mark and pos[5-i] == mark and pos[5] == mark:
            print('\nWow! You Win!')
            return 0

    # 중심을 제외한 가장자리에서 일어날 수 있는 결과 중 3개 모두 일치하는 것이 있는지 판별하기(1,2,3 / 1,4,7 / 3,6,9 / 7,8,9)
    for i in (1, 9):
        for j in (3, 7):
            if pos[i] == mark_Com and pos[j] == mark_Com and pos[int((i+j)/2)] == mark_Com:
                print('\nSo stupid... You lose')
                return 0
            elif pos[i] == mark and pos[j] == mark and pos[int((i+j)/2)] == mark:
                print('\nWow! You Win!')
                return 0

    temp = 0    # 1~9 위치 중 문자가 있으면 temp를 1 증가시켜, 모든 문자가 있고(temp==9) 끝나지 않았다면 비긴 결과를 출력하기
    for i in range(1,10):
        if pos[i] != ' ':
            temp += 1
    if temp == 9:
        print('Draw')
        return 1
    else:
        return 1

def run_Ai(mark, mark_Com):
    # 가운데 5 위치를 기준으로 상하좌우 대각선 중 공격 포인트 탐색하기
    for i in range(-4, 5):
        # 가운데에 Com 표식이 있고 가장자리에 Com 표식이 있으면 가운데를 중심으로 점대칭적인 위치에 Com 표식을 놓을 수 있는지 판별한 뒤 공격하기
        if i != 0 and pos[5] == mark_Com and pos[5+i] == mark_Com and pos[5-i] == ' ':
            return 5-i
        # 가운데에 표식이 없지만 가운데를 중심으로 서로 점대칭적인 위치에 Com 표식이 있으면 가운데에 Com 표식 놓아 공격하기
        elif i != 0 and pos[5] == ' ' and pos[5+i] == mark_Com and pos[5-i] == mark_Com:
            return 5

    # 꼭짓점 부근을 탐색하여 이웃한 두 꼭짓점에 모두 Com 표식이 있을 때 그 사이에 있는 위치가 비었다면 표식을 놓아 공격하기
    for i in (1, 9):
        for j in (3, 7):
            if pos[i] == mark_Com and pos[j] == mark_Com and pos[int((i+j)/2)] == ' ':
                return int((i+j)/2)

    # 가운데 5 위치를 기준으로 상하좌우 대각선 중 수비 포인트 탐색하기
    for i in range(-4, 5):
        # 가운데에 플레이어 표식이 있고 가장자리에 플레이어 표식이 있으면 가운데를 중심으로 점대칭적인 위치에 Com 표식을 놓을 수 있는지 판별한 뒤 방어하기
        if i != 0 and pos[5] == mark and pos[5+i] == mark and pos[5-i] == ' ':
            return 5-i
        # 가운데에 표식이 없지만 가운데를 중심으로 서로 점대칭적인 위치에 플레이어 표식이 있으면 가운데에 Com 표식 놓아 방어하기
        elif i != 0 and pos[5] == ' ' and pos[5+i] == mark and pos[5-i] == mark:
            return 5

    # 꼭짓점 부근을 탐색하여 이웃한 두 꼭짓점에 플레이어 표식이 있을 때 그 사이에 있는 위치가 비었다면 표식을 놓아 방어하기
    for i in (1, 9):
        for j in (3, 7):
            if pos[i] == mark and pos[j] == mark and pos[int((i+j)/2)] == ' ':
                return int((i+j)/2)

    # 모든 상황을 만족하지 않으면 유리하게 꼭짓점 선점하기
    for i in (1, 3, 7, 9):
        if pos[i] == ' ':
            return i
    # 꼭짓점 부근이 모두 채워져있다면 각 모서리의 가운데 부근과 가운데 부분 중 빈 공간에 두기
    for i in (5, 2, 4, 6, 8):
        if pos[i] == ' ':
            return i

# 게임을 실행하는 함수
def play_Game():
    global pos
    chance = 0                          # 시행 횟수
    end = 1                             # 결과 판별을 위한 변수
    turn = random.randint(0,1)          # 순서 정하기
    mark, mark_Com = player_Mark()      # 표식 정하기
    while chance < 9 and end == 1:
        chance += 1
        if turn == 1:                   # 플레이어 차례
            print("[Your turn]")
            n = get_value()             # 위치 입력값 저장
            pos[n] = mark
            turn = 0                    # 다음은 컴퓨터 차례
        else :                          # 컴퓨터 차례
            print("[Computer's turn]")
            n = run_Ai(mark, mark_Com)
            pos[n] = mark_Com           # 위치 판단값 저장
            turn = 1                    # 다음은 플레이어 차례
        display_board()                 # 현재 보드 상황 출력
        end = ending(mark, mark_Com)    # 결과 판단

play_again = 'yes'
while play_again == 'yes' or play_again == 'y':                           # 리플레이 진행
    pos = [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']            # 값들 초기화
    display_intro()
    play_Game()
    print('\n' + ('=' * 60))
    play_again = input('Do you want to play again? (yes or no): ')     # 플레이어가 다시 플레이할지 입력받기

