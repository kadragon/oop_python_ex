# -*- coding: utf-8 -*-
"""
Title       Baseball Game (n자리 대응용: 3~9자리까지 가능)
Date        2018.08.29
"""

import random


def is_digit(user_input_number):  # 문자열 값을 입력받아 정수로 변환 가능할 경우에는 True, 그렇지 않다면 False로 변환해줌
    result = user_input_number.isdigit()
    return result


def is_vaildated_number(user_input_number):  # 10^n-1 ~ (10^n)-1 범위의 숫자를 입력하였는가?
    result = None
    inres = int(user_input_number)
    # print((10 ** (baseball_count-1)))
    # print((10 ** (baseball_count))-1)
    if (10 ** (baseball_count - 1)) <= inres <= ((10 ** baseball_count) - 1):
        result = True
    else:
        result = False
    return result


def is_duplicated_number(three_digit):  # n자리 양의 정수값을 입력받아 중복되는 수가 있는지 검사
    return len(set(three_digit)) != baseball_count


def is_validated_number(user_input_number):  # 숫자형 문자열이고, 100 이상 1000 미만, 중복되는 숫자가 없는지 이 세가지의 조건을 만족해야만 True
    result = None
    a = is_digit(user_input_number)
    if a:
        b = is_vaildated_number(user_input_number)
        c = is_duplicated_number(user_input_number)
        if b and not c:
            result = True
        else:
            result = False
    else:
        result = False
    return result


def get_not_duplicated_three_digit_number():  # random number를 생성할 때 중복되는 숫자가 없는지 확인
    answer = []

    def generate_number():
        while len(answer) < int(baseball_count):
            number = random.randint(1, 9)
            if number in answer:
                number = random.randint(1, 9)
            else:
                answer.append(number)
        return answer

    answer = generate_number()
    res = ''
    for i in range(0, int(baseball_count)):
        res += str(answer[i])

    return int(res)


def get_strikes_or_ball(user_input_number,
                        random_number):  # 사용자가 입력한 세 자리 정수 문자열, 컴퓨터가 생성한 세 자리 정수 문자열을 입력받아, strikes, balls 반환
    result = [0, 0]
    for i in range(0, baseball_count):
        for j in range(0, baseball_count):
            if user_input_number[i] == str(random_number[j]) and i == j:
                result[0] += 1
            if user_input_number[i] == str(random_number[j]) and i != j:
                result[1] += 1
    return result


# 꼭 yes / no 를 분리해서 판단해야 하는지 고민해보자.
def is_yes(one_more_input):  # 문자열값이 대소문자에 관계 없이 Y 또는 YES인지 감지
    if one_more_input.startswith('y') or one_more_input.startswith('Y'):
        return True
    else:
        return False


def is_no(one_more_input):  # 문자열값이 대소문자에 관계 없이 N 또는 NO인지 감지
    if one_more_input.startswith('n') or one_more_input.startswith('N'):
        return True
    else:
        return False


baseball_count = 0
while True:
    inp = input("Enter Number(3 ~ 9): ")  # 자리수를 입력받아, 사용이 가능한지 (정수인지, 3~9 범위에 있는지) 검증함.
    if not is_digit(inp):
        print("Wrong Input, Input again")
    else:
        if int(inp) > 9 or int(inp) < 3:
            print("Wrong Input, Input again")
        else:
            baseball_count = int(inp)
            break


def main():
    print("Play Baseball Game (enter 0 to exit)")
    user_input = 999
    arr = [0, 0]
    while True:
        find = 0
        random_number = str(get_not_duplicated_three_digit_number())  # 중복되지 않는 random number 출력
        print("random number: " + random_number)
        guess = 1
        print("guess random number!")
        while True:
            user_input = input("Guess #" + str(guess) + " : ")  # 0이 입력되거나 (바로 Game 끝)

            if str(user_input) == "0":
                print("Thank you for using this program")
                print("End of the Game")
                exit()

            if not is_validated_number(user_input):  # 세 가지 조건을 만족하지 않으면 False (함수에서 설명)
                print("Wrong Input, Input again")

            else:
                if guess >= 10:  # 10회 입력을 초과한 경우(다시 플레이하는지 질문) 게임 끝
                    chk = input('GAME OVER, one more(Y/N) ?')
                    if is_no(chk):
                        print("Thank you for using this program")
                        print("End of the Game")
                        exit()
                    if is_yes(chk):
                        find = 1
                        break
                else:
                    arr = get_strikes_or_ball(random_number, user_input)
                    if arr[0] == 0 and arr[1] == 0:
                        print('OUT!')
                    else:
                        print(str(arr[0]) + " S" + " / " + str(arr[1]) + " B")  # Strike, Ball 출력
                    guess += 1
                    if arr[0] >= int(baseball_count):
                        while True:
                            chk = input('You win, one more(Y/N) ?')  # Game에서 이긴 경우
                            if is_no(chk):  # No
                                print("Thank you for using this program")
                                print("End of the Game")
                                exit()
                            if is_yes(chk):  # Yes
                                find = 1
                                break
                            else:
                                print("Wrong Input, Input again")
                    if find == 1:
                        break


if __name__ == "__main__":
    main()
