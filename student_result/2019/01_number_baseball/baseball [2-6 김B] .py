import random


def get_random():   # 조건을 충족하는 랜덤 수 생성, 랜덤 수를 리턴
    n = random.randrange(100, 999)
    while not checked(n):
        n = random.randrange(100, 999)
    return n


def is_in_range(input_number):  # 세 자리 수인지 확인, input 데이터를 받아 T/F 리턴
    input_number = int(input_number)
    if input_number >= 100 and input_number < 1000: # 세자리 수이면 승인
        ok = True
    else:
        ok = False
    return ok


def is_not_same(nums):  # 중복된 숫자는 없는지 확인, input 데이터를 받아 T/F 리턴
    nums = str(nums)
    l = len(set(nums))
    if l == 3:  # 중복된 숫자가 하나도 없이 숫자 3개로 이루어져 있으면 승인
        ok = True
    else:
        ok = False
    return ok


def checked(input_number):  # 모든 조건들을 충족하는지 최종 확인, input 데이터를 받아 T/F 리턴
    # if is_in_range(input_number) == True and is_not_same(input_number) == True:
    if is_in_range(input_number) and is_not_same(input_number):
        ok = True
    else:
        ok = False
    return ok


def set_answer():   # 정답 정수 생성
    random_number = get_random()
    while not checked(random_number):   # 정답 정수가 조건에 맞지 않을 경우 재생성
        random_number = get_random()
    result = random_number
    return result


def strike_ball(input_number, answer):  # input 데이터와 정답을 인수로 받아 비교하여 S/B/O 판단 및 T/F 리턴
    a = list(map(int,list(str(input_number))))  # input 데이터의 세 자리 숫자를 리스트로 변환
    b = list(map(int,list(str(answer))))    # 정답 정수의 세 자리 숫자를 리스트로 변환
    strike = 0
    ball = 0
    for i in range(0, 3):
        for j in range(0, 3):
            if a[i] == b[j]:
                if i == j:
                    strike = strike + 1
                else:
                    ball = ball + 1
    out = 3 - strike - ball
    result = [strike, ball, out]
    return result


def onemore_yes(input_onemore):   # 문자열을 받아 한 번 더 할 것을 동의하는 경우(Y 또는 Yes) True 리턴, 아니면 False 리턴
    input_onemore = input_onemore.upper()
    if input_onemore == "Y" or input_onemore == "YES":
        result = True
    else:
        result = False
    return result


def onemore_no(input_onemore):  # 문자열을 받아 한 번 더 할 것을 거절하는 경우(N 또는 No) True 리턴, 아니면 False 리턴
    input_onemore = input_onemore.upper()
    if input_onemore == "N" or input_onemore == "NO":
        result = True
    else:
        result = False
    return result


def onemore():  # 한 번 더 할 것을 제안, 답을 받아 onemore_yes, onmore_no 함수에 input 데이터를 보내 재시작 여부(True/False) 확인 및 리턴
    s = input("한 번 더? Y/N >>> ")
    if onemore_yes(s):
        ok = True
    elif onemore_no(s):
        ok = False
    else:
        print("왜 다르게 입력해요? 흥")
        ok = False
    return ok


def scan_and_is_int(): #input 데이터가 정수인지 확인(True/False) 및 리턴
    while True:
        try:
            input_number = int(input("Guess #%d >>> " % i))
        except:
            print("잘못 입력했잖아요!")
        else:
            return input_number


print("숫자 야구 게임!"
      "저는 지금 중복되지 않은 숫자로 이루어진 세 자리 숫자를 생각하고 있어요. 무슨 수일지 맞춰보세요!\n"
      "답을 제시할 때마다 정답이 아닐 경우 Strike / Ball / Out으로 힌트를 제공한답니다!\n"
      "Strike의 수만큼 숫자와 위치가 일치하는 숫자가 있다는 뜻이에요!\n"
      "Ball의 수만큼 숫자는 맞지만 위치가 틀린 숫자가 있다는 뜻이에요!\n"
      "Out의 수만큼 숫자와 위치가 전부 틀린 숫자가 있다는 뜻이에요!\n"
      "자, 그럼 시작해볼까요?\n")
ok = 1  # ok=1일 경우 계속 게임 진행
while ok:   # 게임하는 동안
    win = 0
    answer = get_random()
    for i in range(1, 11):
        input_number = scan_and_is_int()
        while not checked(input_number):   # input이 조건을 성립하는지 확인
            print("잘못 입력했잖아요!") # 조건에 맞지 않으면 출력
            input_number = scan_and_is_int()    # 다시 input
        a = strike_ball(input_number, answer)
        if a[0] == 3:
            print("축하해요! 당신이 이겼어요!!\n")
            win=1
            break
        print(a[0], "/", a[1], "/", a[2])
    if win == 0:    # 10번 시도했는데 3 스트라이크가 나오지 않은 경우
        print("당신이 졌어요! 뭬-롱\n정답:",answer)
    if not onemore():
        break
