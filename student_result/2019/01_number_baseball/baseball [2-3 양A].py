"""
숫자 야구 게임 2019.09.23
made by 2309 양현서
"""


import random


NUM_DIGITS = 3      # 정답 숫자의 자릿수를 나타내는 상수
NUM_CHANCES = 10    # 문제를 맞추는 전체 기회의 수를 나타내는 상수
ANSWER = ""         # 정답 숫자를 문자열로 저장하는 상수


def start_notification():
    """
    숫자 야구 게임을 시작하기 전에 실행되는 함수로서, 플레이어의 요구에 따라 숫자 야구의 규칙에 대해 설명하는 함수.
    :return: 없음.
    """
    global NUM_DIGITS, NUM_CHANCES, ANSWER      # 전역 변수 사용을 위한 선언

    print('=' * 100)
    print("<숫자 야구 게임>이 시작되었습니다.")
    print("┻┳|\n"
          "┳┻|__∧   ...야구?\n"
          "┻┳|•﹃•)\n"
          "┳┻|⊂ﾉ\n"
          "┻┳|Ｊ\n")
    print("<숫자 야구 게임>의 규칙 설명을 들으시겠습니까? (y/(n))", end=' ')

    rule = input()      # 규칙 설명을 듣는지 여부에 대한 대답 입력.

    if rule == 'y' or rule == 'yes':        # y, 또는 yes가 입력될 경우 규칙에 대한 설명 제공
        rule_explain()

    if rule == "developer":
        # 편리한 디버깅을 위해 제작한 개발자 모드, 위 질문에 developer를 입력하면 정답 숫자의 자릿수와 정답 기회를 설정할 수 있다.
        print("개발자 모드로 전환합니다.")
        print("NUM_DIGITS =", end=' ')
        NUM_DIGITS = int(input())           # 1부터 10까지의 정수를 입력받아 정답 숫자의 자릿수 NUM_DIGITS를 재설정
        print("NUM_CHANCES =", end=' ')
        NUM_CHANCES = int(input())          # 자연수를 입력받아 정답 기회 NUM_CHANCES를 재설정
        print("숫자의 자릿수는 %d, 정답 입력 기회는 %d(으)로 재설정되었습니다." % (NUM_DIGITS, NUM_CHANCES))

    print('\n' + '=' * 100)
    print("Enter를 누르면 시작합니다!", end=' ')
    input()         # Enter를 누른 후에 게임이 시작되도록 임의의 입력을 받음.


def rule_explain():
    """
    숫자 야구 게임의 규칙을 출력하는 함수.
    :return: 없음.
    """
    global NUM_DIGITS

    print('\n' + '=' * 100)
    print("|숫자 야구 게임 규칙|")
    print("각 자리수가 모두 다른 %d자리 숫자가 랜덤으로 생성됩니다." % NUM_DIGITS)
    print("그 %d자리 숫자를 %d번 안에 맞추면 승리하고, 그렇지 못하면 패배합니다." % (NUM_DIGITS, NUM_CHANCES))
    print("숫자를 입력하면, 입력한 숫자가 정답과 얼마나 유사한지 '숫자 야구' 형식으로 알려줍니다.")
    print("각 '숫자 야구' 정보가 의미하는 바는 다음과 같습니다.")
    print("")
    print("Strike (S): 정답에 포함되고, 위치도 일치하는 숫자의 개수")
    print("Ball   (B): 정답에 포함되지만, 위치는 일치하지 않는 숫자의 개수")
    print("Out    (O): 정답에 포함되지 않는 숫자의 개수")


def random_number():
    """
    NUM_DIGITS 만큼의 자릿수를 가진 임의의 숫자를 문자열의 형태로 랜덤 반환하는 함수.
    :return: 문자열 형식의 랜덤으로 만들어진 정답 숫자
    """
    global NUM_DIGITS

    num_list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]       # 0부터 9까지의 정수 리스트 선언
    random.shuffle(num_list)                        # 랜덤으로 리스트를 섞음

    answer = ""                             # 정답을 문자열 형태로 선언
    for i in range(NUM_DIGITS):             # 문제 숫자 자릿수 만큼 반복
        answer += str(num_list[i])          # 정답 문자열의 뒷부분에 랜덤으로 섞은 정수 문자를 추가

    return answer       # 문자열 형식의 정답 반환


def is_right_input(number):
    """
    플레이어가 입력한 문자열이 옳은 형식인지 여부를 리턴하는 함수.
    입력 문자열이 옳지 않은 형식일 경우, 어떠한 부분이 잘못되었는지 알려줌.
    :param number: 문자열 형태의 플레이어가 입력한 숫자.
    :return: 옳은 형식의 입력일 경우 True, 옳지 않은 형식의 입력일 경우 False를 반환.
    """
    global NUM_DIGITS, ANSWER

    digits = "0123456789"   # 0~9의 정수로 이루어진 문자열. 입력된 문자가 숫자 문자인지 판단할 때 사용.
    check = [0] * 20        # 0~9의 정수가 입력되었는지 기록하는 리스트. 정수 k가 이전에 입력된 경우, check[k]의 값은 1, 그렇지 않은 경우 0.

    for i in number:        # number의 모든 구성 문자에 대해 확인.
        if i not in digits:     # number의 구성 문자가 정수 문자가 아닐 때,
            print("영문, 한글, 특수문자, 공백 등의 숫자가 아닌 문자는 입력할 수 없습니다.\n")   # 입력 오류 안내
            return False    # 옳지 않은 입력이므로 False 반환.

    if len(number) < NUM_DIGITS:    # number의 자릿수가 정답 숫자의 자릿수보다 작을 때
        print("입력하신 숫자의 개수가 너무 적습니다. %d개의 숫자를 입력해 주십시오.\n" % NUM_DIGITS)    # 입력 오류 안내
        return False    # 옳지 않은 입력이므로 False 반환.

    if len(number) > NUM_DIGITS:    # number의 자릿수가 정답 숫자의 자릿수보다 클 때
        print("입력하신 숫자의 개수가 너무 많습니다. %d개의 숫자를 입력해 주십시오.\n" % NUM_DIGITS)    # 입력 오류 안내
        return False    # 옳지 않은 입력이므로 False 반환.

    for i in number:    # number의 모든 구성 문자에 대해 확인.
        if check[int(i)] == 1:      # 같은 숫자가 2번 number에 두 개 이상 존재할 때,
            print("같은 숫자는 입력할 수 없습니다.\n")   # 입력 오류 안내
            return False    # 옳지 않은 입력이므로 False 반환.

        check[int(i)] = 1       # 정수 i가 입력되었다는 것을 기록.

    return True     # 위의 모든 경우에 해당하지 않는 경우 옳은 입력이므로 True 반환.


def baseball_information(number):
    """
    플레이어가 입력한 옳은 형식의 정수 문자열이 정답 정수 문자열과 얼마나 유사한지 '숫자 야구' 형식으로 알려주는 함수.
    플레이어가 입력한 문자열의 정답 여부를 반환한다.
    :param number: 플레이어가 입력한 옳은 형식의 정수 문자열.
    :return: 플레이어가 입력한 정수 문자열이 정답과 일치할 경우 True, 일치하지 않을 경우 False를 반환.
    """
    # strike, ball, out의 개수를 저장할 변수들 선언.
    strike = 0
    ball = 0
    out = 0

    for i in range(NUM_DIGITS):     # 0 ~ NUM_DIGITS-1 의 인덱스, 즉, 문자열의 모든 문자에 대해 확인.
        if number[i] == ANSWER[i]:  # number에 속한 문자와 정답 문자의 종류와 위치가 모두 같은 경우,
            strike += 1             # strike 개수 증가
        elif number[i] in ANSWER:   # number에 속한 문자와 정답 문자의 종류는 같지만 위치가 다른 경우,
            ball += 1               # ball 개수 증가
        else:                       # number에 속한 문자가 정답 문자열에 존재하지 않는 경우,
            out += 1                # out 개수 증가

    print("\nStrike → %d | Ball → %d | Out → %d" % (strike, ball, out))       # '숫자 야구' 형식의 정보 안내.

    if strike == NUM_DIGITS:    # 스트라이크의 개수와 정답 숫자의 자릿수가 같은 경우, 즉, number가 정답 문자열인 경우,
        return True             # number가 정답이므로 True 반환.
    else:                       # number가 정답 문자열이 아닌 경우,
        return False            # number가 오답이므로 False 반환.


def win(round):
    """
    주어진 기회 내에 정답을 맞춘 경우, 정답을 맞춘 라운드와 승리 문구를 출력하는 함수.
    :return: 없음.
    """
    print('\n' + '-' * 100)
    print("...Λ＿Λ\n"
          "（ㆍωㆍ)つ━☆*。\n"
          "⊂　　 ノ 　　　.정\n"
          "　し-Ｊ　　　°。답 *´¨)\n"
          "　　　　　　..　.· ´¸.·이*´¨) ¸.·*¨)\n"
          "　　　　　　　　　　(¸.·´ (에요!¸.'*\n")
    print("%d 라운드 만에 정답을 맞추어 승리하셨습니다!" % round)


def lose():
    """
    주어진 기회 내에 정답을 맞추지 못한 경우, 패배 문구를 출력하는 함수.
    :return: 없음.
    """
    global NUM_CHANCES

    print('\n' + '-' * 100)
    print("╭┈┈┈┈╯   ╰┈┈┈╮\n\n"
          " ╰┳┳╯    ╰┳┳╯\n\n"
          "  N 　    N\n\n"
          " ○  　     ○\n"
          "    ╰┈┈╯\n"
          "  O  ╭━━━━━╮　 O\n"
          "     ┈┈┈┈\n"
          "　　o     　　 o\n")
    print("%d 라운드 만에 정답을 맞추지 못해 패배하셨습니다..." % NUM_CHANCES)


def play_game():
    """
    하나의 게임을 시작하는 함수.
    :return: 없음
    """
    global NUM_DIGITS, NUM_CHANCES, ANSWER

    ANSWER = random_number()    # 정답 문자열을 랜덤으로 생성.
    for i in range(1, NUM_CHANCES+1):   # 1 ~ NUM_CHANCES 의 라운드를 총 NUM_CHANCES 회 진행.
        print('\n' + '-' * 100)
        print("%d 라운드입니다. %d번의 기회가 남아있습니다\n" % (i, NUM_CHANCES - i + 1))   # 라운드와 잔여 기회 정보 안내.

        while True:     # 옳은 형식의 문자열이 입력될 때까지 반복.
            print("숫자를 입력하세요:", end=' ')
            number = input()    # 플레이어의 문자열 입력.

            if number == "exit":    # 만약 exit 가 입력되면, 게임을 중도 종료.
                print('\n' + "=" * 100)
                print("게임을 종료합니다.")
                return      # 함수 전체를 리턴함으로써 게임 종료.

            if is_right_input(number):      # 옳은 형식의 문자열이 입력되면, 반복문 탈출
                break

        is_answer = baseball_information(number)    # 플레이어가 입력한 문자열의 '숫자 야구' 정보를 안내하고, 정답 여부를 받아옴.
        if is_answer:   # 플레이어가 입력한 문자열이 정답일 경우,
            win(i)       # 승리 문구 출력.
            return      # 함수 전체를 리턴함으로써 게임 종료.

    lose()      # 플레이어가 입력한 문자열이 정답이 아니어서 함수가 리턴되지 않은 경우, 패배 문구를 출력.


def play_again():
    """
    게임을 다시 플레이할지 물어보고, 플레이어의 대답에 따라 재시작 여부를 반환하는 함수.
    :return: 플레이어가 게임을 다시 플레이 하겠다고 답하면 True, 그렇지 않다면 False를 반환.
    """
    print('\n' + '-' * 100)
    print("다시 플레이 하시겠습니까? (y/(n))", end=' ')

    replay = input()    # 재시작 여부에 대한 대답 입력.

    if replay == "y" or replay == "yes":    # y 또는 yes가 입력될 경우, 플레이어가 재시작을 원한다는 의미의 True 리턴.
        return True
    else:                                   # 그렇지 않을 경우, 플레이어가 재시작을 원하지 않는다는 의미의 False 리턴.
        return False


start_notification()    # 숫자 야구 게임에 대한 설명을 제공함으로써 게임의 시작을 알림.
while True:     # 사용자가 재시작을 원하지 않을 때까지,
    play_game()     # 게임을 시작.

    if not play_again():    # 게임이 끝나면 재시작 여부에 관해 질문, 플레이어가 재시작을 원하지 않는다고 답하면 프로그램을 종료.
        break

