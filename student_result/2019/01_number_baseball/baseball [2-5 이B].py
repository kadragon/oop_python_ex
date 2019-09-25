import random


# 랜덤 숫자 형성을 위해서

def make_answer(leng):
    ans_1 = ''
    """
    leng 길이만큼의 문자열 반환, 임의의 숫자로 되어있다
    return:임의의 문자열
    """
    list_0 = list(range(10))  # 리스트 [0, 1, 2, 3, 4, 5, 6, 7, 8, 9] 생성
    random.shuffle(list_0)  # 리스트를 무작위로 섞는다
    for i in range(3):
        ans_1 += str(list_0[i])  # 정답 생성
    return ans_1


def SBO(guess_1, answer_1):
    """
    목적:사용자가 입력한 값의 S, B, O 값을 알려준다
    guess_1:사용자가 입력한 수
    answer_1:랜덤으로 생성된 정답
    return:S, B, O의 값을 정리한 문자열
    """
    if guess_1 == answer_1:  # 답이 맞을 시에 승리
        return "You've got it!"
    s = 0  # S값의 변수
    b = 0  # B값의 변수
    o = 0  # O값의 변수
    for i in range(3):  # S의 개수를 센다
        if guess_1[i] == answer_1[i]:
            s += 1
    for j in guess_1:  # B의 개수를 센다
        for k in answer_1:
            if j == k:
                b += 1
    b -= s
    o = 3 - b - s  # O의 개수를 센다
    return str(s) + 'S ' + str(b) + 'B ' + str(o) + 'O\n'


def test(num):
    """
    목적:사용자가 입력한 값이 세자리 숫자인지 판별한다
    num:사용자가 입력한 문자
    return:True면 세자리 숫자 False면 다른 형식의 문자열
    """
    if num == ' ':
        return False

    for i in num:
        if int(i) not in list(range(0, 10)):  # 각 자리의 수가 0~9인지 확인
            return False
    return True


print('=' * 15)
# 게임 시작
while True:
    ans = make_answer(3)  # 세자리 숫자로 이루어진 임의의 문자열 생성
    print("I made a answer, try to guess")
    tri = 1  # tri:시도횟수
    while tri <= 10:
        guess = ' '
        while len(guess) != 3 or not test(guess):  # 사용자가 입력한 값이 세자리 숫자일때까지 반복해서 입력받음
            if len(guess) != 3 and guess != ' ':
                print('your answer is uncorrect format, type like "123"')
            print('Guess #%s:' % tri, end='')
            guess = input()

        print(SBO(guess, ans))  # S, B, O값 출력
        tri += 1

        if guess == ans:  # 답을 입력할 시 게임 종료
            break

        if tri > 10:  # 시도가 10번 초과했을 때 게임 종료
            print("You are wrong, The answer is %s" % ans)
    print("Retry?")
    print("Type yes or no")
    if not input().lower().startswith('y'):  # 게임을 계속할지 결정
        break
