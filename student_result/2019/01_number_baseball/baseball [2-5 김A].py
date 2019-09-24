# 숫자야구

import random


def make_num():
    answer = []
    num = list(range(10))  # 0~9의 숫자를 리스트로 만든다
    random.shuffle(num)  # 리스트를 랜덤으로 섞는다
    for i in range(3):
        answer.append(num[i])  # answer 이라는 리스트에 랜덤으로 섞은 0~9를 세개만 넣는다.
    return answer  # 만든 answer 리스트를 리턴


def scanf():
    print("입력해봐 : ", end='')
    mine = input()
    list = []
    try:
        for ch in mine:
            list.append(int(ch))
        if len(list) != 3:  # 입력받은 값이 숫자 3자리가 아닐 때 다시 입력 받게함
            print("다시 입력하시오!!")
            return scanf()
    # T. 예외처리를 할때에는 명확하게 어떠한 예외를 처리 할지 명기 해야 한다.
    except:  # 입력받은 값은 숫자가 아닐때 다시 입력받게 함
        print("다시 입력하시오!!")
        return scanf()
    return list  # 숫자 3개가 들어있는 리스트를 리턴


def check(my_list):
    # T. python 에서 모든 문자가 대문자인 변수는 '상수' 로 인식한다.
    S = 0
    B = 0
    O = 0
    if my_list == answer:  # 내가 입력한 리스트와 정답 리스트가 같을 시 1을 리턴하고 함수 종료
        print("지렸어요. 정답입니다!! 기분 쨰지죠?")
        return 1

    for i in range(3):  # 내가 입력한 리스트와 정답 리스트를 비교하며 채점
        if my_list[i] is answer[i]:
            S += 1
        elif my_list[i] is answer[0]:
            if i != 0:
                B += 1
        elif my_list[i] is answer[1]:
            if i != 1:
                B += 1
        elif my_list[i] is answer[2]:
            if i != 2:
                B += 1
        else:
            O += 1

    print("S %d" % S)  # 채점 결과 출력
    print("B %d" % B)
    print("O %d" % O)

    return 0  # 답이 아닐 시 0을 리턴하며 함수 종료


print("지금부터 숫자야구 게임을 시작합니다. 10번의 시도 안에,세자릿수의 숫자를 맞추어주세요!!")
print("규칙은 다음과 같습니다.")
print("서로 다른 세자리 수로 이루어진 세자리 자연수가 랜덤으로 설정된다.")
print("세자리 자연수를 띄어쓰기 없이 연속해서 입력하여 맞춘다..")
print("S : 숫자의 위치와 종류까지 맞춘 자릿수의 수.")
print("B : 숫자의 위치는 다르나, 종류를 맞춘 자릿수의 수.")
print("O : 숫자의 위치와 종류 모두 다른 자릿수의 수.")
print("이제 시작해주세요 ^0^")
print("=" * 50)

p = 1
return_o = 0

while p:
    answer = make_num()  # 정답 랜덤으로 생성
    try_n = 1

    while try_n <= 10:  # 시도 횟수가 10번 이하일 때만 실행
        my_list = scanf()  # 도전자에게 입력 받음
        correct = check(my_list)  # 채점함수의 리턴값을 변수로 받음
        if correct == 1:  # 정답이 맞다면 while 문 종료
            break
        if try_n != 10:  # 현재 시도 횟수 알려줌
            print("현재 시도 횟수는 %d 회입니다 !! 화이팅" % try_n)
        try_n += 1

    if try_n > 10:
        print("시도 가능한 기회를 모두 소진해버렸어요 ㅠㅠ 바보")

    print("한 번 더 시도해 볼래? (y/n)")

    # while 1:
    while True:
        return_o = input()  # 다시 게임할지 안할지 입력받음

        if return_o == 'n':  # 안한다고 한다면 while문 종료 후 프로그램 종료
            p = 0
            break

        if return_o == 'y':  # 한다고 한다면 다시 실행
            break

        print('y 또는 n으로 대답하렴 ^^')  # y 또는 n으로 대답하지 않았다면 다시 입력하게 함
