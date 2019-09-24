import random  # 플레이어가 맞출 정답을 랜덤 생성하는 함수를 호출하기 위해


def line():  # 가독성을 위한 줄을 출력하는 함수
    print("*" * 80)


length = 3  # 문제에서 주어진 숫자의 길이
right = 0  # 정답을 맞추었는지 확인하는 변수
life = 10  # 기회의 초깃값


def dap_make(leng):  # 랜덤한 답을 지정된 자릿수에 따라 만들어 주는 함수
    ans = ''  # 만들어진 답을 저장할 변수
    while len(ans) != leng:  # 자릿수 만큼 생성될 때까지 반복
        i = random.randint(0, 9)  # 0~9 까지의 랜덤한 값
        i = str(i)  # 문자열로 전환하여 비교
        if i in ans:
            continue  # 중복된 값이 있으므로 추가하면 안됨
        else:
            ans += i  # 문자열에 추가
    return ans  # 만들어진 세자리의 문자열형 답을 리턴


# T. 변수명이 무슨 의미인지 직관적으로 다가오지 않음.
def check_num(needap):  # 입력된 값이 서로 다른 3 자리의 0 이상의 정수인지 확인하는 함수, 결과가 참이면 잘못된 입력
    if len(needap) != length:  # 자릿수가 우리가 정한 자릿수와 다르면
        return True
    try:  # 예외 처리
        int(needap)  # 정수형으로 변환 가능?
    except ValueError:  # 정수형이 아닌 문자가 섞여 있다면
        return True
    if needap[0] == needap[1] or needap[1] == needap[2] or needap[0] == needap[2]:  # 중복된 값이 있습니까?
        return True
    return False


def check_dap(needap, ans):  # 입력된 값, 만들어진 답을 비교하여 정답의 여부와 S, B, O 출력을 하는 함수
    s = 0
    b = 0
    o = 0  # S, B, O 초기화

    for i in range(length):  # 입력된 값, 만들어진 답의 길이는 length 이므로, 각 인덱스를 비교한다
        if needap[i] == ans[i]:  # 완전히 동일한가?
            s += 1
        elif needap[i] in ans:  # 정수가 만들어진 답 안에 있는가?
            b += 1
        else:  # 완전히 없는 정수인가?
            o += 1

    if s == 3:  # 맞춤
        print("정답입니다!")
        return True
    else:  # 틀림
        print("S:%s B:%s O:%s" % (s, b, o))  # S, B, O 출력
        return False


def bye():  # 재도전 여부를 묻는 함수
    print("재도전 하시겠습니까? yes / no")
    x = input()  # 입력 받기
    if x == 'yes':  # 재도전 희망
        print("재도전!")
        return True
    elif x == 'no':  # 재도전 X
        print("잘가용!")
        return False
    else:  # 'yes', 'no' 이외의 값들을 처리
        print("안할거라고 생각할게용 빠이~!")
        return False


# 기초적으로 유저에게 알려줄 게임의 규칙 설명
# 이 밑으로 메인 함수
line()
print("숫자야구게임에 오신걸 환영합니다... 당신은 %d자리 자연수를 맞추셔야 합니다! " % length)  # 맞출 자릿수를 알려줌
print("물론 힌트가 있습니다... 다음 힌트들을 잘 머릿속에 새겨두세요...")
line()
print("S는 스트라이크! 숫자와 자리가 모두 맞은 경우!")
print("B는 볼! 숫자는 있지만 자리가 틀린 경우!")
print("O는 아웃! 숫자가 아예 없는 경우입니다...")
print("그럼 건투를 빕니다, 아래쪽에 서로 다른 숫자 세 개를 띄어쓰기 없이 입력해 주세요!")
line()

while True:  # break가 아닌 이상 계속 반복한다
    life = 10  # 새롭게 시작되는 게임을 위해 목숨 초기화
    right = 0  # 새롭게 시작되는 게임을 위해 정답 변수 초기화
    dap = dap_make(length)  # 새롭게 시작되는 게임을 위해 정답 생성
    print("게임 시작...")

    while life >= 1 and right == 0:  # 목숨이 1개 이상 남았거나, 답을 맞추지 못했다면
        line()
        print("남은 목숨: %s개" % life)
        print("숫자를 입력해주세요...: ")
        yourdap = input()  # 유저의 답 입력 받기

        if yourdap == 'cheat':
            print("그런거 없음 ㅋ")
            line()
            continue
        elif check_num(yourdap):  # 올바르게 입력 했는지 확인
            print("똑바로 써라 핫산, 목숨은 받아가지")
            life -= 1  # 벌칙
            line()
            continue  # 바로 위의 while 문의 처음으로

        if check_dap(yourdap, dap):  # 유저의 답과 만들어진 답을 비교해 정답 확인
            right = 1  # 맞았으면 정답 변수 변경
        else:
            life -= 1  # 틀렸다면 벌칙
        line()

    if right == 0:  # 정답 변수가 초기화가 안된 채로 while 문을 빠져나옴 - 목숨을 전부 소비하고 맞추지 못함
        print("실패! 답은 %s였습니다..." % dap)

    if bye():
        continue  # 재도전 여부 질문
    else:
        break
