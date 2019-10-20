import time  # time.sleep 함수 사용을 위함


def init(du, boa):  # 현재 승률을 출력하는 함수
    # du: 바로 전에 잘못된 입력이 들어오면, 중복됨을 나타내는 du가 1이 되어 중복 방지
    # boa: 현재 승률을 나타냄
    if not du:  # 중복이 아니면
        print("틱텍토!")
        print("X가 먼저 시작합니다")
        print("현재 승률: %d판 %d승 %d무 %d패" % (boa[0], boa[1], boa[2], boa[0] - boa[1] - boa[2]), end=' ')
        if boa[0] != 0:  # 실행횟수 0일 경우 출력 안함
            print("%.1f%%" % boa[3])
        else:
            print('')
    print("X로 하실래요, O로 하실래요?")


def printarr(douser, karr):  # 화면에 현재 상태를 출력하는 함수
    # douser: 사용자가 둘 차례인 경우, 추가 설명을 기입하기 위해 1, 컴퓨터가 두는 경우 0
    # karr: 게임 상황을 기록하는 리스트
    if douser:
        print("=" * 15)
        for i1 in range(3):
            for j1 in range(3):
                if karr[i1][j1] != 0:
                    print(karr[i1][j1], end=' ')
                else:
                    print('-', end=' ')
            if i1 != 1:
                print(' ' * 5, end='')
            else:
                print(' ' + '<' + '-' * 2 + ' ', end='')
            for j1 in range(3):
                print(3 * i1 + j1 + 1, end=' ')
            if i1 == 2:
                print(' ' * 5, end='')
                print("1~9까지의 숫자를 입력하세요", end='')
            print('')
        print("=" * 15)
    else:  # 컴퓨터가 둘 차례인 경우 설명을 기입할 필요가 없음
        print("=" * 15)
        for i1 in range(3):
            for j1 in range(3):
                if karr[i1][j1] != 0:
                    print(karr[i1][j1], end=' ')
                else:
                    print('-', end=' ')
            print('')
        print("=" * 15)


def usergame(flag, arrr):  # 사용자가 입력한 정수를 위치에 맞게 리스트에 표시하는 함수
    # flag: user가 X문자를 둘 경우 1, O문자를 둘 경우 0
    # arrr: 게임의 상황을 표시하는 리스트
    try:
        lo = int(input('->'))
        lo -= 1
        if 0 > lo or lo > 8:
            print("1~9까지의 숫자를 입력해주세요")
            usergame(flag, arrr)
            return
        if arrr[lo // 3][lo % 3] != 0:
            print("이미 둔 곳입니다")
            usergame(flag, arrr)
            return
        if flag == 1:
            arrr[lo // 3][lo % 3] = 'X'
        else:
            arrr[lo // 3][lo % 3] = 'O'
    except ValueError:
        print("1~9까지의 숫자입니다, 공백이나 문자가 아니라")
        usergame(flag, arrr)
        return


def rank(flag, a, x, y):  # 컴퓨터가 둘 때, 우선순위를 매기는 함수: 컴퓨터가 질 수 있음
    # flag: 사용자가 X문자인 경우 1,O문자인 경우 0
    # a: 게임 상황을 기록하는 리스트
    # x,y: 둘 위치를 나타냄
    if a[x][y] != 0:  # 이미 표시되었을 경우 가장 낮은 -1
        return -1
    if flag == 1:  # 사용자가 X문자인 경우 - 컴퓨터가 O문자인 경우
        a[x][y] = 'O'
    else:  # 컴퓨터가 X문자인 경우
        a[x][y] = 'X'
    if a[x][0] == a[x][1] == a[x][2] != 0 or a[0][y] == a[1][y] == a[2][y] != 0 or a[0][0] == a[1][1] == a[2][2] != 0 or \
            a[0][2] == a[1][1] == a[2][0] != 0:  # 컴퓨터가 특정한 곳에 두었을 때, 게임을 이기는 경우
        a[x][y] = 0  # 시험하기 위함이므로 다시 0으로 만듬
        return 4  # 가장 높은 순위
    if flag == 1:  # 사용자가 X문자인 경우
        a[x][y] = 'X'
    else:  # 사용자 O문자인 경우
        a[x][y] = 'O'
    if a[x][0] == a[x][1] == a[x][2] != 0 or a[0][y] == a[1][y] == a[2][y] != 0 or a[0][0] == a[1][1] == a[2][2] != 0 or \
            a[0][2] == a[1][1] == a[2][0] != 0:  # 사용자가 특정한 곳에 두었을 때 게임을 이기는 경우
        a[x][y] = 0
        return 3  # 그 다음으로 높은 순위
    a[x][y] = 0
    if (x == 0 and y == 0) or (x == 0 and y == 2) or (x == 2 and y == 0) or (x == 2 and y == 2):  # 귀에 놓을 경우
        return 2  # 그 다음
    if x == 1 and y == 1:  # 가운데에 놓을 경우
        return 1  # 그 다음
    return 0


def comgame(flag, a):  # 컴퓨터가 다음에 둘 곳을 판단하는 함수
    # flag: 사용자가 X문자이면 1, O문자이면 0
    # a: 게임 상황을 기록하는 리스트
    maxi = 0
    maxj = 0
    print("컴퓨터가 두는 중...")
    time.sleep(1)  # 굳이 필요없지만, 사용자가 둔 수를 잠깐이나마 보게 하기 위함
    for x in range(3):
        for y in range(3):
            if rank(flag, a, x, y) > rank(flag, a, maxi, maxj):  # rank의 수가 가장 큰 위치를 찾아 maxi,maxj에 저장
                maxi = x
                maxj = y
    if flag == 1:  # 기록
        a[maxi][maxj] = 'O'
    else:  # 기록
        a[maxi][maxj] = 'X'
    print("완료했습니다")


def game(tim, isx, arr):  # 리스트를 먼저 출력한 뒤, 사용자가 둘 차례면 usergame 실행, 컴퓨터가 둘 차례면 comgame 실행
    # tim: 현재 두는 횟수, isx:사용자가 X이면 1, O이면 0, arr: 게임 상황을 기록하는 리스트
    if (isx + tim) % 2 == 0:  # 사용자가 둘 차례면
        printarr(1, arr)
        usergame(isx, arr)
    else:  # 컴퓨터가 둘 차례면
        printarr(0, arr)
        comgame(isx, arr)


def result(a, tm):  # 리스트를 검사하여, 게임이 안 끝났으면 2리턴, 사용자가 이겼으면 1리턴, 컴퓨터가 이겼으면 0리턴
    # a: 게임 상황 기록하는 리스트, tm: 사용자의 문자, anti: 컴퓨터의 문자
    if tm == 'X':
        anti = 'O'
    else:
        anti = 'X'
    for i3 in range(3):
        if a[i3][0] == a[i3][1] == a[i3][2] == tm or a[0][i3] == a[1][i3] == a[2][i3] == tm:  # 가로방향, 세로방향
            return 1
        if a[i3][0] == a[i3][1] == a[i3][2] == anti or a[0][i3] == a[1][i3] == a[2][i3] == anti:  # 가로방향, 세로방향
            return 0
    if a[0][0] == a[1][1] == a[2][2] == tm or a[2][0] == a[1][1] == a[0][2] == tm:  # 대각선
        return 1
    if a[0][0] == a[1][1] == a[2][2] == anti or a[2][0] == a[1][1] == a[0][2] == anti:  # 대각선
        return 0
    return 2


def printresult(t):  # 결과를 출력하는 함수
    # t: 사용자의 문자
    if result(arra, t) == 1:
        print("이겼네? 우와 정말 데단해!")
    elif result(arra, t) == 2:
        print("비기다니! 당신은 컴퓨터급인가?")
    else:
        print("졌네? 집중을 안해서 그래! 더 노오오오력하라고")


def isre():  # 사용자에게 다시 플레이할 것인지 물어보는 함수
    while True:
        print("다시 하시겠어요? Y/N")
        trig = input('->')
        if trig == 'N':
            return 0
        elif trig != 'Y':
            print("Y/N 둘 중 하나로 입력해주세요")  # 잘못된 문자 입력: 다시 실행
        else:
            return 1


def writrate(ar, m, boar):  # 승률을 기록함(갱신함)
    boar[0] += 1  # 진행횟수+=1
    if result(ar, m) == 1:
        boar[1] += 1  # 이긴횟수 +=1
    elif result(ar, m) == 2:
        boar[2] += 1  # 비긴횟수 +=1
    boar[3] = float(boar[1] / boar[0]) * 100  # 승률계산: boar[1]은 0이 아님
    return boar  # 갱신된 리스트 리턴


board = [0, 0, 0, 0]  # 진행횟수, 이긴횟수, 비긴횟수, 승률
dup = 0  # 전에 잘못된 입력이 들어왔다면 1로 바뀜
while 1:
    init(dup, board)  # 게임 소개, 승률 출력
    dup = 0
    arra = []
    for _ in range(3):
        arra.append([0] * 3)  # 게임 상황을 기록할 리스트 만들기
    tmp = input('->')
    if tmp != 'O' and tmp != 'X':  # 잘못된 입력
        print("O/X로 답해주세요")
        dup = 1
        continue
    for i in range(9):  # for문을 돌며 사용자(X)-> 컴퓨터(O) 혹은 컴퓨터(X)-> 사용자(O) 순으로 차례가 돌아감
        if tmp == 'X':
            game(i + 1, 1, arra)
        elif tmp == 'O':
            game(i + 1, 0, arra)
        if result(arra, tmp) != 2:  # 승부가 났다면
            break  # 게임 종료
    printarr(0, arra)  # 리스트에 기록된 결과 출력
    printresult(tmp)  # 누가 이겼는지 결과 출력
    board = writrate(arra, tmp, board)  # 승률을 기록
    if isre() == 0:  # 다시 시도하지 않을 경우
        break  # 프로그램 종료
