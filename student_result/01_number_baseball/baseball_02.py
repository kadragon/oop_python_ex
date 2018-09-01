import random


# check 라는 함수 하나에, 입력 값 검증 및 S B O 판정까지 모두 들어가 있는 것은 효율적이지 못함
# 한 함수는 한개의 것만 하는것이 나중에 유지보수 하기 편하고 목적 지향적임
def check(a, b, c, ans, innings):
    while a > 9 or b > 9 or c > 9 or a == b or a == c or b == c or a < 0 or b < 0 or c < 0:
        print('입력오류 :(')
        print('다시 입력하세요')
        t = int(input())
        a = t // 100
        b = (t % 100 - t % 10) / 10
        c = t % 10

    strike = 0
    ball = 0
    if a == ans[0]:
        strike += 1
    if b == ans[1]:
        strike += 1
    if c == ans[2]:
        strike += 1
    if a == ans[1] or a == ans[2]:
        ball += 1
    if b == ans[0] or b == ans[2]:
        ball += 1
    if c == ans[0] or c == ans[1]:
        ball += 1
    if strike == 3:
        print('정답!!!')
        return True
    else:
        if innings == 9:
            print('실패 TT')
            # print('정답은 %d%d%d' % int(a, b, c)) // int() 형을 변경할때, 인자를 1개만 받는다.
            print('정답은 %d%d%d' % (int(a), int(b), int(c)))
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

    t = int(input())
    a = t // 100
    b = (t % 100 - t % 10) // 10
    c = t % 10

    if check(a, b, c, ans, innings):
        return True


while True:
    print("게임 시작")
    random_number = list(range(10))
    random.shuffle(random_number)

    ans = random_number[:3]
    # ans = [0, 0, 0]
    # i = 0
    # while i <= 2:
    #     ans[i] = random_number[i]
    #     i += 1

    for i in range(9):
        if get_number(i + 1, ans):
            break
    print('다시 하시겠습니까?')
    print('no 를 입력하시면 종료되고, 그 외를 입력하시면 게임이 재개됩니다')
    retry = input()
    if retry.strip().startswith('n'):
        break
    # if retry[0] == 'n':
    #     break
