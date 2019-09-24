import random
number = 0
guessnum=0
def intro():
    print('='*30)
    print("2616 황인서 || 숫자 야구 게임")
    print("각 자리가 다른 세 자리의 자연수가 임의로 정해집니다.")
    print("첫 자리 숫자는 0일 수 있습니다.")
    print("당신이 추측한 수의 자릿수 중")
    print("제가 생각한 수의 자릿수와 숫자, 위치 모두 같으면 strike,")
    print("제가 생각한 수의 자릿수와 숫자만 같으면 ball,")
    print("제가 생각한 수의 자릿수와 하나도 같지 않으면 out입니다.")
    print("10번의 기회를 드리겠습니다. 맞히실 수 있나요?")
    print("="*30)
def input1(): #입력
    global guessnum
    while True:
        oryu = 0
        temp = input("숫자를 맞혀보세요. ")
        for i in range(0, len(temp)): #수열인가?
            if temp[i]<'0' or temp[i]>'9':
                oryu=1
                print("잘못 입력하셨습니다.")
                break
            if oryu == 1:
                continue
        if(temp[0]==temp[1] or temp[0]==temp[2] or temp[1]==temp[2]): #자리수가 다른 수 입력
            oryu=1
            print("각 자리가 다른 수를 입력해주세요.")
        if oryu == 1:
           continue
        guess=list(map(int,temp))
        if(len(guess)!=3):#세자리수입력
            oryu=1
            print("3자리 수를 입력해주세요.")
        if oryu==0:#숫자 입력
            guessnum=guess[2]+guess[1]*10+guess[0]*100
            break
def makenum(): #랜덤 수 입력
    global number
    numlist=list(range(999))
    random.shuffle(numlist)
    i=0
    while True: #자릿수 겹치지 않는 수 만들기
        tmp=numlist[i]
        h=tmp//100
        t=tmp//10-10*h
        o=tmp%10
        if(h!=t and t!=o and h!=o):
            break
    else:
        i+=1
    number=numlist[i]

#코드 시작

intro()
makenum()
cnt=0
while cnt<10:
    strike=0
    ball=0
    input1()
    guessn=[guessnum%10, (guessnum%100-guessnum%10)/10, guessnum//100] #입력받은 수 리스트 만들기
    num=[number%10, (number%100-number%10)/10, number//100] #문제 수 리스트 만들기
    for i in range(0,3): #스트라이크 판독
        if guessn[i]==num[i]:
            strike+=1
        else : #스트라이크 아니면 볼 판독
            for j in range (0,3):
                if guessn[i]==num[j] and i!=j:
                    ball+=1
    cnt+=1
    if ball+strike==0 : #나머지는 아웃 판독
        print("Out 입니다.")
    else:
        print("%d Strike %d Ball 입니다." % (strike, ball) )
        if strike==3:
            print("%d 번 만에 맞히셨습니다! 축하합니다. 정답은 %03d" % (cnt, number))
            break
    if cnt==10:
        print("못 맞히셨네요. 정답은 %d 였습니다." %number)
        break
