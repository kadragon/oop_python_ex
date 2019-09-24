"""
필요한 기능:
1. 3가지의 랜덤 숫자를 정한다
2. 사용자가 입력한 값이 어떤 상태인지 정한다
3. 입력이 주어진 형식에 맞는지 알려준다
4. 게임을 다시 시작할지 결정한다
"""

import random  # 사용자가 맞출 랜덤한 숫자들을 만들기 위해서


def random_number(num_len):
    """
    num_len 개 만큼의 랜덤하고 서로 다른 숫자를 만든다
    :param num_len: 사용자가 입력할 숫자의 개수
    :return: ans
    """
    ans = ""  # 세자리 숫자 str 로 정답을 나타낸다
    number = list(range(0, 10))  # 0부터 9까지 있는 리스트를 number 라 말한다
    random.shuffle(number)
    for i in range(num_len):
        ans += str(number[i])  # ans 의 뒤쪽에 섞어준 number 을 하나씩, num_len 개 붙인다
    return ans


def sbo(user_key, ans):
    """
    user_key 를 ans 과 비교했을 때 Strike, Ball, Out 를 판정한다
    :param user_key: 사용자가 입력한 값
    :param ans: 정답
    :return:
    """
    if user_key == ans:
        return "정답입니다!"  # 입력한 값이 정답이면 정답임을 리턴

    s = 0  # strike, ball, out 를 0으로 초기화
    b = 0
    o = 0

    for i in range(len(user_key)):
        for j in range(len(user_key)):
            if user_key[i] == ans[j]:
                if i == j:
                    s += 1
                else:
                    b += 1
                break

    o = len(user_key) - s - b
    return "결과 : {0}S {1}B {2}O".format(s, b, o)


def correct_input(user_key):
    """
    유저가 입력한 것이 형식에 맞는지 체크해줌
    :param user_key: 사용자가 입력한 값
    :return: 형식에 맞으면 True, 형식에 맞지 않으면 False 반환
    """
    if len(user_key) != NUM_DIGITS:  # 길이가 다르면 거짓
        return False

    for i in range(0, len(user_key)):
        # if user_key[i] not in str(list(range(0, 10))):  # 숫자로만 구성되어 있지 않으면 거짓
        # T. 이렇게 하면, ,,, 을 입력하면 정상 처리됨.
        if user_key[i] not in "0123456789":  # 숫자로만 구성되어 있지 않으면 거짓
            return False
    return True


def play_again():
    """
    유저가 게임을 다시 시작할지 결정
    :return: 재시작 여부를 True 혹은 False 로 리턴
    """
    command = str(input("다시 시작하려면 re를 입력하세요. 끝내려면 엔터를 눌러주세요."))
    if command == "re":
        return True
    return False


NUM_DIGITS = 3
LIFE = 10

print("=" * 80)
print("숫자 야구 게임에 오신 걸 환영합니다")
print("규칙은 아시죠?")
print("숫자는 %s개 목숨은 %s개입니다!" % (NUM_DIGITS, LIFE))
print("=" * 80)

while True:
    answer = random_number(NUM_DIGITS)
    print("숫자가 생성되었습니다.")
    num_guesses = 1  # 정답을 맞춘 횟수
    while num_guesses <= LIFE:
        guess = ""
        flag = 0
        while not correct_input(guess):
            if flag != 0:
                print("입력이 형식에 맞지 않습니다.")
            print("{0}번째 기회/목숨 {1}개, 숫자 입력:".format(num_guesses, LIFE))
            guess = input()
            flag += 1

        print(sbo(guess, answer))
        num_guesses += 1

        if num_guesses > LIFE:
            print("기회가 끝났습니다. 정답은 %s입니다." % answer)
        if guess == answer:
            break

    if not play_again():
        break
