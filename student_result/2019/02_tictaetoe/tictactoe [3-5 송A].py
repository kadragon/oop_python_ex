from random import randrange
import random

winners_case = [[0, 1, 2], [3, 4, 5], [6, 7, 8], [0, 3, 6], [1, 4, 7], [2, 5, 8], [0, 4, 8],
                [2, 4, 6]]  # 승리를 판단하기 위해 필요한 줄들

b = []  # 게임판
win = 0  # 승리
lose = 0
tie = 0
total = 0  # 총 게임 수

for index in range(0, 9):
    b.append(' ')


def game_board():  # 게임판 출력
    print(" " + b[0] + " | " + b[1] + " | " + b[2])
    print("ㅡ" * 8)
    print(" " + b[3] + " | " + b[4] + " | " + b[5])
    print("ㅡ" * 8)
    print(" " + b[6] + " | " + b[7] + " | " + b[8])


def check(index, user, com):
    """
    현재 winners_case 중 특정 요소에서 me와 pc가 어떻게 배치되어 있는지 보여주는 함수
    :param com: 컴퓨터
    :param user: 사용자
    :param index: winners_case안에서의 인덱스 (1~8)
    :return: [(), (), (): 특정 인덱스의 게임판에 me가 들어있으면 2, pc가 들어있으면 1, 비어있으면 0]
    """
    ind = 0
    checklist = [0, 0, 0]
    for j in winners_case[index]:
        if b[j] == user:
            checklist[ind] = 2
        elif b[j] == com:
            checklist[ind] = 1
        else:
            checklist[ind] = 0
        ind += 1
    return checklist


def fullboard():
    """
    돌을 더 놓을 수 있는지 확인
    :return: 없음
    """
    ok = 0
    for i in range(9):
        if b[i] == ' ':
            ok = 1

    if not ok:  # 판이 다 차 돌을 더 둘 수 없습니다.(끝)
        return 1

    else:
        return 0


def isempty(localindex):
    """
    원하는 인덱스에서의 게임판이 비어있는지 확인하는 함수
    :param localindex: 게임판에서의 인덱스
    :return: TRUE or FALSE
    """
    if b[localindex] == ' ':
        return 1
    else:
        return 0


def isfinish(mark):
    """
    게임이 끝났는지 확인하는 함수
    :param mark: 특정 마크 (O or X)
    :return: TRUE or FALSE
    """
    for index in winners_case:
        if b[index[0]] == mark and b[index[1]] == mark and b[index[2]] == mark:
            return 1

    return 0


def AI(user, com):
    """
    컴퓨터가 돌을 놓아야 할 곳을 선택하는 함수
    :param com: 컴퓨터 (O or X)
    :return: 없음
    """
    li = list(range(9))
    random.shuffle(li)
    ok = 0  # 괜찮은 위치인 것을 확인했는지의 여부
    for index in range(8):
        res = check(index, user, com)
        if res.count(1) == 2 and res.count(0) == 1:  # pc 2개 + 빈칸 -> 놓아야 함
            b[winners_case[index][res.index(0)]] = com
            ok = 1
            break

    if ok == 0:
        for index in range(8):
            res = check(index, user, com)
            if res.count(2) == 2 and res.count(0) == 1:  # 컴퓨터 입장: 위험 (한 줄에 빈 칸이 1개, user_mark 2개)
                b[winners_case[index][res.index(0)]] = com
                ok = 1
                break

    if ok == 0:
        for j in li:  # 랜덤으로 배치
            if isempty(j):
                b[j] = com
                ok = 1
                break


def wrong(entered, letter):
    """
    사용자가 입력한 정보가 틀리게 입력되는지 확인하는 함수
    :param entered: 입력된 문자
    :param letter: 입력되어야 하는 문자
    :return: TRUE or FALSE
    """
    if entered == letter:
        return 0
    else:
        return 1


def percent(num):  # 승률 계산해주는 함수
    """
    :param num: 계산할 대상
    :return: 승률
    """
    result = num / total
    return result


def play_again():
    """
    사용자가 게임을 다시 지속할지 결정
    :return:
    """
    return input('다시 플레이 하시겠습니까? (y or n)').lower().startswith('y')


print("틱택토 게임에 오신걸 환영합니다!")
print("틱택토 게임은 먼저 자신의 연속된 세 돌이 있을 때 승리하는 게임입니다.")
print("그럼 행운을 빌어요!")
print("=" * 100)

while True:
    for index in range(9):  # 게임판 setting
        b[index] = ' '
    me = input("말을 선택하세요!(O 또는 X) : ").upper()
    theend = 0  # 게임이 끝났는지 확인
    if me != 'O' and me != 'X':  # 잘못된 입력 다시 받기
        print("잘못된 입력입니다. 다시 입력해 주세요.")
        continue

    if me == 'O':
        pc = 'X'
    elif me == 'X':
        pc = 'O'

    while 1:  # 먼저 시작할 사람 결정
        playfirst = 0
        playfirst = randrange(0, 1, 1)
        if playfirst == 0:
            break
        elif playfirst == 1:
            break

    if playfirst == 1:
        AI(me, pc)
        game_board()

    while 1:
        choice = input("1~9 중 위치를 입력하세요. : ")
        print()
        if choice not in ['1', '2', '3', '4', '5', '6', '7', '8', '9']:
            print("잘못된 입력입니다. 다시 입력해주세요.")
            continue
        localindex = int(choice) - 1
        if isempty(localindex) == 0:
            print("놓을 수 없는 곳입니다.")
            continue
        b[localindex] = me
        AI(me, pc)
        game_board()
        print()

        if isfinish(me):
            print("이겼습니다!")
            theend = 1
            win += 1
            break

        if isfinish(me):
            print("You LOSE!")
            theend = 1
            lose += 1
            break

        if fullboard():
            break

    if theend != 1:
        tie += 1
        print("비겼습니다.")

    total += 1
    print("현재 사용자의 결과: 승 %.2f 무 %.2f 패 %.2f 경기 수 %d" % (percent(win), percent(tie), percent(lose), total))
    if not play_again():
        exit()

## 선생님 코드를 짜다가 코드가 계속 꼬이고 안되어서 친구가 생각한 알고리즘을 받아서 했어요ㅠㅠㅠ
