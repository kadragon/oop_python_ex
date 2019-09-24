import random


def print_equal_15():
    """
    =를 15개 출력한다.
    :return: 없음
    """
    print('=' * 15)


TRY_NUM = 10  # 시도할 수 있는 최대 횟수. 3~20번 제한됨
BSB_LEN = 3  # 게임에 사용되는 숫자의 길이

list_0_to_9 = list(range(10))  # 0~9 숫자 리스트

user_answers: list = []  # 플레이어의 답을 저장, "show my answers"를 입력하면 이 리스트를 출력한다.


def make_random_number():
    """
    게임을 시작할 때, 랜덤 숫자를 만들어 반환한다
    :return: BSB_LEN 갯수의 숫자(0~9)를 가진 리스트
    """
    the_shuffle_list = list_0_to_9
    random.shuffle(the_shuffle_list)  # 0~9리스트를 섞는다.
    the_answer_list = []
    for i in range(BSB_LEN):  # 섞은 리스트의 앞 BSB_LEN 개수만큼 가져와 답을 만든다.
        the_answer_list.append(the_shuffle_list[i])
    return the_answer_list


def is_error(new_answer):
    """
    유저의 답에 오류가 있는지 판단한다.
    :param new_answer: BSB_LEN 길이의 유저 답 리스트 권장. 그러나 공백으로 띄워진 숫자 리스트도 답으로 인정한다
    :return: new_answer 가 BSB_LEN 개의 숫자를 가졌으면 다듬은 숫자 리스트를 반환. 그렇지 않으면 False 반환
    """
    the_list = list(new_answer)  # 유저의 답(str)을 문자 한글자씩을 원소로 가지는 list 형태로 바꾼다.

    while True:
        try:  # 공백이 없을 때까지 try 를 반복하여 공백을 지운다.
            the_list.remove(' ')  # (remove 함수는 찾는 것이 없으면 에러가 난다.)
        except:
            break

    try:
        the_list = list(map(int, the_list))  # 리스트의 모든 문자를 숫자로 만든다
    except:
        return False  # 숫자 이외의 것이 있으면 거짓을 반환한다.

    if len(the_list) is not BSB_LEN:
        return False  # 숫자의 길이가 맞지 않으면 거짓을 반환한다.

    for i in range(BSB_LEN):
        for j in range(BSB_LEN):
            if i == j:
                continue
            if the_list[i] == the_list[j]:  # 만일 숫자에 같은 숫자 2개가 있다면 거짓을 반환
                return False

    return the_list  # 와! 이모든 역경을 거치고 드디어 다듬은 숫자형 리스트를 반환한다!! 와!!


def is_it_answer(new_answer, answer):
    """
    is_it_answer? 답인가?
    strike 와 ball 개수를 반환한다.
    :param new_answer: 다듬어져 있는 유저의 답.
    :param answer: 정답
    :return: new_answer 와 answer 가 같다면 False, 그렇지 않다면 strike 와 ball 개수를 리스트로 반환한다.
    """
    if new_answer == answer:  # new_answer 와 answer 가 같을 때. False 를 반환
        return False

    strike = 0  # strike 개수 저장용 변수
    ball = 0  # ball 개수 저장용 변수

    for i in new_answer:  # new_answer (리스트)의 각 원소에 대해서
        if i in answer:  # 원소가 답에 포함되어 있을 때
            if new_answer.index(i) == answer.index(i):  # 원소의 위치가 같을 때 (strike)
                strike += 1
            else:  # 원소의 위치가 다를 때 (ball)
                ball += 1

    return [strike, ball]  # 스트라이크와 볼 개수를 리스트로 반환


def check_and_print_user_answers(the_user_answer):
    """
    user_answers 를 반환하는 커맨드가 맞는지 확인한다.
    :param the_user_answer: 유저의 답. 다른 수정을 거치지 않았다.
    :return: bool
    """
    if the_user_answer == "show my answers":
        return True
    else:
        return False


admin_dict: dict = {'soi': 0, 'kdragon': 0}  # admin 권한을 가진 pw. id가 admin 일 때 입력할 수 있다.
admin_check: bool = 0  # admin 인지 아닌지 확인하는 bool

user_id = input("user_id>>")
user_pw = ''
while user_id == 'admin' and user_pw is '':  # 유저가 답을 입력할 때 까지 입력을 받도록 대기한다.
    user_pw = input('admin_pw>>')
    if user_pw in admin_dict:  # admin_dict 에 pw가 있다면 admin 권한을 준다.
        print("Welcome! you are the admin_" + str(user_pw))
        admin_dict[user_pw] = 1
        admin_check = 1

check: bool = 1  # 게임을 계속할 것인지 아닌지 확인하는 bool

while check:
    user_answers = []  # user_answers 리스트 초기화
    i = 0  # try 횟수를 세는 i 변수 초기화
    print_equal_15()
    print("user:", user_id)
    print("start new game")
    set_len = input("the baseball length? (3~10):")
    len_check_FxxK = 3  # 참는 횟수
    while True:
        try:
            set_len = int(set_len)
            if 3 <= set_len <= 10:  # 예쁜 값을 적었다면 빠져나간다
                BSB_LEN = set_len
                print("set LEN to", BSB_LEN)
                break
            else:
                len_check_FxxK -= 1  # 값이 이상하면 기회를 하나씩 줄인다
                print("not right integer.")
                if len_check_FxxK == 0:  # 기회를 모두 소진했다 하하!!
                    print("you don't have another chance")
                    BSB_LEN = 10
                    print("F YOU")
                    break
                print("you have", len_check_FxxK, "chance")
                set_len = input("please write right number(3~10):")
        except:
            len_check_FxxK -= 1  # 값이 이상하면 기회를 하나씩 줄인다
            print("not integer.")
            if len_check_FxxK == 0:  # 기회를 모두 소진했다 하하!!
                print("you don't have another chance")
                BSB_LEN = 10
                print("F YOU")
                break
            print("you have", len_check_FxxK, "chance")
            set_len = input("please write integer(3~10):")
    print("the length is", BSB_LEN)
    the_answer = make_random_number()  # 정답을 만든다.
    if admin_check:  # admin 인 경우만, 정답을 알려준다.
        print("***admin: the answer is ", end='')
        for j in the_answer:
            print(j, end='')
        print(" ***")
    set_try_num = input("the maximum try num?(3~20)")
    try_num_check_FxxK = 3  # 참는 기회를 준다
    while True:
        try:
            set_try_num = int(set_try_num)
            if 3 <= set_try_num <= 20:  # 예쁜 값을 적었다면 break 한다.
                print("set TRY to", set_try_num)
                TRY_NUM = set_try_num
                break
            try_num_check_FxxK -= 1  # 이상한 값 적으면 기회를 하나씩 줄인다.
            if try_num_check_FxxK == 0:
                print("you don't have another chance")
                TRY_NUM = 3
                print("F YOU")
                break
            print("you have", try_num_check_FxxK, "chance")
            set_try_num = input("please write right number(3~20):")
        except:
            print("not integer.")
            try_num_check_FxxK -= 1  # 정수값을 적지 않으면 기회를 하나씩 줄인다.
            if try_num_check_FxxK == 0:
                print("you don't have another chance")
                TRY_NUM = 3
                print("F YOU")
                break
            print("you have", try_num_check_FxxK, "chance")
            set_try_num = input("please write number(3~20):")
    print("the try chance:", TRY_NUM)
    print_equal_15()
    print("If you want to show your history, write 'show my answers'")
    print_equal_15()

    for i in range(TRY_NUM + 1):
        if i == TRY_NUM:  # 맞출 기회를 모두 소진했을 때, 바깥의 if 문에서 거르기 위하여 사용되었다.
            break
        while True:
            print('try', i + 1, '>>', end='')
            user_answer = input()
            answer_error_check = is_error(user_answer)  # 답에 오류가 있는지 검사하고, 답을 정제한다.
            check_and_print = check_and_print_user_answers(user_answer)  # 커맨드인지 검사합다.

            if answer_error_check is False and check_and_print is False:  # 답도, 커맨드도 아닐 때
                print("your answer isn't right, try again")
            elif check_and_print is False:  # 답으로 적었을 때(커맨드가 아닐 때)
                user_answer = answer_error_check
                break
            else:  # 커맨드를 입력했을 때
                if not user_answers:  # 이제까지의 답이 하나도 없을 때
                    print("you don't have history!")
                else:  # 지금까지의 답을 알려준다.
                    print("print your answers")
                    for j in user_answers:
                        for k in j[0]:
                            print(k, end='')
                        print(" ", end='')
                        if j[1] == [0, 0]:
                            print("out")
                        else:
                            print("strike", j[1][0], "ball", j[1][1])

        answer_check = is_it_answer(user_answer, the_answer)  # strike, ball 개수를 세온다.
        if answer_check is False:  # 답이 맞았을 때, 맞았음을 알리고 for 문에서 탈출한다
            print("right answer!")
            break
        else:
            user_answers.append([user_answer, answer_check])  # 답과 상태를 저장한다.
            if answer_check == [0, 0]:  # strike 와 ball 이 모두 0일때: out!
                print("out!")
            else:  # strike, ball 개수 출력
                print('strike', answer_check[0], '// ball', answer_check[1])

    # 게임이 끝남
    user_answers = []
    if i is TRY_NUM:  # 횟수 내에 맞추지 못했을 때, 답이 무엇이었는지 알려준다.
        print('Oh, the answer was ', end='')
        for j in the_answer:
            print(j, end='')
        print("")

    while True:
        the_last_answer = input('one more game?(y/n) >>')  # 게임을 더 할 것인지 묻는다.
        yes_the_game = ['y', 'Y', 'yes', 'Yes', 'YES']  # 여러가지로 답을 해도 된다.
        no_the_game = ['n', 'N', 'no', 'No', 'NO']
        if the_last_answer in yes_the_game or the_last_answer in no_the_game:  # 적절한 답을 받을 때까지 입력을 받는다.
            break
    if the_last_answer in yes_the_game:  # 게임을 다시 시작한다
        print('ok')
    else:  # 게임을 완전히 끝내고 프로그램을 종료한다
        print('okok...')
        check = 0
