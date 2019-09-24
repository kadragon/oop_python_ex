import random
import sys


class Setting(object):
    def __init__(self):
        self.size_of_ball = 3
        self.chance_to_guess = 10


set = Setting()     # 세팅을 저장하는 오브젝트


class Baseball(object):
    def __init__(self):
        # 생성시 임의의 3개 수를 설정
        self.ans = list(range(10))
        random.shuffle(self.ans)
        self.ans = self.ans[:set.size_of_ball]

    def print_result(self, guess):
        # guess 가 들어왔을 때, strike, ball, out 의 개수를 측정
        # 만약 숫자가 정확하다면 True 를 반환하여 정답을 맞추었음을 표현
        strike = 0
        ball = 0
        out = 0

        for i in range(set.size_of_ball):
            if self.ans[i] == guess[i]:
                strike += 1
            elif guess[i] in self.ans:
                ball += 1
            else:
                out += 1

        if strike == set.size_of_ball:
            print("You got it!!")
            return True
        else:
            print("%d Strike | %d Ball | %d Out \n" % (strike, ball, out))
            return False


def chk_input(ipt):
    # 들어온 인풋이 정확한 형식에 맞추었는지 체크하는 함수
    # 형식에 맞다면 True, 형식에 맞지 않다면 False 반환
    if len(ipt) != set.size_of_ball:
        return False

    for i in range(set.size_of_ball):
        try:
            int(ipt[i])
        except ValueError:
            return False
    return True


def start_game():
    # 정답(ball) 생성
    ball = Baseball()
    print(f"""
#################################################################################################################
I have thought up a {set.size_of_ball} digits of number. You have {set.chance_to_guess} guesses to get it.
You can guess what I thought with put {set.size_of_ball} digits of number in input.
If your guess is wrong, I'll give you some clue

strike:     One digit is correct and in the right position.
Ball:       One digit is correct but in the wrong position.
Out:        One digit is not in answer

If you enter wrong input, you lost a chance.
If you want to quit the game, enter "quit".
If you want to restart the game while playing, enter "re".
If you want to restart and change setting, enter "change setting"
################################################################################################################
""")

    i, t = 1, set.chance_to_guess
    while i <= t:
        # 입력부
        guess = input("Guess #%d: " % i)

        # 종료코드 입력될 경우 종료
        if guess == "quit":
            oh = input("""You really want to quit the game?
if you want to quit, enter y
else, you could enter any other key
[y/(n)]: """)
            if oh == "y":
                sys.exit()

        # 리겜 입력될 경우 리겜
        elif guess == "re":
            oh = input("""You really want to restart the game?
if you want to restart, enter y
else, you could enter any other key
[y/(n)]: """)
            if oh == "y":
                print("\n"*10)
                start_game()
                return

        elif guess == "change setting":
            oh = input("""You really want to restart and change setting?
if you want to do it, enter y
else, you could enter any other key
[y/(n)]: """)
            print("")
            if oh == "y":
                hm = input("""enter digits of answer between 3 to 9
(if you enter another number or word, digits of answer will be 3(default))
: """)
                try:
                    hm = int(hm)
                    if 3 <= hm <= 9:
                        set.size_of_ball = hm
                    else:
                        set.size_of_ball = 3
                except ValueError:
                    set.size_of_ball = 3

                print("")
                hm = input("""enter number of chance to guess
(if you enter word which is not number, the chance will be 10(default))
: """)
                try:
                    hm = int(hm)
                    set.chance_to_guess = hm
                except ValueError:
                    set.chance_to_guess = 10
                print("")

                start_game()
                return

        # 치트키 매크로
        elif guess == "Power Overwhelming":
            t += 999999999
            print("I have never tasted death.\n")

        elif guess == "Black Sheep Wall":
            print(''.join(map(str, ball.ans))+'\n')

        # 인풋이 정확한지 확인
        # 정확하다면 결과 출력
        elif chk_input(guess):
            i += 1
            guess = list(map(int, guess))
            if ball.print_result(guess):
                return
        else:
            i += 1
            print("WRONG INPUT (Lost a chance)\n")
    print("Answer is "+''.join(map(str, ball.ans)))
    print("")


while True:
    start_game()
    re = input("""You really want to play new game?
if you want to do again, enter y
else, you could enter any other key
[y/(n)]: """)
    if re != "y":
        break
    print("\n" * 10)
