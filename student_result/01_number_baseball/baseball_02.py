import random


def check(a, b, c, ans, innings):
    while a > 9 or b > 9 or c > 9 or a == b or a == c or b == c or a < 0 or b < 0 or c < 0:
        print('입력오류 :(')
        print('다시 입력하세요')
        t=int(input())
        a=t//100
        b=(t%100-t%10)/10
        c=t%10
    strike = 0
    ball = 0
    if a == ans[0]:
        strike+=1
    if b == ans[1]:
        strike+=1
    if c == ans[2]:
        strike+=1
    if a == ans[1] or a == ans[2]:
         ball+=1
    if b == ans[0] or b == ans[2]:
        ball+=1
    if c == ans[0] or c == ans[1]:
       ball+=1
    if strike == 3:
       print('정답!!!')
       return True
    else:
        if innings == 9:
            print('실패 TT')
            print('정답은 %d%d%d' % int(a, b, c))
            return True
        out = 3 - strike - ball
        print(' %d strike %d ball %d out' % (strike, ball, out))
        return False


def get_number(innings, ans):
    if innings == 1:
        print('1st inning')
    elif innings == 2:
        print('2nd inning')
    else:
        print('%drd inning' % innings)
    t=int(input())
    a=t//100
    b=(t%100-t%10)//10
    c=t%10
    if check(a, b, c, ans, innings):
        return True


while True:
    print("게임 시작")
    random_number = list(range(10))
    random.shuffle(random_number)
    ans=[0,0,0]
    i=0
    while i <= 2:
        ans[i] = random_number[i]
        i+=1
    for i in range(9):
        if get_number(i+1, ans):
            break
    print('다시 하시겠습니까?')
    print('no 를 입력하시면 종료되고, 그 외를 입력하시면 게임이 재개됩니다')
    retry = input()
    if retry[0] == 'n':
        break
