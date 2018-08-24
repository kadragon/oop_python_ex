"""
Title       야구 게임
Reference   나만의 Python Game 만들기 Chapter 11 p.231
Author      kadragon
Date        2018.08.24
"""

# 플레이어가 추측해야 할 임의의 비밀번호를 만드는 함수를 정의하기 위하여
import random


def get_secret_num(num_digits):
    """
    num_digits 길이만큼의 문자열을 반환. 임의의 숫자로 이루어지도록
    https://docs.python.org/ko/3/library/random.html?highlight=random%20shuffle#random.shuffle

    :param num_digits: 원하는 문자열의 길이
    :return: 중복되지 않은 숫자로 이루어진 문자열
    """
    numbers = list(range(10))  # range() 함수의 반환형은 iterator 형식의 객체 / list() 를 이용하여 list 형으로 변경
    random.shuffle(numbers)  # list 의 값을 임의의 순서로 섞는다. [0, 1, ~ 8, 9] > [1, 7, ~ 6, 2] 와 같이..
    secret_number = ''
    for i in range(num_digits):  # 원하는 길이 만큼 반복하며 원하는 길이의 문자열을 만듬
        secret_number += str(numbers[i])
    return secret_number


def get_clues(user_guess, secret_number):
    """
    Strike, ball, out 를 판정하여 반환
    :param user_guess: 사용자가 선택한 값
    :param secret_number: 정답
    :return: 결과를 작성한 문자열 " 0 S | 1 B | 2 O "
    """
    if user_guess == secret_number:  # 사용자가 선택한 값이 정답과 같으면 승리로 결과
        return 'You got it!'

    ans_s = 0  # strike 인 경우 갯수 세기
    ans_b = 0  # ball   인 경우 갯수 세기
    ans_o = 0  # out    인 경우 갯수 세기

    for i in range(len(user_guess)):  # 0 ~ 사용자가 선택한 문자열의 갯수
        if user_guess[i] == secret_number[i]:  # strike 인 경우
            ans_s += 1
        elif user_guess[i] in secret_number:  # ball 인 경우
            ans_b += 1
        else:  # out 인 경우
            ans_o += 1

    return str(ans_s) + ' S | ' + str(ans_b) + ' B | ' + str(ans_o) + ' O\n'


def is_only_digits(num):
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


def play_again():
    """
    플레이어가 게임을 다시 지속할지 결정
    :return:
    """
    return input('Do you want to play again? (yes or no)').lower().startswith('y')


# Python 에서 상수처럼 사용하고 싶으면, 대문자 + _ 을 사용
NUM_DIGITS = 3  # 맞출 정답의 길이 설정하는 것
MAX_GUESS = 10  # 최대 시도 횟수

print("=" * 80)
print("I am thinking of a %s-digit number. Try to guess what it is." % NUM_DIGITS)
print("Here are some clues:")
print("When I say:  That means:")
print("Strike (S)   One digit is correct and in the right position.")
print("Ball   (B)   One digit is correct but in the wrong position.")
print("Out    (O)   No digit is correct.")
print("=" * 80)

while True:
    secret_num = get_secret_num(NUM_DIGITS)  # 정답 생성
    print('\nI have thought up a number. You have %s guesses to get it.' % MAX_GUESS)

    num_guesses = 1                         # 몇번 시도했는지 확인하기 위한 변수 객체
    while num_guesses <= MAX_GUESS:         # 시도 횟수가 초과하지 않았는지 확인
        guess = ' '                         # 사용자 입력 값 저장하기 위한 변수 객체
        while len(guess) != NUM_DIGITS or not is_only_digits(guess):    # 입력한 값이 길이가 적당한지, 정수만 입력했는지 확인
            print('Guess #%s:' % num_guesses, end=' ')
            guess = input()

        print(get_clues(guess, secret_num))
        num_guesses += 1

        if guess == secret_num:
            break
        if num_guesses > MAX_GUESS:
            print('You ran out of guesses. The answer was %s.' % secret_num)

    if not play_again():
        break
