import random  # 난수 발생을 위해 random 모듈 import
import datetime  # 이스터 에그를 위해 datetime 모듈 import

instruction = '*' * 40 + '''
>> <숫자야구 게임 규칙>
>> 중복이 없고 0이 포함된 수열이 있습니다. 게임의 목표는 이 수열을 맞추는 것입니다.
>> 당신이 어떤 수열을 부르면, 그에 대한 결과값이 스트라이크, 볼, 아웃으로 표현됩니다.
>> 스트라이크: 수의 값과 위치가 모두 맞는 경우
>> 볼: 수의 값만 맞는 경우
>> 아웃: 수열에 수가 포함되어 있지 않은 경우
>> 
>> 답을 입력할 때, 답 대신 키워드를 입력할 수 있습니다.
>> 키워드를 입력하면 각 키워드에 해당하는 결과를 출력합니다. 기회는 차감되지 않습니다.
>> 
>> 키워드 종류
>> help: 도움말
>> hint: 정답 힌트
>> summary: 역대 게임 요약
>> quit: 중도 포기
>>
>> 힌트로는 정답보다 작은 수, 큰 수가 주어지며, 사용할수록 범위가 줄어듭니다.
>> 결과를 바탕으로 답을 유추해보세요.
''' + '*' * 40   # 게임 설명문

easter_date = ['2020.4.12', '2021.4.4', '2022.4.24', '2023.4.9', '2024.3.31', '2025.4.20']  # 부활절 날짜


class DigitError(Exception):  # 잘못된 자릿수를 입력했을 때 발생되는 오류
    def __init__(self):
        super().__init__('>> 잘못된 자릿수입니다.')


class OverlapError(Exception):  # 입력값에 중복된 숫자가 존재할 때 발생되는 오류
    def __init__(self):
        super().__init__('>> 중복된 숫자가 있습니다.')


def create_answer():  # 정답의 자릿수를 입력 받아 정답을 만들어내고 문자열로 반환하는 함수
    while True:  # 사용자가 올바른 입력을 줄 때까지
        try:
            ans_len = int(input('>> 정답을 몇 자리로 설정할 지 입력해주세요 [3 ~ 10]: ').strip())  # 정답의 자릿수를 입력 받음
            if not 3 <= ans_len <= 10:  # 입력값이 3 이상 10 이하가 아니거나 문자, 띄어쓰기를 포함하면 오류 발생
                raise ValueError
            temp_array = list(range(10))  # 정답을 만들기 위한 숫자 생성, 중복은 없음
            random.shuffle(temp_array)  # 숫자의 순서를 섞음
            ans = ''.join(list(map(str, temp_array[0: ans_len])))  # 정답의 자릿수만큼 순서가 섞인 숫자들을 문자열로 정답에 저장
            print('>> 정답이 생성되었습니다. 모든 자릿수는 0부터 9까지 수 중 하나이며, 중복은 없습니다.')
            return [ans, ans_len]  # 생성된 정답과 정답의 자릿수를 반환
        except ValueError:  # 원하는 입력이 아니라면 입력값 범위 출력
            print('>> 3 이상, 10 이하의 자연수를 하나 입력해주세요.')


def scan_chance():  # 최대 시도 횟수를 입력 받고 그대로 반환하는 함수
    while True:  # 사용자가 올바른 입력을 줄 때까지
        try:
            chance = int(input('>> 최대 시도 횟수를 입력해주세요 [3 ~ 100]: ').strip())  # 최대 시도 횟수를 입력 받음
            if not 3 <= chance <= 100:  # 입력값이 3 이상 100 이하가 아니거나 문자, 띄어쓰기를 포함하면 오류 발생
                raise ValueError
            return chance  # 최대 시도 횟수 반환
        except ValueError:  # 원하는 입력이 아니라면 입력값 범위 출력
            print('>> 3 이상, 100 이하의 자연수를 하나 입력해주세요.')


def scan_hint():  # 최대 힌트 갯수를 입력 받고 그대로 반환하는 함수
    while True:  # 사용자가 올바른 입력을 줄 때까지
        try:
            clue = int(input('>> 최대 힌트 갯수를 입력해주세요 [0 ~ 10]: ').strip())  # 최대 힌트 갯수를 입력 받음
            if not 0 <= clue <= 10:  # 입력값이 0 이상 100 이하가 아니거나 문자, 띄어쓰기를 포함하면 오류 발생
                raise ValueError
            return clue  # 최대 힌트 갯수 반환
        except ValueError:  # 원하는 입력이 아니라면 입력값 범위 출력
            print('>> 0 이상, 10 이하의 정수를 하나 입력해주세요.')


def success(turn):  # 현재 시도 횟수를 전달 받아 사용자가 추측한 값을 입력 받고 정답을 맞췄는지 여부를 반환하는 함수
    while True:  # 사용자가 올바른 입력을 줄 때까지
        try:
            guess = input(f'>> # {turn:d}번째 시도: ').strip()  # 사용자가 추측한 값을 입력 받음
            if guess == 'quit':  # 중도 포기를 원한다면
                print('>> 정답은 ' + answer + '였습니다.')  # 정답 출력
                return True  # 함수 종료, False 반환되면 main 함수에서 다시 질문을 출력하므로 True 반환
            if guess == 'help':  # 도움말을 원한다면
                print(instruction)  # 도움말 출력
                continue  # 기회 차감 없이 다시 진행
            if guess == 'hint':  # 힌트를 원한다면
                print_hint()  # 힌트 출력
                continue  # 기회 차감 없이 다시 진행
            if guess == 'summary':  # 역대 게임 요약을 보고 싶다면
                print_summary(turn)  # 역대 게임 요약 출력
                continue  # 기회 차감 없이 다시 진행
            if guess == 'easter egg':  # 이스터 에그를 원한다면
                easter_egg()  # 이스터 에그 출력
                continue
            if int(guess) < 0 or guess[0] == '-':  # 입력값이 음수이거나 문자, 띄어쓰기를 포함하면 오류 발생
                raise ValueError
            if len(guess) != answer_length:  # 입력값의 자릿수가 정답의 자릿수와 다르다면 오류 발생
                raise DigitError
            return judge(guess)  # 입력값과 정답이 같은지 판단해서 같으면 True, 다르면 False 반환
        except ValueError:  # 입력값에 문자, 띄어쓰기 등이 포함된 경우
            print('>> 잘못된 입력입니다.')
        except Exception as error:  # 입력값의 자릿수나 중복 여부가 잘못된 경우
            print(error)  # 오류 메세지 출력


def judge(guess):  # 입력값을 잔달 받아 정답과 같은지 여부를 반환하는 함수
    strike = 0  # 스트라이크 개수, 0으로 초기화
    ball = 0  # 볼 개수, 0으로 초기화
    out = 0  # 아웃 개수, 0으로 초기화
    try:
        for i in range(answer_length):  # 첫 번째 자릿수부터 하나씩
            if guess.count(guess[i]) > 1:  # 이 숫자가 입력값에 한 번 이상 들어있다면 중복 오류 발생
                raise OverlapError
            elif answer.count(guess[i]) == 1:  # 이 숫자가 정답에 한 번만 들어있다면
                if guess[i] == answer[i]:  # 정답에서와 입력값에서 이 숫자의 위치가 같다면 스트라이크 개수 1 증가
                    strike += 1
                else:  # 정답에서와 입력값에서 이 숫자의 위치가 다르다면 볼 개수 1 증가
                    ball += 1
            else:  # 정답에 이 숫자가 들어있지 않다면 아웃 개수 1 증가
                out += 1
        if strike == answer_length:  # 모든 숫자를 맞췄다면 정답임을 알리고 True 반환
            print('>> 정답입니다.')
            return True
        print(f'>> {strike:d} strike {ball:d} ball {out:d} out')  # 모든 숫자를 맞추지 못했다면 결과 출력
        guess_history.append(guess + f': {strike:d} strike {ball:d} ball {out:d} out')  # 추측값과 그 결과를 저장
        return False  # 정답을 못 맞췄다면 False 반환
    except OverlapError:  # 숫자가 중복되어 있다면 이 함수를 호출한 상위 함수에 중복 오류 발생
        raise


def easter_egg():  # 이스터 에그를 출력하는 함수
    today = datetime.datetime.today()  # 오늘 날짜를 구함
    today = '.'.join(list(map(str, [today.year, today.month, today.day])))  # 오늘 날짜를 형식에 맞게 문자열로 변환
    if today in easter_date:  # 오늘이 부활절이라면
        print('''>> 행복한 부활절 되세요!

                                    -----
                                 ===========
                               ---------------
                             -------------------
                            =====================
                           *********Happy*********
                           ********Easter!********
                            =====================
                              -----------------
                                 -----------
                        ''')
    else:  # 부활절이 아니라면
        print('>> 오늘은 부활절이 아닙니다.')


def print_hint():  # 힌트를 출력하는 함수
    try:
        global hint  # 사용한 힌트 수를 가져옴
        global up  # 힌트에 사용될 변수 up 가져옴
        global down  # 힌트에 사용될 변수 down 가져옴
        global hint_range_error  # 힌트 범위 판정 변수 hint_range_error 가져옴
        if hint < max_hint:  # 사용한 힌트 수가 최대 힌트 수보다 적다면
            down = random.randrange(down, int(answer))  # 이전 범위 내에서 답보다 작은 수 생성
            up = random.randrange(int(answer) + 1, up)  # 이전 범위 내에서 답보다 큰 수 생성
            print(f'>> [Hint #{hint + 1:d}] 답은 {down:d}보다 크고 {up:d}보다 작습니다.')  # 답이 두 수 사이에 있음을 출력
            hint_history.append(f'답은 {down:d}보다 크고 {up:d}보다 작습니다.')  # 힌트를 저장
            hint += 1  # 사용한 힌트 수 1 증가
        else:  # 사용한 힌트 수가 최대 힌트 수와 같다면
            print('>> 남은 힌트가 없습니다.')  # 힌트 사용 불가를 알림
    except ValueError:  # 힌트의 범위가 너무 좁아지면
        hint_range_error = True  # 힌트의 범위가 너무 좁아졌음을 체크
        print('>> 힌트의 범위를 더 이상 좁힐 수 없습니다.')


def print_summary(turn):  # 현재 시도 횟수를 전달 받아 현재 게임 상황과 역대 결과, 힌트들을 요약해 출력하는 함수
    print('-' * 20)
    print('>> 정답의 자릿수:', answer_length)  # 정답의 자릿수 출력
    print('>> 남은 기회:', max_chance - turn + 1)  # 남은 시도 횟수 출력
    if hint_range_error:  # 만약 힌트의 범위가 너무 좁다면
        print('>> 남은 힌트: * 범위가 너무 좁아져 더 이상 사용 불가 *')  # 힌트 사용 불가를 알림
    else:
        print('>> 남은 힌트:', max_hint - hint)  # 남은 힌트 갯수 출력
    for index, value in enumerate(guess_history):  # 역대 추측값과 결과 순서대로 출력
        print('>> ' + f'[Guess #{index + 1:d}] ' + value)
    for index, value in enumerate(hint_history):  # 역대 힌트 순서대로 출력
        print('>> ' + f'[Hint #{index + 1:d}] ' + value)
    print('-' * 20)


def replay():  # 사용자에게 다시 플레이할 지 여부를 물어보고 다시 플레이하면 True, 아니라면 False 반환하는 함수
    while True:  # 사용자가 올바른 입력을 줄 때까지
        try:
            choice = input(">> 다시 플레이하시겠습니까? '예'라면 y, '아니오'라면 n을 입력해주세요 [y/n]: ")  # 사용자에게 다시 플레이할 지 물어봄
            if choice == 'y':  # 그렇다고 답하면 True 반환
                return True
            elif choice == 'n':  # 아니라고 답하면 False 반환
                return False
            else:  # 원하는 입력이 아니면 오류 발생
                raise ValueError
        except ValueError:  # 원하는 입력이 아니면 입력 범위 출력
            print('>> 소문자 y 혹은 n을 입력해주세요.')


# main 함수
while True:  # 사용자가 원할 때까지
    print(instruction)  # 게임 설명문 출력
    answer, answer_length = create_answer()  # 정답과 정답의 자릿수 입력 받음
    max_chance = scan_chance()  # 최대 시도 횟수 입력 받음
    max_hint = scan_hint()  # 최대 힌트 갯수 입력 받음
    hint = 0  # 현재 사용한 힌트의 개수, 0으로 초기화
    hint_range_error = False  # 힌트의 범위가 너무 좁은지 여부, False 초기화
    guess_history = []  # 사용자가 추측한 값과 그 결과를 문자열로 저장하는 리스트, 빈 리스트로 초기화
    hint_history = []  # 힌트로 제공된 명제를 문자열로 저장하는 리스트, 빈 리스트로 초기화
    down = 1  # 힌트에 사용될 변수, 정답보다 작은 수, 1로 초기화
    up = 10 ** answer_length - 1  # 힌트에 사용될 변수, 정답보다 큰 수, 10 ^ (정답의 자릿수) - 1로 초기화
    print('>> 게임이 시작됩니다.')
    print(f'>> 중복이 없는 {answer_length:d}자리 숫자를 띄어쓰기 없이 입력해주세요.')
    trial = 1  # 시도 횟수, 1로 초기화
    while trial <= max_chance:  # 시도 횟수가 최대 시도 횟수 이하일 때까지
        if success(trial):  # 만약 정답을 맞췄다면 while 탈출
            break
        else:  # 정답을 맞추지 못했다면 시도 횟수 1 증가
            trial += 1
    if trial > max_chance:  # 시도 횟수가 최대 시도 횟수를 넘었다면, 즉 기회를 모두 소진했다면
        print('>> 기회가 모두 소진되었습니다. 정답은 ' + answer + '였습니다.')
    if not replay():  # 사용자가 다시 플레이하고 싶어하지 않는다면
        print('>> 수고하셨습니다.')
        break  # 게임 종료
