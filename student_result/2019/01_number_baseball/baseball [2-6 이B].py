import random

num_len = 3  # 답의 자릿수
guess_given = 10  # 주어진 추리 기회
got_answer = False  # 답 맞았는지 여부


# functions
def is_number(s):  # 주어진 s 이 숫자로만 이루어진 string 인지 아닌지 확인하는 함수
    try:
        float(s)  # s가 문자인 경우, 'ValueError: could not convert string to float' 이 발생하고, 따라서 False 를 반환하게 된다.
        return True  # 문제가 발생하지 않으면 숫자로 이루어졌다는 뜻이므로 True 를 반환한다.
    except ValueError:
        return False


def think_answer():  # 답 생성 함수 (이걸 맞춰야 한다)
    goal = list(range(10))  # [0, 1, 2, 3, ... ] 리스트 생성
    random.shuffle(goal)  # 섞음
    goal_num = ''  # 답이 될 string
    for i in range(num_len):
        goal_num += str(goal[i])  # [2, 3, 9, ... ] 인 경우 '' -> '2' -> '23' -> '239' 이렇게 바뀐다. 이 경우 최종 string 은 239.
    return goal_num


def right_input(inp):  # 입력이 제대로 된 입력인지 확인하는 함수
    if len(inp) != num_len:  # 입력의 길이가 올바르지 않은 경우
        return False
    if not is_number(inp):  # 숫자가 아닌 문자가 포함된 경우
        return False
    for i in range(0, num_len):  # 중복된 숫자가 입력된 경우 (ex: 000)
        for j in range(0, num_len):
            if (i != j) & (inp[i] == inp[j]):
                return False
    return True  # 세 경우 다 해당되지 않으면 올바른 입력이므로 True 를 반환한다.


def give_hint(string):  # 사용자가 입력한 string 을 받아, S,B,O를 알려주는 함수
    strike = 0
    ball = 0
    is_answer = False
    for i in range(num_len):
        if string[i] == answer[i]:  # 내가 입력한 수의 i 번째 숫자가 숫자, 위치 모두 맞는 경우 (strike)
            strike += 1

    if strike == num_len:
        is_answer = True  # strike 의 수가 답의 길이와 같은 경우, 답을 맞춘 것이다.
    else:
        for i in range(3):
            if (string[i] != answer[i]) & (string[i] in answer):  # 내가 입력한 수의 i 번째 숫자가 위치는 다른데, 답에 있는 숫자이기는 한 경우 (ball)
                ball += 1

    if not is_answer:
        print("%d S | %d B | %d O" % (strike, ball, num_len - strike - ball))  # 답을 맞추지 못했을 경우 S,B,O를 출력한다.
    return is_answer


def play_check():  # 다시 플레이할 건지 확인하는 함수
    while True:
        print("Do you want to play again? (Y/N)", end=' ')
        reply = input()
        if (reply == 'Y') | (reply == 'y'):  # 새로운 게임 시작
            print('=' * 60)
            print("Loading New game...")
            print('=' * 60)
            return True
        elif (reply == 'N') | (reply == 'n'):  # 게임 종료
            print("Good Bye")
            return False
        else:  # 다시 질문한다.
            print("Please answer with 'Y' or 'N'.")


# 게임 안내
print('=' * 60)
print("I am thinking of a %d-digit number. All digits are different. Try to guess what it is." % num_len)
print("Here are some clues:\n")
print("When I say:  That means:")
print("Strike (S)   One digit is correct and in the right position.")
print("Ball   (B)   One digit is correct but in the wrong position.")
print("Out    (O)   No digit is correct.")
print("=" * 60)

# 게임 시작
play_game = True  # 게임 플레이 여부 (이후 게임이 끝난 뒤에 다시 할 건지 물어볼 때 쓰인다)
while play_game:
    answer = think_answer()  # 게임의 정답. 랜덤으로 생성된다
    used_guesses = 1  # 현재 추리 시도 횟수

    print("I have thought up a number. You have %d guesses to get it." % guess_given)
    while (used_guesses <= guess_given) & (not got_answer):  # 답을 아직 맞추지 못했고, 추리 시도 횟수가 남아있는 동안 계속 시행된다.
        a = ' '  # 입력 받기 전 상태... 이후 input 받으면서 갱신됨

        while not right_input(a):  # 올바른 입력이 들어오기 전까지 계속 시행된다.
            print("Guess #%d:" % used_guesses, end=' ')  # 몇 번째 입력인지 표시
            a = input()  # 입력을 받아 a 에 저장한 뒤, right_input 함수를 통해 올바른 입력인지 확인한다.
            if not right_input(a):  # 올바른 입력이 아닐 경우, 잘못되었음을 알려 주고 다시 입력을 받는다.
                print("Wrong input!")

        used_guesses += 1  # 추리 시도 횟수를 1 증가시킨다.
        got_answer = give_hint(a)  # 답이 맞았을 경우 give_hint 함수에서 True 가 반환된다.

    if got_answer:  # 답이 맞아서 while 문을 빠져나온 경우
        print("You've got the answer!!")
        got_answer = False
    else:  # 답이 안 맞았는데 while 문을 빠져 나온 경우, 즉 추리 횟수를 모두 소진한 경우
        print("You lose... :(\nAnswer was %s" % answer)  # 답을 알려준다.

    play_game = play_check()  # 다시 플레이할 건지 여부를 확인한다.
