# Time access and conversions
# Generate pseudo-random numbers
import random
import time

# Python 에서는 상수 선언이 없다. 다만, 표기를 대문자와 '_' 만을 사용하여 구분함.
TEXT_LINE = 80
SLEEP_TIME = 1


def display_intro():  # intro 함수 python 에서는 함수를 def 을 이용하여 정의한다. 반환형을 명시하지 않는다.
    print('=' * TEXT_LINE)
    print("""
    I am thinking of a 3-digit number. Try to guess what it is
    Here are some clues: 
    When I say:     That means:
    Strike  (S)     One digit is correct and in the right position
    Ball    (B)     One digit is correct but in the wrong position
    Out     (O)     No digit is correct
    """)
    print('=' * TEXT_LINE)


def random_number():
    # 변수를 선언할때에는 var_length OR varLength 와 같은 형태로 선언
    numlist = list(range(10))
    random.shuffle(numlist)
    strnum = ''
    for i in numlist[0:3]:
        strnum += str(i)
    return strnum


def choose_number():  # 동굴을 선택하는 함수
    number = ' '
    while True:
        number = input('select 3 different number from 0 ~ 9 and input without a space : ')
        if number.isdigit() and len(number) == 3:
            break
        print("only 3 'number'")
    return number


def check_number(chosen_number, ans_number):  # 결과를 보여주는 함수
    print('wait a second...')
    time.sleep(SLEEP_TIME)
    strk = 0
    ball = 0
    out = 0
    for i in chosen_number:
        if ans_number.find(i) == chosen_number.find(i):
            strk += 1
        elif i in str(ans_number):
            ball += 1
        else:
            out += 1

    print("%d S | %d B | %d O\n" % (strk, ball, out))
    return strk


# main
play_again = 'yes'  # 플레이를 지속할지를 입력 받아 임시 저장하는 공간
while play_again == 'yes' or play_again == 'y':
    display_intro()
    base_num = random_number()
    # print(base_num) #정답을 확인
    j = 0
    while True:
        base_number = choose_number()
        strike = check_number(base_number, base_num)
        if strike == 3:
            print("Win! you got answer just for %d tries!" % j)
            break
        elif j < 8:
            j += 1
        else:
            print("Sad... the answer was %s" % base_num)

    print('\n' + ('=' * TEXT_LINE))
    play_again = input('Do you want to play again? (yes or no): ')
