import random  # 리스트의 값을 섞어서 컴퓨터가 임의의 값을 넣을 수 있게 함.

a = ''  # 처음 사용자가 입력하는 기호(변수 선언)
b = list(range(9))  # 판의 번호 의미
c = list(range(9))  # 컴퓨터에서 숫자를 선택할 때 섞이는 번호-1(c의 번호 순서를 바꾼 후 컴퓨터에서 c의 숫자 선택, 0부터 셈)
for i in range(9):
    b[i] = b[i] + 1  # 판의 번호는 편의상 1~9번
if_test = 0  # 컴퓨터가 이기거나 사용자를 막아야 할 때 사용한 if문을 들어갔는지 확인
win = 0  # 누가 이겼는지 판단
user_win = 0  # user가 이긴 횟수
com_win = 0  # 컴퓨어가 이긴 횟수
same = 0  # 비긴 횟수


# rule: 규칙 보여주는 함수
def rules():
    print('규칙\n1. O와 X 중 X 먼저 게임을 시작합니다'
          '\n2. 유저와 컴퓨터가 번갈아서 한 번씩 둡니다'
          '\n3. 3x3 판에서 3개의 연속된 표시가 완성되면 승리합니다'
          '\n4. 3x3 판의 번호를 입력하면 해당 칸이 비어있을 때 선택한 기호를 넣을 수 있습니다'
          '\n5. 판의 번호는 다음과 같습니다')
    for i in range(3):
        print(' %s | %s | %s ' % (b[3 * i], b[3 * i + 1], b[3 * i + 2]))
    print('판의 번호 앞에 0을 붙이면 번호와 같은 것으로 간주합니다(ex: 0005 = 5)')


# rules_test: 처음 입력에서 rules 면 규칙 출력 및 True 반환
def rules_test(input):
    if input == 'rules':
        rules()
        return True
    else:
        return False


# input_test: 처음 입력에서 OX인지 확인(rules인 경우는 rules_test 불러옴)
def input_test(input):
    while not rules_test(input):
        if input.upper() != 'X' and input.upper() != 'O':
            print('O 또는 X를 입력하세요')
            return False
        else:
            return True


# win_test: win 변수를 이용해 누가 이겼는지 판단
def win_test():
    global win
    global user_win
    global com_win
    while e > 4:
        for i in range(3):
            if d[3 * i] == d[3 * i + 1] and d[3 * i] == d[3 * i + 2] and d[3 * i] != ' ':
                print(1)
                if d[3 * i] == a.upper():
                    win = 1
                    user_win += 1
                else:
                    win = 2
                    com_win += 1
                return True

            elif d[i] == d[i + 3] and d[i] == d[i + 6] and d[i] != ' ':
                print(2)
                if d[3 * i] == a.upper():
                    win = 1
                    user_win += 1
                else:
                    win = 2
                    com_win += 1
                return True

        if d[0] == d[4] and d[0] == d[8] and d[0] != ' ':
            print(3)
            if d[0] == a.upper():
                win = 1
                user_win += 1
            else:
                win = 2
                com_win += 1
            return True
        elif d[2] == d[4] and d[2] == d[6] and d[2] != ' ':
            print(4)
            if d[2] == a.upper():
                win = 1
                user_win += 1
            else:
                win = 2
                com_win += 1
            return True

        return False


# com_sym: 컴퓨터의 기호 판단해서 값 넣음(사용자와 다르게 설정)
def com_sym(num):
    if a.upper() == 'X':
        d[num] = 'O'
    else:
        d[num] = 'X'


# com_test: 컴퓨터가 자신이 이길 수 있는 경우나 사용자를 막아야 하는 경우 판단
def com_test():
    global if_test
    for i in range(3):
        if d[3 * i] == d[3 * i + 1] and d[3 * i + 2] == ' ' and d[3 * i] != a.upper() and d[3 * i] != ' ':
            com_sym(3 * i + 2)
            if_test = 1
        elif d[3 * i + 1] == d[3 * i + 2] and d[3 * i] == ' ' and d[3 * i + 1] != a.upper() and d[3 * i + 1] != ' ':
            com_sym(3 * i)
            if_test = 1
        elif d[3 * i] == d[3 * i + 2] and d[3 * i + 1] == ' ' and d[3 * i + 2] != a.upper() and d[3 * i + 2] != ' ':
            com_sym(3 * i + 1)
            if_test = 1
        elif d[i] == d[i + 3] and d[i + 6] == ' ' and d[i] != a.upper() and d[i] != ' ':
            com_sym(i + 6)
            if_test = 1
        elif d[i] == d[i + 6] and d[i + 3] == ' ' and d[i] != a.upper() and d[i] != ' ':
            com_sym(i + 3)
            if_test = 1
        elif d[i + 6] == d[i + 3] and d[i] == ' ' and d[i + 3] != a.upper() and d[i + 3] != ' ':
            com_sym(i)
            if_test = 1
        else:
            if_test = 0

    if if_test != 1:
        if d[0] == d[4] and d[8] == ' ' and d[0] != a.upper() and d[0] != ' ':
            com_sym(8)
            if_test = 2
        elif d[0] == d[8] and d[4] == ' ' and d[0] != a.upper() and d[0] != ' ':
            com_sym(4)
            if_test = 2
        elif d[4] == d[8] and d[0] == ' ' and d[4] != a.upper() and d[4] != ' ':
            com_sym(0)
            if_test = 2
        elif d[2] == d[4] and d[6] == ' ' and d[2] != a.upper() and d[2] != ' ':
            com_sym(6)
            if_test = 2
        elif d[4] == d[6] and d[2] == ' ' and d[4] != a.upper() and d[4] != ' ':
            com_sym(2)
            if_test = 2
        elif d[2] == d[6] and d[4] == ' ' and d[6] != a.upper() and d[6] != ' ':
            com_sym(4)
            if_test = 2

    if if_test != 1 and if_test != 2:
        for i in range(3):
            if d[3 * i] == d[3 * i + 1] and d[3 * i + 2] == ' ' and d[3 * i] == a.upper():
                com_sym(3 * i + 2)
                if_test = 3
            elif d[3 * i + 1] == d[3 * i + 2] and d[3 * i] == ' ' and d[3 * i + 2] == a.upper():
                com_sym(3 * i)
                if_test = 3
            elif d[3 * i] == d[3 * i + 2] and d[3 * i + 1] == ' ' and d[3 * i + 2] == a.upper():
                com_sym(3 * i + 1)
                if_test = 3
            elif d[i] == d[i + 3] and d[i + 6] == ' ' and d[i + 3] == a.upper():
                com_sym(i + 6)
                if_test = 3
            elif d[i] == d[i + 6] and d[i + 3] == ' ' and d[i + 6] == a.upper():
                com_sym(i + 3)
                if_test = 3
            elif d[i + 6] == d[i + 3] == a.upper() and d[i] == ' ':
                com_sym(i)
                if_test = 3

    if if_test != 1 and if_test != 2 and if_test != 3:
        print(2)
        if d[0] == d[4] and d[8] == ' ' and d[0] == a.upper():
            com_sym(8)
            print(1)
            if_test = 4
        elif d[0] == d[8] and d[4] == ' ' and d[8] == a.upper():
            com_sym(4)
            if_test = 4
        elif d[4] == d[8] and d[0] == ' ' and d[8] == a.upper():
            com_sym(0)
            if_test = 4
        elif d[2] == d[4] and d[6] == ' ' and d[4] == a.upper():
            com_sym(6)
            if_test = 4
        elif d[4] == d[6] and d[2] == ' ' and d[4] == a.upper():
            com_sym(2)
            if_test = 4
        elif d[2] == d[6] and d[4] == ' ' and d[2] == a.upper():
            com_sym(4)
            if_test = 4


# com_simin: com_test인 경우가 아닐 때 컴퓨터가 임의의 위치에 값을 넣음
def com_simin():
    random.shuffle(c)
    global if_test
    if e < 8:
        if if_test == 0:
            if d[c[0]] != ' ':
                com_simin()
            else:
                com_sym(c[0])


# com_sel: com_test와 com_simin을 이용해 컴퓨터가 넣는 값을 정해주는 함수
def com_sel(a):
    global if_test
    if a.upper() == 'X' and e == 2:
        print(1)
        com_test()
    elif e >= 4:
        com_test()

    if if_test == 0:
        com_simin()


# user_sel: user가 입력한 값에 대한 판단을 하고 값을 넣는 함수
def user_sel(u, a):
    try:
        if int(u) not in list(range(10)) or int(u) == 0:
            print('1~9까지의 자연수를 입력하십시오')
            u = input()
            user_sel(u, a)
        else:
            if d[int(u) - 1] != ' ':
                print('이미 선택된 칸입니다. 다른 번호를 선택하십시오')
                u = input()
                user_sel(u, a)
            else:
                d[int(u) - 1] = a.upper()
    except Exception:
        print('1~9까지의 자연수를 입력하십시오')
        u = input()
        user_sel(u, a)


# ttt_box: 게임 결과를 출력하는 함수
def ttt_box():
    for i in range(3):
        print(' %s | %s | %s ' % (d[3 * i], d[3 * i + 1], d[3 * i + 2]))


# game: 전체적으로 게임을 실행하는 함수
def game(e):
    if e == 0:
        if a.upper() == 'X':
            print('사용자 먼저 시작합니다. 숫자를 선택하십시오')
            user = input()
            user_sel(user, a)
        else:
            print('컴퓨터 먼저 시작합니다')
    else:
        print('사용자 차례입니다. 숫자를 선택하십시오')
        user = input()
        user_sel(user, a)

    if e < 8:
        com_sel(a)
    elif e == 8 and a.upper() == 'O':
        for i in range(9):
            if d[i] == ' ': d[i] = 'X'
    ttt_box()


# again: 다시할지 알려주는 함수
def again():
    print('게임을 다시 하시겠습니까? 다시 하려면 yes를 입력하세요')  # ~출력
    ans = input()  # 입력받음

    if ans == 'yes':
        return True  # 입력값이 yes 면 True 반환
    else:
        return False  # 나머지면 False 반환


while True:
    print('\ntictactoe 게임을 시작합니다\n')
    rules()
    print('O와 X 중 무엇으로 게임할지 선택하세요\n\nrules를 입력하면 규칙을 볼 수 있습니다.\nO,X 선택 후에는 확인할 수 없습니다')
    d = [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']  # 틱택토 게임의 각 칸을 의미하는 리스트
    e = 0  # 지금까지 몇 번 실행했는지를 확인하는 수(0~8일 때까지만 게임 실행)
    if_test = 0
    win = 0
    a = input()
    while not input_test(a):  # 이상한 값 입력받으면 다시 입력받음
        a = input()
    user = ''  # user가 입력하는 번호

    while e < 9 and not win_test():
        game(e)
        e += 2

    if win == 0:
        print('비겼습니다')
        same += 1
    elif win == 1:
        print('당신이 이겼습니다')
    else:
        print('컴퓨터가 이겼습니다')

    print('지금까지 당신은 %s번, 컴퓨터는 %s번, 비긴 횟수는 %s번 입니다' % (user_win, com_win, same))

    if not again():
        print('게임을 종료합니다')  # 다시 시작하지 않는다고 할 때(yes 입력하지 않은 경우) 게임을 종료합니다 출력
        break  # 출력한 후 종료
