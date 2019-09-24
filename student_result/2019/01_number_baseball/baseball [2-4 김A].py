import random

memo = [] #여태까지 user가 입력한 정보를 저장하는 리스트입니다
cnt = 1 #게임의 턴 수를 세는 변수입니다
special_def = ["help", "show", "show_ans"] #특수한 기능을 가진 함수를 저장한 리스트입니다


def explain() -> None:
    """
    숫자 야구의 규칙을 간략하게 설명해주는 합수입니다
    :return: None
    """
    print("숫자 야구 게임은 정해진 숫자를 맞추는 게임입니다.\n숫자가 정답에 포함되어 있고 위치도 맞으면 s,포함만 되어있다면 b, 둘 모두 아니라면 o입니다")
    print("입력은 붙여서 하세요!")
    print("재밌게 하세요!")
    print()


def make_sec_num(num_len : int) -> str:

    '''
    랜덤한 숫자 문자열(정답)을 만들어 반환해주는 함수입니다.
    :param num_len: 만들어지는 숫자 문자열의 길이를 뜻합니다
    :return: 랜덤하게 num_len 길이만큼의 숫자 문자열을 return합니다
    '''

    numbers = list(range(10))  # range() 함수의 반환형은 iterator 형식의 객체 / list() 를 이용하여 list 형으로 변경
    random.shuffle(numbers)  # 첫 숫자(가장 큰자리 수)가 0이 아닐 때까지 list 의 값을 임의의 순서로 섞는다.
    ans_num = ''
    for i in range(num_len):  # 섞은 숫자를 이용하여 num_len 길이 만큼의 문자열을 만든다.
        ans_num += str(numbers[i])
    return ans_num


def num_right(user_n: str) -> bool:
    """
    user가 입력한 숫자문자열이 양식에 맞는지 확인합니다.
    1. 문자열이 숫자로만 구성되어있는지 확인합니다.
    2. 반복된 숫자가 없는지 확인합니다.
    :param user_n: user가 입력한 숫자 문자열입니다
    :return: user_n이 양식에 맞다면 True, 그렇지 않으면 False를 return합니다
    """
    for k in user_n:
        if '0' > k or '9' < k:
            return False   #문자열이 숫자로만 구성되어 있는지 확인

    if len(user_n) != len(set(user_n)):
        return False   #문자열에 중복이 없는지 확인

    return True  #위 두 조건을 통과하면 정상 문자열로 판단


def num_cmp(user_n : str, ans_num: str, num_len: int) -> bool:
    """
    user가 입력한 답과 정답을 비교하여 s,b,o를 출력해주고
    정답인지 아닌지도 알려줍니다.
    또한 user의 입력과 s,b,o 기록을 memo에 저장합니다
    :param user_n: user가 입력한 답입니다
    :param ans_num: 정답입니다
    :param num_len: 게임을 진행하는 숫자의 길이입니다
    :return: 정답인지 아닌지 return 합니다
    """
    sbo_li = [0, 0, 0] #s,b,o를 저장할 리스트

    for k in user_n:
        if k in ans_num:
            if user_n.index(k) == ans_num.index(k):
                sbo_li[0] += 1
            else:
                sbo_li[1] += 1
        else:
            sbo_li[2] += 1 #정답과 user의 추측을 비교하여 s,b,o 점수 매김

    print("s:%d b:%d o:%d" %(sbo_li[0], sbo_li[1], sbo_li[2])) #s,b,o를 유저에게 보여줌
    print()

    memo.append((user_n, sbo_li[0], sbo_li[1], sbo_li[2])) #memo에 user의 숫자와 s,b,o를 저장함

    if sbo_li[0] == num_len:
        return True #정답을 맞췄을 경우 True return
    else:
        return False #틀렸을 경우 false return


def len_input() -> int:
    """
    user가 게임을 몇자리로 플레이할지 입력받는 함수입니다
    :return: user가 설정한 길이를 return 합니다
    """
    print("몇 자리 숫자로 플레이하시겠습니까? (1자리 이상 9자리 이하로 가능합니다)")
    num_len_ip = ''

    while type(num_len_ip) is not int:
        k = input()
        if k.isdigit() is False or len(k) >= 2 or k < '1':
            print("똑바로 좀 입력합시다")
            continue #user가 입력하는 input이 올바른지 확인하고 그렇지 않으면 계속해서 다시 받음
        else:
            num_len_ip = int(k)
            print("좋아요 %d자리 숫자로 플레이하죠" % num_len_ip)
            print() #user가 제대로 입력했으면 user의 선택을 다시 한번 알려줌

    return num_len_ip #user가 선택한 게임 진행 숫자의 길이 return


def get_input(num_l: int, cnt: int) -> str:
    """
    user로 부터 num_l만큼 길이의 숫자 문자열을 입력받는 함수입니다.
    입력이 양식에 맞는지 체크하고 그렇지 않을 경우 다시 입력하도록합니다
    :param num_l: user가 입력해야하는 숫자문자열의 길이입니다
    :param cnt: 턴 수 입니다
    :return: user가 입력한 숫자 문자열을 return 합니다
    """
    user_n = ""
    print("%d번째 턴입니다. 숫자를 입력하세요" % cnt)
    print("참고로 숫자 대신 help를 입력하면 숨겨진 함수를 볼 수 있습니다")

    while len(user_n) != num_l or num_right(user_n) is False:

        if user_n == "":
            user_n = input()
            continue #처음에 경고 메시지 안 띄우게 해주는 역할

        if user_n in special_def:
            if user_n == "show":
                show()
            elif user_n == "show_ans":
                show_ans()
            elif user_n == "help":
                help()
            print("이제 다른 것을 입력해보세요") #특수 함수를 입력했을 때 이를 실행함

        else:
            print("제대로 좀 입력하자;;") #잘못된 입력일 때 경고 메시지

        user_n = input()

    return user_n #user의 입력 return


def play_again() -> bool:
    """
    다시할지 그만둘지를 입력받는 함수입니다
    :return: Yes가 입력되면 True를, No가 입력될 경우 False를 return합니다
    """
    play = ''

    print("다시 하시겠습니까? 다시하려면 Yes, 아니라면 No를 눌러주세요")

    while play != "Yes" and play != "No":

        play = input()

        if play == "Yes":
            print("좋아요 다시합시다")
            return True #Yes를 입력할 경우 True return

        elif play == "No":
            print("넹 잘가요ㅃㅃ")
            return False #No를 입력할 경우 False return

        else:
            print("Yes나 No 중에 하나로 답하세요^^") #Yes나 No가 아닐 경우 다시 입력하도록 경고


def show() -> None:
    """
    여태까지의 기록을 보여주는 함수입니다
    :return: None
    """
    for k in memo:
        print("num:%s | s:%d | b:%d | o:%d" % (k[0], k[1], k[2], k[3])) #memo에 저장된 기록을 출력해줌
    print()


def show_ans() -> None:
    """
    정답을 보여주는 함수입니다
    :return: None
    """
    print("정답은 %s입니다" % ans) #정답을 출력함
    print()


def help() -> None:
    """
    자신을 제외한 특별 함수들을 보여주는 함수입니다
    :return: None
    """
    print("help입니다!")
    for k in special_def:
        if k == "show":
            print("show: 여태까지의 기록을 보여줍니다")
        elif k == "show_ans":
            print("show_ans: 정답을 보여줍니다")
    print()


if __name__ == '__main__':
    big_cnt = 1 #게임의 횟수를 알려주는 변수입니다
    pl = True #게임을 on/off 해주는 변수입니다

    while pl is True:
        tmp = False #한 게임 안에서 정답을 맞췄는지를 알려주는 변수입니다

        if big_cnt == 1:
            explain() #첫 판인 경우 규칙을 설명함

        memo.clear()

        num_len = len_input()

        ans = make_sec_num(num_len)

        cnt = 1
        big_cnt += 1

        while tmp is False and cnt <= 10: #정답을 맞추지 않았고, 턴수가 10회가 넘지 않았으면 반복

            user_num = get_input(num_len, cnt)

            tmp = num_cmp(user_num, ans, num_len)

            if tmp is True:
                print("%d번만에 정답을 맞추셨네요!" % cnt)
            else:
                cnt += 1 #턴 수 증가
                continue

        if cnt > 10:
            print("이걸 못 맞추네요?ㅋㅋㅋㅋㅋㅋㅋㅋ 걍 새로 하죠") #10턴 동안 답을 맞추지 못한 경우 조롱
        pl = play_again()




