import random

rannum = [1, 2, 3, 4, 5, 6, 7, 8, 9]  # 랜덤 정수 생성 위함
random.shuffle(rannum)
randomnumber = rannum[0] * 100 + rannum[1] * 10 + rannum[2]  # 셔플한 리스트의 앞 3개 숫자를 사용
randnum = [rannum[0], rannum[1], rannum[2]]

trycount = 0  # 시도 횟수
strike = 0  # 스트라이크 개수
ball = 0  # 볼 개수
play = True  # 계속 할지 판단


def check_strike():  # 스트라이크 개수 판별 함수
    global strike
    abc = 0
    for a in randnum:
        if a == num[abc]:
            strike += 1
        abc += 1


def check_ball():  # 볼 개수 판별 함수
    global ball

    if num[0] == randnum[1] or num[0] == randnum[2]:
        ball += 1
    if num[1] == randnum[0] or num[1] == randnum[2]:
        ball += 1
    if num[2] == randnum[0] or num[2] == randnum[1]:
        ball += 1


while True:
    while play:
        tryconut = 0
        number = input('Count : %d, Try : ' % trycount)
        number = int(number)
        num = [number // 100, (number // 10) % 10, number % 10]
        if "number".isdigit == False or number < 100 or number > 999:
            print('NO!!!')
            break
        trycount += 1
        if trycount > 10:
            print('Game Over. So Sad...')
            break

        check_strike()
        check_ball()

        if strike == 0 and ball == 0:
            print('OUT!!!')
        elif strike == 3:
            print('Great!')
            break
        elif strike != 0 or ball != 0:
            print("%d strike %d ball" % (strike, ball))

        strike = 0
        ball = 0

    play = input('GAME END. Do you want to play again? (y / n)').lower().startswith('y')  # 재시작?

    if not play:
        break
