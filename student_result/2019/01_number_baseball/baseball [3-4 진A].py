NUM_LENGTH = 3  #정답의 길이
MAX_TRY = 10  #최대 시도 횟수

import random

def generate_unknown_number(NUM_LENGTH):
    number = list(range(0,10))  #정답에 들어갈 수 있는 숫자
    random.shuffle(number)  #랜덤으로 숫자 조합하기
    unknown_number = ''
    for i in range(NUM_LENGTH): #같은 숫자가 중복이 되지 않도록 하는 방법
        unknown_number += str(number[i])
    return unknown_number #랜덤으로 만들어진 NUM_LENGTH자리 수 반환

def error_check(guess_number):
    if len(guess_number) == 0: #공백이 입력되었을 때
        print("수가 입력되지 않았습니다.")
        return False

    for i in guess_number: #숫자 외에 문자나 특수기호 등이 입력되었을 때
        if i not in {'0','1','2','3','4','5','6','7','8','9'}:#정수가 아닌 문자로 저장
            print("숫자 외에 문자나 공백, 특수기호 등은 입력하실 수 없습니다.")
            return False

    if len(guess_number) != NUM_LENGTH: #NUM_LENGTH가 아닌 자리수의 수가 입력되었을 때
        print("현재 %d자리의 수가 입력되었습니다. %d자리의 수를 다시 입력해주세요." %(len(guess_number), NUM_LENGTH))
        return False

    return True

def offer_hint(unknown_number, guess_number, time_tried):

    if unknown_number == guess_number:
        print("정답입니다! %d번만에 정답을 맞추는 데 성공하셨군요!" %(time_tried))
        return True #게임이 끝났음을 의미
    if time_tried == MAX_TRY:
        print("아쉽지만 정답을 맞추는 것에 실패하셨습니다. 정답은 %s이었습니다."%(unknown_number))
        return True #게임이 끝났음을 의미
    print("아쉽지만 %s는 정답이 아닙니다." %(guess_number))
    print("%d번 째 힌트는 다음과 같습니다." %(time_tried))
    strike = 0 #strike 개수 초기화
    ball = 0 #ball 개수 초기화
    out = 0 #out 개수 초기화

    for i in  range(NUM_LENGTH): #strike, ball, out 개수 구하기
        if unknown_number[i] == guess_number[i]:
            strike += 1
        elif guess_number[i] in unknown_number:
            ball += 1
        else:
            out += 1

    print("strike: %d ball: %d out: %d" %(strike, ball, out)) #힌트 출력
    return False #게임이 끝나지 않았음을 의미

def one_more_game(tried_number):
    print("한 게임 더 하시겠습니까? 과도한 게임은 플레이어분을 게임 중독에 빠지게 할 수 있습니다.")
    print("게임을 추가로 더 하고 싶다면 YES를, 그만하고 싶다면 NO를 입력해주세요.")
    print("YES와 NO외에 다른 값을 입력하시면 간만에 쓴 뇌가 과부화에 걸린 것으로 간주하고 게임을 종료하겠습니다.")
    play_again = str(input()) #플레이어의 추가 게임 의사 입력

    if play_again == 'YES':
        if tried_number > 8:
            print("벌써 %d판 째 입니다. 뭐든지 과한 건 좋지 않아요." %(tried_number+1))
        return True #게임 계속하기
    elif play_again == 'NO':
        print("잘 생각하셨습니다. 오늘은 이걸로도 충분해요.")
        return False #게임 끝내기
    else:
        print("플레이어분의 상태를 보니 오늘은 그만하는게 좋을 것 같군요.")
        return False #게임 끝내기

tried_number = 1 #게임 시행 횟수
play = True #게임을 계속 진행할지에 대한 여부

while play:
    print("="*80)
    print("지금 제가 생각하고 있는 %d자리 수를 맞혀보세요." %(NUM_LENGTH))
    print("첫번째 숫자가 0일수도 있습니다.")
    print("맞출 수 있는 기회는 총 %d번 입니다" %(MAX_TRY))
    print("한 번 시도할 때마다 정답여부와 힌트를 알려드립니다.")
    print("힌트는 strike:  ball:  out:  의 형태로 주어집니다.")
    print("strike는 숫자와 위치가 모두 일치하는 숫자의 개수,")
    print("ball은 숫자는 일치하지만 위치는 일치하지 않는 숫자의 개수,")
    print("out은 정답에 포함되어 있지 않은 숫자의 개수를 의미합니다.")
    print("="*80)

    finish = False #하던 게임이 끝냈는지에 관한 여부

    while finish == False:
        unknown_number = generate_unknown_number(NUM_LENGTH)
        time_tried = 1 #정답을 맞추는 시도를 한 횟수

        while time_tried <= MAX_TRY: #최대 시도 횟수를 넘지 않았을 때까지 실행
            print("%d자리 수를 입력해주세요" %(NUM_LENGTH))
            guess_number =input() #예측한 정답 입력
            while not error_check(guess_number): #오류없이 입력될때까지 실행
                guess_number = input() #수를 문자열로 입력받음

            if offer_hint(unknown_number, guess_number, time_tried): #하던 게임이 끝났을 때
                if one_more_game(tried_number): #플레이어 게임을 더 하고 싶어할 때
                    tried_number += 1 #게임 플레이 횟수 증가
                else:
                    play = False #게임을 끝내기
                finish = True #현재 하던 게임은 끝났음을 의미
                break
            else:
                print("현재 총 %d번의 기회 중 %d번의 기회를 사용하여 %d번의 기회가 남아있습니다." %(MAX_TRY, time_tried, MAX_TRY-time_tried))
                time_tried += 1 #정답 시도 횟수 증가