import random#랜덤 리스트 생성하기 위해서

guess_list=[]#맞춰야 하는 랜덤 리스트
user_guess=[]#입력받는 리스트

def rule():
    print("당신은  %d개의 목숨을 가지고 있습니다. " %life)
    print("당신은 제가 생각하는 3자리의 정수를 맞추면 됩니다. ")
    print("당신이 답을 말할 때마다 제가 당신의 답을 평가합니다.")
    print("Strike(S) = 하나의 숫자가 맞았고 올바른 위치에 있다.")
    print("Ball(B) = 하나의 숫자가 맞았으나 위치는 틀렸다.")
    print("Out(O) = 숫자가 틀렸다.")

def make_number():
    num_list=list(range(10))#0부터 9까지 num_list에 넣기
    random.shuffle(num_list)#순서를 랜덤으로 바꾸기
    #guess_list에 앞의 세 숫자를 넣기
    guess_list.append(num_list[0])
    guess_list.append(num_list[1])
    guess_list.append(num_list[2])
def guess_check():
    if(user_guess[0]>=100):#숫자가 공백없이 입력받아졌을 경우
        temp=user_guess[0]
        del user_guess[0]
        user_guess.append(temp//100)
        user_guess.append((temp%100)//10)
        user_guess.append(temp%10)
    elif(user_guess[0]>=10 and user_guess[0]<100):#숫자가 공백 없이 입력받아졌는데 맨 앞자리가 0인 경우
        temp=user_guess[0]
        del user_guess[0]
        user_guess.append(0)
        user_guess.append(temp//10)
        user_guess.append(temp%10)

def guess_grading():
    strike = 0  # strike 갯수
    ball = 0  # ball 갯수
    out = 0  # out 갯수
    if (guess_list==user_guess):#정답 리스트와 사용자 리스트가 같은 경우
        print("정답!!")
    else :
        for i in range(len(user_guess)):
            if(user_guess[i]==guess_list[i]):#위치가 같은 경우
                strike+=1
            elif(user_guess[i] in guess_list):#위치는 다르나 안에 있는 경우
                ball+=1
            else:#아예 없을 경우
                out+=1
        print("%d S | %d B | %d O"%(strike,ball,out))

def life_input():
    temp=int(input())
    while temp>10 :
        if(temp>10):
            print("다시 입력하시오")
            temp=int(input())

    print("적당합니다 ")
    return temp
print("="*80)
print("원하는 목숩을 입력하세요. 단, 10개 이하로 입력하세요")
life=life_input()
print("규칙을 알고 싶으면 0, 바로 시작하고 싶으면 1을 입력하시오")
start=int(input())
if(start==0):
    rule()
while True:
    try_num=1
    make_number()
    while (try_num<=life) :#시도가 목숨보다 적을 경우만 실행
        print("Guess %d:"%try_num,end=' ')
        user_guess=list(map(int,input().split()))
        guess_check()#숫자가 원하는 형태로 입력되었는지 확인하는 함수
        guess_grading()
        try_num+=1
        if(guess_list==user_guess):
            break
        if(try_num>life):
            print("목숨을 다 잃었습니다. 정답은 ",end='')
            print("".join(map(str,guess_list)))#리스트를 출력할 때 대괄호와 컴마를 없애줌
    print("다시 하겠습니까? yes or no로 대답해주십시오")
    again=input()
    if(again[0]=='n'):
        break
    else:
        guess_list=[]#맞춰야할 리스트 초기화
        user_quess=[]#입력받을 리스트 초기화
        print("목숨을 재설정 하겠습니다? yes or no로 대답해주십시오")
        life_check=input()
        if(life_check[0]=='y'):
            print("얼마로 재설정하겠습니까?")
            life=life_input()



