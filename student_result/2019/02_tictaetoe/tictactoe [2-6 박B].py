import random  # 랜덤한 값들을 호출하는 함수를 사용하기 위해

Win = 0  # 누적 승리 횟수
Lose = 0  # 누적 패배 횟수
Draw = 0  # 누적 무승부 횟수
rate = 0  # 통산 승률


def line():  # 가독성을 위한 줄을 출력하는 함수
    print("*" * 80)


def draw_pad(pad):  # 현재 상태를 출력하는 함수
    print(pad[1] + ' | ' + pad[2] + ' | ' + pad[3])
    print(pad[4] + ' | ' + pad[5] + ' | ' + pad[6])
    print(pad[7] + ' | ' + pad[8] + ' | ' + pad[9])


def who_first():  # 컴퓨터와 플레이어 중 선공을 랜덤하게 지정하는 함수
    if random.randint(0, 1) == 1:  # 0과 1중 랜덤한 값을 받아서 결과에 따라 선공을 정한다
        return 'player'  # 플레이어 선공
    else:
        return 'com'  # 컴퓨터 선공


def get_symbol():  # 플레이어의 문자를 입력받아 플레이어와 컴퓨터의 문자를 지정하는 함수
    symbol = ''  # 문자열형으로 초기화
    while symbol != 'X' and symbol != 'O':  # 입력받은 값이 조건에 맞을 때 까지
        line()
        print("시작할 문자를 골라주세요, X or O?: ")
        symbol = input().upper()  # x, o 를 입력했을때도 대문자로 인식 하도록 해줌
        if symbol != 'X' and symbol != 'O':  # 오류 메세지 출력
            print("이상한거 고르지 마세요... 다시 고르세요")
    if symbol == 'X':  # 호출할때, 두 문자를 동시에 호출하기 위해 리스트를 리턴한다
        return ['X', 'O']
    else:
        return ['O', 'X']


def move_able(pad, move):  # 현재 게임판에서 해당 위치로 이동 할 수 있는지 알려주는 함수
    if pad[int(move)] == ' ':  # 해당 위치로 이동할 수 있습니까?
        return True
    else:
        return False


def game_win(pad, symbol):  # 해당 문자를 가진 플레이어 또는 컴퓨터가 승리했는지 알려주는 함수
    if (pad[1] == symbol and pad[2] == symbol and pad[3] == symbol) or \
            (pad[4] == symbol and pad[5] == symbol and pad[6] == symbol) or \
            (pad[7] == symbol and pad[8] == symbol and pad[9] == symbol) or \
            (pad[1] == symbol and pad[4] == symbol and pad[7] == symbol) or \
            (pad[2] == symbol and pad[5] == symbol and pad[8] == symbol) or \
            (pad[3] == symbol and pad[6] == symbol and pad[9] == symbol) or \
            (pad[1] == symbol and pad[5] == symbol and pad[9] == symbol) or \
            (pad[3] == symbol and pad[5] == symbol and pad[7] == symbol):  # 승리 조건을 만족하는 8개 줄의 조건문, 가로줄, 세로줄, 대각선

        return True
    else:
        return False


def copy_pad(pad):  # 다음 수의 경우를 예측하기 위한 현재 상황의 복제본
    copy = []  # 복제본을 위한 빈 리스트 생성
    for item in pad:  # 현재 상황 복제
        copy.append(item)  # 복제본에 삽입
    return copy


def full(pad):  # 게임판이 꽉 찼는지 알려주는 함수
    for num in range(1, 10):  # 1 부터 9 까지의 인덱스를 확인하여
        if pad[int(num)] == ' ':  # 빈 공간이 있으면, 꽉 차지 않았다
            return False
    return True


def player_move(pad, symbol):  # 플레이어에게 위치를 입력 받아서 말을 두는 함수
    p_symbol = symbol  # 플레이어의 문자 확인
    while True:  # 올바른 입력을 할 때까지 반복
        print("말을 놓을 위치를 1~9 사이의 수에서 입력하세요: ")
        move = input()  # 입력 받음
        try:  # 예외 처리
            int(move)  # 정수형으로 변환 가능?
        except ValueError:  # 정수형이 아닌 문자가 섞여 있다면
            print("똑바로 좀 써라 핫산.")
            line()
            continue
        if not 1 <= int(move) <= 9:  # 정수형이지만 인덱스 밖의 값을 입력하면
            print("좀 생각을 하고 써라 핫산..")
            line()
            continue
        if not move_able(pad, move):  # 이미 문자가 존재하는 인덱스를 입력하면
            print("이미 뭐가 있으니 다른 걸 써라 핫산...")
            line()
            continue
        break  # 올바르게 썻으므로 나온다
    pad[int(move)] = p_symbol  # 지정한 위치에 말을 둔다


def com_move(pad, symbol):  # 컴퓨터가 상황에 따라 말을 두는 함수
    c_symbol = symbol  # 컴퓨터의 문자 확인
    if c_symbol == 'X':  # 다음 상황을 확인하기 위해, 미리 두 변수를 지정해 문자를 저장해둔다
        p_symbol = 'O'
    else:
        p_symbol = 'X'
    for num in range(1, 10):
        copy = copy_pad(pad)  # 다음 상황을 만들 복제본 생성
        if move_able(copy, num):  # 복제본에서 움직일 수 있는 곳 탐색
            copy[int(num)] = c_symbol  # 시험삼아 넣어본다
            if game_win(copy, c_symbol):  # 컴퓨터가 이길 수 있다면
                pad[int(num)] = c_symbol  # 원래 게임판의 그 위치에 삽입
                return
    for num in range(1, 10):
        copy = copy_pad(pad)
        if move_able(copy, num):
            copy[int(num)] = p_symbol  # 시험삼아 플레이어의 말을 넣어본다
            if game_win(copy, p_symbol):  # 플레이어가 이길 수 있다면
                pad[int(num)] = c_symbol  # 방어를 위해 그 위치에 자신의 말을 삽입한다
                return
    while True:  # 조건이 맞는 랜덤 위치가 나올 때 까지 반복
        copy = copy_pad(pad)
        rand_num = random.randint(1, 9)  # 1 부터 9 까지의 수 중 랜덤으로 얻는다
        if move_able(copy, rand_num):
            pad[int(rand_num)] = c_symbol  # 원래 게임판의 그 위치에 삽입
            return


def bye():  # 재도전 여부를 묻는 함수
    print("재도전 하시겠습니까? yes / no")
    x = input()  # 입력 받기
    if x == 'yes':  # 재도전 희망
        print("재도전!")
        return True
    elif x == 'no':  # 재도전 X
        print("잘가용!")
        return False
    else:  # 'yes', 'no' 이외의 값들을 처리
        print("안할거라고 생각할게용 빠이~!")
        return False


def win_rate(case):  # 승률을 기록하고 출력하는 함수
    if case == 'win':  # 플레이어가 이겼다면
        global Win  # 전역변수 Win 에
        Win += 1  # 1을 더한다
    elif case == 'lose':  # 플레이어가 졌다면
        global Lose  # 전역변수 Lose 에
        Lose += 1  # 1을 더한다
    elif case == 'draw':  # 플레이어가 비겼다면
        global Draw  # 전역변수 Draw 에
        Draw += 1  # 1을 더한다
    global rate  # 전역변수 rate 를 불러온다
    rate = Win / (Win + Lose + Draw)  # rate 의 계산
    print("전적: %d 승 %d 패 %d 무" % (Win, Lose, Draw))  # 게임 통산 전적 출력
    print("승률: %.3f" % rate)  # 게임 통산 승률 출력


# 여기서 부터 메인 함수

line()
print("틱-택-토 게임에 온 것을 환영합니다~~~")
print("틱-택-토 게임은 오목과 아주 유사한 형태인 추상전략 보드게임으로, 외국어로 이 놀이를 언급한 대목에서 번역자들이 삼목이라고 번역하는")
print("경우도 있습니다. 종이와 펜만 있으면 어디서든 할 수 있는 간단한 놀이이며, 심지어 종이나 펜이 없어도 모래 위에 그리거나, ")
print("돌이나 나뭇잎 같은 것들로 모양만 갖추면 언제 어디서나 할 수 있습니다. - 출처 : 나무위키")
print("판 크기는 3×3의 정사각형이고, 가로 세로 대각선으로 같은 말 3개가 이어지면 이깁니다.")
print("당신은 1~9 까지의 숫자를 입력해 말을 둘 수 있습니다")
print("판은 다음과 같이 생겼고, 당신이 숫자를 입력했을때 말이 어디에 놓아지는지 표시했습니다")
example_pad = [''] * 10  # 위치를 표시할 예시 게임판 생성
for i in range(1, 10):
    example_pad[int(i)] = str(i)  # 1 부터 9 까지 순서대로 입력
draw_pad(example_pad)  # 게임판 출력 형식대로 보여준다
print("물론 지겠지만, 열심히 하세요! 화이팅!!!")
line()
while True:  # break 가 아닌 이상 계속 반복한다
    only_pad = [' '] * 10  # 이번 게임에서 사용될 게임판 생성
    draw_pad(only_pad)  # 현재 상황 출력
    player_symbol, com_symbol = get_symbol()  # get_symbol() 로 얻은 리스트 안의 문자열형 값을 넣어준다
    turn = who_first()  # 랜덤 함수를 통해 임의로 순서 결정
    if turn == 'com':
        print("컴퓨터가 선공입니다")
    else:
        print("당신이 선공입니다")
    game_now = True  # 이번 게임이 진행되는 것을 확인하는 변수
    while game_now:
        if turn == 'player':  # 플레이어의 차례
            line()
            print("당신의 차례")
            draw_pad(only_pad)  # 현재 상황 출력
            player_move(only_pad, player_symbol)  # 플레이어의 말을 명령에 따라 놓음
            line()
            if game_win(only_pad, player_symbol):  # 만약 플레이어가 이겼다면
                draw_pad(only_pad)  # 현재 상황 출력
                print("당신이 이겼어요, 축하해요! 물론 당연히 이겨야 되는건 알죠?")
                win_rate('win')  # 플레이어가 이긴 경우
                game_now = False  # 게임 종료
            else:
                if full(only_pad):  # 게임판이 가득 찼다면, 즉 무승부라면
                    draw_pad(only_pad)
                    print("이게 무승부가 나네... 요즘 좀 힘드신거죠?")
                    win_rate('draw')  # 무승부인 경우
                    game_now = False
                else:
                    turn = 'com'  # 컴퓨터의 턴으로
        elif turn == 'com':  # 컴퓨터의 차례
            line()
            print("컴퓨터의 차례")
            draw_pad(only_pad)
            com_move(only_pad, com_symbol)  # 컴퓨터가 말을 상황에 따라 움직임
            line()
            if game_win(only_pad, com_symbol):  # 만약 컴퓨터가 이겼다면
                draw_pad(only_pad)
                print("엥 진짜...? 사람임...?")
                win_rate('lose')  # 컴퓨터가 이긴 경우
                game_now = False
            else:
                if full(only_pad):
                    draw_pad(only_pad)
                    print("이게 무승부가 나네... 요즘 좀 힘드신거죠?")
                    win_rate('draw')
                    game_now = False
                else:
                    turn = 'player'  # 플레이어의 차례
    if bye():  # 재도전 여부 질문
        continue
    else:
        break
