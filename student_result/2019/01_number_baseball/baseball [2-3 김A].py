import random

def makeans(): ##정답인 세 숫자를 생성, 리스트로 리턴한다
    list=[]
    randn = random.randint(0, 9)
    for i in range(3):
        while randn in list:
            randn = random.randint(0, 9)
        list.append(randn)
    return list

def giveinf(): ## 숫자야구를 아는지 여부 묻고 소개
    print("""안녕 친구, 너는 지금부터 숫자야구 게임을 하게 될거야.
게임을 하기 전!
숫자야구의 규칙은 알고 있니?(y/n) :""", end=' ')
    know = input()
    if know == 'y':
        print("알고 있구나! 그럼 시작해볼까?")
    else:
        print("""그럼 지금부터 설명을 시작하지
0에서 9까지의 숫자가 세개 있어, 아 물론 중복 가능해
너는 지금부터 나한테 세 개의 숫자를 띄어쓰기 없이 입력하면, 나는 네 숫자들과 답을 비교할꺼야.
만약 네가 제시한 숫자가 답에 없으면 OUT!!!
네가 제시한 숫자가 답에 있으면서도 자리까지 같으면 STRIKE!!!
제시한 숫자가 답에 있지만 자리가 다르면 BALL!!!
이렇게 해서 각각의 개수를 내가 출력할꺼야.
설명 끝! 그럼 시작해볼까?""")

def getmyguess(): ## 추측 세 숫자를 입력받고 리스트 형태로 리턴
    print("%d번째 시도 : " % cnt, end='')
    myans = input()
    list = []
    try:
        for i in myans:
            list.append(int(i))
        if len(list)!= 3:
            print("다시 입력하시오")
            return getmyguess()
        else:
            return list
    except:
        print("다시 입력하시오")
        return getmyguess()

def check(list): ##추측이 맞았는지 여부를 리턴
    strike=0
    ball=0
    out=0
    for i in range(3):
        if list[i] not in anslist:
            out+=1
            continue
        for j in range(3):
            if list[i] is anslist[j]:
                if i is j:
                    strike+=1
                else:
                    ball+=1
    print("strike : ", strike, "\n", "ball :", ball, "\n", "out : ", out) ## strike, ball, out 개수 출력
    if strike == 3:
        return True
    else:
        return False

def isitright(state, times): ##맞았으면 횟수에 따라 축하말을 하고, 게임이 끝나면 다시 플레이할지 여부 묻고 리턴
    again=1
    if state: ##정답이 맞은 경우(strike = 3)
        print("!!!!!CONGRATULATIONS!!!!!")
        if times == 1:
            print("금손이군!")
        elif times <= 3:
            print("꽤 하는군!")
        elif times <= 6:
            print("양호하군!")
        else:
            print("그럭저럭 하는군!")
        print("한번 더 해보겠나?(y/n) : ", end='')
        again = (input() == 'y')
    else:
        if times < 10: ## 도전 회수 남음
            print("다시 도전!")
        else: ##도전 횟수 모두 소비
            print("실 패!!\n다시 도전할텐가?(y/n)", end=' ')
            again = (input() == 'y')
    return again

##main
play=1
giveinf() ## 숫자야구 규칙 아는지 물음

while play: ##플레이어가 플레이하고 싶은 동안(play==True) 게임을 함
    print("START!! 띄어쓰기 제외하고 숫자 세개 입력하시오")
    anslist=makeans() ##정답 만들기
    cnt=1
    right=0
    while cnt<=10 and not right: ##기회는 10번으로 제한, 정답이 맞으면 탈출
        mylist=getmyguess() ##mylist에 정답이 되는 세 정수를 리스트로 넣음
        right = check(mylist) ##제시한 추측이 정답인지 확인
        play=isitright(right, cnt) ## 정답의 여부에 따라 축하하는 말을 전함, 게임이 끝나면 다시 플레이할지 여부를 물어 play에 넣음(true, false)
        cnt+=1 ##횟수+=1

print("그럼 GOOD BYE~")