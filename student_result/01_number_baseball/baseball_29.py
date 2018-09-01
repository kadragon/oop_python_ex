import random

def get_random_number(): #문자형으로 이루어진 임의의 N자리 숫자 반환
    number=list(range(10)) #임의의 숫자 리스트 생성
    random.shuffle(number) #숫자리스트 섞기
    str(number) #문자형으로 변환
    secret_number = [] #secret_number를 리스트형으로 선언
    for i in range(N):
        secret_number.append(number.pop()) #임의의 N자리 수를 리스트로 생성
    return secret_number #secret_number 반환

def different(num): #숫자 num중 겹치는 수의 유무
    for ic in range(N):
        for jc in range(N):
            if ic != jc and num[ic] == num[jc]:
                return False
    return True

def judge_play(k): #k의 정수형 판단과 범위 판단
    if k.isdigit() == False: #k의 정수형 판단
        return False
    elif int(k)<1 or int(k)>10: #k의 범위 판단
        return False
    else:
        return True

def judge(number): #number(list형)의 문자길이와 정수형 판단
    if len(number) != N: #number의 문자길이 판단
        return False
    if number.isdigit() == False: #number의 정수형 판단
        return False
    else:
        return different(number) #different 함수 호출

def strike(host,custom): #strike 수 찾기
    count1=0
    for ist in range(N):
        if host[ist] == int(custom[ist]): #추측한 수와 같은 위치에 동일한 숫자가 있을 시 count1에 +1
            count1 += 1
    return count1

def ball(host,custom): #ball 수 찾기
    count2=0
    for ib in range(N):
        for jb in range(N):
            if ib != jb and host[ib] == int(custom[jb]): #추측한 수와 동일한 숫자가 있을 시 count2에 +1 단, 같은 위치에 있으면 strike임으로 같은 위치는 제외
                count2 += 1
    return count2

while True:
    turn=1
    print("how many balls do you want?")
    N=input() #플레이 할 공의 개수 입력
    while judge_play(N)==False: #judge_play함수 호출
        print('You have to play only 1~10')
        N=input()
    N=int(N)
    secret = get_random_number() #get_random_number함수 실행
    while turn<=10:
        print('guess %d:' % turn)
        guess=input()
        while judge(guess) == False: #judge함수 호출
            print('guess again.')
            guess = input()
        if strike(secret,guess)!=N: #모두 strike이면 게임 종료
            print('%dS | %dB' % (strike(secret,guess),ball(secret,guess)))
        else:
            print('win!')
            break
        turn+=1 # 턴 증가
    if turn == 11: # 10턴을 넘겨버리면 턴 종료
        print('lose...\nthe answer was ',end='')
        for item in secret: #정답 호출
            print(item,end='')
    if input('\nDo you want to play again? (yes or no): ').lower().startswith('y') == False: #사용자로 부터 값을 입력 > 소문자로 변환 > 만약 'y' 로 시작하는 문자열이라면 True, 아니면 False
        break