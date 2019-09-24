import random
import sys


def making_number():
    a = list(range(10))
    random.shuffle(a)
    number = [a[0], a[1], a[2]]
    return number


'''
0~9까지의 배열을 섞어 앞의 세 개를 반환하는 함수이다. 정답을 지정하는 데 사용한다.
'''


def intro():
    print('안녕~! 난 숫자야구공주야♥\n나랑 숫자야구를 하고 싶어서 온 거지??><\n내가 할 숫자야구의 규칙은 다음과 같아!\n')
    print(
        '1. 넌 0~9의 서로 다른 숫자 3개를 10번 입력할 수 있어!\n'
        '2. 나는 만약 숫자가 맞지만 위치가 틀리면 볼, 숫자와 위치가 전부 맞으면 스트라이크, 숫자와 위치가 전부 틀리면 아웃이라고 알려줄 거야!\n'
        '3. 너는 10번 안으로 내가 정한 3개의 숫자를 위치까지 맞추면 돼!\n')
    print('입력은 서로 다른 숫자 3개를 띄어쓰기로 입력하면 돼!! 예시는 \'1 2 3\' 이야 알았지??? 똑똑한 너라면 이해할 수 있을 거야! 자 그럼 이제 시작!!\n')


'''
게임의 간단한 소개와 규칙을 설명하는 함수이다.
'''


def scan_number(count):
    print('\n%d번째 시도야!' % count)
    try:
        user = list(map(int, input().split()))
    except (TypeError, ValueError):
        print('입력 형식을 준수하지 않는 사람은 이 게임을 할 수 없어!')
        sys.exit()
    return user


'''
count 번째 사용자의 입력을 받아 list 형으로 반환하는 함수
'''


def check_number(num):
    if len(num) != 3:  # 숫자를 띄우지 않았거나, 숫자를 3개 입력하지 않은 경우
        print('\'3개\'를 \'띄워서\'입력하랬잖아!! 규칙을 준수하지 않는 넌 이 게임을 할 수 없어!')
        sys.exit()

    for i in range(0, 3, 1):  # 0~9까지의 수를 입력하지 않은 경우
        if num[i] not in list(range(0, 10)):
            print('입력 형식을 준수하지 않다니... 맙소사!! 넌 이 게임을 할 수 없어!')
            sys.exit()

    if num[0] == num[1] or num[0] == num[2] or num[1] == num[2]:  # 같은 숫자를 입력한 경우
        print('\'서로 다른\' 숫자랬지!! 말을 듣지 않는 넌 이 게임을 할 수 없어!')
        sys.exit()


'''
사용자의 답(num)이 서로 다른 숫자 3개로 이루어져 있는지 확인하는 함수이다.
만약 서로 다른 숫자 3개로 이루어져 있지 않다면, 게임을 종료한다.
'''


def check(ans, num):
    if ans == num:
        return '우와 정답이야!! 너 영재니??'
    s = 0
    b = 0
    o = 0
    for i in range(3):
        if num[i] == ans[i]:  # 스트라이크 갯수 체크
            s += 1
        elif num[i] in ans:  # 볼 갯수 체크
            b += 1
        else:  # 아웃 갯수 체크
            o += 1
    return str(s) + 'S ' + str(b) + 'B ' + str(o) + 'O'


'''
사용자의 값 num 과 정답 ans 의 스트라이크, 볼, 아웃 개수를 세는 함수이다.
만약 num 과 ans 가 일치한다면 정답이라고 쓰인 문자열을 반환한다.
일치하지 않는다면 스트라이크, 볼, 아웃 개수를 쓴 문자열을 반환한다.
'''


def ask_again():
    print('다시 할래?? 하고 싶으면 y, 싫으면 y로 시작하지 않는 말을 쳐줘~><')
    return input().lower().startswith('y')


'''
다시 게임을 할 건지 물어보는 함수이다.
y로 시작하는 단어를 입력했다면 True를 반환하고, 아니면 False를 반환한다.
'''

intro()
while True:
    count = 1  # 시도 횟수
    answer = making_number()  # 정답(answer) 설정
    while count <= 10:
        guess = scan_number(count)  # 추측한 정답(guess) 입력 받음
        check_number(guess)  # guess 가 양식에 맞는지 확인함
        print(check(answer, guess))  # guess 와 answer 의 관계 출력
        count += 1  # 시도 횟수 증가

        if answer == guess:
            break  # guess 와 answer 이 동일할 경우 멈춤
        if count > 10:  # 10번 안에 맞추지 못했을 경우 출력
            print('10번 안에 못 맞췄네! 내가 이겼지롱 메롱메롱 :p\n 정답은 %d %d %d였어!' % (answer[0], answer[1], answer[2]))
    if not ask_again():  # y로 시작하지 않는 문구를 쳐서 다시 하고 싶지 않다는 입력을 받았을 때 종료
        print('안녕 잘 있어ㅓ~~')
        break
