
import random

guess_length = 3 #추측할 숫자의 개수
TotalGuess = 10 #맞출 수 있는 기회의 수
guessTaken = 1

go_play = True
go_guessing = True
go_checking = False   #True일 경우 비교 시작
go_results = False
go_ask = False

def secret():
    '''
    numbers의 숫자들을 랜덤하게 섞음.
    guess_length만큼 secret_numbers를 생성.
    '''
    numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9] #섞어줄 숫자들
    secret_numbers = list(range(guess_length)) #게임에 사용할 3개의 숫자
    random.shuffle(numbers)
    
    for i in range(guess_length):
        secret_numbers[i] = str(numbers[i])
    print(secret_numbers)
    return secret_numbers

def start():
    print("<게임설명>")
    print('-'*80)
    print("제가 생각하고 있는 3개의 숫자를 맞춰주세요!")
    print("답을 중복되지 않은 3개의 숫자를 띄어쓰기로 구분하여 입력해주시면 됩니다.\n")
    print("    S(strike) : 위치와 숫자 모두 맞춘 갯수")
    print("    B(ball) : 숫자는 맞았으나 위치가 틀린 갯수")
    print("    O(out) : 숫자와 위치가 모두 틀린 갯수\n")
    print("위와 같이 알려주는 결과를 통해 숫자를 맞춰나가 보세요!")
    print('-'*80)

def guessing(secret_numbers):
    '''
    플레이어가 추측한 숫자를 입력받음.
    숫자 1개씩 띄어쓰지 않았을 경우, 숫자를 3개 입력하지 않았을 경우 다시 입력받음.
    '''
    guess_i = list(range(guess_length)) #플레이어가 추측한 숫자들
    go_guessing = True
    while go_guessing == True:
        guess_i = input('숫자를 입력해주세요 : ').split()
        x = 0
        for i in range(len(guess_i)):
            if len(guess_i[i]) != 1:
                print("다시 입력해주세요!")
                break
            else:
                x += 1
        if x == guess_length:
            go_guessing = False
        else:
            print("다시 입력해주세요!")

    return guess_i

def results(cnt_strike,cnt_ball,cnt_out):
    '''
    결과를 보여줌.
    '''
    print("Strike 갯수 : %d 개" % cnt_strike)
    print("Ball 갯수 : %d 개" % cnt_ball)
    print("Out 갯수 : %d 개" % cnt_out)
    
def checking(guess_i,secret_numbers):
    cnt_strike,cnt_ball,cnt_out = 0,0,0
    
    for i in range(guess_length):
        if guess_i[i] ==  secret_numbers[i]:
             cnt_strike += 1
        elif guess_i[i] in secret_numbers:
             cnt_ball += 1
        else:
             cnt_out += 1

    results(cnt_strike,cnt_ball,cnt_out)
    
    if cnt_strike == guess_length:
        print("앗 당신이 맞췄어요+_+")
    else:
        print("아쉽네요.. 한 번 더 시도해보세요!")
    return cnt_strike

def ask():
    '''
    게임을 다시시작할것인지 물음.
    Yes라고 대답시 다시 시작.
    '''
    answer = input("게잉을 다시 시작하시겠습니까? Yes / No : ")
    if answer == 'Yes':
        go_play = True
    else:
        go_play = False
    return go_play
            
while go_play == True:
    secret_numbers = secret()
    start()
    guessTaken = 1
    
    while guessTaken <= TotalGuess: #물어보고 확인하는 부분은 따로 빼서 돌려주자
        guess_i = guessing(secret_numbers)
        cnt_strike = checking(guess_i,secret_numbers)
        guessTaken += 1
        if cnt_strike == 3:
            break
    
    go_play = ask()
