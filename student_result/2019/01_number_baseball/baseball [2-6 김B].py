#2606 김태웅
import random #난수를 생성하여 임의로 정답을 만들기 위해 필요


ANS_LEN=3 #정답의 길이
MAX_ATTEMPT=10 #최대 시도 가능 횟수 


def generate_ans(digits):
    """
    정답을 생성하는 함수
    매개변수 : digits를 통해 생성할 정답의 자리수를 넘겨받음
    리턴값 : 중복을 허용하지 않는 임의의 0~9사이 숫자로 구성된 문자열
    """
    nums=list(range(10)) #중복 방지를 위해 미리 리스트에 0부터 9까지의 숫자 생성
    random.shuffle(nums) #리스트의 순서를 섞어줌
    rand_num=''
    for i in range(digits): #digits만큼의 숫자를 뽑아줌
        rand_num+=str(nums[i])
    return rand_num


def hint(guess, ans):
    """
    입력값에 대한 힌트를 제공하는 함수
    매개변수 : guess는 사용자 입력값, ans는 정답을 뜻함
    리턴값 : 정답인 경우 "정답!"을 출력, 그렇지 않은 경우 S,B,O값을 형식과 함께 리턴
    """
    if guess == ans: #정답인 경우
        return '정답!'

    strike = 0
    ball = 0
    out = 0

    for i in range(len(guess)):
        if guess[i] == ans[i]: #위치와 값이 둘다 맞는 경우 : S
            strike+=1

        elif guess[i] in ans: #값은 존재하지만 위치가 다른 경우 : B
            ball+=1

        else: #둘 중 어느 것도 아닌 경우 : O
            out+=1

    return str(strike) + 'S' + str(ball) + 'B' + str(out) + 'O\n'


def isNotRight(data):
    """
    사용자 입력값의 오류를 찾아내는 함수
    매개변수 : 사용자 입력값
    리턴값 : 형식에 맞으면 False, 그렇지 않으면 True 리턴
    """
    if data == ' ': #아무것도 없는 경우
        return True

    elif len(data) != ANS_LEN: #문자의 길이가 다른 경우
        return True

    elif data[0] == data[1] or data[0] == data[2] or data[1] == data[2]: #길이는 3이나 중복되는 문자가 존재하는 경우
        return True
    
    elif data.isdecimal() == False: #숫자가 아닌 문자가 포함된 경우
        return True

    else: #올바른 입력일 때
        return False


def replayInput(input):
    """
    리플레이 유무 입력 과정에서의 입력오류를 찾아내는 함수
    매개변수 : 사용자 입력값
    리턴값 : 형식에 맞으면 False, 그렇지 않으면 True 리턴
    """
    if input=='Y' or input=='N': #올바른 입력일 때
        return False

    else: #Y, N이외의 문자가 입력된 경우
        return True


print("<숫자 야구 게임>")
print("3자리의 임의의 숫자를 맞추는 게임\n")
print("="*70+"\n")
print("규칙")
print("사용되는 숫자는 0~9까지 서로 다른 숫자")
print("숫자와 위치가 모두 맞으면 스트라이크 (S)")
print("숫자는 맞지만 위치가 틀리면 볼 (B)")
print("숫자와 위치가 모두 틀리면 아웃 (O)")
print("단, 무엇이 볼이고 스트라이크인지 알 수 없음\n")
print("="*70)

#메인루프 실행
while True:
    ans = generate_ans(ANS_LEN) #답 생성
    print('\n숫자를 입력하십시오. 총 %s번의 기회가 주어집니다.' % MAX_ATTEMPT)
    attempts=1 #시도 횟수를 저장하는 객체

    while attempts <= MAX_ATTEMPT:  #최대 시도 횟수 초과 전까지
        guess=' '   #사용자 입력값을 저장하는 객체

        while isNotRight(guess):   #입력값이 제대로 입력될 때까지 반복
            print('%s번째 기회 :' % attempts)
            guess=input()

        print(hint(guess, ans)) #힌트 정보 출력
        attempts+=1

        if guess == ans: #정답인 경우 리플레이 여부를 붇는 코드로 이동
            break

        if attempts > MAX_ATTEMPT:
            print('기회를 모두 사용하셨습니다. 답은 %s 이었습니다.' % ans)

    res=' ' #리플레이 여부 입력값을 저장할 객체
    print("다시 플레이하시겠습니까? Y 또는 N을 입력하십시오.")
    res=input()

    while(replayInput(res)): #입력이 제대로 이루어지지 않은 경우
        print("올바르지 않은 입력입니다. Y 또는 N을 입력하십시오.")
        res=input() #재입력

        if replayInput(res) == False: #다시 올바른 값이 입력되면 while문 탈출
            break

    if res == 'N': #입력이 N인 경우 프로그램 종료
        break