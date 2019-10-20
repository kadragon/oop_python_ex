import random

a = [[0] * 5 for i in range(0, 5)]  # O와 X를 숫자로 저장하는 2차원 리스트
tic_set = [[" "] * 5 for i in range(0, 5)]  # 현재 판의 O와 X를 저장하는 2차원 리스트
order = 0  # 몇번 시행했는지 보여주는 변수
user_order = 0
finish = 0  # 게임이 끝났는지를 알려주는 변수
user_win = 0  # 사용자의 승리 횟수
com_win = 0  # 컴퓨터의 승리 횟수


def rule():  # 규칙을 알려주는 함수
    print("3*3 격자판에 O 또는 X를 입력하기")
    print("먼저 같은 문양으로 한 줄을 만드면 이김")
    print("만약 9칸을 모두 채워도 승부가 갈리지 않으면 무승부")


def choose_shape(user_shape):  # 사용자가 선택한 문양에 따라 컴퓨터의 문양을 결정하는 함수
    if (user_shape == "X"):
        return "O"
    else:
        return "X"


def who_first():  # 선공 결정 게임
    print("1부터 100까지 숫자 중 제가 랜덤으로 하나를 생각할겁니다")
    print("만약 당신이 제가 생각한 숫자와 제가 생각한 숫자의 차이의 절대값이 20이하이면 당신이 선 그게 아닐 경우 제가 먼저 플레이합니다.")
    ran = random.randrange(1, 101)  # 랜덤으로 변수를 하나 입력받음
    use = int(input())
    if (abs(ran - use) <= 20):  # 입력받은 숫자와 랜덤값과 비교
        print("당신이 선")
        return 1
    else:
        print("제가 선")
        return 0


def print_situ():  # 현재 상황을 출력하는 함수
    print("===========")
    print(" %s | %s | %s " % (tic_set[1][1], tic_set[1][2], tic_set[1][3]))
    print("-----------")
    print(" %s | %s | %s " % (tic_set[2][1], tic_set[2][2], tic_set[2][3]))
    print("-----------")
    print(" %s | %s | %s " % (tic_set[3][1], tic_set[3][2], tic_set[3][3]))
    print("===========")


def user_choose(x, y):  # 사용자가 고른 부분을 사용자의 문양으로 채우는 함수
    tic_set[y][x] = user_shape
    a[y][x] = 1  # 사용자가 고른 부분은 1로 저장
    print_situ()  # 현재 상황을 출력


def random_num():  # 컴퓨터가 특별히 막거나 공격할 곳이 없을 때 랜덤으로 입력하는 함수
    ran_x = random.randrange(1, 4)
    ran_y = random.randrange(1, 4)
    if (a[ran_y][ran_x] == 0):  # 이미 있는지 없는지 확인하는 조건문
        tic_set[ran_y][ran_x] = com_shape
        a[ran_y][ran_x] = -1
        print_situ()
    else:
        random_num()


def check():  # 공격하거나 방어하거나 게임이 끝났는지 확인하는 변수
    change = 0  # 공격이나 방어를 했는지 확인하는 변수
    for i in range(1, 9):  # 사용자가 이겼는지 확인하는 반복문, 사용자의 문양을 1로 저장했기 때문에 한줄을 더했을 때 3일 경우 이긴걸로 처리
        k = 0
        if (i == 1):
            for j in range(1, 4):
                k += a[1][j]
            if (k == 3):
                return 1
        if (i == 2):
            for j in range(1, 4):
                k += a[2][j]
            if (k == 3):
                return 1
        if (i == 3):
            for j in range(1, 4):
                k += a[3][j]
            if (k == 3):
                finish = 1
                return
        if (i == 4):
            for j in range(1, 4):
                k += a[j][1]
            if (k == 3):
                return 1
        if (i == 5):
            for j in range(1, 4):
                k += a[j][2]
            if (k == 3):
                return 1
        if (i == 6):
            for j in range(1, 4):
                k += a[j][3]
            if (k == 3):
                return 1
        if (i == 7):
            for j in range(1, 4):
                k += a[j][j]
            if (k == 3):
                return 1
        if (i == 8):
            for j in range(1, 4):
                k += a[j][4 - j]
            if (k == 3):
                return 1
    for i in range(1, 9):  # 공격할 곳이 있는지 확인하는 반복문, 컴퓨터가 -1로 저장했기 때문에 줄을 더했을 때-2면 공격 가능
        k = 0
        if (i == 1):
            for j in range(1, 4):
                k += a[1][j]
            if (k == -2):
                for j in range(1, 4):
                    if (a[1][j] == 0):
                        a[1][j] = -1
                        tic_set[1][j] = com_shape
                        change = 1
                        print_situ()
                return -1
        if (i == 2):
            for j in range(1, 4):
                k += a[2][j]
            if (k == -2):
                for j in range(1, 4):
                    if (a[2][j] == 0):
                        a[2][j] = -1
                        tic_set[1][j] = com_shape
                        change = 1
                        print_situ()
                return -1
        if (i == 3):
            for j in range(1, 4):
                k += a[3][j]
            if (k == -2):
                for j in range(1, 4):
                    if (a[3][j] == 0):
                        a[3][j] = -1
                        tic_set[3][j] = com_shape
                        change = 1
                        print_situ()
                return -1
        if (i == 4):
            for j in range(1, 4):
                k += a[j][1]
            if (k == -2):
                for j in range(1, 4):
                    if (a[j][1] == 0):
                        a[j][1] = -1
                        tic_set[j][1] = com_shape
                        change = 1
                        print_situ()
                return -1
        if (i == 5):
            for j in range(1, 4):
                k += a[j][2]
            if (k == -2):
                for j in range(1, 4):
                    if (a[j][2] == 0):
                        a[j][2] = -1
                        tic_set[j][2] = com_shape
                        change = 1
                        print_situ()
                return -1
        if (i == 6):
            for j in range(1, 4):
                k += a[j][3]
            if (k == -2):
                for j in range(1, 4):
                    if (a[j][3] == 0):
                        a[j][3] = -1
                        tic_set[j][3] = com_shape
                        change = 1
                        print_situ()
                return -1
        if (i == 7):
            for j in range(1, 4):
                k += a[j][j]
            if (k == -2):
                for j in range(1, 4):
                    if (a[j][j] == 0):
                        a[j][j] = -1
                        tic_set[j][j] = com_shape
                        change = 1
                        print_situ()
                return -1
        if (i == 8):
            for j in range(1, 4):
                k += a[j][4 - j]
            if (k == -2):
                for j in range(1, 4):
                    if (a[j][4 - j] == 0):
                        a[j][4 - j] = -1
                        tic_set[j][4 - j] = com_shape
                        change = 1
                        print_situ()
                return -1
    for i in range(1, 9):  # 반어할 곳이 확인하는 반복문, 사용자를 1로 정했기 때문에 줄을 더했을 때 2가 되면 공격 가능
        k = 0
        if (i == 1):
            for j in range(1, 4):
                k += a[1][j]
            if (k == 2):
                for j in range(1, 4):
                    if (a[1][j] == 0):
                        a[1][j] = -1
                        tic_set[1][j] = com_shape
                        change = 1
                        print_situ()
                return 0
        if (i == 2):
            for j in range(1, 4):
                k += a[2][j]
            if (k == 2):
                for j in range(1, 4):
                    if (a[2][j] == 0):
                        a[2][j] = -1
                        tic_set[2][j] = com_shape
                        change = 1
                        print_situ()
                return 0
        if (i == 3):
            for j in range(1, 4):
                k += a[3][j]
            if (k == 2):
                for j in range(1, 4):
                    if (a[3][j] == 0):
                        a[3][j] = -1
                        tic_set[3][j] = com_shape
                        change = 1
                        print_situ()
                return 0
        if (i == 4):
            for j in range(1, 4):
                k += a[j][1]
            if (k == 2):
                for j in range(1, 4):
                    if (a[j][1] == 0):
                        a[j][1] = -1
                        tic_set[j][1] = com_shape
                        change = 1
                        print_situ()
                return 0
        if (i == 5):
            for j in range(1, 4):
                k += a[j][2]
            if (k == 2):
                for j in range(1, 4):
                    if (a[j][2] == 0):
                        a[j][2] = -1
                        tic_set[j][2] = com_shape
                        change = 1
                        print_situ()
                return 0
        if (i == 6):
            for j in range(1, 4):
                k += a[j][3]
            if (k == 2):
                for j in range(1, 4):
                    if (a[j][3] == 0):
                        a[j][3] = -1
                        tic_set[j][3] = com_shape
                        change = 1
                        print_situ()
                return 0
        if (i == 7):
            for j in range(1, 4):
                k += a[j][j]
            if (k == 2):
                for j in range(1, 4):
                    if (a[j][j] == 0):
                        a[j][j] = -1
                        tic_set[j][j] = com_shape
                        change = 1
                        print_situ()
                return 0
        if (i == 8):
            for j in range(1, 4):
                k += a[j][4 - j]
            if (k == 2):
                for j in range(1, 4):
                    if (a[j][4 - j] == 0):
                        a[j][4 - j] = -1
                        tic_set[j][4 - j] = com_shape
                        change = 1
                        print_situ()
                return 0
    if (change == 0 and order != 9):  # change가 바뀌지 않았으면 랜덤으로 형성한다.
        random_num()
        return 0
    return 0


def now_score():  # 현재 스코어를 출려하는 함수
    print("현재 스코이")
    print("user:com=%d:%d" % (user_win, com_win))


def replay():  # 다시 플레이할건지 확인하는 함수
    print("다시 플레이 하시겠습니까?예는 0 아니오는 1로 입력해주십시오")
    re = int(input())
    return re


print("규칙을 알고 있습니까? 알면 1 모르면 0을 입력")
rule_num = int(input())
if (rule_num == 0):
    rule()
while True:
    print("O와 X 중 선택해주십시오. 단 대문자 O 또는 X로 입력해주세요")
    user_shape = input()
    while (user_shape != "X" and user_shape != "O"):
        print("다시 입력해주세요. 입력 형태는 대문자 O 또는 X입니다")
        user_shape = input()
    com_shape = choose_shape(user_shape)

    print("game start")
    print("선공 결정 게임")
    user_order = who_first()

    print("입력은 좌표로 입력해주세요. 왼쪽 상단이 (1,1) 오른쪽 하단이(3,3)")
    print("첫번째 입력이 x좌표 두번째 입력이 y좌표입니다")
    print("입력 형태는 원하는 좌표를 공백을 두고 숫자로만 입력하면 됩니다")
    print_situ()

    while (order < 9):
        if (user_order == 1):
            user_cor = list(map(int, input().split()))
            while (a[user_cor[1]][user_cor[0]] != 0):
                del user_cor[:]
                print("이미 있습니다 다시 입려해주세요")
                user_cor = list(map(int, input().split()))
            user_choose(user_cor[0], user_cor[1])
            order += 1

        finish = check()
        if (finish == 1):
            print("당신이 이겼습니다")
            user_win += 1  # user_win 변수를 증가
            break
        elif (finish == -1):
            print("제가 이겼습니다")
            com_win += 1  # com_win 변수를 증가
            break
        order += 1
        user_order = 1
    if (finish == 0):
        print("무승부")
    now_score()  # 게임이 끝나고 나서 현재 스코어 출력
    re = replay()  # 리플레이 할지를 확인
    if (re == 1):
        break
    else:  # 다시 리스트를 초기화
        for i in range(1, 4):
            for j in range(1, 4):
                a[i][j] = 0
                tic_set[i][j] = " "
        finish = 0
        order = 0
