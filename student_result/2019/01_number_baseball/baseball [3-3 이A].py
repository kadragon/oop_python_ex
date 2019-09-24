import random


# shuffle  # 임의의 숫자 생성하기
def shuffle():
    num = list(range(10))
    random.shuffle(num)
    return num  # 0~9까지 순서를 랜덤하게 섞은 리스트 리턴


# numinput  # 숫자 제대로 입력되었는지 확인하기
def numinput(a):
    k = 0
    # 정수가 입력되었는지 확인
    for i in a:
        if i not in list(map(str, range(10))):
            return False  # 정수가 아닌 값이 입력되었을 때 false 리턴
        k += 1

    return k == 3  # 3자리 정수일 때 true 리턴


# numoutput  # 숫자 판단하고 결과 출력
def numoutput(a, num):
    if numinput(a):  # 입력된 값이 적절하면 실행
        alist = [int(i) for i in a]  # 3자리 정수를 각각 쪼개기

        strike = 0
        ball = 0
        out = 0

        for i in range(3):
            if alist[i] == num[i]:
                strike += 1  # 자리와 수가 일치하면 스트라이크
            elif alist[i] in num:
                ball += 1  # 수만 일치하면 볼
            else:
                out += 1  # 자리도 수도 일치하지 않으면 아웃

        if strike == 3:
            print("정답입니당~~\n")
            return 1  # 정답 맞추면 1 리턴
        else:
            print("%dSTRIKE_ %dBALL_ %dOUT\n\n" % (strike, ball, out))
            return 0  # 정답 아니면 0 리턴

    print("입력오류!ㅠㅠ\n")  # 입력된 값이 적절하지 않으면 0 리턴
    return 0


# gamestart  # 게임 진행 함수
def gamestart():
    s = 0

    # 게임 정답 생성
    num = shuffle()

    # 10번 목숨 카운트
    for i in range(10):
        for j in range(10 - i):
            print("♥", end="")
        for j in range(i):
            print("♡", end="")
        print("")
        print("%d번째 도전! 정답은? " % (i + 1))

        a = input()
        s = numoutput(a, num[0:3])
        if s == 1:
            break  # 정답일때 게임 종료

    if s == 0:
        print("ㅠㅠㅠㅠㅠㅠㅠㅠㅠㅠㅠㅠ실패했어요ㅠㅠ분발하세요ㅠㅠㅠㅠㅠㅠㅠㅠㅠㅠ\n")


# gameend  # 게임 종료 함수
def gameend():
    print("게임을 이어하고 싶다면 Y를 입력해주세요. 공백 혹은 다른 값을 입력하면 종료됩니다.\n")
    a = input()
    if a == 'Y':
        return False  # 게임을 이어하고 싶다면 false 리턴
    return True  # 게임을 그만하고 싶다면 True 리턴


# 게임 시작
print("   " * 8 + "💥💥💥💥💥숫자야구게임💥💥💥💥💥\n\n")
print("=====" * 15)
print(
    "💡0~9사이의 서로 다른 세 숫자를 순서를 고려하여 !공백없이! 입력하세요\n\n"


    "💡STRIKE : 숫자 일치, 자리 일치\n"
    "💡BALL : 숫자 일치, 자리 불일치\n"
    "💡OUT : 숫자 불일치, 자리 불일치\n\n"

    "💡Example\n정답 : 123\n입력값 : 138\n출력값 : 1STRIKE_1BALL_1OUT\n\n"
    "💡기회는 단 10번!! GOOD LUCK🕱 -hyewon- \n"
)
print("=====" * 15)

while 1:
    gamestart()

    if gameend():
        break  # 게임을 그만하고 싶다면 전체 종료 아니라면 계속 반복
