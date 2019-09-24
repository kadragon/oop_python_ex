"""
함수 rules: 규칙 설명하는 함수
함수 creating_answer: 정답을 정하는 함수, 첫자리가 0이면 정답 다시 만듦
함수 count: 틀린 횟수와 남은 기회를 알려주는 함수
함수 int_test: 입력한 값이 조건을 만족하는지를 확인하는 함수
함수 ans_test: 사용자가 입력한 값과 컴퓨터가 정한 답이 얼마나 일치하는지 확인하는 (S,B,O를 판정하는) 함수
"""
import random  # random 함수 불러오기


def rules():
    print(
        "\n규칙\n1. 세 자리 자연수를 입력하세요\n"
        "2. 숫자와 위치 모두 맞으면 1Strike 입니다\n"
        "3. 숫자만 맞으면 1Ball 입니다\n"
        "4. 숫자와 위치 모두 틀리면 1Out 입니다\n"
        "5. 세 자리 자연수가 아닌 수 또는 문자를 입력하면 처음에는 넘어가지만 그 다음부터는 기회가 줄어듭니다\n"
        "6. 틀리면 기회가 줄어듭니다")


def creating_answer():
    numbers = list(range(10))  # numbers = [0,1,2,3,4,5,6,7,8,9] 만듦
    random.shuffle(numbers)  # numbers 의 수 순서를 바꿈"""
    answer = ''  # 정답(answer) 변수 선언

    for i in range(3):
        answer += str(numbers[i])  # answer 가 바뀐 numbers 의 앞 세 수

    while answer[0] == '0':  # answer 첫 수가 0이면 다시 answer 만듦
        answer = ''  # answer 를 초기값 공백으로 지정
        random.shuffle(numbers)  # numbers 의 수를 다시 섞음

        for i in range(3):
            answer += str(numbers[i])  # answer 다시 지정

    return answer  # answer 값 반환


def count():
    print('%s번 잘못 입력했고, 남은 기회는 %s번입니다' % (c, life))  # c번 잘못 입력했고, 남은 기회는 life 번입니다 (c와 life 는 변수)


def int_test(num):
    if num == 'rules':  # num 이 rules 이면 rules 함수를 실행하고 True 반환
        rules()
        return True
    elif num == 'count':  # num 이 count 이면 rules 함수를 실행하고 True 반환
        count()
        return True
    elif len(num) != 3:  # num 의 자릿수가 3이 아니면 False 반환
        return False
    else:
        try:  # 일단 실행: 아래에서 int(i)가 존재하지 않는 경우 에러 처리하기 위해서
            for i in num:
                if int(i) not in range(10):  # int(i)가 0~9에 없는 경우 False 반환
                    return False
        except Exception:  # 에러가 나오는 경우(=int(i)가 존재하지 않을 때: i가 문자일 때) False 반환
            return False
    return True


def ans_test(user_guess, com_ans):
    s = 0  # strike 수 =0
    b = 0  # ball 수 =0
    o = 0  # out 수 =0

    for i in range(3):
        if user_guess[i] == com_ans[i]:
            s += 1  # user_guess 의 i+1번째 수=com_ans 의 i+1번째 수면 strike 하나 늘림
        elif com_ans.find(user_guess[i]) != -1:
            b += 1  # user_guess 의 i+1번째 수가 com_ans 에 있으면 ball 하나 늘림(strike 인 경우 제외)
        else:
            o += 1  # 그 외에는 out 하나 늘림

    print('%sS | %sB | %sO' % (s, b, o))  # sS | bB | oO 출력(s,b,o)변수


def again():
    print('게임을 다시 하시겠습니까? 다시 하려면 yes를 입력하세요')  # ~출력
    a = input()  # 입력받음

    if a == 'yes':
        return True  # 입력값이 yes 면 True 반환
    else:
        return False  # 나머지면 False 반환


life = ''  # life 변수 선언
c = ''  # c 변수 선언
answer = ''  # answer 변수 선언

print("\n게임을 시작합니다")  # 출력

rules()  # 규칙 출력: 규칙 함수 사용

print("\n규칙을 확인하려면 rules 를 입력하세요")  # 출력
print("틀린 횟수와 남은 기회를 확인하려면 count 를 입력하세요")  # 출력

while True:
    life = 10  # life = 10으로 지정(다시 시작할 때 life 초기화)
    c = 0  # c=0으로 지정(다시 시작할 때 c 초기화)
    answer = creating_answer()  # answer 제작(함수 사용)

    print('\n수를 정했습니다. 맞춰보세요!\n')  # 출력
    guess = ' '  # guess 변수 선언

    while life > 0:  # life 가 0보다 클 때
        guess = input()  # guess 입력
        while int_test(guess) is False and life > 0:  # 올바르지 않은 수 또는 문자를 입력했을 때, 이 while 문을 돌 때 life 확인을 위해 life>0 필요
            print('세 자리 자연수를 입력하세요')  # 출력
            if c >= 1:  # 잘못 입력한 횟수가 한번보다 많으면 life 차감
                life -= 1
            c += 1  # 잘못 입력한 횟수 하나 추가(이 경우는 틀린 경우니까 추가)
            if life == 0:  # life 가 0이되면 이 while 문에서 나감
                break
            else:
                guess = input()  # life 가 0이 아니면 새로운 guess 값을 입력받음

        try:
            if guess != 'count' and guess != 'rules':  # guess 가 count 또는 rules 가 아니고
                if int_test(guess):  # guess 가 세 자리 정수 일 때 life 차감(정답이 아닌 것을 입력했을 때 life 차감)
                    life -= 1
                if guess == answer:
                    print('축하합니다! 정답입니다')  # 출력
                    break  # 이 while 문 나감
                else:
                    ans_test(guess, answer)  # 답이 아닌 경우 S,B,O 판정
        except Exception:  # 공백 또는 enter 를 입력받았을 때 생길 수 있는 에러 해결
            continue

    print('기회가 없습니다. 정답은 %s였습니다' % answer)  # life가 0일 때 출력
    if not again():
        print('게임을 종료합니다')  # 다시 시작하지 않는다고 할 때(yes 입력하지 않은 경우) 게임을 종료합니다 출력
        break  # 출력한 후 종료
