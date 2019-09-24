import random

def make_num(num):
    """
    처음에 몇 자리수로 게임을 진행할 지 정해줌
    :param num: 입력
    :return: 입력값의 형식이 옳다면 게임을 진행할 자리수
    """
    num_cnt = 0

    for i in num:
        if '3' <= i <= '6':
            num_cnt += 1
            b = int(i)
    if num_cnt != 1 or len(num)!=1:
        return -1
    else:
        return b

def explain_rule():
    """
    규칙을 설명해줌
    """
    print("<설명>")
    print("숫자야구게임은 랜덤의 숫자를 주어진 힌트들을 바탕으로 추리해내는 게임입니다!")
    print("3~6자리수 중 원하는 자릿수로 플레이할 수 있습니다. 정답은 서로 다른 숫자들로 이루어진 수입니다.")
    print("기회는 오직 10번입니다. 다음은 단서들의 의미입니다.")
    print("S는 자리와 숫자가 정확히 일치하는 것입니다.")
    print("B는 자리는 맞지 않지만 같은 숫자가 존재하는 것입니다.")
    print("O는 숫자가 맞지 않는 것입니다.")
    print("그럼, 건투를 빕니다.")

def set_randnum(num):
    """
    사용자가 선택한 자릿수의 임의의 숫자를 생성함.
    :param num:
    :return: 중복되지 않은 숫자로 이루어진 문자열
    """
    numbers = list(range(10))
    random.shuffle(numbers)
    ans = ''
    for i in range(num):  # 사용자가 선택한 (num)자릿수로 제작
        ans += str(numbers[i])
    return ans

def check_input(guessstr,num):
    """
    입력값의 형식이 틀렸다면 왜 틀렸는지 설명해주고, 옳다면 다음 단계로 넘어가도록 함
    :param guessstr: 입력값의 형식이 옳은지 판단해줌
    :param num: 정답의 자릿수
    :return: 입력값의 형식이 옳은지의 여부
    """
    check=[0]*10

    isok=1
    for i in guessstr: # 0에서 9 사이의 숫자가 입력되었는지 확인
        if i==' ':
            print("감독의 말: 띄어쓰기를 제외해!")
            isok=0
            break
        elif not '0'<=i<='9':
            print("감독의 말: 입력 형식이 옳지 않아!")
            isok=0
            break
        elif check[int(i)]==1:
            print("감독의 말: 중복된 숫자가 있어서는 안된다!")
            isok=0
            break
        if check[int(i)]==0:
            check[int(i)]=1

    if len(guessstr)!=num and isok==1: # 설정한 자릿수가 맞는지 확인
        isok=0
        print("감독의 말: 설정한 자릿수를 초과하였어!")

    return isok

def check_clue(guess, ans, num):
    """
    주어진 입력이 실제 정답과 같다면 맞다는 것을 표현해주고, 틀렸다면 S, B, O로 단서를 제공해줌
    :param guess: 추리한 입력값
    :param ans: 실제 정답
    :param num: 자릿수
    :return: Strike, Ball, Out의 개수
    """
    strike = 0
    ball = 0
    out = 0
    for i in range(num):
        if guess[i]==ans[i]:
            strike+=1
        elif guess[i] in ans:
            ball+=1
        else:
            out+=1
    if strike == num: # 정답!
        return '스트ㅡㅡㅡ라이크!!'
    return '%d S  %d B  %d O' %(strike,ball,out)

def try_again():
    """
    사용자가 다시 게임을 진행할 것인지 물어보고 다시 시작함
    :return: 다시 시작하는지의 여부
    """
    while True: # 올바른 입력값이 들어올 때까지
        print("다시 하시겠습니까?(다시 하려면 Y, 아니면 N)")
        trystr=input()
        if trystr=='Y':
            isok=1
            break
        elif trystr=='N':
            isok=0
            break
        print("트와이스: 둘 중에 하나만 골라~")

    return isok


while True:
    print("9회 말 2사 만루. 당신의 공에 모든 것이 달려 있는 절체 절명의 상황!")
    print("당신은 놀라운 추리력으로 상대 타자의 스윙 방향을 담은 숫자를 추리하려고 한다.")
    print()
    explain_rule()
    print()
    print("---------------Settings---------------")
    while True:
        print("몇 자리 수로 게임을 진행하시겠습니까?(3~6자리)")
        num = make_num(input())
        if 3 <= num <= 6:
            break
        print("3~6자리로 선택해주세요!!")
    print(num, "자리수로 선택하셨습니다.")
    print("--------------------------------------")
    print("Game Start!")

    ans = set_randnum(num) #숫자를 설정함
    heart = 10  # 목숨은 처음에 10개이다.

    while heart > 0:
        print("목숨이 %d개 남았습니다." % (heart))
        while True:
            print("%d 자리수를 입력하세요." % (num))
            guess=input()
            if check_input(guess,num)==True: #추리한 값을 검사한다.
                break
        clue=check_clue(guess, ans, num)
        print(clue)
        if clue=='스트ㅡㅡㅡ라이크!!':
            break
        heart-=1

    if heart == 0: # 정답을 맞추지 못함
        print("정답은 %s였다. 당신의 직구는 상대 타자에게 정확히 들어맞아 홈런으로 이어졌다..." %(ans))

    else: # 정답을 맞춤
        print("삼진 아웃! 심판의 스트라이크 판정과 함께 경기장에는 환호성이 터져나왔다. 당신의 마무리로 팀은 승리의 트로피를 거머쥐게 되었다.")

    if try_again() == False: # 더 이상 실행하지 않음
        print("게임을 종료합니다.")
        break
    else: # 게임을 반복함
        print("""게임을 다시 시작합니다 
              
              
              
             """)