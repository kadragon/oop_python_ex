import random


def check_victory(ttt, wh):
    # 세로줄 확인
    for i in range(0, 3):
        cnt = 0
        for j in range(0, 3):
            if ttt[j][i] == wh:
                cnt += 1
        if cnt == 3:
            return 1

    # 가로줄 확인
    for i in range(0, 3):
        cnt = 0
        for j in range(0, 3):
            if ttt[i][j] == wh:
                cnt += 1
        if cnt == 3:
            return 1

    # 오른 대각선 확인
    cnt = 0
    for i in range(0, 3):
        if ttt[i][i] == wh:
            cnt += 1
    if cnt == 3:
        return 1

    # 왼 대각선 확인
    cnt = 0
    for i in range(0, 3):
        if ttt[i][2 - i] == wh:
            cnt += 1
    if cnt == 3:
        return 1

    # 전부 차있나 확인 (별다른 숭부가 안 날 때 무승부 여부 확정을 위하여)
    fullcnt = 0
    for i in range(0, 3):
        for j in range(0, 3):
            if ttt[i][j] != '0':
                fullcnt += 1
    if fullcnt == 9:
        # 전부 차있다면 무승부로 결정
        return 2

    # 모든 케이스 확인 후 아무런 해당사항 없을 시 return 0
    return 0


# 사용자 입력값 적용 함수
def putin(ttt, a):
    # 입력값 오류 시 입력 거부
    if a == '':
        return 3
    if a not in "123456789":
        return 3
    a = int(a)
    if a not in range(1, 10):
        return 3

    # 지정 칸에 이미 값이 있지 않으면 삽입 허용, 아니라면 거부
    if ttt[int((a - 1) / 3)][int(a % 3 - 1)] == '0':
        ttt[int((a - 1) / 3)][int(a % 3 - 1)] = 'X'
        return 1
    else:
        return 2


# 상태 표시 함수
def show_state(ttt):
    for i in range(0, 3):
        for j in range(0, 3):
            if ttt[i][j] == '0':
                print('*', end=' ')
            else:
                print(ttt[i][j], end=' ')
        print('')


# 최종 위치 결정(i축 값, j축 값, 1=rand/0=받은 위치)
def end_choose(ttt, i, j, rand):
    # 만약 랜덤 결정일 시
    if rand == 1:

        # 별다른 위험상황이 아니고, 만약 가운데(5)가 비어있으면 가운데 선점
        if ttt[1][1] == '0':
            ttt[1][1] = 'O'
            return
        while True:

            # 0 ~ 9까지 섞고
            lists = list(range(9))
            random.shuffle(lists)

            # 앞의 수 +1을 결정
            pls = lists[0] + 1

            # 해당 수를 2차원으로 바꿔서 삽입
            if ttt[int((pls - 1) / 3)][int((pls - 1) % 3 - 1)] == '0':
                ttt[int((pls - 1) / 3)][int((pls - 1) % 3 - 1)] = 'O'
                return
    else:

        # 랜덤 아닐 시 그냥 시키는 대로 삽입
        ttt[i][j] = 'O'
        return


# 컴퓨터 다음 수 판단 함수
# 판단 방법 요약:
# 첫째, 자신이 당장 놓았을 때에 바로 승리할 수 있는 자리 (자기 말이 2개 있는 줄) 를 찾고, 검색에 성공할 시 그 자리에 놓는다.
# 둘째, 방치했을 시 상대가 바로 승리하게 되는 자리 (상대 말이 2개 있는 줄) 를 찾고, 검색에 성공할 시 그 자리에 놓는다.
# 마지막, 이 모든 경우가 실패하였을 시 랜덤하게 배치한다. 다만 가운데에 놓는 것이 승리할 확률이 높을 것이라 판단하였기에, 5 자리가 비었으면 반드시 5에다가 말을 놓는다.
def choose_next(a, ttt):
    # 최종 결정에 사용될 변수
    puti = 0
    putj = 0

    # 승리에 필요한 부분 판단
    # 당장 승리 가능성이 있는 위치 판단
    for i in range(0, 3):

        # 지금 가로줄에 있는 사용자의 말 개수 카운트
        cnt = 0
        pivot = 0

        # 만약 자기 말이 2개라면 말이 놓일 위치 결정
        for j in range(0, 3):

            # 상대 말 껴있으면 가망 없음
            if ttt[i][j] == 'X':
                break

            # 자기 말 개수 카운트
            if ttt[i][j] == 'O':
                cnt += 1

            # 놓을 빈 자리가 있기는 한지
            elif ttt[i][j] == '0':
                puti = i
                putj = j
                pivot = 1

        # 이 줄에 2개 있고 빈 자리가 있었다면
        if cnt == 2 and pivot == 1:
            # print("승리 c1")

            # 자리 확정, 함수 끝
            end_choose(ttt, puti, putj, 0)
            return

    # 이길 수 있는 세로줄 판단 (내부 알고리즘은 위와 동일하므로 생략)
    for i in range(0, 3):
        cnt = 0
        pivot = 0
        for j in range(0, 3):
            if ttt[j][i] == 'X':
                break
            if ttt[j][i] == 'O':
                cnt += 1
            elif ttt[j][i] == '0':
                pivot = 1
                puti = j
                putj = i
        if cnt == 2 and pivot == 1:
            # print("승리 c2")
            end_choose(ttt, puti, putj, 0)
            return

    # 승리 대각선 판단
    # 오른 대각선
    cnt = 0
    pivot = 0
    for i in range(0, 3):
        if ttt[i][i] == 'X':
            break
        if ttt[i][i] == 'O':
            cnt += 1
        elif ttt[i][i] == '0':
            pivot = 1
            puti = i
            putj = i
    if cnt == 2 and pivot == 1:
        # print("승리 c3")
        end_choose(ttt, puti, putj, 0)
        return

    # 왼 대각선
    cnt = 0
    pivot = 0
    for i in range(0, 3):
        if ttt[i][2 - i] == 'X':
            break
        if ttt[i][2 - i] == 'O':
            cnt += 1
        elif ttt[i][2 - i] == '0':
            pivot = 1
            puti = i
            putj = 2 - i
    if cnt == 2 and pivot == 1:
        # print("승리 c4")
        end_choose(ttt, puti, putj, 0)
        return

    # 막아야 할 부분 판단
    # 위험 가로줄 판단
    for i in range(0, 3):

        # 지금 가로줄에 있는 사용자의 말 개수 카운트
        cnt = 0
        pivot = 0

        # 만약 위험 상태라면 말이 놓일 위치
        for j in range(0, 3):

            # 자기 말이 하나라도 그 줄에 있으면 안전하므로 바로 루프 탈출
            if ttt[i][j] == 'O':
                break

            # 상대 말 개수 카운트
            if ttt[i][j] == 'X':
                cnt += 1

            # 빈 자리 있나 확인
            elif ttt[i][j] == '0':
                pivot = 1
                puti = i
                putj = j

        # 빈 자리 있고, 상대 말 개수 2개이면 방어 확정
        if cnt == 2 and pivot == 1:
            # print("패배 c1")
            end_choose(ttt, puti, putj, 0)
            return

    # 위험 세로줄 판단 (알고리즘은 위와 동일하므로 생략)
    for i in range(0, 3):
        cnt = 0
        pivot = 0
        for j in range(0, 3):
            if ttt[j][i] == 'O':
                break
            if ttt[j][i] == 'X':
                cnt += 1
            elif ttt[j][i] == '0':
                pivot = 1
                puti = j
                putj = i
        if cnt == 2 and pivot == 1:
            # print("패배 c2")
            end_choose(ttt, puti, putj, 0)
            return

    # 위험 대각선 판단
    # 오른 대각선
    cnt = 0
    pivot = 0
    for i in range(0, 3):
        if ttt[i][i] == 'O':
            break
        if ttt[i][i] == 'X':
            cnt += 1
        elif ttt[i][i] == '0':
            pivot = 1
            puti = i
            putj = i
    if cnt == 2 and pivot == 1:
        # print("패배 c3")
        end_choose(ttt, puti, putj, 0)
        return

    # 왼 대각선
    cnt = 0
    pivot = 0
    for i in range(0, 3):
        if ttt[i][2 - i] == 'O':
            break
        if ttt[i][2 - i] == 'X':
            cnt += 1
        elif ttt[i][2 - i] == '0':
            pivot = 1
            puti = i
            putj = 2 - i
    if cnt == 2 and pivot == 1:
        # print("패배 c4")
        end_choose(ttt, puti, putj, 0)
        return

    # 요기까지 걸린 경우가 없다면 랜덤으로 선택 (end_choose함수의 마지막 변수가 1이면 랜덤을 뜻함)
    end_choose(ttt, 0, 0, 1)


# 다시 플래이? 함수
def re_or_not(a):
    if a == 'y':
        return 1
    else:
        return 0


# 게임 규칙 설명 함수
def rule_expl():
    print("재미있는 틱택토 게임이에요!")
    print("틱택토 게임에서는 가로, 세로, 혹은 대각선으로 자신의 말을 3개 이어서 먼저 배치하면 이기는 게임입니다!")
    print("제가 O 할거고, 님이 X를 하세요.")
    print("판은 이렇게 생겼습니다.")
    print("1 2 3")
    print("4 5 6")
    print("7 8 9")


# 승률 기록 함수
def win_rate(p, c, win_r, numb):
    p = float(p)
    win_r = p / numb
    return win_r


# 사전 설명
# 사용자는 'X'를 사용합니다.
# 택택토 판 - 문자 0은 비어있음을 표시
ttt = [['0', '0', '0'], ['0', '0', '0'], ['0', '0', '0']]

# 코드 시작!

# 사용자 승리 수
player_vic = 0

# 컴퓨터 승리 수
com_vic = 0

# 승률
win_r = 2

# 경기수
numb = 0

# 사용자가 게임을 포기하지 않는 이상 계속 도는 while
while True:
    print("*" * 100)
    numb += 1
    rule_expl()
    print("%d번째 라운드 입니다!" % numb)
    if numb != 1:
        print("ㅎㅎ 또 만났네요")
        if player_vic == 0:
            print("그래도 한번은 이기셔야죠?")

    # 초기화
    ttt = [['0', '0', '0'], ['0', '0', '0'], ['0', '0', '0']]

    # 입력 받고
    while True:
        print("자신이 말을 배치할 곳의 숫자를 입력하세요!")

        # a는 사용자의 입력 값을 저장
        while True:
            a = input()
            if putin(ttt, a) == 1:
                break
            elif putin(ttt, a) == 3:
                print("정확한 값을 입력하세요!")
            elif putin(ttt, a) == 2:
                print("아직 말이 없는 곳에 입력하세요!")

        # 사용자 입력 후 사용자 승리 확인
        pivot = 1

        # 판이 꽉 찼는지 확인
        if (check_victory(ttt, 'X') == 2):
            print("무승부 입니다~")
            show_state(ttt)

            # 만약 꽉 찼다면 무승부
            break
            pivot = 0

        # 플레이어 승리 여부 확인
        if check_victory(ttt, 'X') and pivot == 1:
            print("당신의 승리입니다!~")
            show_state(ttt)

            # 승리했다면 플레이어 점수 +1
            player_vic += 1
            break

        # 컴퓨터의 수 결정 함수
        choose_next(a, ttt)

        # 컴퓨터 입력 후 컴퓨터 승리 확인
        if check_victory(ttt, 'O') and pivot == 1:
            print("풋 제가 이겼네요~")
            show_state(ttt)

            # 승리했다면 컴퓨터 점수 +1
            com_vic += 1
            break

        # 각자 한 수 씩 두고 상태 표시
        show_state(ttt)

    # 끝낼지 질문
    print("한 판 더 하시겠습니까?, 'n' or 'y' ")
    a = ''
    while True:
        a = input()
        if not (a == 'n' or a == 'y'):
            print("'n' or 'y' 만 입력하세요.")
        else:
            break
    if not re_or_not(a):
        break

# 모든 게임이 끝난 이후 결과 표시
print("총 경기수는 %d! 저는 %d번 이겼고요, 님은 %d번 이겼네요!" % (numb, com_vic, player_vic))
a = win_rate(player_vic, com_vic, win_r, numb)

# a에 아무런 업데이트가 없을 시 승률은 0(무의미) 표시하지 않는다
if a == 2:
    print("아직 승부가 안나서 딱히 님의 승률은 없어요.")

# 아니라면 승률 소숫점 2자리까지 표시
else:
    print("님의 승률은 %.2f입니다!" % a)

# 컴퓨터와 사용자의 승리 횟수에 따른 상대적인 멘트
if com_vic > player_vic:
    print("저보다 못하시네")
elif com_vic < player_vic:
    print("으.. 저보다 나으시네요")
elif com_vic == player_vic:
    print("저희 둘이 비슷비슷하네요 ㅎㅎ")
