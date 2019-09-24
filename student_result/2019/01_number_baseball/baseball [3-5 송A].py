"""
<숫자 야구 로직>
# 중복되지 않은 숫자로 이루어진 3자리 정수 생성
# 입력하는 세 자리 중 모든 자리에 0 입력 허용
# 3자리 정수 입력 (기회 10번 제한)
# 입력한 숫자 결과 보여주기 (정답 - 축하메시지 / 오답 - S/B/O)
# 리플레이 여부 확인
"""
import random  # 맞추어야 하는 임의의 숫자 생성


def form_pw():
    """
    form_pw는 임의의 숫자열을 반환하는 함수를 의미함
    """
    number_list = list(range(10))  # 0부터 9까지의 정수 리스트
    pw = random.sample(number_list, 3)  # pw: number_list 에서 세 숫자
    return pw


def num_only(number):
    """
    플레이어가 입력한 배열의 모든 항이 한 자리 수로 이루어진 배열에 속해 있으면 True
    배열에 속하지 않은 항이 하나라도 있을 경우 False
    :param number: 플레이어가 입력한 값
    :return: True or False
    """
    if number == ' ':
        return False

    number_list = list(range(10))  # 0부터 9까지의 리스트
    for i in number:
        try:
            int(i)
        except ValueError:
            return False

        if int(i) not in number_list:
            return False

    return True


def hints(guess, pw):
    """
    :param guess: 플레이어가 입력한 값
    :param pw: 정답
    :return: 입력한 값에 대한 결를 작성한 문자열
    """

    ans_s = 0  # strike 인 숫자 개수 카운트
    ans_b = 0  # ball 인 숫자 개수 카운트
    ans_o = 0  # out 인 숫자 개수 카운트

    for i in range(len(guess)):
        if int(guess[i]) == int(pw[i]):  # strike
            ans_s = ans_s + 1
        elif int(guess[i]) in pw:  # ball
            ans_b = ans_b + 1
        else:  # out
            ans_o = ans_o + 1

    if ans_s == 3:
        return '정답이에요!!!'

    return str(ans_s) + ' S | ' + str(ans_b) + ' B | ' + str(ans_o) + ' O '
    #   str: int 형태와 문자 형태를 이어 붙이기 위해 사용


def play(repeat):
    """
    플레이어가 게임을 계속할지 결정
    :param repeat:
    :return: 0 or 1
    """
    if repeat == 'y':
        return 1
    else:
        return 0


# 게임 실행

max_guess = 10  # 최대로 시도할 수 있는 횟수

print("=" * 100)
print("제가 생각하고 있는 숫자가 무엇인지 맞춰보세요!")
print("지금부터 게임을 시작할건데, 그 전에 제가 제공할 힌트에 대해 말씀드릴게요")
print("제공되는 힌트의 의미는 다음과 같습니다")
print("Strike  (S) - 하나의 숫자의 위치와 존재여부가 모두 일치합니다")
print("Ball    (B) - 하나의 숫자가 존재하지만 위치가 다릅니다")
print("Out     (O) - 하나의 숫자가 존재하지 않습니다")
print("=" * 100)
repeat = 1
while repeat == 1:
    while True:
        pw = form_pw()
        print('\n 숫자를 생각했어요. %s번의 기회가 있으니 게임을 시작하세요!' % max_guess)
        print(pw)
        tries = 1  # 시도 횟수 확인
        while 1 <= tries <= 10:
            g = ' '
            if len(g) != 3 or not num_only(g):
                print('추측 #%s:' % tries, end=' ')
                g = input()
                if len(g) != 3:
                    print("잘못 입력하셨어요. 다시 입력하세요.")
                    continue
                elif g[0] == g[1] or g[1] == g[2] or g[0] == g[2]:
                    print("잘못 입력하셨어요. 다시 입력하세요.")
                    continue

                try:
                    if len(g) == 3:
                        print(hints(g, pw))
                    tries = tries + 1

                    if tries > max_guess:
                        print('힌트를 모두 사용하셨네요. 답은 %s였어요!!!' % str(pw))
                        break

                except Exception:
                    print("잘못 입력하셨어요. 다시 입력하세요.")
                    break
                if hints(g, pw) == "정답이에요!!!":
                    repeat = input('게임을 계속하시겠습니까? 계속하고 싶은 경우 y를, 그렇지 않으면 y를 제외한 나머지 키를 누르세요. : ')
                    if not play(repeat) == 1:
                        exit()
                    break

        repeat = input('게임을 계속하시겠습니까? 계속하고 싶은 경우 y를, 그렇지 않으면 y를 제외한 나머지 키를 누르세요. : ')

        if play(repeat) == 1:
            continue
        elif play(repeat) != 1:
            break
