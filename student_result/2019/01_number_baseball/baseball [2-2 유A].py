import random  # 3자리의 정답을 생성할 때 랜덤하게 생성해야 하기 위함


def createnum():
    """
    3자리의 정수, 즉 게임에서의 정답이 되는 수를 랜덤으로 생성하는 함수
    :return: 중복되지 않은 숫자로 이루어진 3자리의 문자열
    """
    ans = list(range(10))  # range() 함수의 반환형은 iterator 형식이므로, list 형으로 변형하여 0~9까지의 수가 들어간 list 만듬
    random.shuffle(ans)  # 임의의 값으로 이루어진 3자리 정수를 반환해야 하므로 list의 값을 임의로 섞음
    ansnum = ''
    for i in range(3):  # 3자리의 정수로 된 문자열을 만듬
        ansnum += str(ans[i])
    return ansnum  # 3자리의 정답 문자열 반환


def comparenum(num, answer_num):
    """
    사용자가 입력한 입력값과 정답을 비교해서 s,b,o를 판정하고 출력해주는 함수
    :param: num: 사용자가 입력한 예상값
    :param: answer_num: 이전의 createnum 함수에서 생성한 정답
    comparenum 함수 자체에서 출력하도록 코딩해 반환값은 존재하지 않도록 함
    """
    s = 0  # strike 인 경우를 세 주는 변수
    b = 0  # ball   인 경우를 세 주는 변수
    o = 0  # out    인 경우를 세 주는 변수
    for i in range(3):
        if num[i] == answer_num[i]:  # strike 인 경우
            s += 1
        elif num[i] in answer_num:  # ball 인 경우
            b += 1
        else:  # out 인 경우
            o += 1
    print('S:%d B:%d O:%d' % (s, b, o))  # s,b,o 판정값을 함수 내에서 출력해줌


def check(guess):
    """
    사용자가 입력한 입력값이 세 자리의 정수로 이루어진 옳은 입력인지 판단함
    :param: guess: 사용자가 입력한 예상값
    :return: 3자리의 정수로 이루어진 옳은 예상값일 경우 True, 아닐 경우 False
    """
    if len(guess) == 3:  # 입력값이 3자리의 문자열인지 파악
        for i in range(3):
            try:  # 문자열의 각 자리의 수가 0~9까지의 수인지 파악
                if 0 > int(guess[i]) or int(guess[i]) >= 10:
                    return False
            except ValueError:  # 입력에서 수가 아닌 문자 등이 입력되었을 때의 ValueError를 방지
                return False
            if guess[(i + 1) % 3] == guess[i % 3]:  # 각 자리가 모두 다른 세 정수로 이루어졌는지 파악
                return False
        return True  # 모든 조건을 통과하였을 경우 True 반환


def replay():
    """
    게임이 종료되었을 경우 다시 게임을 플레이 할지 판단하는 함수
    :return: '네'가 입력되었을 경우 True, '아니요'가 입력되었을 경우 False
    """
    print("다시 한 번 플레이하시겠어요?, '네' 혹은 '아니요'로 대답해주세요!")
    while True:
        replay = input()  # 다시 플레이할지 여부를 입력
        if replay == '아니요':  # '아니요'인 경우 False 반환
            return False
        elif replay == '네':  # '네'인 경우 재시작을 위해 "="로 구분해 준 후 True 반환
            print("=" * 80)
            return True
        else:  # 다른 값이 입력된 경우 재입력을 위해 문장 출력
            print("아니 말좀 들어요... '네' 혹은 '아니요'로 대답해달랬잖아요...")


print("=" * 80)
print("숫자 야구 게임에 오신 것을 환영합니다!!!")
print("으으으음... 세 자리 숫자가 하나 떠오르네요")
print("한번 맞춰 보시겠어요??")
print("힘드신가요?? 그럼 제가 손님의 입력에 따라서 힌트를 드리죠")
print("스트라이크(S): 숫자와 위치가 모두 맞은 경우")
print("볼(B): 숫자는 맞지만 위치가 틀린 경우")
print("아웃(O): 숫자와 위치가 모두 틀린 경우")
print("그럼 이제 3자리 숫자를 공백없이 입력해주세요, 그러면 힌트를 드릴게요!!")
print("힌트는 총 10번 기회를 드리죠!")
print("=" * 80)

while True:  # 게잉을 재시작하는 경우를 위해 전체를 while 문에 넣어 줌
    life = 10  # 예상을 할 수 있는 남은 기회를 저장하는 변수
    ans = createnum()  # creatnum 합수를 통해 3자리의 정답을 생성
    while life > 0:
        print("\n%d번째 예상은?: " % (11 - life), end='')
        guess = ''  # 사용자 입력을 저장하는 변수

        try:
            guess = input()  # 사용자로부터 입력을 받음
        except KeyboardInterrupt:  # 게임 중 python 프로그램을 종료하게 되면 일어나는 KeyboardInterrupt 오류를 방지
            print("\n\n게임을 강제종료합니다ㅠㅠ")
            break  # 종료하게 되면 다시 replay 함수를 통해 재시작 할 수 있음

        if ans == guess:  # 정답일 경우 게임을 종료
            print("정답입니다!! 오우 좀 하시는데요~~")
            break

        if check(guess):  # check 함수를 통해 입력값에 오류가 없는지 판단
            comparenum(guess, ans)  # comparenum 함수를 통해 s,b,o 여부 판정 및 출력
            life -= 1  # 입력값에 오류가 없어 s,b,o 판정한 후에는 기회 1 감소
        else:  # 입력값에 오류가 존재하는 경우
            print("하... 제대로 입력 안하면 힌트 안줄꺼에요... 다시 입력해요")

        if life == 0:  # 기회를 모두 사용한 경우
            print("\n10번이면 충분할 줄 알았는데... 게임 못하시네요... 정답은 %s 였어요" % ans)

    if not replay():  # 게임의 재시작 여부 판단해 False 인 경우 break 해 프로그램 종료
        break
