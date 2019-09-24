import random
import sys

num = []


def num_gen():
    numbers = list(range(10))  # range() 함수의 반환형은 iterator 형식의 객체 / list() 를 이용하여 list 형으로 변경
    random.shuffle(numbers)
    # num = [numbers[0], numbers[1], numbers[2]]  # 섞인 리스트의 앞 세 숫자로 게임에 사용할 숫자를 만듬

    # return num  # 그 리스트 반환
    return numbers[0:3]  # 섞인 리스트의 앞 세 숫자로 게임에 사용할 숫자를 만듬


def check(list):
    strike = 0
    ball = 0
    out = 0

    for i in range(3):
        if list[i] in num:  # list 속 원소가 num안에 있는 경우
            if list[i] == num[i]:
                strike = strike + 1  # 같은 위치에서 값이 같을 경우 스트라이크 1 증가
            else:
                ball = ball + 1  # 같기만 하니까 볼 1 증가
        else:
            out = out + 1  # 없으면 아웃

    result = [strike, ball, out]  # 리스트로 반환할거임
    return result


def starter(again):  # 게임을 실행 여부 묻는 함수, again 은 처음하는 건지 아니면 다시하는 건지에 대해 알려주는 변수
    while 1:
        if again == 1:  # 다시하는 거임
            start = input("게임을 다시 하시겠습니까? Yes/No")
        else:  # 처음하는 거임
            start = input("게임은 시작하시겠습니까? Yes/No")

        # if start == 'Yes' or start == 'yes' or start == 'YES':  # 다양한 방법의 yes 입력
        if start in "Yes yes YES".split():  # 다양한 방법의 yes 입력
            print("게임을 시작합니다")
            return 1

        # elif start == 'No' or start == 'no' or start == 'NO':  # 다양한 no 입력, no 입력시 프로그램 종료
        elif start in "No no NO".split():  # 다양한 no 입력, no 입력시 프로그램 종료
            print("게임을 종료합니다")
            sys.exit('게임종료')
            # T. sys.exit() 의 경우 문자열을 넣는 것이 아니라 종료 상태 Code 를 넣도록 되어 있습니다.
            # T. 이렇게 하면 에러나요.
            # T. os._exit(args[0])
            # T. TypeError: an integer is required (got type str)

        else:
            print("다시 입력하세요")  # 잘못 입력한 경우


def get_num():  # 사람이 추측한 숫자를 입력받는 함수
    # while 1:
    while True:
        print("3자리 수를 띄어쓰기 없이 입력하세요!")
        guess = input()
        try:  # 정수로 한번 변환 해 보고 안되면
            int(guess)
        except:  # 다시 하라고 한다
            print("제대로 다시 숫자로 입력하시오")
            continue

        guess = [int(i) for i in guess]

        flag = 0

        for i in range(3):  # 반복문을 돌면서 중복된 숫자가 없는지 확인한다
            for j in range(3):
                if j != i and guess[i] == guess[j]:
                    flag = 1  # 있으면 flag 갱신
                    break

        if flag:
            print("숫자를 중복해서 입력하지 마세용")  # 중복하지 말라고 전달한다
            continue

        if len(guess) != 3:  # 3글자가 아니면 다시 입력하라고 한다
            print("3자리 숫자를 입력하세요")
        else:
            return guess  # 조건문 잘 통과하면 guess를 리스트로 만들어서 반환


again = 0   # 다시 하는건지 확인하는 숫자
cnt = 10    # 남은 기회 수
x = 1       # 새로 시작하는 여부
a = 0       # 게임 진행 여부
num = 0     # 랜덤숫자

# while 1:
while True:
    if cnt == 0:  # cnt 가 0이면 패배로 간주한다
        ans = 100 * num[0] + 10 * num[1] + num[2]
        print("이런 맞추기에 실패하셨네용~~ 정답은 ", ans, "였습니다~")
        again = 1  # again 과 x를 1로 바꾸어서 다시 하는 경우로 바꾸고, 새로 진행할 수 있도록 한다
        x = 1
        cnt = 10
        # print("------------------------------------------")
        print("-" * 40)

    if x == 1:  # 새로 진행한다는 뜻
        a = starter(again)  # 다시 할건지 물어본다
        x = 0  # 이제 다시 새로 할 필요 없다

    if a:  # 게임을 시작한다는 조건
        if cnt == 10:  # 기회가 10번 남은 건 새로 시작했다는 뜻 이므로 숫자를 새로 생성함
            num = num_gen()
        print(cnt, "번의 기회가 남았습니다")
        guess = get_num()  # 플레이어의 추측하는 숫자를 입력받는다
        checklist = check(guess)  # 스트라이크 볼 아웃 판정한다

    # T. 위의 if 문이 반드시 실행되야 여기까지 내려오겠지만..
    # T. if a: 문이 반드시 실행되야 선언되는 변수를 이렇게 사용하는 것은 권장하지 않음.
    if checklist[0] == 3:  # 삼진이면 게임 종료
        print("----------------------------------------------")
        print("3 스트라이크! 정답을 맞추셨습니다!", 10 - cnt + 1, '번 만에 맞추셨네요!')
        cnt = 10
        again = 1
        x = 1
        print("----------------------------------------------")
        continue
    else:  # 오답시 결과 출력하고 다음 기회를 준다.
        print('strike :', checklist[0], 'ball :', checklist[1], 'out :', checklist[2])
        cnt = cnt - 1
        print(cnt, "번 남으셨습니다")
        print("----------------------------------------------")
