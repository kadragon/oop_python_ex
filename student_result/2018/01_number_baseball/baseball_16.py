import random

# 숫자 야구 길이와 최대 시도 횟수 설정
length = 3
max_trial = 10


# 랜덤 숫자 생성 함수
def make_random_number():
    rand_list = list(range(10))  # 리스트(0~9)
    string = ""  # 랜덤 숫자를 문자열로 저장할 비어있는 문자열
    for i in range(length):
        x = random.choice(rand_list)  # 0~9 중 하나를 선택
        rand_list.remove(x)  # 중복 제거
        string = string + str(x)  # 랜덤 숫자 붙이기
    return string  # 랜덤 숫자 문자열로 return


# 게임 종료 여부
Game_is_Done = False


# 중복 체크. 중복이면 참을 반환. set은 집합 자료형으로서, 중복을 제거하는 필터 역할
def check_duplicated(string):
    if len(string) > len(set(string)):
        return True
    else:
        return False


# 입력 받기. 입력이 잘못되었을 때에 처리 포함(입력이 3자리가 아닐 때, 숫자에 중복이 포함될 때, 문자열이 들어올 때)
def get_guess():
    while True:
        # 변수명의 시작은 소문자로..!
        User_Guess = str(input('Input a %d digit number : ' % length).replace(" ", ""))  # 입력. 띄어쓰기 입력받으며 제거
        try:  # 숫자로 입력되는가
            if len(User_Guess) > 3:  # 입력이 3자리 초과
                print('Please enter a %d digit number' % length)
            elif len(User_Guess) < 3:  # 입력이 3자리 미만 -> 앞에 0을 붙여서 User_Guess에 대입
                User_Guess = str('0' * (length - len(User_Guess)) + User_Guess)
            elif int(User_Guess) not in range(1, 10 ** length):  # 숫자 범위를 벗어날 때
                print('Please enter a %d digit number' % length)
            if check_duplicated(User_Guess):  # 숫자 중복 사용
                print('Each digit does not duplicated')
            else:
                return User_Guess
        except ValueError:  # 문자열 입력
            print('Please input an integer')


# 다시 플레이 할 것인지 확인하는 함수. 앞 글자를 소문자로 변환한 뒤, 그것이 y이면 다시 시작. 아니면 종료.
def play_again():
    return input('Do you want to play again? Y/N').lower().startswith('y')


# 사용자가 입력한 숫자가 생성된 숫자와 어느 정도 일치하는지 확인
# 함수명의 시작은 소문자로..!
def Judge_Correct(User_Guess):
    # SBO 초기화
    strike = 0
    ball = 0
    out = 0

    for i in range(length):
        if User_Guess[i] not in made_number:  # 플레이어가 고른 숫자가 랜덤 숫자에 포함되지 않을 때 아웃 카운트 +1
            out += 1
        else:
            if User_Guess[i] == made_number[i]:  # 플레이어가 고른 숫자가 랜덤 숫자의 위치까지 일치
                strike += 1
            else:  # 플레이어가 고른 숫자가 랜덤 숫자와 같지만 위치는 다를 때
                ball += 1

    # 모두 맞췄을 때
    if strike == length:
        celebrate()
        global Game_is_Done
        Game_is_Done = True
    # 틀렸을 때
    else:
        print('S', strike, '  | B', ball, '  | O', out)


# 모두 맞췄을 때 축하 메시지
def celebrate():
    print('Congratulation! You guessed a random number! The random number was %d!' % made_number)


# 숫자 야구 설명
print('=' * 120)
print(
    'You are playing a Bulls and Cows game.\n'
    'A computer will generate a %d digit random number and each digit does not duplicated.\n'
    'Guess A Number.\n'
    '*** You have %d chances to guess ***' % (length, max_trial))
print('=' * 120)

# 초기 조건 설정 및 랜덤 숫자 설정
guess_time = 1
made_number = make_random_number()

# 입력받아 게임이 끝났는지 확인 후, 다시 플레이하는지 확인. 끝나지 않았으면 몇 번 입력했는지를 출력
while True:
    guess = get_guess()
    Judge_Correct(guess)
    if Game_is_Done:
        if play_again():
            Game_is_Done = False
            guess_time = 1
            made_number = make_random_number()
        else:
            break

    else:
        if guess_time < max_trial:
            print('You guessed %d times.' % guess_time)
            guess_time += 1
        else:
            if play_again():
                Game_is_Done = False
                guess_time = 1
                made_number = make_random_number()
            else:
                break
