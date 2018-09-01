"""
Title       숫자 야구 게임
Reference   나만의 Python Game 만들기
Author      triplepoint
Date        2018.08.27
"""

import time
SLEEP_TIME = 0.5

print("안녕하세요 고객님!")
time.sleep(SLEEP_TIME)
print("우리가 이번에 할 게임은 '숫자 야구'게임인데요,")
time.sleep(SLEEP_TIME)
print("룰은 생각보다 간단합니다.")
time.sleep(SLEEP_TIME)
print("""0~9까지의 숫자중
제가 생각한 3자리 숫자를 맞히면 돼요.""")
time.sleep(SLEEP_TIME)
print("""그냥 맞히긴 힘들테니 힌트를 드릴게요.
힌트는 strike, ball, out으로 드릴꺼에요.
strike는 숫자와 위치가 정확히 일치한 자릿수의 개수이구요,
ball은 숫자는 일치하지만 위치가 다른 자릿수의 개수이구요,
out은 고객님께서 말씀하신 3개의 숫자중에서 제가 생각한 숫자가 없는 겁니다.""")
time.sleep(SLEEP_TIME)
print("두자리나 한자리를 입력하면 앞쪽은 다 0으로 자동입력돼요!")
time.sleep(SLEEP_TIME)
print("""기회는 총 10번 드릴게요.
그안에 맞춰 보등가요. 할 수 있으면 해봐요.
드루와~ 드루와~
""")
time.sleep(SLEEP_TIME)

example=['0','1','2','3','4','5','6','7','8','9']


def in_put():
    while 1 :
        numbers=input('답? >>> ')
        check=0
        
        for i in range(len(numbers)):
            if not numbers[i] in example :
                check=1

        if check==1:
            print('뭐라고? 잘 안들려;;\n')
            continue

        numbers=int(numbers)

        if (numbers//1000)!=0:
            print('뭐라고? 잘 안들려;;\n')
            continue

        return [numbers//100,(numbers//10)%10,numbers%10]


def gostage():
    import random
    
    answer=(random.randint(0,9),random.randint(0,9),random.randint(0,9))    # 답 생성!

    if ((answer[0]==answer[1]) or (answer[1]==answer[2]) or (answer[2]==answer[0])) :
            gostage()     # 답에 같은 숫자가 있을경우 다시 생성
    
    for h in range(1,11) :

        number=in_put()

        
        result=[0,0,0]  #결과 초기화
        
        for i in range(3) :
            for j in range(3) :
                if answer[j] == number[i] :
                    if i==j : result[0]+=1   #strike 개수
                    else : result[1]+=1      #ball 개수
        result[2]=3-result[0]-result[1]      #out 개수

        print("strike : %d, ball : %d, out : %d" %(result[0],result[1],result[2])) #strike, ball, out 출력
        
        if result[0] == 3 :  # 성공시 실행
            print("오~ 좀 하는 구먼.. %d번만에 맞히다니...다음에 다시 도전하도록 하죠 형님;;" %h)
            return
        
        else :  # 10번 이내에서 실패시 재실행
            print("10번의 기회 중 %d번째 기회를 써버렸어.." %h)
            print()

    print("기회를 모두 써버렸느니라!")
    print("미개한것... 더 수련하고 오너라... 답은 %d%d%d였느니라~" % (answer[0],answer[1],answer[2])) # 최종 실패시 결과 공개
    return





go=input('컴퓨터의 도전장을 받아들이시겠습니까? (Y/N) ')     # 위의 조건을 다 읽고 시작버튼을 누르는 느낌?
while go=='Y' or go=='y' :
    time.sleep(SLEEP_TIME)
    print('그럼 시작합니다~~\n')
    gostage()
    go=input('다시 ㄱㄱ? (Y/N) ')
else :
    print('쫄았네.. ㅂㅂ')
