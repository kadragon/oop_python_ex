import random
TEXT_LINE = 80

b=['1','2','3','4','5','6','7','8','9','0']
c=0
d=['0','0','0']
random.shuffle(b) #b를 섞어주는 함수
for i in b:
    if c<3:
        #print(i)
        d[c]=i #b의 리스트 중에서 앞의 3개만 따로 빼서 d에 저장한다.
        c+=1
    else:
        break

def display_intro():  # intro 함수 python 에서는 함수를 def 을 이용하여 정의한다. 반환형을 명시하지 않는다.
    print('=' * TEXT_LINE)
    print("""
    This is number baseball game!
    (game rule)
    1. Random number will given which is three digits and digits are all different
    2. If you write three digit number ex)123 or 345, I will answer strike, ball and out
    strike - position and the number is right
    ball   - only number is right
    out    - all numbers wrong

    < Get the high score! >
    """)
    print('=' * TEXT_LINE)
def GAME(): #게임을 진행하는 함수
    game=0 #게임의 진행 횟수를 알려주는 것
    while True:
        if (game == 10):
            print("그걸 못맞추냐 ㅉㅉ")
            break
        strike = 0
        ball = 0
        out = 0
        while True:
            count = 0
            a = input()
            if a[0] == a[1]: count += 1
            if a[0] == a[2]: count += 1
            if a[1] == a[2]: count += 1
            if len(a) > 3 or count != 0: # 같은 숫자가 존자하거나 숫자 3개 이상 혹은 띄어쓰기 같은 다른 것이 들어갔을 때 다시 입력을 받기 위한 반복문
                print("다시 입력해주세욤 >.<")
            else:
                break
        game += 1 #게임을 시작하기 때문에 게임 횟수를 더해줌
        j = 0
        while j < 3: #d에 있는 숫자 3개와 입력된 숫자를 차례로 비교해주면서 스트라이크 볼 아웃을 더해준다.
            x = 0
            for k in d:
                if a[j] == k:
                    break
                else:
                    x += 1
            #      print(x)
            if x == 3:
                out += 1
            elif x == j:
                strike += 1
            elif x != j:
                ball += 1
            j += 1
        # print(out)
        # print(ball)
        # print(strike)
        if strike == 3: #스트라이크가 3이면 숫자를 맞췃다는 것을 의미하므로 반복문을 끝낸다.
            print("Good")
            break
        else:
            print('%d S %d B %d O' % (strike, ball, out))
play_again='yes'
while play_again=='yes' or play_again=='y': # 다시하는 함수를 만들어줌
    display_intro()
    GAME()
    play_again= input('다시하쉴?(yes or no): ')
