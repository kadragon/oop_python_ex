import random


# 변수 or 함수를 선언할때에는 var_length OR varLength 와 같은 형태로 선언
def isNumber(a):  # 숫자니?
    if a in "0 1 2 3 4 5 6 7 8 9".split():
        return True
    return False


def makeAnswer():  # 답 만들기
    a = [0, 0, 0]
    for i in range(3):
        flag = True
        while flag:
            flag = False
            a[i] = random.randint(0, 9)  # 랜덤으로 잡아서
            for j in range(i):
                if a[i] == a[j]:  # 아까 나온 수면 다시
                    flag = True

    return a  # 리스트로 반환


def getAnswer():  # 답 입력받기
    while True:
        ans = input('Guess your number! ')  # 문자열로 받아서
        ret = []
        for i in ans:
            if isNumber(i):  # 그 중에 숫자인 것만
                ret.append(int(i))  # 리스트에 삽입하고
        if len(ret) == 3:
            return ret  # 반환
        else:
            print('Enter your number again with 3 numbers!')


play_again = True  # 다시 할래?

while play_again:  # 다시 하겠다고 하면 계속
    print()
    print('------------------------------------')
    print()
    print("Welcome to the Number Matching Game!")

    answer = makeAnswer()  # 답 만들고
    flag = False
    for i in range(10):
        key = getAnswer()  # 답 입력받고
        s, b = 0, 0

        for j in range(3):
            for k in range(3):
                if answer[j] == key[k]:  # 모든 자리수를 비교하면서 같으면
                    if k == j:  # 같은 자리에서 같으면 스트라이크
                        s += 1
                    else:  # 다른 자리에서 같으면 볼
                        b += 1

        if s < 3:  # 3 스트라이크가 아니면
            print("Trial %d: S %d / B %d / O %d" % (i + 1, s, b, 3 - s - b))
        else:  # 답을 맞췄으면
            flag = True  # 맞췄다고 표시하고
            break  # 탈출

    print("The answer was %d%d%d!" % (answer[0], answer[1], answer[2]))  # 짜잔! 답은 이거였어!
    print("%s" % "You got the right answer in %d time(s)!" % (i + 1) if flag else "You got the wrong answer!")
    again = input("Wanna play again? (Yes, No) ")  # 다시 할래?
    play_again = True if again[0] == 'Y' or again[0] == 'y' else False
