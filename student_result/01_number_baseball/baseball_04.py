
import random
num=[0,1,2,3,4,5,6,7,8,9]   #랜덤 수 리스트

print("Welcome to number baseball game!")
print("Heres 3digits, and you will guess it.")
print("If you had a correct digit in the rigt place, you will have a 1S.")
print("If you had a correct digit but in the wrong place, you will have a 1b.")
print("Either of them, you will have a 1O.")
print("Good Luck!\n")

while True:
    pick = random.sample(num, 3)    #게임이 시작되면 랜덤 수 3개 뽑기
    flag=1  #게임이 끝났는지 판정
    while flag: #게임이 끝나기 전까지
        s_cnt=0
        b_cnt=0
        o_cnt=0
        user=input("Input number: ")   #숫자 입력받기
        if(len(user)!=3):   #입력받은 수가 3개가 아니면 재입력
            print("Wrong Input. Do it again.\n")
            continue
        elif user.isdigit()!=1: #입력받은 수가 정수가 아니면 재입력
            print("Wrong Input. Do it again.\n")
            continue
        elif (user[0]==user[1] or user[1]==user[2] or user[2]==user[1]):    #중복되는 수가 있다면 재입력
            print("Wrong Input. Do it again.\n")
            continue

        for i in range(0,3):
            for j in range(0,3):
                if((user[i]==str(pick[j])) and i==j):   #숫자가 같고 자리수가 같다면
                    s_cnt+=1    #스트라이크 카운트 +1
                elif((user[i]==str(pick[j])) and i!=j): #숫자가 같지만 자리수가 다르면
                    b_cnt+=1    #볼 카운트 +1
        o_cnt=3-(s_cnt+b_cnt)   #나머지는 아웃 카운트
        print("%dS %dB %dO\n" %(s_cnt, b_cnt, o_cnt))
        if s_cnt==3: #스트라이크 카운트가 3이면 게임 종료 표시
            flag=0
    print("You got a correct number!")
    a=input("Would you play again? yes / no\n")
    if(a=='no'):    #다시 하지 않으면 프로그램 종료
        break