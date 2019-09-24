import random
import sys
num=[] #게임에서의 정답
a=[] #사용자에게 입력받은 숫자
s=0 #스트라이크의 개수
b=0 #볼의 개수
o=0 #아웃의 개수
life=10 #목숨의 개수

def intro(): #사용자에게 게임에 대해서 설명해준다.
    print("0부터 9까지의 숫자 중 중복되지 않은 3개의 정수로 이루어진 3자리 수 숫자를 맞추는 게임입니다.")
    print("숫자와 위치가 모두 맞으면 S,")
    print("숫자는 맞지만 위치가 틀리면 B,")
    print("숫자와 위치가 모두 틀리면 O입니다.")
    print("총 기회는 10번 주어집니다.")

def build(): #0부터 9까지의 정수 중 겹치지 않게 세 개의 정수를 고른다.
    global num
    num=[] #num 초기화
    ran_num=random.randint(0,9) #0부터 9 사이의 임의의 정수
    for i in range(3): #num에 임의의 정수 세 개를 넣는다.
        while ran_num in num:
            ran_num=random.randint(0,9)
        num.append(ran_num)
        
def game(): #사용자에게 세 개의 정수를 입력받아 스트라이크인지 볼인지 아웃인지 판단한다.
    global s,b,o
    a=list(input()) #a는 사용자의 입력값
    while ' ' in a: #사용자 입력 공백 제거
        a.remove(' ')
    if len(a)==3: #사용자가 입력한 리스트의 길이가 3이라면
        if a[0].isdecimal()==False or a[1].isdecimal()==False or a[2].isdecimal()==False: #세 원소 중 하나라도 정수가 아니면 함수 재실행
            print("정수를 입력해주세요!")
            game()
    if len(a)!=3: #정수를 3자리로 입력하지 않으면 함수 재실행
        print("세 자리로 입력해주세요!")
        game()
    a[0]=int(a[0])
    a[1]=int(a[1])
    a[2]=int(a[2])

    for i in range(3):
        if a[i]==num[i]: #num과 숫자와 위치가 같을 때 s 증가
            s=s+1
    for i in range(3): #num과 숫자는 같지만 위치가 다를 때 b 증가
        if a[0]==num[i] and i!=0:
            b=b+1
        if a[1]==num[i] and i!=1:
            b=b+1
        if a[2]==num[i] and i!=2:
            b=b+1
    o=3-(b+s) #num과 숫자와 위치가 모두 다르면 o 증가
    print("%dS %dB %dO 입니다!" % (s,b,o))
    print('='*30)
    result()

def result(): #게임 하나의 실행이 끝난 후, 결과를 알려준다.
    global life,s,b,o

    if s==3: #3 스트라이크이면 승리 메세지 출력
        print("축하합니다, 승리하셨습니다!")
        s=0
        b=0
        o=0
        restart()

    s=0
    b=0
    o=0
    life=life-1 #기회 1개 감소
    if life==0: #기회가 남지 않았으면 게임 종료
        restart()
    print("기회가 %d번 남았습니다!" % (life))
    game()

def restart(): #게임이 모두 끝난 후 다시 시작하는 동작을 결정하는 함수
    global life
    life=10
    print("게임을 다시 하시겠습니까? (y/n)")
    answer=list(input())
    while ' ' in answer: #사용자 입력 공백 제거
        answer.remove(' ')
    if len(answer)==1:
        if ord(answer[0])==121 or ord(answer[0])==89: #y나 Y가 입력되었을 때 재실행
            intro()
            build()
            game()
        elif ord(answer[0])==110 or ord(answer[0])==78: #n이나 N이 입력되었을 때 종료
            print("안녕히 가세요!")
            sys.exit()
        else:
            print("y나 n을 입력해주세요!")
            restart()
    if len(answer)==3:
        if (ord(answer[0])==121 or ord(answer[0])==89) and (ord(answer[1])==101 or ord(answer[1])==69) and (ord(answer[2])==115 or ord(answer[2])==83): # yes, Yes, yEs, yeS, YEs, YeS, YEs, YES가 입력되었을 때 재실행
            intro()
            build()
            game()
        else:
            print("y나 n을 입력해주세요!")
            restart()
    if len(answer)==2:
        if (ord(answer[0])==110 or ord(answer[0])==78) and (ord(answer[1])==111 or ord(answer[1])==79): #no, No, nO, NO가 입력되었을 때 종료
            print("안녕히 가세요!")
            sys.exit()
        else:
            print("y나 n을 입력해주세요!")
            restart()
    else:
        print("y나 n을 입력해주세요!")
        restart()

        
intro()
build()
for i in range(10):
    game()
    result()
