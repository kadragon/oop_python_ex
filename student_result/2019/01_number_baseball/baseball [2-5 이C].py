import random


def make_number():
    """
    랜덤 숫자 3개를 만드는 함수. 0~9를 나열한 리스트에서 임의로 3개를 샘플링한다.
    :return: 문자열 secret_number
    """
    number = list(range(10))
    random.shuffle(number)
    secret_number = ''
    for i in range(3):
        secret_number += str(number[i])

    return secret_number


def number_test(num):
    """
    입력받은 숫자가 범위 안에 있는지 판단하는 함수이다.
    :return: True or False
    """
    if len(num) != 3:  # 숫자의 길이는 3개로 제한함.
        return False

    try:
        for i in num:
            if int(i) not in list(range(0, 10)):
                return False
    except ValueError:  # 입력받은 값이 숫자가 아니어서 오류가 뜬다면 예외로 처리하고 false 로 리턴한다.
        return False

    for i in range(3):
        for j in range(3):
            if i != j and num[i] == num[j]:
                return False  # 만약 중복되는 숫자를 입력받았다면 다시 입력해야 한다.

    return True  # 모든 조건을 만족하면 True 로 리턴.


def game(answer_num, predict_num):
    """
    :param answer_num: 실제 정답인 숫자
    :param predict_num: 사용자가 예측한 숫자
    :return: 스트라이크, 볼, 아웃이 각각 몇개인지
    """

    ans_s = 0
    ans_b = 0
    ans_o = 0

    for i in range(len(predict_num)):

        if predict_num[i] == answer_num[i]:  # 스트라이크 개수
            ans_s += 1
        elif predict_num[i] in answer_num:  # 볼 개수
            ans_b += 1
        else:  # 아웃 개수
            ans_o += 1

    return 'Strike : ' + str(ans_s) + '   Ball : ' + str(ans_b) + '   Out : ' + str(ans_o)


while True:
    print('숫자야구 게임입니다~')
    answer = make_number()
    cnt = 1
    while cnt <= 10:

        print('-' * 50)
        print('10번 안에 성공해야 해! --> 현재 시도횟수 : %d' % cnt)
        print('서로 다른 숫자 3개를 입력해봐!')
        predict = input()  # 문자열로 저장.

        if answer == predict:
            print('♥♥♥♥♥정답♥♥♥♥♥')
            break

        if number_test(predict):
            print(game(answer, predict))
            cnt = cnt + 1
            if cnt == 11:
                print('10번 틀렸어! 정답은 %s야.' % answer)
        else:
            print('숫자를 다시 입력해!')

    print('-' * 50)
    print('게임 다시 할거야? (tell yes or no)')
    tell_answer = input()
    if tell_answer == 'no':
        break
