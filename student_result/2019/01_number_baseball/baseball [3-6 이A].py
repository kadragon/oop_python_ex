import random
num_digits = 3  # 입력자릿수 변화 대비
mguesses = 10  # 최대 입력 변화 대비
guesses = 1  # 카운트를 1부터 시작한다.


def make_number(num_digits):  # random을 이용해 임의의 3자리 숫자를 불러온다.
    candidate_list = list(range(10))  # 1부터 10까지 불러와 리스트 형태로 저장한다.
    random.shuffle(candidate_list)  # 리스트의 순서를 재배열한다.
    answer = ''
    for i in range(num_digits):
        answer += str(candidate_list[i])
    return answer


def output(user_guess, answer):  # 출력하는 함수이다.
    if user_guess == answer:
        return '정답입니다'

    s_ans = 0
    b_ans = 0
    o_ans = 0

    for i in range(len(user_guess)):  # for문을 이용해 정답을 자릿수별로 나누어 SBO갯수를 체크한다.
        if user_guess[i] == answer[i]:
            s_ans += 1
        elif user_guess[i] in answer:
            b_ans += 1
        else:
            o_ans += 1

    return str(s_ans) + ' S | ' + str(b_ans) + ' B | ' + str(o_ans) + ' O | \n'


def play_again():
    return input('다시 진행하시겠습니까? (Y/N)').lower().startswith('y')  # Y가 첫글자인지만 보고 판단한다.


def only_int(num):
    if num == ' ':  # 공백을 입력받았을 경우
        return False

    if len(guess) != num_digits:  # 숫자가 아닌 입력을 받았을 경우
        return False

    for i in num:
        if int(i) not in list(range(0, 10)):  # 문자열과 같이 받은 경우
            return False

    return True


print("+" * 60)
print("숫자 야구 게임을 시작합니다.")
print("      규칙을 모르신다면 다음 사이트를 참고하십시오.")
print("      https://namu.wiki/w/숫자야구#s-2\n")
print("제가 생각하고 있는 %d자리 숫자를 맞춰보세요." % num_digits)
print("+" * 60)
print("")

while True:
    answer = make_number(num_digits)  # 정답 생성
    print("\n숫자를 생각했습니다. %d번 안에 맞추십시오." % mguesses)

    guesses = 1

    while (guesses <= mguesses):
        guess = ' '
        while not only_int(guess):
            print("%d번째 입력" % guesses)
            guess = input()

        print(output(guess, answer))  # 답을 도출하는 함수를 불러온다.
        guesses += 1

        if guess == answer:
            break

        if guesses > mguesses:
            print("게임이 종료되었습니다. 정답은 %s였습니다." % answer)

    if not play_again():
        break
