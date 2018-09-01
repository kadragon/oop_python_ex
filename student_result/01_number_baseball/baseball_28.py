import random

def get():
    num=list(range(10))
    random.shuffle(num)
    number=[]
    number.append(num[0])
    number.append(num[1])
    number.append(num[2])
    return number

def check(nowlist):
    s=b=0
    cnt=0
    for i in nowlist:
        if i in number:
            if nowlist[cnt]==number[cnt]:
                s+=1
            else:
                b+=1
        cnt+=1
    
    if s==0 and b==0:
        print("아웃")
    else:
        print("%dS %dB"%(s,b))
def put():
    now=input()
    now=now.replace(" ","")
    if len(now)==3:
        now=int(now)
        nowlist=[]
        nowlist.append(now//100)
        nowlist.append((now%100-now%10)//10)
        nowlist.append(now%10)
        return nowlist
    elif len(now)==2:
        now=int(now)
        nowlist=[]
        nowlist.append(0)
        nowlist.append(now//10)
        nowlist.append(now%10)
        return nowlist
    print(nowlist)

def game(number,cnt):
    while cnt<10:
        cnt+=1
        lis=put()
        if lis[0]==number[0] and lis[2]==number[2] and lis[1]==number[1]:
            print("정답입니다")
            break
        else:
            check(lis)
    if cnt>10:
        print("10번 이상 입력했습니다.")
    print("다시 플레이하시겠습니까?(yes, no)")
    ans=input()
    return ans

while(True):
    number=get()
    print(number)
    an=game(number,0)
    if an[0]=="n" or an[0]=="N" or an[0]=="아":
        break
        
