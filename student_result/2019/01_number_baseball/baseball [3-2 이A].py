import random
import time

DIGITS_MAX = 10  # 최대 길이 10으로 게임할 수 있음
PLAY_MAX = 20  # 게임 플레이 1회 당 최대 20번의 맞출 기회가 주어짐


def make_answer(user_len):
    """
    사용자가 입력한 숫자(user_len)만큼의 길이를 가진 암호를 생성하는 함수
    :param user_len: 사용자가 입력한 '숫자 길이'
    :return: user_len만큼의 길이를 가진 현재 게임의 암호
    """
    num_list = list(range(10))
    random.shuffle(num_list)  # 중복되지 않은 0부터 9까지의 숫자들을 랜덤으로 섞는다
    answer = ''
    for i in range(user_len):
        answer += str(num_list[i])  # 사용자가 입력한 숫자만큼의 암호를 생성한다

    return answer  # 답을 반환한다


def give_clues(user_enter, game_ans):
    """
    매 회마다 힌트를 주는 함수
    :param user_enter: 사용자가 입력한 숫자열
    :param game_ans: 게임의 암호
    :return: TRUE or FALSE
    """
    strike = 0  # 스트라이크 횟수
    ball = 0  # 볼 횟수
    out = 0  # 아웃 횟수
    if user_enter == game_ans:  # 사용자가 입력한 답과 게임의 암호가 같으면 1을 반환한다 (이후에 while-break 로 이어짐)
        print("오이오이 좀 하잖아~~")
        return True

    for i in range(len(user_enter)):  # 사용자가 입력한 답과 게임의 암호를 비교해 strike, ball, out 의 값을 계산한다
        if user_enter[i] == game_ans[i]:  # 숫자와 위치가 동일하면 strike 의 수를 1 올린다
            strike += 1
        elif user_enter[i] in game_ans:  # 숫자만 동일하면 ball 의 수를 1 올린다
            ball += 1
        else:  # 아무것도 해당 되지 않을 경우 out 의 수를 1 올린다
            out += 1

    print(str(strike) + 'S ' + str(ball) + 'B ' + str(out) + 'O')  # Ex. 2S 0B 1O 로 출력해서 사용자에게 보여준다
    return False  # 0을 반환한다


def cond_error(user_enter, game_cond):
    """
    사용자가 입력한 조건에 오류가 있는지 판별하는 함수 : 게임 진행 횟수, 숫자 길이
    :param user_enter: 사용자가 입력한 정보 (게임 진행 횟수, 숫자 길이)
    :param game_cond: 게임의 조건 (최대 도전 횟수, 최대 길이)
    :return: TRUE or FALSE
    """
    if user_enter > game_cond:  # 사용자가 입력한 숫자인 user_enter 가 게임 조건인 game_cond 보다 클 경우
        print("조건이 보이시지 않나요? ><")
        return True  # 1을 반환한다
    else:
        return False  # 0을 반환한다


def isnaturalnum(user_enter):
    """
    사용자가 입력한 정보가 자연수인지 판별하는 함수
    :param user_enter: 매 회마다 사용자가 입력한 자연수열
    :return: TRUE or FALSE
    """
    try:
        int(user_enter)  # 사용자가 자연수를 입력할 시 정상적으로 되지만, 그렇지 않다면 ValueError 가 발생한다
        if int(user_enter) <= 0:  # 사용자가 양이 아닌 정수를 입력했을 시에 오류 메시지와 함께 0을 반환함
            print("자연수를 입력하세요><")
            return False
        else:
            return True  # ValueError 가 작동하지 않았을 때에는 1을 반환한다

    except ValueError:  # ValueError 가 발생했을 시
        print("'자연수'를 '띄어쓰기 없이' 입력하세요><")
        return False  # 오류 메시지와 함께 0을 반환함 (이후에 while - continue 구문에서 사용됨)


def repeat(enter):  # 게임을 재반복할 것인지 확인하는 함수
    if enter == 'y':  # y 를 누를 경우 반복
        return 1
    elif enter == 'n':  # n 을 누를 경우 종료
        return 0
    else:  # 다른 키를 누를 경우 WRONG 반환
        return 'WRONG'


def wrong_enter(user_enter):  # 매 회마다 사용자가 입력한 문자열의 오류가 있는지 확인함, 자연수열이 아닐 경우 1을 반환함
    for i in user_enter:
        if not isnaturalnum(user_enter):  # 문자열의 각 문자마다 isnaturalnum 함수를 통해 자연수인지 아닌지 확인함
            return 1  # 자연수가 아닐 경우 1을 반환함

    return 0  # 그렇지 않을 경우, 즉 사용자가 자연수열을 입력한 경우 0을 반환함


def check_len(user_enter, game_psw):
    """
    매 회마다 사용자가 입력한 자연수열의 길이가 암호의 길이와 동일한 지 확인하는 함수
    :param user_enter: 매 회마다 사용자가 입력한 자연수열
    :param game_psw: 현재 게임의 암호
    :return: TRUE or FALSE
    """
    if len(user_enter) == len(game_psw):
        return True

    print("길이 맞춰서 써라;;;;")
    return False


def overlap(enter):
    """
    입력된 숫자열 중에 중복되는 것이 있는지 확인하는 함수
    :param enter: 사용자가 입력하는 숫자열
    :return: TRUE or FALSE
    """

    for i in range(0, len(enter)):
        for j in range(i + 1, len(enter)):
            if enter[i] == enter[j]:
                print("[충격] 중복된 숫자를 입력하는 바보가 있다??")
                return 1

    return 0


print("자기소개서가 끝난 후에 만드는 야구 게임")  # 게임 시작 메시지
print("면접 2달 전에 만드는 야구 게임")
print("혼자 놀려고 만든 야구 게임")
print("=" * 80)
print("숫자랑 위치가 맞으면 Strike(S)")
print("숫자는 같은데 위치가 다르면 Ball(B)")
print("숫자가 다르면 Out(O)")
print("=" * 80)

while True:
    game_len = input("원하는 숫자 길이를 입력하세요! 최대 숫자 길이는 10입니다. : ")  # 숫자 길이를 입력받는 객체 game_len
    if not isnaturalnum(game_len):  # game_len이 숫자가 아니라면 다시 반복
        continue
    if cond_error(int(game_len), DIGITS_MAX):  # game_len(숫자 길이)이 DIGITS_MAX(최대 길이)에 벗어나면 다시 반복
        continue

    play_digit = input("도전 횟수를 입력하세요! 각 게임 당 최대 도전 횟수는 20회입니다. "
                       "잘못 입력하면 처음부터~ . : ")  # 도전 횟수를 입력받는 객체 play_digit
    if not isnaturalnum(play_digit):  # play_digit이 숫자가 아니라면 다시 반복
        continue
    if cond_error(int(play_digit), PLAY_MAX):  # play_digit(도전 횟수)이 PLAY_MAX(최대 도전 횟수)에 벗어나면 다시 반복
        continue

    print("게임을 생성하는 중입니다.... Loading")
    time.sleep(3)  # 3초 대기 (그냥 했어요)
    print("=" * 80)
    print('드루와')
    password = make_answer(int(game_len))  # 현재 게임의 암호를 생성하고, 그것을 받는 객체가 password
    count = 1  # 현재 게임 진행 횟수를 받는 객체 count

    while count <= int(play_digit):  # 게임 진행 횟수가 사용자가 입력한 도전 횟수를 넘지 않을 때까지 반복
        print("%s차 시도 두두둥: " % count, end=' ')  # Ex. 3차 시도 두두둥:  (count = 3)
        user_ans = input()  # 사용자가 입력한 문자열을 받는 객체인 user_ans
        if wrong_enter(user_ans):  # user_ans가 자연수열이 아닐 경우 다시 입력 반복
            continue
        if not check_len(user_ans, password):  # user_ans의 길이가 암호의 길이와 다를 경우 반복
            continue
        if overlap(user_ans):  # user_ans에 중복되는 숫자가 있으면 반복
            continue
        if give_clues(user_ans, password) == 1:  # 게임 진행 중 사용자가 입력한 답과 게임의 암호가 동일할 경우 STOP!
            break
        count += 1

    if count > int(play_digit):  # 답을 맞추지 못했을 경우에 메시지 출력
        print("오이오이 그것도 못 맞추면 어떡하냐구~ 답 : %s" % password)

    while True:
        rep = input("자자 게임을 다시 해볼 거냐고? 다시 하고 싶으면 y, 싫으면 n을 누르세요: ")  # 사용자의 반복 여부를 받는 객체
        if repeat(rep) == 1:  # 사용자가 반복을 원하는 경우 y를 누르면 다시 반복
            break
        elif repeat(rep) == 0:  # 반복을 원하지 않는 경우 n을 눌러 시스템 종료
            exit()
        else:
            print("오이오이 입력 좀 똑바로 하라고~")  # 나머지 키를 누를 경우 다시 반복

    print("=" * 80)
