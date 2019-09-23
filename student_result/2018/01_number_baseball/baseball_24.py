import random


# 변수를 선언할때에는 var_length OR varLength 와 같은 형태로 선언
def makenumber():
    L = list(range(10))
    random.shuffle(L)
    return L[0] * 100 + L[1] * 10 + L[2]


def checkballcount(guessa, guessb, guessc):
    strk = 0
    ball = 0
    a, b, c = x // 100, (x % 100) // 10, x % 10

    guess_list = [guessa, guessb, guessc]
    in_list = [a, b, c]

    for i in range(3):
        if in_list[i] == guess_list[i]:
            strk += 1
        elif in_list[i] in guess_list:
            ball += 1

    return strk * 10 + ball


def printresult(p, trytime):
    if p == 30:
        print("you right!\nyou tried %d times!\n" % trytime)
        return False
    elif p == 0:
        print("%d try: OUT!\n" % trytime)
        return True
    else:
        strikes = p // 10
        balls = p % 10
        print("%d try's BALLCOUNT: %dS %dB \n" % (trytime, strikes, balls))
        return True


tryagain = 'Y'
while tryagain == 'Y':

    x = makenumber()
    trytime = 0

    i = True

    while i:
        print("write your number in 3 digits: ")
        arr = [*map(int, input().split())]
        if arr[0] < 10:
            p = checkballcount(arr[0], arr[1], arr[2])
        else:
            p = checkballcount(arr[0] // 100, (arr[0] % 100) // 10, (arr[0] % 10))
        trytime += 1
        i = printresult(p, trytime)

    print("Do you want to play again? yes: Y // NO: N")
    tryagain = input()
