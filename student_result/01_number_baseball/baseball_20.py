import random
n=10
ten=10
for i in range(1,n):
    ten=ten*10


def tof(chk):
    cnt = 0
    for i in range(0,n):
        for j in range(0,n):
           if chk[i] == chk[j] and i != j:
                cnt = cnt+1
    if cnt == 0:
        return False
    else:
        return True


def strike(ans, rand):
    st=0
    for i in range(0,n):
        if ans[i] == rand[i]:
            st=st+1
    return st


def ball(ans, rand):
    ba=0
    for i in range(0,n):
        for j in range(0,n):
            if(ans[i] == rand[j]):
                ba=ba+1
    return ba-strike(ans,rand)


print("숫자 야구 게임입니다.")
print("%d자리 정수를 입력해주세요 (첫자리는 0이 아닙니다)" % n)
print("방법 설명은 인터넷을 참고하세요")
print("도전 기회는 10번입니다.")
rand = str(random.randrange(ten/10, ten))
while tof(rand):
    rand = str(random.randrange(ten / 10, ten))
flag=True
counter=1
while flag:
    print("%d자리 정수를 입력해주세요. %d 번째 입력입니다." % (n,counter))
    counter = counter + 1
    a=input('입력 : ')
    print("you entered : %s" % a)
    if a.isdigit() and len(a)==n:
        ballcnt=int(ball(a,rand))
        strikecnt=int(strike(a,rand))
        print("%d Ball || %d Strike || %d Out"% (ballcnt,strikecnt,n-ballcnt-strikecnt))
        if strikecnt==n:
            print("축하합니다. 정답을 맞추셨습니다!")
            play=input("다시 하시겠습니까? Y/N")
            if play=='y' or play=='Y':
                flag=True
                rand = str(random.randrange(ten / 10, ten))
                while tof(rand):
                    rand = str(random.randrange(ten / 10, ten))
                counter=1
            else:
                flag=False
    else:
        print("형식 오류 # 다시 입력하세요!")
        counter=counter-1
    if counter==10 and flag==True:
        print("정답은 %s 였습니다. 화이팅!" % rand)
        play = input("다시 하시겠습니까? Y/N")
        if play == 'y' or play == 'Y':
            flag = True
            rand = str(random.randrange(ten / 10, ten))
            while tof(rand):
                rand = str(random.randrange(ten / 10, ten))
            counter = 1
        else:
            flag = False