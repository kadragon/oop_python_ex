# 컴퓨터가 랜덤 숫자를 발생
# (import random)(random.shuffle(list))
# 사용자가 숫자를 입력 (띄어쓰기 있는 입력) (예외처리) (최대 10회)
# S/B/O 판정 후 출력 (클래스)
# 재플레이 의사
## 형태
# Guess #2:
# 1 S | 0 B | 2 O

def help():
    """
    게임 규칙 도움말
    """
    print('=' * 65)
    print('숫 자 야 구 !')
    print('본 게임은 임의의 3자리 숫자를 맞추는 게임입니다')
    print()
    print('< 게임 방법 >')
    print(' 1. 띄어쓰기로 구분된 3자리 숫자를 입력하세요 ')
    print(' 2. 입력한 숫자의 S / B / O 개수를 보여드립니다')
    print(' 3. 추리를 통해 컴퓨터가 생각한 3자리 숫자를 맞추세요! 기회는 10번입니다')
    print()
    print(' * S (Strike) : 숫자와 위치가 모두 맞았습니다')
    print(' * B (Ball) : 숫자는 맞지만 위치가 틀렸습니다')
    print(' * O (Out) : 숫자와 위치가 모두 틀렸습니다')
    print('=' * 65)


def generate():
    """
    무작위 수 생성
    이 리스트의 0,1,2번째 숫자만 사용함
    """
    import random

    a = list(range(10))
    random.shuffle(a)

    return a


def do(cnt):
    """
    입력 받기
    예외 처리 등을 통해 잘못된 입력 형태를 걸러냄.

    T. b, c, d 와 같이 의미 없는 변수명을 지양할것.
    """
    print('Guess #%d' % cnt)
    try:
        b, c, d = map(int, input().split())
    except ValueError:
        print(' 잘못된 입력 방식입니다. 다시 입력해주세요')
        b, c, d = do(cnt)

    if b >= 10 or c >= 10 or d >= 10 or b < 0 or c < 0 or d < 0:
        print(' 0 ~ 9 사이의 숫자만 입력 가능합니다. 다시 입력해주세요')
        b, c, d = do(cnt)
    elif b == c or c == d or d == b:
        print(' 같은 숫자는 입력할 수 없습니다. 다시 입력해주세요')
        b, c, d = do(cnt)

    return b, c, d


def ck(s, b, o, a, i, value):
    """
    S,B,O 중 어느 것에 해당하는지 알려주는 함수
    """
    if a[i] == value:
        return s + 1, b + 0, o + 0
    elif a[0] == value or a[1] == value or a[2] == value:
        return s + 0, b + 1, o + 0
    else:
        return s + 0, b + 0, o + 1


def check(a, b, c, d):
    """
    S,B,O 개수를 합산하여 출력하는 함수
    3S 이면 중단하도록 return 값을 1로 줌
    """
    S, B, O = 0, 0, 0
    S, B, O = ck(S, B, O, a, 0, b)
    S, B, O = ck(S, B, O, a, 1, c)
    S, B, O = ck(S, B, O, a, 2, d)

    print('%dS | %dB | %dO' % (S, B, O))

    if S == 3:
        print('이겼습니다!!')
        return 1
    else:
        return 0


def retry():
    """
    게임을 다시 할 것인지 물어보는 함수
    잘못된 입력을 걸러냄
    """
    print('게임을 다시 하시겠습니까?')
    print('예 : 1 / 아니오 : 0')
    r = input()
    if r != '1' and r != '0':
        print('잘못된 입력입니다. ')
        r = retry()
    return int(r)


# 규칙 설명은 한번만 출력
help()

# re == 1 이면 게임을 계속 다시 함
re = 1
while re == 1:
    # 도전한 횟수를 저장
    cnt = 1
    # 다 맞추었는지 여부를 저장
    ch = 0
    # 0~9까지의 수를 무작위로 섞은 리스트
    a = generate()

    while ch != 1 and cnt <= 10:
        # 입력 받기
        b, c, d = do(cnt)
        # 다 맞추었는지 여부 저장
        ch = check(a, b, c, d)
        cnt += 1

    if cnt > 10 and ch != 1:
        print('게임 오버ㅠㅠ')

    # 다시 플레이 할 것인지 여부 저장
    re = retry()
