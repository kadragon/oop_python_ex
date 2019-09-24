"""
객체지향프로그래밍
소과제 1
숫자야구게임 제작하기

2306 박유진
"""

import random
import sys
import time

secret = []  # 컴퓨터가 만들어내는 임의의 숫자 3개를 담을 리스트
user = []  # 사용자가 입력하는 3개의 숫자의 리스트


def intro():
    """
    사용자에게 게임과 규칙에 대한 설명을 출력하는 함수
    :return: 없음
    """
    print("=" * 20)
    print("SASA의 숫자야구게임")
    print("컴퓨터가 만들어내는 3자리 임의의 숫자를 플레이어가 맞추는 게임")
    print("숫자는 0~9까지 서로 다름")
    print("숫자와 위치가 모두 맞으면 스트라이크(S)")
    print("숫자는 맞지만 위치가 틀리면 볼(B)")
    print("숫자와 위치가 모두 틀리면 아웃(O)")
    print("기회는 10번이고, 입력이 형식(숫자 3개)이 아니어도 기회가 줄어드니 조심하세요...")
    print("=" * 20)


def makenum():
    """
    사용자가 맞춰야할 임의의 숫자를 만들어주는 함수
    임의의 서로다른 0~9까지의 숫자 3개로 구성된 리스트를 제작한다.
    :return 없음
    """
    temp = list(range(10))
    print("3자리 임의의 숫자 생성...")
    random.shuffle(temp)
    for i in range(3):
        secret.append(temp[i])


def takeinput(i):
    """
    사용자가 입력하는 공백으로 띄워진 숫자 3개를 받아들여 리스트로 변환한다
    숫자 3개의 리스트를 반환한다.
    형식에 맞춰서 들어오지 않은 입력은 에러를 발생시켜서 제외한다
    :param i: 사용자에게 남은 횟수를 __main__에서 받음. 출력에 사용
    :return: 없음
    """
    print("3개의 숫자(0~9)를 공백으로 띄워 입력해주세요:\n>남은 횟수: %d" % i)
    result = []
    try:
        templist = map(str, input().split(" "))
        for i in templist:
            for j in i:
                result.append(int(j))
        if len(result) == 3:
            return result
        else:
            print("\n에러발생\n형식을 맞춰 입력해주세요\n")

    except (KeyError, ValueError, TypeError, IndexError) as e:
        print("\n에러 발생 (%s) \n형식을 맞춰주세요\n" % e)


def calcguess():
    """
    사용자가 입력한 숫자 3개와 컴퓨터가 정한 숫자 3개를 비교해서, S, B, O의 개수를 반환한다
    반환형식은 tuple이다
    :return int, int, int
    """
    S = 0   # type: int
    B = 0
    O = 0
    for i in range(3):
        cmp = user[i]  # cmp로 임시 지정
        for j in range(3):
            if cmp == secret[j]:  # 같은 수가 있는 경우
                if i == j:  # 같은 자리인 경우(S)
                    S += 1
                else:  # 다른 자리인 경으(B)
                    B += 1
    O = 3 - S - B
    return S, B, O


def det_process():
    """
    사용자가 입력한 숫자와 임의로 제작한 숫자를 비교한 calcguess의 반환 값을 출력하고
    숫자를 맞췄으면 축하하고 main의 for을 탈출할 수 있는 True를 반환한다
    :return: True / False (True면 맞춘것)
    """
    try:
        score = calcguess()
        if score[0] == 3:  # score[0] = S의 개수
            print("맞췄습니다! 축하합니다!")
            time.sleep(0.5)
            return True
        else:
            print("S:%d B:%d O:%d" % score)

    except (KeyError, ValueError, TypeError):
        print("exception...\n")


intro()
makenum()
while True:
    for i in range(10, 0, -1):
        user = takeinput(i)
        correct = det_process()
        if correct:
            secret = []
            makenum()
            break

    print("다시 도전하고 싶으십니까? (yes or no)")
    try:
        ans = input()
        if (ans == "yes") or (ans == 'y') or (ans == 'Y'):  # 다시 도전하면 While문을 돎
            print('reset...')
        else:
            print("종료함...")
            break
    except (KeyError, ValueError, TypeError, IndexError) as e:
        print("종료함...")
        time.sleep(0.5)
        break

print("정답은: %d%d%d" % tuple(secret))