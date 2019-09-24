# 컴퓨터가 랜덤한 세자리수를 생성하기 위해 random을 import 해줍니다
import random
import time

def make_number():
    """
    일반적인 숫자 야구 규칙에 맞도록 세자리 숫자를 만드는 함수입니다
    """
    num_list= list(range(10))          # 우선 0부터 10까지의 수가 순서대로 나열된 리스트 형태의 num_list 를 만듭니다
    random.shuffle(num_list)         # num_list 의 값을 무작위로 섞어줍니다
    answer_num = ''     # 사용자가 맞추어야할 정답인 answer_num을 초기화시켜줍니다
    for i in range(3):     # 무작위로 섞은 num_list의 앞의 세  수를 활용해 세자리수 answer_num을 만듭니다
        answer_num += str(num_list[i])
    return answer_num


def strike_ball_out(try_num, answer_num):
    """
    사용자가 예측한 세자리수인 try_num과 정답인 answer_num을 비교하여 규칙에 맞게 strike, ball, out의 개수를 알려줍니다
    """
    if try_num == answer_num:  # 예측한 수와 정답이 일치하면 정답 표시와 함께 함수를 종료합니다
        return ("")

    strike = 0  # strike 의 개수를 셉니다
    ball = 0     # ball 의 개수를 셉니다
    out = 0      # out 의 개수를 셉니다

    for i in range(0,3):  # 각 자리수별로 strike, ball, out을 판별합니다
        if try_num[i] == answer_num[i]:  # strike 인 경우
            strike += 1
        elif try_num[i] in answer_num:  # ball 인 경우
            ball += 1
        else:  # out 인 경우
            out += 1

    return str(strike) + ' S | ' + str(ball) + ' B | ' + str(out) + ' O\n'


def right_number(insert):
    """
    사용자가 입력한 값이  세자리 수인지, 숫자들로만 구성되어있는지 , 겹치는 수는 없는지 판별합니다
    """
    er = 0

    if insert == ' ':
        return False

    for i in insert:
        if not i.isdigit():  # 사용자가 입력한 값 중 하나라도 숫자가 아니라면 False를 return 합니다
            er +=1
    if er != 0:
        print("/ 0 에서 9까지 숫자로 구성되어야 한다니까", end=' ')

    if len(insert)!=3: # 사용자가 입력한 수가 세자리수가 아니라면 Fasle를 return 합니다
        print("/ 세자리 정수를 입력하라고;;", end = ' ')
        er +=1
    elif  insert[0]==insert[1]: # 사용자가 입력한 값 중 중복된 값이 있다면 False를 return 합니다
        print("/ 백의자리수와 십의자리수가 중복되잖아", end = ' ')
        er +=1
    elif insert[0]==insert[2]:
        print("/ 백의자리수와 일의자리수가 중복되잖아", end = ' ')
        er +=1
    elif insert[1]==insert[2]:
        print("/ 십의자리수와 일의자리수가 중복되잖아", end = ' ')
        er +=1

    if er!=0:
        return False

    return True


def play_again():
    """
    사용자가 게임을 다시 플레이할 것인지 의사를 묻습니다
    """
    return input('\n어때, 한번 더 도전해보지 않을래? 애.송.아 \n(yes / no)\n>').lower().startswith('y')

print("=" * 70)
print("숫자야구에 온 것을 환영한다! 나는 오직 숫자야구를 위해 만들어진 alpha-num_baseball이지\n")
print("설마 규칙을 모르는건 아니겠지..?\n")
print("규칙을 안다면 숫자 1을 누르고 그러지 않다면 숫자2를 눌러 :", end = ' ')
while 1:
    a  = input()
    if a == '1':
        print("좋아. 그럼 바로 시작해볼까?")
        break
    elif a=='2':
        print("\n그럴줄 알았다...")
        time.sleep(1)
        print("\n우선 너는 0 부터 9까지 서로 다른 세가지 수로 구성된 세자리 수를 입력해야 해\n그리고 내가 앞으로 하는 말은 이런 뜻일거야")
        time.sleep(2)
        print("\nStrike (S)  네가 말한 세자리 수 중 정답과 자리까지 일치한 수의 개수를 의미한다")
        time.sleep(1)
        print("Ball (B)   네가 말한 세자리 수 중 정답에 포함되지만 자리는 틀린 수의 개수를 의마한다")
        time.sleep(1)
        print("Out (O)   네가 말한 세자리 수 중 정답에 포함되지 않은 수의 개수를 의미한다\n")
        time.sleep(1.5)
        print("이제 알겠어? 그럼 시작하도록 하지")
        break
    else:
        print("1이나 2만 누르라니까!")
    time.sleep(1)
print("=" * 70)

while True:
    answer = make_number()  # 정답이 될 세자리수를 생성합니다
    time.sleep(1)
    print('\n세자리수를 생각했으니 이제 한번 맞혀봐\n참! 기회는 열 번 뿐이다')
    trial = 1                         # 사용자의 시도 횟수를 저장하는 변수입니다

    while trial <=10:         # 시도 횟수가 10번을 초과하지 않도록 설정합니다
        guess = ' '                 # 사용자 입력한 값을 저장하는 변수입니다
        while not right_number(guess):    # 입력한 값이 정수로 이루어진 세자리 자연수인지 확인합니다
            print('\n%s번째 시도' % trial, end=' ')
            guess = input('>')

        trial += 1
        print(strike_ball_out(guess, answer))

        if guess == answer:
            if trial<=4:
                print("%d번 만에 정답이라니,,, 찍어서 맞춘거나 다름없어!" % (trial-1))
            elif 4 < trial <=7:
                print("오호라 문제를 푸는데 %d번이면 충분하다...\n\n뭐, 이정도면 나쁘지 않은 실력이네" % (trial-1))
            elif 7< trial <=10:
                print("%d번만 더 놓쳤어도 틀렸을텐데... 운이 좋았네" % (11-trial))
            else:
                print("이런 정답이잖아!\n\n다 끝나는 경기였는데,,, 운이 좋은 줄로 알아라")
            break

        if trial<=10:
            if trial==2:
                print("틀.렸.어!\n설마 단번에 맞출수 있다고 생각한건 아니겠지?")
            if trial==3:
                print("2번째 도전인데 무엇을 바라겠어... 땡!")
            if trial==4:
                print("세 번 틀리는 것 까지는 봐줄만 하지")
            if trial==5:
                print("이제 쯤이면 슬슬 맞출 때가 되었는데\n너는 아직 멀었다")
            if trial==6:
                print("벌써 절반의 기회가 날라갔어! 잘 좀 생각해봐!")
            if trial==7:
                print("흐음,, 실망인걸?\n규칙은 제대로 이해한 것 맞아?")
            if trial==8:
                print("또또또 ... 틀렸어!\n 오늘 안에 맞출수 있긴 한거니?")
            if trial==9:
                print("내 승리가 코앞이다", end = ' ')
                time.sleep(1)
                print("하하하")
            if trial==10:
                print("마지막까지 왔구만... 이 기세로는 맞히지 못할것 같은걸")
            time.sleep(1)

            print("\n이제 남은 기회는 %d번 뿐이다" % (11-trial))

        if trial > 10:
            print('10번을 도전해도 맞히지 못하다니. 실망이군\n정답은 %s이었다' %answer)

    if not play_again():
        print("=" * 70)
        print("숫자야구 경기 종료" )
        print("=" * 70)
        break

