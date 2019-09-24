import random

#똑바로 입력했나 판단
def fin_check(a):
    if(a == 'y' or a == 'n'):
        return True
    return False

#입력값에 따라 게임 지속 여부 판단
#게임을 끝내겠습니까?
def which_func(a):
    if a == 'y':
        #아뇨
        return False
    else:
        #네
        return True

def make_func():
    #랜덤하게 0~9 나열 - 앞의 3개만 사용 예정
    lists = list(range(10))
    random.shuffle(lists)
    return lists

#숫자인지 확인하는 함수
def only_number(Guess_List, Ball_Numb):
    a = 0
    for i in Guess_List:
        if not (i == '0' or i == '1' or i == '2' or i == '3' or i == '4' or i == '5' or i == '6' or i == '7' or i == '8' or i == '9'):
            return False
    return True

def check(Guess_List, Ball_Numb):
    #입력한 값이 조건에 부합하나 확인
    #길이가 맞는지, 다 숫자가 맞는지 확인
    if(len(Guess_List) == Ball_Numb and only_number(Guess_List, Ball_Numb)):
        return True
    return False

def compare_func(Ans_List, Ball_Numb):
    #추정 입력값 받기
    a = 1
    #해당 while문에서는 입력을 받고, 잘못된 방법으로 값을 입력시 똑바로 할떄까지, 12번까지만 다시 시킵니다.
    while True:
        guess_list = input().split()
        #요기에서 check를 통해 확인합니다
        if not check(guess_list, Ball_Numb):
            a += 1
            print("똑바로 찍어")
        else:
            #문자로 입력받은 guess_list 이기에 정수 리스트로 바꿉니다(이러지 않으면 이후 비교가 힘듭니다)
            guess_list = list(map(int, guess_list))
            break
        if (a == 4):
            print('')
            print("너 대머리")
        if (a == 8):
            print('')
            print("너 친구들도 대머리")
        if (a == 12):
            print("접어 그냥")
            print("다 아웃")
            return 0, 0
    #확인하기
    #strike
    s = 0
    #ball
    b = 0
    #추정 값과 정답을 하나하나 대조
    for i in range(0, Ball_Numb):
        for j in range(0, Ball_Numb):
            #만약 대조한 값이 같을 때
            if Ans_List[i] == guess_list[j]:
                #자리도 같으면 스트라이크
                if i == j:
                    s += 1
                #자리는 다르면 볼
                else:
                    b += 1
    return s, b

def expl_rule(chance_numb):
    print('*' * 80)
    print("저는 0 ~ 9 까지의 숫자 중에서 세개의 숫자를 머릿속에 떠올렸습니다.")
    print("앞으로 %d번의 기회가 주어지며," %chance_numb)
    print("그 안에 제가 생각하는 숫자의 종류와 위치를 전부 맞추어야 승리할 수 있습니다.")
    print("시도를 한번 할때마다 추측이 답에 얼마나 근접했는지 알려드리겠습니다.")
    print("")
    print("strike는 당신의 추측에서 숫자의 '종류', 그리고 '위치'가 전부 맞은 추측의 개수입니다.")
    print("ball은 당신의 추측에서 숫자의 '종류'는 맞았으나, '위치'가 틀린 추측의 개수입니다.")
    print("out은 당신이 추측한 숫자 중 '위치', '종류'가 다 틀린 추측의 개수입니다.")
    print("이떄, '한 자리 숫자' 세개를 하나씩 '띄어쓰기로' 분리해서 입력하세요. 그렇지 않으면 화가 날 것 같습니다.")
    print("시작 하자마자 enter누르지도 말고요")
    print("계속 실수하시면 그에 합당한 저주가 있을 것입니다.")
    print("아무튼 행운을 빕니다.")
    print('*' * 80)

def IQ_Test(i):
    if i in range(1, 4):
        print("우와 정말 똑똑하다...       솔직히 찍은 거죠?")
    elif i in range(4, 6):
        print("음... 실력은 그럭저럭. 다시 시도해 보세요")
    elif i in range(6, 10):
        print("오늘 좀 상태가 안좋은 모양이네요... %d번은 좀 심했다." %i)
    elif i == 10:
        print("겨우 맞췄네요..")
    else:
        print("우와... 바보다... 다시 해도 안될 것 같으니까 포기하세요. 뭐... 그래도 예의상 묻기는 할게요.")

#추측하는 숫자의 개수와 시도 횟수 설정
#ball_numb는 수정할 수 없습니다.
ball_numb = 3
#chance_numb는 바꿀 수 있습니다.
chance_numb = 10
#규칙을 설명하는 함수
expl_rule(chance_numb)
#코드 시작!
while True:
    #사용한 기회를 저장하는 변수
    chance = 1
    #정답이 입력되는 리스트, 다만 이 리스트는 길이가 10이지만, 앞의 3개만 사용할 것입니다.
    ans_list = []
    #make_func에서 정답 랜덤 생성
    ans_list = make_func()
    #아래 주석을 제거하면 정답을 보고 플레이 할 수 있습니다.-앞 3 수가 답입니다.
    #print(ans_list)
    while True:
        #시도 횟수가 다 차면 끝내는 부분
        if chance > chance_numb:
            break
        #아래로는 s, b, o 계산 후 결과 산출
        print("%s번째 시도" %chance)
        S, B = compare_func(ans_list, ball_numb)
        O = 3 - S - B
        #스트라이크 3개면 만점
        if S == 3:
            print("정답!")
            break
        #그 외 결과
        else:
            print("strike = %s, ball = %s, out = %s" %(S, B, O))
        #시도 횟수 1 증가
        chance += 1
    #10 번 시도시
    if chance == chance_numb + 1:
        print("그만 해요 끝났어요")
        print("정답은 %d, %d, %d 였답니다." % (ans_list[0], ans_list[1], ans_list[2]))
    #지능을 판단하는 함수
    IQ_Test(chance)
    print("다시 하고 싶어요?")
    print("다시 하려면 y, 포기하려면 n   '글씨만' 입력하세요.")
    a = input()
    #입력 값이 y, n 이 아니면 강제 종료
    if not fin_check(a):
        print("쯧... 그냥 관두세요\n글씨를 못 읽는 사람인가..")
        break
    # n 이라고 입력해도 종료
    elif which_func(a):
        break