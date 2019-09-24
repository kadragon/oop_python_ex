from random import *

# 숫자야구 게임을 해보자!

def INTRO():    # 인트로

    print("Welcome to Eunho\'s land!! Today's game is number baseball game!")
    print("Lets' start.\n")


def INPUT():
    """
    3개의 숫자를 입력받는 부분
    :return: 입력 받은 세 숫자의 리스트
    """
    li = []
    num = input("Give three numbers")    # num 에 string 형태로 입력 받기
    tmp = []
    while 1:
        if len(num) == 3:       # 길이가 3이고 모두 숫자일때, 그대로 리스트로 바꿔 return
            if num.isdigit():
                li = list(num)
                break
        else:
            tmp = list(num)
            check = 0
            for i in range(len(num)):   # string 돌며 숫자만 리스트에 넣고 체크
                if str(tmp[i]).isdigit():
                    li.append(tmp[i])
                    check += 1
            if check == 3:  # 체크된 개수가 3개일 때 return
                break
            else:           # 아니면 리스트 초기화
                li = []
        num = input("0부터 9까지의 정수를 3개 입력해줘요..")  # 다시 입력 받기

    for j in range(0, 3):
        li[j] = int(li[j])      # 모두 정수형으로 바꾸어 리스트에 넣기

    print("%d %d %d 입력한걸로 알게요!" % (li[0], li[1], li[2]))    # 입력 데이터 확인
    return li


def playagain():
    """
    한 판 더할지 결정
    :return: 1또는 0으로 리턴
    """
    ag = 0
    a = input('Play again? Yes or No')
    while 1:
        if a == 'Yes':  # Yes 에서만 1로!
            ag = '1'
            break
        elif a == 'No':  # No 에서만 0으로!
            ag = '0'
            break
        else:            # 다른 경우 다시 입력받기!
            a = input('Just say Yes or No')
    return int(ag)


INTRO()
turn = 0    # 턴 수
strike = 0  # 스트라이크 수
ball = 0    # 볼 수
out = 0     # 아웃 수
again = 1   # 한판 더 할지 결정하는 인자
answer = list(sample(range(0, 9), 3))  # 리스트에 실제 답 랜덤한값 넣기
while again:
    # 초기화 과정 시작
    strike = 0
    ball = 0
    out = 0
    # 초기화 과정 끝
    turn += 1   # 한번씩 돌 때마다 턴 수 증가
    chk = [0, 0, 0]
    reply = INPUT() # 입력 받기

    for i in range(0, 3):
        if reply[i] == answer[i]:   # 위치와 값 일치시,
            strike += 1             # 스트라이크 수 증가
        else:
            for j in range(0, 3):
                if reply[i] == answer[j] and i != j:    # 위치 다르고 값 동일시
                    ball += 1                           # 볼 수 증가
                if reply[i] != answer[j]:               # 입력 데이터와 실제 답 비교
                    chk[i] += 1                         # 각 데이터에 해당하는 체크 값 증가
            if chk[i] == 3:                             # 체크 값이 3이면 모든 값과 다른 것이므로
                out += 1                                # 아웃 수 증가

    if strike != 3 and turn <= 10:
        print('<%d turn>  %d strike / %d ball / %d out' % (turn, strike, ball, out))    # 스트라이크, 볼, 아웃 수 출력
    else:
        if strike != 3:  # 10번째 턴에서도 틀리면 아래와 같이 출력
            print('You didn\'t got it!')
            print('Answer was %d %d %d' %(answer[0],answer[1],answer[2]))   # 답도 함께 출력
        else:
            print('You got 3 strikes for %d turn' % (turn - 1))     # 답 맞추면 몇 턴만에 맞춘지 출력
        answer = list(sample(range(0, 9), 3))  # 리스트에 실제 답 넣기
        turn = 0    # 몇 턴째인지 초기화
        again = playagain() # 게임 더 할건지 값으로 입력 받기