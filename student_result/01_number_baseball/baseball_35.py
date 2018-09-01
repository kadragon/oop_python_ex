import random

TEXT_LINE = 80


def display_intro():  # intro 함수 python 에서는 함수를 def 을 이용하여 정의한다. 반환형을 명시하지 않는다.
    print('=' * TEXT_LINE)
    print("""
    This is number baseball game!
    (game rule)
    1. Random number will given which is three digits and digits are all different
    2. If you write three digit number ex)123 or 345, I will answer strike, ball and out
    strike - position and the number is right
    ball   - only number is right
    out    - all numbers wrong
    < Get the high score! >""")
    print('=' * TEXT_LINE)


def make_num():  # 숫자를 생성하는 함수
    b = list(range(10))
    random.shuffle(b)
    if b[0] == 0:  # 백의 자리에 0이 있으면 다시
        make_num()
    else:
        return b[:3]


def check_num(data):  # 잘 입력받았는지 확인하는 함수
    b = list(range(10))
    point = 0
    for i in b:  # 하나씩 대조함
        if i == data:
            point += 1
    if point == 3:
        return True
    else:
        return False


def hit_num(d, ans, count):  # 데이터와 정답을 비교하는 함수
    data = int(d)

    a = (data - data % 100) / 100  # 입력받은 데이터의 자릿수를 각각 분할(이미 세자리의 수임을 증명함)
    b = (data - data % 10 - 100 * a) / 10
    c = data - a * 100 - b * 10

    strike_stack = 0  # 스트라이크 수
    ball_stack = 0  # 볼 수

    user_list = [a, b, c]
    for i in range(3):  # 각 자릿수를 i번째 정답숫자와 비교한다.
        if user_list[i] == ans[i]:
            strike_stack += 1
        elif user_list[i] in ans:
            ball_stack += 1

    if strike_stack == 0 and ball_stack == 0:  # 아웃상황
        print('out!')
    elif strike_stack == 3:  # 정답 맞춘 상황
        print('Your right! you clear in %d turns Congratulation!' % (count))
        return True
    else:  # 그 외
        print('%dS %dB' % (strike_stack, ball_stack))

    return False


play_again = 'yes'  # 플레이를 지속할지를 입력 받아 임시 저장하는 공간
while play_again == 'yes' or play_again == 'y':
    display_intro()
    a = make_num()  # 정답생성
    count = 0  # 제한되는 턴

    while count < 10:
        data = str(input())
        letter = 0  # 문자열의 크기
        point = 1  # 잘 받았는지 임시 저장

        for i in data:
            if check_num(i):  # 숫자 맞는지
                point = 0
            letter = letter + 1

        if data[0] == data[1] or data[1] == data[2] or data[0] == data[2]:  # 서로 다른지
            point = 0

        if point == 0 or letter > 3:  # 하나라도 잘못됨 혹은 문자길이 3개 이상
            print('Write again please\n')
            continue

        count += 1  # 입력이 잘 되었으면 count 추가

        if hit_num(data, a, count):
            break  # 승리하면 리겜

        if count == 10:
            print('Turn over.....')  # 턴넘으면 리겜

    print('\n' + ('=' * TEXT_LINE))
    play_again = input('Do you want to play again? (yes or no): ')
