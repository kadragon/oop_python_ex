import random

commands = ['quit', 'restart']  # 명령어 목록
input_modes = ['default', 'cmd_only']  # 입력 모드 목록


def get_input(input_string, input_mode='default'):
    """
    입력을 받는 함수입니다.
    입력 조건이 맞지 않으면 입력을 다시 받습니다.
    :param input_string: 입력 받을 때 콘솔에 띄울 안내 문구
    :param input_mode: 입력 모드
    :return: 각 자릿수를 분리한 list 혹은 명령어
    """

    if input_mode not in input_modes:  # 입력 모드 목록에 없으면
        raise Exception(f"input_modes 목록에 없습니다. {input_modes} 중 하나를 선택하세요.")

    while True:

        my_input = input(input_string)  # 안내 문구를 넣어서 입력 받기

        if input_mode == 'default':

            try:
                if my_input in commands:  # 명령어 목록에 있다면
                    return my_input  # 입력 그대로 반환
                elif my_input == 'help':
                    print_instructions()  # 도움말 다시 출력
                    print("계속 하세요!")
                    continue

                tear_apart = list(map(int, my_input))  # int mapping 시도, 오류 발생 시 except 실행

                if len(tear_apart) != 3:  # 길이가 3이 아니라면
                    raise Exception("숫자 3자리를 입력해주세요.")
                if len(set(tear_apart)) != 3:  # 중복된 숫자가 있다면
                    raise Exception("중복된 숫자를 입력하지 말아주세요.")

                return tear_apart

            except Exception as e:  # 예외 발생 시
                print("잘못 입력하셨습니다...!")
                print(e)

        elif input_mode == 'cmd_only':
            if my_input in commands:
                return my_input
            else:
                print(f"명령어를 입력하세요: {commands}")


def find_sbo(ans_list, user_list):
    """
    strike, ball, out의 개수를 찾는 함수입니다.
    :param ans_list: 정답 숫자열
    :param user_list: 들어온 숫자열
    :return: strike, ball, out 개수를 담는 dictionary
    """
    result = {'strike': 0, 'ball': 0, 'out': 0}
    for j in range(0, 3):
        if user_list[j] == ans_list[j]:  # 위치와 숫자 모두 일치
            result['strike'] += 1
        elif user_list[j] in ans_list:  # 숫자만 일치
            result['ball'] += 1
        else:
            result['out'] += 1
    return result


def play_round(round_number):
    """
    라운드 하나를 플레이하는 함수입니다.
    :param round_number: 라운드 번호
    :return: (라운드 도중 혹은 라운드가 끝나고 입력된) 명령어
    """
    print(":"*20+f" ROUND {round_number} "+":"*20)

    ans_list = random.sample(range(0, 10), 3)  # 랜덤 샘플링, 0 ~ 9 중에서 3번 비복원 추출
    num_list = None
    is_successful = False

    # reveal_answer(ans_list)
    try:
        for i in range(1, 11):  # 10번의 기회가 주어짐
            something = get_input(f"Trial {i}: ")  # get_input 실행
            if something in commands:
                return something
            else:
                num_list = something
            sbo = find_sbo(ans_list, num_list)
            print(f"Strike: {sbo['strike']} | Ball: {sbo['ball']} | out: {sbo['out']}")  # S/B/O 정보 출력
            if sbo['strike'] == 3:  # 모두 맞았으면
                is_successful = True  # 성공으로 표시
                break  # for 문 탈출
    finally:
        if is_successful:  # 성공이라면
            print("You got it!\n")  # 잘했어요
        else:  # 아니라면
            reveal_answer(ans_list)  # 답을 공개함

    something = get_input("Quit or restart?\n[quit / restart]: ", 'cmd_only')
    return something


def print_instructions():
    """
    게임 안내 문구를 출력하는 함수입니다.
    :return: None
    """
    print("""
    안녕하세요! 숫자 야구 게임에 오신 것을 환영합니다!
    
    세 자리 수를 입력하시면, 저는 스트라이크 / 볼 / 아웃의 개수를 알려드립니다.
    스트라이크: 숫자와 위치가 모두 맞는 것의 개수
    볼: 숫자는 맞지만 위치가 틀린 것의 개수
    아웃: 숫자와 위치 모두 틀린 것의 개수
    
    중복되는 숫자는 없으며, 맨 앞 자리 숫자가 0일 수도 있습니다.
    ex) 945 (O) | 012 (O) | 330 (X) | 888 (X)
    그럼 게임 시작할게요!
    
    **참고**
    게임을 끝내고 싶으시다면? -> quit
    게임을 다시 시작하고 싶으시다면? -> restart
    도움말을 다시 보고 싶으시면? -> help
    """)


def reveal_answer(ans_list):
    """
    답을 공개하는 함수입니다.
    :param ans_list: 답 리스트를 받는다
    :return: None
    """
    print("Maybe next time...")
    result = ''
    for i in ans_list:
        result += str(i)
    print(f"The answer is {result}\n")


print_instructions()  # 게임 안내 문구 출력

round_count = 1
while True:
    command = play_round(round_count)  # 게임을 시작하고 만약
    if command == 'quit':  # 게임을 끝내고 싶다면
        break  # while 문 탈출
    round_count += 1
