import random
import sys


print("""숫자 야구 게임을 시작합니다!

0부터 9까지의 숫자가 중복을 제외하여 무작위로 3개가 정해집니다!
플레이어는 중복되지 않는 숫자 세 자리를 입력해주세요!
입력한 숫자가 자리까지 맞는 경우 Strike
자리는 틀렸지만 해당 숫자를 포함 할 경우 Ball
만약 Strike와 Ball이 하나도 없을 경우 OUT! 이 출력되며
3Strike에 성공할 경우 게임은 당신의 승리로 끝납니다!

게임 도중 게임을 그만두고 싶다면 exit을 입력해주세요!

""")


#정답을 정하는 함수
def pick_number():
    ball=[0,0,0]
    whole = list(range(10))
    random.shuffle(whole)                                                   #0부터 9까지의 배열을 랜덤 셔플, 앞의 세 수를 정답으로 저장
    for i in range(3):
        ball[i] = int(whole[i])

    return ball


#사용자가 입력한 답과 정답을 비교하여 Strike와 Ball개수를 세는 함수
def match_number(match, ball):
    b = 0
    s = 0
    o = 0
    for i in range(3):
        if match[i] in ball:                                                #입력값의 숫자가 정답에 존재할 경우 Ball+1
            b += 1

    for i in range(3):
        if match[i] == ball[i]:                                             #입력값의 숫자가 정답에 존재하며, 자리 또한 같을 경우 Strike+1, Strike는 앞의 Ball에서 세어졌으므로 Ball-1
            s += 1
            b -= 1

    if b==0 and s==0:                                                       #Strike와 Ball 모두 0일 경우 o==1
        o = 1

    return b,s,o


#사용자가 입력한 값이 exit을 제외한 문자열(숫자 제외)이거나 세자리수가 아닌 경우를 판단하는 함수
def check_number(match):
    if len(match) != 3:                                                     #입력이 3자리가 아닐 경우 0 반환(재입력)
        return 0

    elif match[0]==match[1] or match[2]==match[1] or match[0]==match[2]:    #입력이 중복될 경우 0 반환(재입력)
        return 0

    for i in match:
        if int(i) not in list(range(10)):                                   #입력이 숫자가 아닐 경우 0 반환(재입력)(exit 제외)
            return 0

    else:
        return 1                                                            #입력이 올바른 경우 1 반환


#사용자의 입력을 받는 함수
def input_number():
    attempt = input()
    if attempt == "exit":                                                   #입력이 exit일 경우 게임 종료 여부를 물음
        print("Are You Sure You Want To Quit This Game??  [Y/N]")
        ex=input()

        if ex == "Y" or ex=='y':                                            #입력이 Y일 경우 게임 종료
            sys.exit()

        else:                                                               #입력이 Y가 아닐 경우 게임을 재개
            print("Then Resume The Game")
            return input_number()

    else:
        while check_number(attempt)==0:
            print("Try Again!")                                             #입력이 바르지 않을 경우 입력을 다시 받음
            return input_number()

    return attempt                                                          #입력값을 반환


#게임에서 승리/패배한 경우 게임을 재시작하는 함수
def restart():
    print("Dou You Want To Play Again??  [Y/N]")
    again = input()                                                         #재시작 여부를 입력

    if again == 'N' or again == 'n':
        print("Game Finished")                                              #입력이 N인 경우 프로그램 종료
        sys.exit()

    elif again == 'Y' or again == 'y':
        print("Then Restart The Game")                                      #입력이 Y인 경우 게임을 재시작
        return 1

    else:
        print("WRITE Y OR N")                                               #입력이 Y 또는 N(소문자 포함)이 아닌 경우 입력을 다시 받음
        return restart()


#게임을 진행하는 함수
def ingame(n,balls):
    k = 0                                                                   #게임의 성공/실패 여부를 판단하는 플래그
    for i in range(n):                                                      #목숨의 개수만큼 입력을 받음
        print("Attempt %d:"%(i+1))
        attempt = input_number()                                            #사용자가 답을 입력
        attempt_number = [0,0,0]

        for j in range(3):
            attempt_number[j] = int(attempt[j])

        b,s,o=match_number(attempt_number,balls)                            #Strike, Ball의 개수와 Out 여부를 판단함

        if o == 1:
            print("OUT!!")                                                  #o==1인 경우 OUT!! 출력

        elif s == 3:
            print("3 Strike!! You Won!!")                                   #3Strike일 경우 3 Strike!! You Won!!을 출력
            k=restart()                                                     #게임 재시작 여부를 판단
            break                                                           #이후 진행된 게임이 종료된 뒤 이전 게임의 진행을 종료

        else:
            print("%d Ball  %d Strike!!"%(b,s))                             #Out이거나 3Strike가 아닌 경우 Strike와 Ball의 개수를 출력

    if k==0:
        print(n,"번이나 실패하셨습니다 선생님...그만하시죠")                #실패한 경우 실패 메세지와 함께 재시작 여부를 판단
        restart()


#목숨의 개수를 입력받고 ingame함수를 계속 실행하는 함수
def number_baseball():
    while True:
        print("목숨의 개수를 입력해주세요! (최대 50개)")                    #목숨 입력
        n = int(input())
        if n > 50:                                                          #목숨이 50개 초과일 경우 50개로 한정
            print("최대 50개.....라고요")
            n = 50

        print("""목숨이 %d개로 설정되었습니다
        Game Start!""" % n)
        balls = pick_number()                                               #정답을 랜덤으로 정함
        ingame(n,balls)                                                     #게임 실행


#실행
number_baseball()