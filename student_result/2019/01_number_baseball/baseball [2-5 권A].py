# 숫자 야구 게임 _2502 권태희

import random
import sys


def opening():
    # 게임 시작 멘트
    print("=" * 40)
    print("숫자 야구 게임을 시작합니다")
    print("정답은 0~9 범위의 서로 다른 숫자 세 개입니다")
    print("정답을 맞출 기회는 총 10번입니다")
    print("0~9 범위의 서로 다른 숫자 세 개를, 공백을 포함하여 입력해주세요")
    print("입력 예시:0 1 2")
    print("정답 여부는 다음과 같이 주어집니다: S (숫자) || B (숫자) || O (숫자)")
    print("S는 숫자와 위치가 모두 맞는 '스트라이크', B는 숫자만 맞은 '볼, O는 모두 틀린 '아웃'의 개수입니다")
    print("무엇이 볼이고, 무엇이 스트라이크인지는 알려주지 않습니다")
    print("그럼, Good Luck!")
    print("=" * 40)


def create_number(li):
    # 정답 숫자 3개 생성하는 함수
    # 중복을 방지하기 위해, 0부터 9까지의 리스트 'li'를 무작위로 섞은 이후 앞의 3개만 슬라이스하여 return
    random.shuffle(li)
    return li[0:3]


def play_scanning(k):
    # 몇 번째 시도인지를 안내하고, 입력을 받아 입력된 값을 리스트의 형태로 return한다
    # 잘못된 입력이 들어오면 다시 입력할 수 있도록 한다
    # k는 (시도 횟수)-1의 값을 저장하는 변수
    global scanlist
    try:
        scanlist = list(map(int, input("%d번째 시도 >>>  " % (k+1)).split( )))

    except (TypeError, ValueError, SyntaxError, KeyboardInterrupt):
        print("잘못된 입력입니다")
        play_scanning(k)
        # 일어날 수 있는 각종 에러의 예외 처리
    else:
        if len(scanlist) != 3:
            print("세 개의 정수를 입력하세요")
            play_scanning(k)
            # 입력된 개수가 3개가 아닌 경우
        else:
            for i in range(3):
                if type(scanlist[i]) != int:
                    print("0~9 범위의 정수만 입력해주세요")
                    play_scanning(k)
                    # 입력된 것이 정수가 아닌 경우
                if scanlist[i] > 9 or scanlist[i] < 0:
                    print("0~9 범위의 정수만 입력해주세요")
                    play_scanning(k)
                    # 입력 범위가 잘못된 경우
            if scanlist[0] == scanlist[1] or scanlist[1] == scanlist[2] or scanlist[0] == scanlist[2]:
                print("세 개의 서로 다른 정수를 입력해주세요")
                play_scanning(k)
                # 중복 입력이 있는 경우

    return scanlist


def play_checking(checklist, answerlist):
    # checklist는 플레이어가 입력한 답, answerlist는 정답
    # s는 스트라이크 개수, b는 볼 개수, o는 아웃 개수
    # 스트라이크와 볼, 아웃의 개수를 출력
    s = 0
    b = 0
    o = 0
    for i in range(3):
        if checklist[i] == answerlist[i]:
            s = s + 1
            # 스트라이크인 경우, s값을 증가
        else:
            for j in range(3):
                if checklist[i] == answerlist[j]:
                    b = b + 1
                    # 볼인 경우, b값을 증가
        if (s + b + o) != (i + 1):
            o = o + 1
            # 스트라이크와 볼이 모두 아닌 경우, o값을 증가
    print("S %d || B %d || O %d" % (s, b, o))
    if s == 3:
        play_ending(1)
        # 3스트라이크인 경우, 더 이상 플레이하지 않고 종료(승리)


def play_ending(win_or_lose):
    # win_or_lose가 1이면 승리, 0이면 패배
    # win_or_lose의 값에 따라 마무리 멘트가 다름
    # 다시 게임을 플레이할 것인지 물어보는 play_more 함수를 호출
    if win_or_lose == 1:
        print("축하합니다! 3 스트라이크!!")
    else:
        print("아쉽게도 10번의 기회를 전부 사용하셨습니다. 다음에는 성공하길 바래요!")
    play_more()


def play_more():
    # 다시 게임을 플레이할 것인지 물어봄. 잘못된 입력에 대한 예외 처리 포함
    # 다시 플레이하는 경우, 다시 main 함수를 호출하여 처음부터 게임을 진행하도록 함
    print("한 번 더 플레이하시겠습니까?")
    try:
        end = int(input("한 번 더 플레이: 1 플레이 종료: 0 >>>  "))
    except(TypeError, ValueError, KeyboardInterrupt):
        print("다시 입력해주세요")
        play_more()
    if end == 1:
        print("좋은 선택이에요!")
        main()
    elif end == 0:
        print("언젠가 다시 만나요!")
        sys.exit()
    else:
        print("다시 입력해주세요")
        play_more()


def main():
    # 게임의 전체적인 흐름
    opening()
    # 오프닝 멘트
    answerlist = create_number(list(range(10)))
    # create_number 함수에서 슬라이스하여 return된 리스트를 answerlist라고 한다

    for i in range(10):
        yourlist = play_scanning(i)
        play_checking(yourlist, answerlist)
        # 10번의 기회 동안 답 입력받고(play_scanning) 정답 판정(play_checking)

    play_ending(0)
    # 정답을 맞추지 못한 경우, 패배 상태로 게임 종료


main()