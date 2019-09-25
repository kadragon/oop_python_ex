import random


def correct_number(length):  # 무작위 답을 생성하는 함수
    correct_number = ''
    Num = list(range(10))  # 0부터 9까지의 수를 리스트로 불러온다
    random.shuffle(Num)  # 무작위로 섞어준다
    for i in range(length):
        correct_number += str(Num[i])  # 원하는 자릿수에 맞을때까지 답 배열에 하나씩 숫자를 추가한다
    return correct_number


def number_appropriate(number):  # 사용자가 입력한 것이 빈것을 넣지 않았는지 또는 문자를 넣지 않았는지 판단하는 함수
    for i in number:
        if '0' > i or i > '9':  # 문자인지 판단
            return 0
    if number == ' ':  # 빈칸인지 판단
        return 0
    return 1


def SO(users, correct_number):  # strike와 ball에 관한 힌트를 준다
    a = 0
    b = 0
    for j in [0, 1, 2]:  # 3자리수 이므로 0, 1,2 까지
        if users[j] == correct_number[j]:  # 같은 자리에 같은 숫자면 카운트
            a += 1
        elif users[j] in correct_number:  # 같은 자리는 아니지만 같은 숫자가 존재하면 카운트
            b += 1
    return str(a) + 'S/ ' + str(b) + 'B/ '  # 문자열로 리턴


def O(users, correct_number):  # 아웃을 카운트
    c = 0
    for j in [0, 1, 2]:
        if users[j] not in correct_number:  # 아예존재하지 않을 경우 카운트
            c += 1
    return str(c) + 'O'


L = 3
flag = 0
while 1:
    correct = correct_number(L)  # 답 생성 후 저장
    print('You need to guess a number or you will die.')
    print('you have 10 life to guess try hard hahaha')
    # print('XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX')
    print('X * 50')
    sum = 0  # sum을 0으로 초기화
    while sum <= 10:
        users = ''
        while len(users) != L or number_appropriate(users) == 0:  # 사용자의 입력이 더 진행할 수 있는지 적합성을 판단
            print('What is your guess? Becareful it owes you a life!')
            print((10 - sum), 'remaining life')
            users = input()  # 입력값 받기
        print(SO(users, correct), O(users, correct))  # 힌트 보여주기
        sum += 1
        if users == correct:
            print('you finally saved your life!')
            break
        if sum == 10:
            print('you died.....^^')
            print(correct)
            break
    print('do you want a replay/ yes or no')  # 다시 게임을 진행할지에 대한 여부를 판정
    ans = input()
    if ans == 'no':
        break
