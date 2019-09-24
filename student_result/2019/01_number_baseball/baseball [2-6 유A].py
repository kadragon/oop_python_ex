# 임의의 key값을 만들기 위해
import random

def make_key(digit): # key 값을 만드는 함수
    num=list(range(10)) # 0~9까지의 숫자를 갖는 리스트를 만든다
    random.shuffle(num) # 0~9를 랜덤으로 섞는다
    key=''
    if num[0] == 0: # 0으로 시작하면 세 자리수가 아니므로 바꿔준다
        num[0] = num[digit]
    for i in range(digit): # 설정한 자리수 만큼 숫자를 리스트에서 가져온다
        key += str(num[i]) # key를 만든다

    return key # key를 리턴한다

def result(user_input, key): # strike, ball, out을 판정 하는 함수 , user_input은 사용자의 입력값

    if user_input == key: # 사용자가 입력한 값이 key 값과 같으면 You won the game! 을 리턴한다
        return 'You won the game!'

    cnt_strike=0 # strike 인 경우 개수 세기
    cnt_ball=0 # ball 인 경우 개수 세기
    cnt_out=0 # out 인 경우 개수 세기

    for i in range(len(user_input)):
        if user_input[i] == key[i]: # strike 인 경우
            cnt_strike += 1
        elif user_input[i] in key: # ball 인 경우
            cnt_ball += 1
        else: # out 인 경우
            cnt_out += 1

    return str(cnt_strike) + ' strike, ' + str(cnt_ball) + ' ball, ' + str(cnt_out) + ' out\n' # strike, ball, out 결과 리턴

def correct_input(x): # 사용자가 정확하게 입력했는지 확인하는 함수

    if x==' ': # 비어있으면 False를 리턴한다
        return False

    for i in x: # 입력에 0~9 까지의 숫자 이외의 문자가 있으면 False를 리턴한다
        if i < '0' or i > '9':
            return False

    for i in range(0,len(x)): # 사용자의 입력에 중복되는 숫자가 있으면 False를 리턴한다
        for j in range(0,len(x)):
            if i != j:
                if x[i] == x[j]:
                    return False

    return True


def play_again(): # 다시 플레이 할 지를 판단하는 함수

    return input('Do you want to play again? (y / else)').lower() == 'y' # y가 입력되면 True를 리턴하고 그 이외에는 False를 리턴한다


digit = 3 # 자리수
max_chance = 10 # 최대 시도 가능 기회

# 규칙 설명
print("=" * 70)
print("I am thinking of a %s-digit number. Try to guess what it is." % digit)
print("Here are rules:")
print("When I say:  That means:")
print("Strike : One digit is correct and in the right position.")
print("Ball : One digit is correct but in the wrong position.")
print("Out : No digit is correct.")
print("Each digit is different.")
print("You can't start with number 0.")
print("=" * 70)


while True:

    answer_key = make_key(digit) # key 생성
    print('\nI have thought up a number. You have %s chances to get it.' % max_chance)

    guess_chance = 1 # 시도한 횟수를 알려주는 변수

    while guess_chance <= max_chance: # 시도한 횟수가 최대로 주어진 기회 이하이면 실행
        guess=' ' # 사용자의 입력값을 저장하는 변수
        while len(guess) != digit or not correct_input(guess): # 자리수가 맞고 0~9 사이의 숫자가 입력되었는지 확인

            print('Guess #%s:' % guess_chance, end=' ')
            guess = input() # 사용자 입력

            if len(guess) != digit or not correct_input(guess): #자리수가 틀리거나 0~9 사이의 숫자가 입력되지 않은 경우
                print('You have to guess %s-digit number with each digit is different!' % digit) # 올바른 입력방법을 알려줌


        print(result(guess, answer_key)) # 결과(strike, ball, out) 출력
        guess_chance += 1 #시도한 횟수 1증가

        if guess == answer_key: # 정답일 경우 break
            break

        if guess_chance > max_chance: # 시도한 횟수가 주어진 기회를 넘을 경우
            print('You lost the game. The key was %s.' % answer_key) # 틀렸을 경우 정답을 알려준다

    if not play_again(): # 다시 플레이 하고 싶지 않다면
        break # break