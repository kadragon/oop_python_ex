import random

# p는 플레이어가 선택한 말이다. a는 판을 나타낸다.
# priority는 컴퓨터가 어디에 두든 상관 없을 때, 수를 놓을 장소의 우선순위다.
p = 'init'
a = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
priority = [[0, 0], [2, 2], [2, 0], [0, 2], [0, 1], [1, 0], [2, 1], [1, 2], [1, 1]]


# full()은 판이 말로 가득 차 있으면 1을, 아니라면 0을 return하는 함수다.
def full():
    global a

    for i in a:
        for j in i:
            if j != 'O' and j != 'X': return 0
    return 1


# bingo()는 판에서 bingo가 발생하였는치 체크하는 함수다. 'O'로 이루어진 빙고가 있으면 1을,
# 'X'로 이루어진 빙고가 있으면 2를, 빙고가 없으면 0을 return한다.
def bingo():
    global a
    for i in range(3):
        if a[i][0] == 'O' and a[i][1] == 'O' and a[i][2] == 'O':
            return 1

    for i in range(3):
        if a[i][0] == 'X' and a[i][1] == 'X' and a[i][2] == 'X':
            return 2

    for i in range(3):
        if a[0][i] == 'O' and a[1][i] == 'O' and a[2][i] == 'O':
            return 1

    for i in range(3):
        if a[0][i] == 'X' and a[1][i] == 'X' and a[2][i] == 'X':
            return 2

    if a[0][0] == 'O' and a[1][1] == 'O' and a[2][2] == 'O':
        return 1

    if a[0][0] == 'X' and a[1][1] == 'X' and a[2][2] == 'X':
        return 2

    if a[0][2] == 'O' and a[1][1] == 'O' and a[2][0] == 'O':
        return 1

    if a[0][2] == 'X' and a[1][1] == 'X' and a[2][0] == 'X':
        return 2

    return 0


# continuef()는 판이 가득 찼거나 빙고가 생겼을 경우 0을 return해 게임이 끝났음을 알린다.
# 아니라면 1을 return한다.
def continuef():
    global a
    global p

    # bingo가 생겼을 경우 WIN인지 LOSE인지 출력해준다.
    b = bingo()
    if b == 1:
        if p == 'O':
            print("WIN!!!")
        else:
            print("LOSE...")
        return 0
    elif b == 2:
        if p == 'O':
            print("LOSE...")
        else:
            print("WIN!!!")
        return 0

    f = full()
    if f == 1:
        print("판이 가득 찼다.")
        return 0
    return 1


# atk()는 컴퓨터가 공격을 실행하는 함수다.
def atk():
    global a
    global p

    # o는 컴퓨터가 사용하는 말이다.
    o = 'init'
    if p == 'X':
        o = 'O'
    else:
        o = 'X'
    # mustbe는 컴퓨터가 'X' 말을 사용하는 경우 2, 'O'말을 사용하는 경우 1이 된다.
    # bingo()가 return한 값이 mustbe가 되면 컴퓨터가 이긴다.
    # mustnot은 3-mustbe이다.
    # bingo()가 return한 값이 mustnot이 되면 player가 이긴다.
    mustbe = 'init'
    mustnot = 'init'
    if o == 'X':
        mustbe = 2
    else:
        mustbe = 1
    mustnot = 3 - mustbe

    # 만약 bingo가 만들어져 이길 수 있는 장소가 있으면 둔다.
    # 수를 둬 보고, bingo()가 mustbe와 같은 값을 return하면 거기에 둔다.
    # 아니면 원래 있었던 수로 다시 돌려 놓는다.
    for i in range(3):
        for j in range(3):
            if a[i][j] != 'X' and a[i][j] != 'O':
                tmp = a[i][j]
                a[i][j] = o
                if mustbe == bingo():
                    return
                else:
                    a[i][j] = tmp

    # 만약 다음 turn에 상대가 두어 bingo를 만들 수 있는 장소가 있으면 둔다.
    # player의 말로 수를 둬 보고, bingo()가 mustnot과 같은 값을 return하면 거기에 둔다.
    # 아니면 원래 있었던 수로 다시 돌려 놓는다.
    for i in range(3):
        for j in range(3):
            if a[i][j] != 'X' and a[i][j] != 'O':
                tmp = a[i][j]
                a[i][j] = p
                if mustnot == bingo():
                    a[i][j] = o
                    return
                else:
                    a[i][j] = tmp

    # 필수적으로 두어야 할 곳이 없을 경우 비어 있으며 priority에서 우선시 되는 곳에 수를 둔다.
    for i in priority:
        x = i[0]
        y = i[1]
        if a[y][x] != 'X' and a[y][x] != 'O':
            a[y][x] = o
            return


# nonsense()는 player가 수를 놓기로 결정한 자리가 1~9의 값이 아니면 1을, 맞으면 0을 return하는 함수다.
def nonsense(t):
    if t != '1' and t != '2' and t != '3' and t != '4' and t != '5' and t != '6' and t != '7' and t != '8' and t != '9':
        return 1
    return 0


# replay는 게임이 끝났을 경우 player가 게임을 다시 시도할 것인지의 여부를 저장한다.
# 다시 시도하기를 원하면 1을, 아니라면 0을 저장한다.
replay = 1

while replay == 1:
    print("네가 O로 플레이할지 X로 플레이할지 입력해라.")

    # player가 어떤 말로 play할지 입력받는다.
    while (p != 'O' and p != 'X'):
        p = input()
        if p == 'X':
            print("너는 X로 플레이하기를 선택했다.", '\n')
        elif p == 'O':
            print("너는 O로 플레이하기를 선택했다.", '\n')
        else:
            print("대문자 O 또는 X만을 입력해라")

    # player가 선공을 맡을지 후공을 맡을지 random으로 정한다.
    turn = random.randrange(0, 2)
    if turn == 1:
        print("당신은 선공을 맡게 되었다!", "\n")
    else:
        print("당신은 후공을 맡게 되었다!", '\n')

    # 게임의 시작 부분. 어느 쪽도 수를 두지 않은 판을 출력한다.
    print("처음 판의 상태")
    for i in range(3):
        print('| ', end="")
        for j in a[i]:
            print(j, end=" ")
            print('| ', end="")
        print("")
        if i != 2:
            for j in range(13):
                print('-', end="")
            print("")
    print("")

    while continuef():
        # turn이 0이라는 것을 컴퓨터의 차례라는 것이다. atk()로 공격한다.
        # 이후 turn을 1로 바꾸어 player의 차례로 넘겨준다.
        if turn == 0:
            atk()
            turn = 1

        # turn이 0이 아니라는 것은 player의 차례라는 것이다.
        # player가 원하는 곳에 수를 두게 한다.
        # 이후 turn을 0으로 만들어 computer의 차례로 넘겨준다.
        else:
            print("네가 수를 놓을 곳을 입력해라.")
            t = 'init'
            x = 0
            y = 0

            # 수를 놓을 곳이 비어있으며, 1~9까지의 숫자일 때까지 입력받는다.
            while nonsense(t) or a[y][x] == 'O' or a[y][x] == 'X':
                print("비어있는 숫자 중 하나를 입력해라")
                t = input()
                if nonsense(t) == 0:
                    x = (int(t) - 1) % 3
                    y = (int(t) - 1) // 3
            a[y][x] = p
            turn = 0

        # 하나의 수를 둔 후 판의 상태를 출력한다.
        if turn == 0:
            print("player의 공격!")
        else:
            print("컴퓨터의 공격!")
        for i in range(3):
            print('| ', end="")
            for j in a[i]:
                print(j, end=" ")
                print('| ', end="")
            print("")
            if i != 2:
                for j in range(13):
                    print('-', end="")
                print("")
        print("")

    # continuef()로 조건을 따지는 whlie문을 빠져나왔다는 것은 게임이 끝났다는 뜻이다.
    # 그러므로 replay를 입력받는다. Y를 입력받으면 1로, N을 입력받으면 0으로
    # replay의 값을 바꾸어 게임을 다시 할지 말지를 결정한다.
    while replay != 'Y' and replay != 'N':
        print("다시 하려면 Y 를, 그만 두려면 N을 대문자로 입력해라")
        replay = input()

    if replay == 'Y':
        for i in range(3):
            for j in range(3):
                a[i][j] = i * 3 + j + 1
        p = 'init'
        replay = 1
    else:
        print("게임종료")
        replay = 0
