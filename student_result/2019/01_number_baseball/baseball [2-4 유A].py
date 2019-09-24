"""
Title 숫자야구게임
제작자 2408 유동헌
Date 2019.09.21
"""
import random
ANS=[] #생성된 세자리 정수를 담아두는 리스트
def makesecret(place): #세자리를 랜덤생성하는 함수
    ARR = list(range(10))#0부터 10까지의 수
    random.shuffle(ARR)#섞음, 원하는 것은 앞의 세자리
    threenum = ARR[0:place] #랜덤생성 리스트를 세자리로 잘라냄
    ANS.extend(threenum)#ANS는 비어있는 리스트, 난수 넣어줌

def ERROR():#발생에러에 대해 에러문을 출력하는 함수
    print("입력값을 인식하지 못했습니다.\n올바르게 다시 입력해주십시오.\n0부터 9까지의 서로 다른 3가지의 수를 하나씩 띄어 입력해주세요.\n예 )123")

def checkresult(guess):#스트라이크,볼,아웃의 수를 계산하는 함수
    strike=0
    ball=0
    out=0
    for i in range(3): #정답과 비교
        if guess[i]==ANS[i]: #위치, 값 모두 맞으면 스트라이크
            strike=strike+1
        elif guess[i] in ANS: #숫자는 맞지만 위치가 틀리면 볼
            ball=ball+1
        else:#위치, 값 모두 틀렸을 때
            out=out+1
    print("%s S | %s B | %s O"%(strike,ball,out))
    if strike==3: #스트라이크가 3개이면 게임이 종료되어야 하니 참값을 리턴
        return True
    else: #스트라이크가 3개가 아니면 게임이 진행되니 거짓값을 리턴
        return False

def simplecheck(write): #입력값이 정수꼴로 들어올때 입력 개수가 3자리를 넘는지, 혹은 각 수가 서로 다른지, 0부터 9까지의 자연수가 입력된 것이 맞는지 검사하는 함수
    data=[] #write는 123과 같이 이어진 형태, 이를 잘라 보관하는 공간
    data.append(write[0])#일단 앞의 세자리를 끊어 보관(입력은 정수이므로)
    data.append(write[1])
    data.append(write[2])
    for i in range(len(data)):#0부터 9인지 확인
        if 0>int(data[i]) or int(data[i])>10:
            return False
    #simplecheck함수는 입력값이 옳으면 비교하기 좋게 리스트를 고쳐 BOOL로 내보내나, 틀릴경우 BOOL에 FALSE를 담아 리턴한다.
    if data[0]==data[1] or data[0]==data[2] or data[1]==data[2]:#각기 다른지 확인
        return False
    if len(data)>3 or len(write)>3:#3자리로 입력됐는지 확인
        return False
    for i in range(len(data)):#data를 다 정수형으로 전환
        data[i]=int(data[i])
    return data #비교하기 좋은 입력값으로 고쳐진 상태인 data로 리턴

def checkwrite(write):#이외 이상한 값의 입력, 세자리도 안되는 정수의 입력에 대한 체크 함수
    try:
        BOOL=simplecheck(write)#일단 맞다 가정하고 간단체크함수 시행
    except Exception:#입력값이 올바르지 않을때(세자리보다 짧거나, 0부터 9까지의 값이 아니거나, 띄어썼거나, 안썼거나 등등)
        ERROR()
        return False
    else: #simplecheck에서 나온 BOOL 사용
        if BOOL: #입력이 옳으면 그대로 BOOL 리턴
            return BOOL
        else: #입력이 그르면 ERROR문 출력
            ERROR()
            return False

def REGAME(code): #다시 플레이할지 물어보고 이에 대해 판단하는 함수
    if code==1: #이겼을 때
        print("YOU WIN! REGAME?[Y/N(혹은 아무거나)]")
    elif code==0: #졌을 때
        print("YOU LOSE!REGAME?[Y/N(혹은 아무거나)]")
    answer=input()
    if answer=='Y':
        del ANS[:] #정답 초기화
        makesecret(3) #다시 정답 생성
        return True
    else:
        print("SEE YOU!")
        return False

#메인코드
makesecret(3) #난수 세자리 생성
count=0 #10번이 되는지 체크
while(count<10): #count 체크하며 플레이
    print("남은 횟수 {0}회".format(10-count)) #남은 횟수 출력
    write=input() #입력
    if checkwrite(write): #입력값 검사
        guess=checkwrite(write) #옳으면 guess에 data저장
        FLAG=checkresult(guess) #guess를 비교하고 리턴값을 flag에 저장
        count=count+1#카운트 수정
        if FLAG: #스트라이크 세개
            if REGAME(1): #이겼다는 문구와 함께 다시할건지 입력받음. 다시 할경우
                count=0 #카운트 초기화
            else:
                break #다시 안할경우
        if count==10: #10번 다 입력
            print("The Answer was {0}{1}{2}!".format(ANS[0],ANS[1],ANS[2])) #모른채로 종료되면 궁금하니 답이 뭐였는지 알려줌
            if REGAME(0): #졌다는 문구와 함께 다시할건지 입력받음.다시 할경우
                count=0 #카운트 초기화
            else:
                break #다시 안할경우

