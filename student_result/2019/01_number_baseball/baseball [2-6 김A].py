import random

start_text = """
숫자야구를 시작합니다!
규칙은 다음과 같습니다
컴퓨터는 0~9로 이루어진 임의의 세자리 숫자를 생성합니다. 이를 정답이라 합니다. 
플레이어는 10번의 시도를 통해 정답을 맞추시면 됩니다.
세자리 숫자를 입력하면, Strike, Ball, Out 의 개수가 출력됩니다. 
단, 세자리 숫자는 모두 다른 숫자를 입력해야 합니다. 모두 같은 숫자를 입력하는 것은 부정행위로 간주합니다. 
행운을 빕니다.

Strike : 입력한 숫자중 정답에 한 개의 숫자가 사용되었고, 올바른 자리에 위치해 있습니다.
Ball : 입력한 숫자중 정답에 한 개의 숫자가 사용되었지만, 틀린 자리에 위치해 있습니다.
Out : 입력한 숫자중 정답에 사용된 숫자는 없습니다. 

입력조건은 다음과 같습니다. 
입력은 각각 정수로 이루어진 세자리 숫자만 가능합니다.
숫자를 입력하고, Enter 키를 누르면 입력이 됩니다. 

총 10회 입력하실 수 있습니다. 행운을 빕니다. 
"""
try_num = 10  # 숫자를 맞히기 위한 실행 횟수
retry = True  # 프로그램을 종료시키기 위한 변수


def make_number():  # 목적: 컴퓨터의 랜덤 숫자를 만들어줌. 단, 중복숫자는 존재하지 않게끔.
    # type: () -> list      # 타입은 이와 같음
    M_ans = []  # T. python 에서 변수의 이름은 소문자로 시작하는걸 권장합니다.

    while len(M_ans) < 3:  # 3개의 숫자가 입력될 때까지
        val = random.randrange(0, 10)  # 랜덤숫자를 뽑음
        if not str(val) in M_ans:  # 같은게 존재하지 않으면 (숫자중복제외) 입력
            M_ans.append(str(val))
    return M_ans


def raw_input():        # 목적 : 사용자의 입력을 프로그래밍에 맞게 바꿔주는 함수
    # type: () -> list  # 타입은 이와 같음
    cheat = False
    try:
        base_input = []  # 사용자의 입력을 list 로 바꾸어 정리할 공간
        num = 100  # 세 자리 숫자를 한 자리씩 구분하기 위한 변수
        input_type = 0  # input 된 값이 띄어쓰기로 구분되었는지 세자리수의 정수인지 확인하기 위한 것

        a = input()
        if ' ' in a:  # 만약 띄어쓰기로 구분된 숫자라면
            input_type = 1  # case 1임
        else:  # 만약 그렇지 않은 숫자라면
            input_type = 0  # case 0임

        if input_type == 0 and len(a) == 3:     # 띄어쓰기로 구분되어있는데 숫자라면 이렇게 처리함
            a = int(a)      # 숫자로 만들고
            for i in range(3):
                if str(int(a/num)) in base_input:       # 중복된 숫자 입력이라면
                    cheat = True                        # 부정행위를 했다는거지
                    break                               # 부정행위라면 더이상의 입력은 필요없음
                base_input.append(str(int(a / num)))    # 한자리씩 분리하고 list 에 넣음
                a = int(a - int(a / num) * num)
                num /= 10
        elif input_type == 1:       # 띄어쓰기로 구분된 거라면
            b = a.split()           # 나누고
            if len(b) == 3:         # 3개인지 검사한 후
                for i in range(3):
                    if b[i].isdecimal() and len(b[i]) == 1:        # 숫자이고 그게 한자리 숫자이면
                        if b[i] in base_input:          # 중복된 숫자 입력이라면
                            cheat = True                # 부정행위를 했다는거지
                            break                       # 부정행위라면 더이상의 입력은 필요없음
                        base_input.append(str(b[i]))    # input list 에 넣음

        if cheat:                   # 부정행위를 했다면
            base_input = []         # error 가 나게 유도하고
            print("NO CHEAT!")      # 부정행위를 하지 말란 표시를 함

        for i in range(3):          # 만약 위에 조건문에 들어가지 못했다면 base_input = []일 것임
            # tmp = base_input[i]     # 그 상태에서 list 을 본다면 error 가 남
            _ = base_input[i]     # 그 상태에서 list 을 본다면 error 가 남  # T. 사용하지 않을 변수라면 (에러 검출용) '_' 을 활용, 메모리 점유 X
        return base_input

    except Exception as inst:       # error 가 나면
        print("Error :", inst)      # 어떤 에러인지 개발자를 위해 표시한 후
        print("Input is wrong. Please type again")      # 사용자를 위해 재입력을 요구
        return False        # False 를 전달하여 다시 입력하도록 함
        # T. 한 Method 의 반환 값은 1종류인 것을 권장함. 어떤건 list, bool 로 구분되지 않아야 함.


def baseball_input():  # 사용자의 입력을 받음. 123의 형태 혹은 1 2 3의 형태를 제외하고는 재입력을 요구함
    # type: () -> list      #타입은 이와 같음
    while 1:
        val = raw_input()
        if val is not False:        # False 가 전달되지 않았다면 제대로 입력된 것이므로
            return val              # 전달함


def baseball_game_unit(answer, base_input):     # 사용자 한번의 입력에 대해 SBO 를 구분해주는 최소단위임. SBO 를 전달함
    # type: (list, list) -> list        #타입은 이와 같음
    try:
        STRIKE = 0  # type: int
        BALL = 0  # type: int
        OUT = 0  # type: int
        for i in range(3):                  # Strike 를 판정
            if answer[i] == base_input[i]:
                STRIKE += 1
        for i in range(3):
            for j in range(3):
                if answer[i] == base_input[j] and i != j:       # BALL을 판정
                    BALL += 1
        for i in range(3):          # OUT 판정
            if base_input[i] != answer[0] and base_input[i] != answer[1] and base_input[i] != answer[2]:
                OUT += 1

        # return STRIKE, BALL, OUT        # strike, ball, out 을 전달함
        # T. 위에 반환형이 list 임을 명시하였기에 리스트로 반환해야 함.
        return [STRIKE, BALL, OUT]        # strike, ball, out 을 전달함
    except Exception as inst:
        print("Error :", inst)
        print("Input error. Please type again")
        # T. 위에 반환형이 list 임을 명시하였음에도 bool 형을 return 하고 있음.
        return False


def print_SBO(ans):         # Strike, Ball, Out을 표시하는 함수. 맞추었는지도 판정
    # type: (list) -> bool  # 타입은 이와 같음
    try:
        b_input = baseball_input()
        Strike, Ball, Out = baseball_game_unit(ans, b_input)  # T. 변수명은 소문자로 시작하는 것을 권장함.
        if Strike == 3:         # 맞추면 축하메세지
            print("Congratulation! It's answer!")
            return True
        else:                   # 틀리면 SBO를 표시
            print("S: %d, B: %d, O: %d" % (Strike, Ball, Out))
            print("")
    except Exception as inst:
        print("Error :", inst)
        print("Input is wrong. Please type again")
        return False


def start_action():     # 시작 설명을 표시하기 위한 함수
    print('=' * 30)
    print(start_text)
    print('=' * 30)


def game_ended(answer: list):     # 맞추지 못하고 게임이 끝났을 때 답과 위로메세지를 표시하는 함수 list 형의 입력을 받음
    print("Answer is", end=' ')
    for i in answer:
        print(i, end='')
    print()
    print("Game ended... Good Luck for next time...")


def yes_or_no():        # 게임 재시작에 대한 입력을 판별하는 함수
    try:
        r = input()
        yes_or_no_list = []
        yes_list = ['y', 'Y', 'yes', 'Yes', 'YES']
        no_list = ['n', 'N', 'no', 'No', 'NO', 'nope']
        if r in yes_list:                   # 만약 재시작을 원하면
            yes_or_no_list.append(True)     # True 를 list 를 넣어주고
        elif r in no_list:                  # 재시작을 원하지 않으면
            yes_or_no_list.append(False)    # False 를 list 에 넣어준다
        val = yes_or_no_list[0]             # 만약 yes 도 no도 아니라면 yes_or_no_list = []일 거고 이 명령을 실행하면 error 가 남
        return val
    except Exception as inst:               # error 가 났다는 것은 재입력이 필요하단 말임
        print("Error :", inst)              # error 의 종류를 표시하고
        print("Input is wrong. Please type again(y/n)")     # 재입력을 요구함
        return 1


def ask_try_again() -> bool:                    # 다시 할 것인지 물어보는 함수
    print('=' * 30)
    print("Will You Try Again? (y/n)")

    while 1:
        reply = yes_or_no()
        if type(reply) is bool:         # reply 의 type 이 bool 이 아니라면 1이 전달된 것이고 다시 물어보아야 한단 뜻임
            return reply                # 제대로 입력되었다면 원하는 대로 실행하기 위해 찬성반대를 전달함


while retry:                            # retry 는 기본적으로 True 인 bool 형 인자임
    start_action()                      # 시작과 함께 규칙설명. 재시작하면 다시 나옴
    right = False                       # type: bool
    ans = make_number()                 # 랜덤으로 만들어진 답 list 형임
    for tmp in range(try_num):          # 10번 이내에 맞추도록 하는 것
        print("#%d" % (tmp + 1))        # 몇 번쨰 실행인지 표시함
        right = print_SBO(ans)
        if right:                       # 맞췄다면
            break                       # 끝냄

    if not right:
        game_ended(ans)             # 맞추지 못하고 게임이 끝나면 답과 위로메세지 출력

    retry = ask_try_again()         # 찬성반대를 받았고 재시작을 원하지 않으면 retry 가 False 가 되어 작동을 종료함

print("Good Bye!")      # 작동을 종료하기 전 마지막 인사
