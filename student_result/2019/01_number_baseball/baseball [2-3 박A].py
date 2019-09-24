# 플레이어가 추측해야 할 임의의 비밀번호를 만드는 함수를 정의하기 위하여
import random


def get_random_number(num_digits):
    """
    num_digits 길이만큼의 문자열을 반환. 임의의 숫자로 이루어지도록
    https://docs.python.org/ko/3/library/random.html?highlight=random%20shuffle#random.shuffle
    :param num_digits: 원하는 문자열의 길이
    :return: 중복되지 않은 숫자로 이루어진 문자열
    """
    numbers = list(range(10))  # range() 함수의 반환형은 iterator 형식의 객체 / list() 를 이용하여 list 형으로 변경
    random.shuffle(numbers)  # list 의 값을 임의의 순서로 섞는다. [0, 1, ~ 8, 9] > [1, 7, ~ 6, 2] 와 같이..
    correct_answer = ''
    for i in range(num_digits):  # 원하는 길이 만큼 반복하며 원하는 길이의 문자열을 만듬 / 이렇게 만들경우 중복이 생기지 않는다.
        correct_answer += str(numbers[i])
    return correct_answer


def get_clues(user_guess, correct_answer):
    """
    Strike, ball, out 를 판정하여 반환
    user_guess: 사용자가 선택한 값
    secret_number: 정답
    :return: 결과를 작성한 문자열 " 0 Strike | 1 Ball | 2 Out "
    """
    if user_guess == correct_answer:  # 사용자가 선택한 값이 정답과 같으면 승리로 결과
        return '축하합니다! 맞추셨습니다!'

    ans_s = 0  # strike 인 경우 갯수 세기
    ans_b = 0  # ball   인 경우 갯수 세기
    ans_o = 0  # out    인 경우 갯수 세기

    for i in range(len(user_guess)):  # 0 ~ 사용자가 선택한 문자열의 갯수
        if user_guess[i] == correct_answer[i]:  # strike 인 경우
            ans_s += 1
        elif user_guess[i] in correct_answer:  # ball 인 경우
            ans_b += 1
        else:  # out 인 경우
            ans_o += 1

    return str(ans_s) + ' Strike | ' + str(ans_b) + ' Ball | ' + str(ans_o) + ' Out\n'


def only_digits(num):
    """
    사용자가 입력한 값이 숫자로 이루어져 있으면 True, 아니면 False
    :param num: 사용자가 입력한 값
    :return: True or False
    """
    if num == ' ':
        return False

    for i in num:
        # list(range(0, 10)) or '0 1 2 3 4 5 6 7 8 9'.split() 사용
        if int(i) not in list(range(0, 10)):  # range(0, 10) > list 형으로 변환하여 사용
            return False

    return True


def play_again():  # 플레이어가 다시 게임을 시작할지 결정한다.

    return input('다시 하시겠습니까? 다시 하시려면 y를 누르고 엔터키를 누르시고, 그렇지 않으면 엔터키를 눌러주세요').lower().startswith('y')


# Python 에서 상수처럼 사용하고 싶으면, 대문자 + _ 을 사용

def decide_level(level):  # 게임의 난이도를 결정한다
    if level == 'a':  # a를 입력할 시 5를 리턴
        return 5
    elif level == 'b':  # b를 입력할 시 7을 리턴
        return 7
    elif level == 'c':
        return 10  # c를 입력할 시 10을 리턴


while True:
    print("난이도를 설정하세요.")

    while True:
        level = ' '  # 난이도 입력을 저장하는 변수
        print("어려운 난이도는 a, 보통 난이도는 b, 쉬운 난이도는 c를 누르고 엔터를 누르세요 :")

        level = input()  # 난이도 입력
        # if level == 'a' or level == 'b' or level == 'c':  # a,b,c를 입력할 때만 레벨을 결정하게 함
        if level in "abc":  # a,b,c를 입력할 때만 레벨을 결정하게 함
            decidedlevel = decide_level(level)  # decide_level로 결정된 리턴 값을 decidedlevel변수에 저장
            break

    max = decidedlevel  # decidedlevel을 max에 대입함으로써 decide level의 리턴 값을 max에 저장

    print("=" * 80)
    print("제가 생각하는 세 자리 정수를 맞춰보세요.")
    print("각 자리의 숫자는 0부터 9까지의 숫자 중 하나이고 세 자리의 숫자들은 모두 다릅니다")
    print("첫 자리가 0일 수도 있습니다")
    print("Strike   어떤 자리의 숫자가 정확하고 위치 또한 정확하다는 의미입니다")
    print("Ball     어떤 자리의 숫자가 정확하지만 위치는 정확하지 않습니다")
    print("Out      맞지 않는 숫자가 있습니다.")
    print("각각의 설명은 이렇습니다")
    print("입력은 123, 234, 579와 같은 형식으로 해 주십시오")
    print("=" * 80)

    real_answer = get_random_number(3)  # 정답 생성
    print('\n수 하나를 생각했습니다. %s번의 기회를 드릴 테니 제가 생각한 수를 맞추십시오.' % max)

    num_guesses = 1  # 몇번 시도했는지 확인하기 위한 변수 객체
    while num_guesses <= max:  # 시도 횟수가 초과하지 않았는지 확인
        guess = ' '  # 사용자 입력 값 저장하기 위한 변수 객체
        while len(guess) != 3 or not only_digits(guess):  # 입력한 값이 길이가 적당한지, 정수만 입력했는지 확인
            print('#%s째 시도 (틀릴 시 #%s번 남음):' % (num_guesses, max - num_guesses), end=' ')
            guess = input()
            if guess == 'cheating':  # cheating 을 입력 시 real_answer, 즉 답이 출력되게 함. 일종의 이스터에그
                print("%s" % real_answer)

        print(get_clues(guess, real_answer))
        num_guesses += 1

        if guess == real_answer:
            break
        if num_guesses > max:
            print('기회가 모두 소진되었습니다. 정답은 %s 이었습니다.' % real_answer)

    if not play_again():
        break
