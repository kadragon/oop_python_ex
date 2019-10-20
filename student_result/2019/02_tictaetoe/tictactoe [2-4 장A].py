import random


def is_it_first(your_pick):  # 누가 선공인지 랜덤으로 만드는 함수
    fir = random.randint(1, 2)  # 선공할 번호 랜덤 뽑기
    if fir is 1:  # 만약 랜덤으로 뽑은 선공 번호가 1번일 때
        print("1 : 선  /  2 : 후")
    else:  # 만약 랜덤으로 뽑은 선공 번호가 2번일 때
        print("1 : 후  /  2 : 선")
    if int(your_pick) == fir:  # 만약 사람이 선공일 때
        print('당신이 선공입니다.')
        return True
    else:  # 컴퓨터가 선공일 때
        print("당신이 후공입니다.")
        return False


def check_empty(where):  # 비었는지 채워져 있는지 체크하는 함수
    if tablemap[where] == 0:
        return True  # 빈 곳이면 True
    else:
        return False  # 이미 있으면 False


def plus_rock(where, who):  # 돌을 추가하는 함수
    if who == 'user':  # 사람일 때
        tablemap[where] = 1  # 1로 체크
    else:  # 컴퓨터 일 때
        tablemap[where] = 2  # 2로 체크


def print_map():  # 게임판 출력하는 함수
    print('-' * 20)  # 그냥 라인
    for i in range(1, 10):  # 1번 자리부터 9번 자리까지
        if tablemap[i] == 1:  # 1로 저장 되어 있으면
            print(' ' + '○' + ' ', end='')  # ○로 출력
        elif tablemap[i] == 2:  # 2로 저장 되어 있으면
            print(' ' + '●' + ' ', end='')  # ●로 출력
        else:  # 나머지 빈칸들은
            print(' ' + 'Χ' + ' ', end='')  # Χ로 출력
        if i % 3 == 0:  # 3워 배수이면 줄 바꿈
            print("")
        else:  # 아니면 칸막이
            print("|", end='')


def check_bingo():  # 빙고인지 아닌지 체크하는 함슈
    for i in range(1, 4):  # 가로 라인들 체크
        if tablemap[3 * i - 1] == 1:
            if tablemap[3 * i - 2] == 1 and tablemap[3 * i] == 1:
                return True
        if tablemap[i] == 1:  # 세로 라인들 체크
            if tablemap[i + 3] == 1 and tablemap[i + 6] == 1:
                return True
        if tablemap[1] == 1 and tablemap[5] == 1 and tablemap[9] == 1:  # 대각선 체크
            return True
        if tablemap[3] == 1 and tablemap[5] == 1 and tablemap[7] == 1:  # 대각선 체크
            return True
        if tablemap[3 * i - 1] == 2:  # 가로 라인들 체크
            if tablemap[3 * i - 2] == 2 and tablemap[3 * i] == 2:
                return True
        if tablemap[i] == 2:  # 세로 라인들 체크
            if tablemap[i + 3] == 2 and tablemap[i + 6] == 2:
                return True
        if tablemap[1] == 2 and tablemap[5] == 2 and tablemap[9] == 2:  # 대각선 체크
            return True
        if tablemap[3] == 2 and tablemap[5] == 2 and tablemap[7] == 2:  # 대각선 체크
            return True


def find_place():  # 컴퓨터가 돌을 넣을 수 있는 장소, 넣어야 되는 장소를 탐색하는 함수
    for i in range(1, 10):  # 모든 자리에
        if check_empty(i):  # 그 자리가 비어 있으면
            tablemap[i] = 1  # 그 자리에 사람 돌을 하나 놓아보고
            if check_bingo():  # 만약이 빙고가 난다면
                tablemap[i] = 2  # 그 자리에 컴퓨터 돌을 놓는다.
                return
            else:  # 만약 빙고가 생기지 않는다면
                tablemap[i] = 0  # 다시 빈 칸으로 놓는다.
    init = False  # 빈 공간이면 True로 바뀐다.
    while not init:  # init 조건이 만족할 때까지
        new_place = random.randint(1, 9)  # 랜덤하게 자리를 하나 잡고
        init = check_empty(new_place)  # 그 자리가 비어 있는지 체크하고 비어있으면 탈출
    plus_rock(new_place, 'com')  # 그 새 자리에 돌을 놓는다.


def play_again():  # 재시작 여부 질문
    print('다시 하시겠습니까?')
    print('insert coin')
    print('Yes  No')
    re = str(input())  # 스캔
    if re == 'yes':  # 재시작 조건 1
        return True
    elif re == 'Yes':  # 재시작 조건 2
        return True
    else:  # 나머지는
        return False


win = 0  # 이긴 횟수
lose = 0  # 진 횟수
draw = 0  # 비긴 횟수
while True:
    print('Tic-Tac-Toe!!')
    print('컴퓨터와 틱택토 게임을 합니다.')
    print('돌을 넣을 칸의 번호를 입력하면 돌이 놓여 집니다.')
    print("게임판은 위에서부터 가로로 1부터 9까지이며")
    print("당신의 돌은 ○ 이고, 컴퓨터의 돌은 ● 입니다. Χ는 비어있는 칸입니다.")
    print('랜덤으로 순서가 결정됩니다.')
    print('숫자 1,2중 하나를 골라주세요. 다른 숫자를 고르면 자동 후공 처리 됩니다^^.')
    okpass = True
    while okpass:
        fs = input()  # 입력을 받아보고
        if fs.isdigit():  # 만약 입력 받는 것이 수가 아니라면
            okpass = False  # 계속 반복
    first = False  # True이면 사람 차례, False이면 컴퓨터 차례
    if is_it_first(fs):  # 누가 선수인지 돌리는 함수
        first = True
    tablemap = []  # 게임판 정의하고
    for i in range(15):  # 게임판을 생성한다.
        tablemap.append(0)
    print('그럼 시작합니다!')
    for i in range(9):  # 최악의 경우 9번 돌을 놓기 때문
        if first:  # 사람 차례이면
            print('당신의 차례입니다.')
            scan = False
            while not scan:
                print("아직 비어있는 곳의 번호를 써주세요")
                place = int(input())  # 일단 입력을 받아보고
                scan = check_empty(place)  # 이미 차 있는 자리라면 다시 입력을 받는다.
            plus_rock(place, 'user')  # 그리고 돌을 놓는다.
            print_map()  # 돌을 놓은 결과 출력
            first = False  # 다음은 컴퓨터 차례
        else:  # 컴퓨터 차례
            find_place()  # 컴퓨터가 놓을 자리 찾는 함수
            print("컴퓨터의 공격!")
            print_map()  # 컴퓨터가 놓은 결과 출력
            first = True  # 다음은 사람 차례
        if check_bingo():  # 빙고가 나왔는지 체크
            print("bingo")
            if first:  # 만약 방금 컴퓨터 차례였으면
                lose += 1  # 진 횟수 1회 적립
                print("컴퓨터의 승리!")
                print(lose)
            else:  # 만약 방금 사람 차례였으면
                win += 1  # 이긴 횟수 1회 적립
                print("당신의 승리!!")
                print(win)
            break
        if i == 8:  # 다 찰 때까지 결론이 나지 않으면
            draw += 1  # 무승부인 것이다.
            print("무승부입니다.")
    if not play_again():  # 더 하는지 물어보고 그만두면 마무리
        print("이긴 횟수 : ", end='')
        print(win)  # 이긴 횟수 출력
        print("진 횟수 : ", end='')
        print(lose)  # 진 횟수 출력
        print("승률 : ", end='')
        print(win / (win + lose + draw))  # 승률 출력
        break
