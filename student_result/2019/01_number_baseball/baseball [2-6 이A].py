import random

def isnum(k): # 각 자리수가 0 ~ 9 사이 숫자인지 확인하는 함수
    if 48 <= ord(k) <= 57:
        return 1
    else:
        return 0

def right(t): # 사용자가 입력한 문자열이 입력 조건에 부합하는지 확인하는 함수
    if len(t) != 3: # 세 글자가 아니면 부합하지 않음
        return 0
    else:
        if t[0] == t[1] or t[1] == t[2] or t[2] == t[0]: # 세 글자 중 어느 두 글자가 같다면 부합하지 않음
            return 0
        else:
            if isnum(t[0]) and isnum(t[1]) and isnum(t[2]): # 세 글자 모두 0 ~ 9 사이 숫자일때만 부합함.
                return 1
            else:
                return 0

def scan(i): # 사용자가 입력한 문자열을 받아 입력 조건에 부합하는지 판단하는 함수
    print('-' * 20)
    t = input('take %d: ' % i) # 몇 번째 입력 시도인지 출력
    if (right(t)): # 입력 조건에 부합하는 문자열이라면 gamestart함수로 리턴
        return t
    else:
        print('잘못된 입력입니다. 다시 입력하세요.') # 잘못된 입력이라면 횟수 차감 없이 재시도
        return scan(i)

def gamestart(): # 게임을 진행하는 함수
    num = [] # (line 31 ~ 42) 컴퓨터가 생각한 세자리 수 abc 를 num에 [a, b, c]형태로 저장 (a, b, c : int)
    print('게임을 시작합니다.')
    a1 = random.randrange(0, 10)
    num.append(a1)
    a2 = a1
    while a1 == a2:
        a2 = random.randrange(0, 10)
    num.append(a2)
    a3 = a1
    while a1 == a3 or a2 == a3:
        a3 = random.randrange(0, 10)
    num.append(a3)

    print('규칙에 맞는 세 자리 수를 입력하세요. 10번의 기회가 주어집니다.')
    for i in range(1, 11): # 시도 횟수를 10번으로 제한
        num2 = [] # (line 46 ~ 49) 사용자가 입력한 수 abc를 num2에 [a, b, c]형태로 저장 (a, b, c : int)
        k = scan(i)
        for i2 in range(3):
            num2.append(int(k[i2]))

        if num == num2: # 정답을 맞췄다면 정답 메시지 출력 후 게임 종료
            print("정답! %d번 만에 맞추셨습니다." % i)
            break;

        s = b = o = 0 # (line 55 ~ 63) 정답이 아니라면 strike, ball, out 의 수 출력
        for i2 in range(3):
            if num[i2] == num2[i2]:
                s += 1
            for i3 in range(3):
                if num[i3] != num2[i3] and num[i3] == num2[i2]:
                    b += 1
        o = 3 - s - b
        print("%d S  %d B  %d O" % (s, b, o))

        if i == 10: # 10번의 기회를 모두 차감했다면 실패 메시지 출력 후 게임 종료
            print("실패!")

def question1(): # 가장 처음 실행되어 게임 시작/종료를 결정하는 함수
    st = input()
    if st == 'y':
        gamestart()
        print("다시 시작하시겠습니까? (y/n)") # 한 번의 게임이 끝났다면 다시 시작할 것인지 사용자에게 확인
        question1()
    elif st == 'n':
        print('게임 종료')
    else :
        print('y/n으로 입력하세요')
        question1()

print('게임 시작 (y/n)') # y:시작, n:종료
question1()