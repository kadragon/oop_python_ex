import random

def answer():
    '''
    랜덤의 숫자로 이루어진 3만큼의 문자열을 반환해주는 함수이다. 이 3자리 숫자는 한 게임에서 사용자가 맞추어야할 숫자이다.
    :return: 중복되지 않고 각 자리가 0~9중 랜덤값으로 이루어진 문자열
    '''
    n = list(range(10)) # range() 함수의 반환형은 iterator 형식의 객체 / list() 를 이용하여 list 형으로 변경
    random.shuffle(n) # list인 n 내부의 값들을 임의의 순서로 섞어준다.
    num = ''
    for i in range(3):  # 숫자길이인 3 만큼 반복하며 길이3의 문자열 num을 만듬 / 이렇게 만들경우 중복이 생기지 않는다.
        num += str(n[i])
    return num

def choosinglife():
    """
    사용자가 맨처음에 정하는 목숨의 개수를 입력받고 반환한다. 여기서 목숨의 개수는 양의 정수로 입력될때만 반환되게 한다.
    :return: 입력받은 양의 정수인 목숨의 개수(MAX_LIFE)문자열을 정수로 변환시킨 MAX_LIFE_n
    """
    while 1: #return이 안됬다면(MAX_LIFE가 숫자로만 안이루어졌을 때) 계속 반복
        print("=" * 80)
        MAX_LIFE = input('먼저 목숨을 몇개 가질지 정해주세요 : ') #사용자가 목숨의 개수를 입력한다. (문자열로)
        if MAX_LIFE.isdigit():                               #문자열이 숫자로 이루어졌을때만 if조건을 통과시켜주는 함수 .isdigit()을 사용하였다.
            print("숫자를 %s번 안에 맞춰주세요" % MAX_LIFE)
            print("=" * 80)
            MAX_LIFE_n = 0
            for k in MAX_LIFE:   #반복문을 사용하여 정수형인 MAX_LIFE_n에 한자리씩 MAX_LIFE의 값들을 대응시킨다. / 문자열'123'-->숫자 123, '092'-->92
                MAX_LIFE_n *= 10
                MAX_LIFE_n += int(k)
            if MAX_LIFE_n == 0:  #MAX_LIFE_n이 0일때는 게임이 바로 끝나게 된다.
                print("\n목숨이 없으면 게임이 바로 끝납니다ㅜㅜ\n")
            if MAX_LIFE_n >= 100: #MAX_LIFE_n이 100보다 크면 되긴 되지만 게임이 너무 길어지니 목숨이 100이상이 안되게 하였다.
                print("욕심이 너무 많네요 목숨 10개만 드리겠습니다")
                MAX_LIFE_n = 10
            return MAX_LIFE_n
        else:
            print('목숨개수는 양의 정수로 입력해주세요')  #목숨 개수를 0이나 양의 정수로 이루어지지 않게 입력했다면 출력되는 메세지

def isitright(n):
    """
    사용자가 숫자를 맞추려고 입력한 것(n)이 게임 조건에 맞는 3자리 정수인지 확인시켜주는 함수이다.
    :param n: 사용자가 입력한 값
    :return: 사용자가 입력한 값이 세자리 정수면 True, 아니면 False
    """
    if n.isdigit():  #n이라는 문자열이 숫자로만 이루어져있을때만 if조건을 통과시켜주는 함수 .isdigit()을 사용하였다.
        if len(n)==3:  #n이라는 문자열의 길이가 3일때만 if조건 통과
            return True
        else:
            return False
    else:
        return False

def makingsbo(guess, num):
    """
    사용자가 입력한 값과 맞추어야하는 값을 비교하여 strike, ball, out 값을 판정하여 출력, 만약 사용자가 입력한 값과
    맞추어야하는 값이 일치한다면 축하메세지를 출력하고 True를 반환
    :param guess: 사용자가 숫자를 맞추려고 입력한 3자리 숫자의 문자열
    :param num: 사용자가 맞추어야하는 중복되지 않는 3자리 숫자의 문자열
    :return: 만약 guess와 num이 같다면 'True'를 반환한다.
    """
    count_strike = 0
    count_ball = 0
    count_out = 0
    if guess == num: #사용자가 숫자를 정확히 맞추었을 때
        print("\n잘했어요!!\n")
        return True
    else:
        for i in range(3): #guess가 3자리 문자열이니 3번반복하며 guess의 숫자들을 모두 분석한다.
            if guess[i] == num[i]: #guess와 num의 i번째 숫자가 자리와 값이 모두 같을 경우 strike+1
                count_strike += 1
            elif guess[i] in num: #guess의 i번째 숫자가 num문자열 안에 들어있지만 자리가 같진 않을때 ball+1
                count_ball += 1
            else:                 #위에 두가지 경우가 모두 아닐 때(guess의 i번째 숫자가 num에 없다) out+1
                count_out += 1
        print('%d S| %d B| %d O' % (count_strike, count_ball, count_out)) #S,B,O결과 출력

def ending():
    """
    사용자가 숫자를 맞추거나 목숨을 다써서 게임 한판이 끝났을 때 사용자에게 게임을 재시작할건지 종료할건지 선택하게 하는
    함수
    :return: 사용자가 게임을 종료한다면 False, 게임을 다시 시작하겠다고 하면 True
    """
    while 1: #return이 안됬다면(질문에 yes,no로 대답안했을 때) 계속 반복
        print("=" * 80)
        a=input('게임을 다시 하시겠습니까? (yes or no)') #a는 첫번째 질문에 대해 사용자가 입력한 것
        if a == 'no':                                   #사용자가 게임을 다시 안하겠다고 했을 때
            while 1: #return이 안됬다면(질문에 yes,no로 대답안했을 때) 계속 반복
                b = input('\n정말 이 게임을 종료시키겠습니까? (yes or no)') #b는 두번째 질문에 대해 사용자가 입력한 것
                if b== 'yes':                                   #사용자가 정말 이 게임 종료하겠다 했을 때 False 반환
                    return False
                elif b== 'no':        #사용자가 아까 no를 잘못눌렀거나 사실 이 게임을 종료하기 싫다고 했을 때 True 반환
                    return True
                else:                        #사용자가 질문에 yes, no로 대답 안했을 때
                    print("똑바로 대답합시다")
        elif a=='yes':                      #사용자가 게임을 다시 하겠다고 했을 때
            return True
        else:                               #사용자가 질문에 yes, no로 대답 안했을 때
            print("똑바로 대답합시다")


print("="*80)
print("제가 중복되는 숫자가 없는 세자리 숫자를 생각해보았습니다. 한번 맞춰보세요")
print("숫자와 위치가 모두 맞으면 스트라이크(S), 숫자는 맞지만 위치가 틀리면 볼(B), 숫자와 위치가 모두 틀리면 아웃(O)입니다")

while 1:
    MAX_LIFE = choosinglife()   #choosinglife 함수에서 반환한 사용자가 정한 목숨개수(정수형) = MAX_LIFE
    attempt = 1                 #사용자가 숫자 맞추려고 시도한 횟수
    num = answer()              #num은 사용자가 맞추어야하는 3자리 숫자
    while attempt <= MAX_LIFE:  #목숨보다 시도 횟수가 작거나 같을 때 계속 반복
        print('\n당신의 목숨은 %d개 남았습니다' % (MAX_LIFE-attempt+1))  #현재 남은 목숨 개수는 목숨-시도횟수+1이다.
        guess = input('당신이 생각하는 세자리 숫자를 입력하세요!') #사용자가 숫자 맞추려고 입력
        if isitright(guess) == True:         #사용자가 입력한 것이 게임 조건에 맞는 3자리 정수인지 판단해서 3자리 정수가 맞다면,
            s = makingsbo(guess, num)        #guess와 num이 같다면 s는 True, 아니면 s에 값이 반환이 안된다.
            if s == True:                    #guess와 num이 같다면 게임 종료
                break
            attempt += 1                     #시도횟수 1증가
            if MAX_LIFE - attempt+1 == 0:    #현재남은 목숨이 0이 되면 메세지와 함께 while조건 벗어나며 게임종료
                print("\n실패하였습니다ㅜㅜ\n")

        else:                               #사용자가 3자리 정수말고 다른 것을 입력하였을 때
            print("제대로 입력해주세요ㅜㅜ")
    a = ending()               #한 게임이 끝났으니 사용자에게 게임을 다시할 것인지 종료할 것인지 선택하게 하는 함수 실행
    if a== True:               #사용자가 게임을 다시 한다고 하였을 때
        continue
    else:                      #사용자가 게임을 종료한다고 하였을 때
        break
print("안녕히가세요^^")        #이 메세지뜨면서 게임종료