import random


def make_answer(digit_count):
    """
    게임의 정답을 만들어보자.
    정답의 자릿수를 입력받고, 중복되지 않은 0~9사이 3개 숫자의 조합을 만들자.
    :param digit_count: 정답의 자릿수
    :return: 게임의 정답. 중복되지 않은 3자리 문자열(숫자)
    """
    digits = list(range(10))  # 0~9의 숫자 나열된 리스트
    random.shuffle(digits)  # 리스트를 램덤으로 섞기
    # ans = ""  # T. 바로 아래에서 ans 이름 붙이고 있어서 여기서 할 필요 없음.
    ans = str(digits[0]) + str(digits[1]) + str(digits[2])  # 섞은 리스트의 첫 3개 숫자로 문자열 생성
    return ans  # 생성된 정답 문자열 반환


def sbo_check(user_num, ans):
    """
    사용자가 입력한 값에서 S/B/O를 판정하고 단서를 반환
    :param user_num: 사용자가 예상한 값
    :param ans: 게임의 정답(3자리 수)
    :return: 게임의 단서(S/B/O)
    """
    if user_num == ans:  # 사용자가 예상한 값이 정답인 경우
        return "정답입니다."

    s, b, o = 0, 0, 0  # STRIKE, BALL, OUT 개수 세기

    for i in list(range(len(user_num))):  # [0, ..., 예상한 문자열의 자리수-1]
        if user_num[i] == ans[i]:  # strike 인 경우
            s += 1
        elif user_num[i] in ans:  # ball 인 경우
            b += 1
        else:
            o += 1  # out 인 경우

    return "{}STRIKE  {}BALL  {}OUT".format(s, b, o)  # s/b/o 단서 반환


def format_check(user_num):
    """
    사용자가 입력한 값의 형태가 옳은지 확인해보자.
    :param user_num: 사용자가 입력한 값
    :return: True or False
    """
    if len(user_num) != 3:  # 3자리수 아니면 False
        return False

    for i in list(range(len(user_num))):  # 숫자 이외의 문자가 포함되면 False
        if user_num[i] not in "1234567890":
            return False

    return True


def one_more():
    """
    게임의 지속 여부를 확인해보자
    :return: 게임을 계속하지 않는 경우 True 반환
    """
    print("한 번 더??? [Y/N]\n", end=">>> ")  # 게임 지속 여부 확인
    cont = input()
    if cont == "N" or cont == "n":
        return True


DIGIT_COUNT = 3  # 정답의 자리수
GUESS_COUNT = 10  # 답변 제시 가능 횟수

print("=" * 50)
print("게임을 시작하지..!!!")
print("내가 %d자리 수를 생각할테니, 맞추어 보아라!" % DIGIT_COUNT)
print("최대 %d번 동안 답을 제시할 수 있고, 각각 다음과 같은 단서를 제시하겠다." % GUESS_COUNT)
print("1STRIKE : 한 개의 숫자가 포함되어 있고, 위치가 맞는 경우")
print("1BALL : 한 개의 숫자가 포함되어 있으나, 위치는 틀린 경우")
print("1OUT : 정답에 전혀 포함되어 있지 않은 경우")
print("=" * 50)

while True:
    ans = make_answer(DIGIT_COUNT)  # 정답 만들기
    g_count = 1  # 사용자가 답변을 제시한 횟수 세기
    print("\n정답을 예상해보세요")
    while g_count <= GUESS_COUNT:
        guess = ""  # 사용자 입력값을 저장할 객체
        while not format_check(guess):  # 입력값이 옳바른지 확인
            print("%d번째 예상" % g_count, end="\n>>> ")
            guess = input()

        print(sbo_check(guess, ans), "\n")  # 단서 제시

        if guess == ans:  # 정답인 경우
            break
        else:
            g_count += 1
        if g_count > GUESS_COUNT:  # 실패한 경우
            print("<<<실패! 정답은 %s입니다...>>>\n" % ans)
            break

    print("=" * 50 + "\n")

    if one_more():
        break

print("\n게임을 이용해 주셔서 감사합니다!!! 다음에 또 이용해 주세용^^")
