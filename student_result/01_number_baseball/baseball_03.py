import random

# 입력 시도 횟수
TRY_NUMBER = 10

# 인트로 함수 내 '=' 출력 횟수
NUMBER_DASH = 50
# 인트로 함수 내 엔터 출력 횟수
NUMBER_ENTER = 10


def intro():    # 게임을 시작할 때 메시지 출력
    print('\n'*NUMBER_ENTER)
    print('='*NUMBER_DASH)
    print('Baseball Game')
    print('='*NUMBER_DASH)
    print('이 게임은 0~9의 무작위 숫자 3개를 맞추는 게임입니다.')
    print('숫자의 종류가 맞고 위치까지 맞으면 스트라이크(S),')
    print('숫자의 종류가 맞았으나 위치가 틀리면 볼(B),')
    print('숫자의 종류가 틀리면 아웃(O) 판정입니다.')
    print('입력할 기회는 %d번 주어집니다.' % TRY_NUMBER)
    print('='*NUMBER_DASH)


def pick_three_numbers():   # 숫자 3개를 랜덤으로 골라 리스트 형태로 반환
    numbers_list = list(range(10))
    random.shuffle(numbers_list)
    return numbers_list[:3]


def restart():  # 게임을 다시 시작할 지의 여부를 bool 형태로 반환
    while True:
        restart_game = input('게임을 다시 시작하시겠습니까? (Y/N) : ')
        restart_game = restart_game.lower()         # 소문자 변경
        if restart_game.startswith('y'):        # y가 입력되면 재시작
            return True
        elif restart_game.startswith('n'):      # n이 입력되면 종료
            return False


game = True

while game:
    intro()

    secret_numbers = pick_three_numbers()     # 3개의 무작위 숫자 선택
    for i in range(TRY_NUMBER):              # 일정 횟수 반복
        refined_input = ''
        while len(refined_input) is not 3 or not refined_input.isnumeric():     # 3개의 숫자 입력
            raw_input = input('Try %d : ' % (i+1))
            refined_input = ''.join(raw_input.split())
        picked_numbers = list(map(int, refined_input))
        strike, ball, out = 0, 0, 0
        for j in range(3):                   # S, B, O 판별
            if picked_numbers[j] is secret_numbers[j]:
                strike += 1
            elif picked_numbers[j] in secret_numbers[:j]+secret_numbers[j+1:]:
                ball += 1
            else:
                out += 1
        if strike is 3:         # 정답 시:
            print('축하합니다! 정답을 맞추셨습니다! 정답은 %d%d%d이었습니다.' % (secret_numbers[0], secret_numbers[1], secret_numbers[2]))
            break
        else:                   # 오답 시 :
            print('%dS %dB %dO' % (strike, ball, out))
            if i is TRY_NUMBER-1:
                print('정답을 맞추지 못하셨습니다. 정답은 %d%d%d이었습니다.' % (secret_numbers[0], secret_numbers[1], secret_numbers[2]))

    game = restart()      # 재시작 여부 입력
