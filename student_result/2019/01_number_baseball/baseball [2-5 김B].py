import random


def get_numbers():  # 비밀번호를 반환
    num = list(range(10))
    random.shuffle(num)

    numbers = ''
    for i in range(3):
        numbers += str(num[i])

    return numbers


def get():  # 유저의 입력값이 형식에 맞는지 확인하고 반환
    while 1:
        num = input()

        try:
            int(num)
        except:  # T. python 에서 예외처리를 할때에는 어떠한 예외를 처리 할지 명기 해야 한다.
            print('숫자 3개를 띄어쓰기 없이 입력하세요')
            continue

        if len(num) != 3:
            print('숫자 세개를 띄어쓰기 없이 입력하세요')
        else:
            return num


def play(secret, user):  # 유저의 입력값과 비밀번호를 비교하여 결과 출력
    if user == secret:
        return '정답!'

    s = 0
    b = 0
    o = 0

    for i in range(3):
        if user[i] == secret[i]:
            s += 1
        elif user[i] in secret:
            b += 1
        else:
            o += 1

    return str(s) + 'S |' + str(b) + 'B |' + str(o) + 'O'


def play_again():  # 게임 재시작 여부 확인
    print('다시 할래요? 다시 하려면 y / 끝내려면 n : ', end=' ')
    answer = input()
    if answer == 'y':
        return 1
    elif answer == 'n':
        return 0
    else:
        return play_again()


while True:
    print('<<재밌는 숫자야구>> 0~9를 중복없이 사용해 만들어진 3자리 비밀번호를 맞춰요!')
    print('숫자 3개를 띄어쓰기 없이 입력하세요')
    secret = get_numbers()

    time = 0
    while time <= 9:
        user = get()
        print(play(secret, user))
        time += 1

        if secret == user:
            break
        if time > 9:
            print('실패.  답: %s' % secret)
        else:
            print('남은 기회: %d\n' % (10 - time))

    if not play_again():
        break
    else:
        print()
