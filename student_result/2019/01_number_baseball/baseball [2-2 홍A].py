import random
import sys

again, can_double, mouth, game_num, re_flag = 0, 0, 1, 3, 0
life, hint_flag, hint_num, try_n, if_prankster, if_double, great_o, great_s, great_b, win_flag = 0, 0, 0, 0, 0, 0, 0, 0, 0, 0  # 값들 설정, 초기화
scoreboard = []
number_list = ['아기', '한', '두', '세', '네', '다섯', '여섯', '일곱', '여덟', '아홉',
               '열']  # game_num에 따라 표현이 달라지게. 예) game_num=5이면 '다섯' 자리 수, 8이면 '여덟' 자리 수...
q_list = ['은*는 정보충입니까?', '강** 선생님은 잘생겼습니까?', '이 게임은 재미있습니까?', '태*이는 학점이 4.3입니까?', '동*이는 빨간색 옷이 어울립니까?',
          '당신은 잘생겼습니까?', '덕*이는 물리를 잘합니까?', '예*이는 께북이를 키웁니까?', '윤*이는 과자를 좋아합니까?', '박**은 정보에 미쳤습니까?',
          '준*는 머리가 동그랍니까?',
          '동*이의 키는 155 이하입니까?', '문** 선생님은 잘생겼습니까?', '박** 선생님은 멋지십니까?', '도서관은 공부하기 편한 곳입니까?', '급식이 맛있습니까?',
          '양**은 음치입니까?',
          '양**은 춤을 잘 춥니까?', '강**는 화학을 잘합니까?', '동*이는 보건실 마스터입니까?']
a_list = ['yes', 'yes', 'yes', 'no', 'no',
          'no', 'no', 'yes', 'yes', 'yes',
          'yes', 'yes', 'yes', 'yes', 'no',
          'no', 'no', 'yes', 'yes', 'yes']
name_reply = [["홍**", "오, 그 정보충! 어쩐지 이상한 걸 많이 시도하더라"], ["양**", "재밌었어, 탱탱볼?"], ["강**", "선생님 사랑해요 감점만은 하지 말아주세요"],
              ["김**", "어? 왠지 제 컴퓨터 카메라로는 아무것도 안보이더니 동*님이었군요!"], ["신**", "청경채 좋아하는 밥돌이..."], ["강**", "땅콩은 화학을 잘해"]]
memo_list = []
special_life = [0, 720, 210, 207, 777, 3, 529, 203]
ans_list = []


def memo_write():  # 메모장 켜주는 함수
    while True:
        player_say = input()
        if player_say == '!!!':  # 메모장 끄는 명령어
            return
        elif player_say == 'clear':  # 한 줄을 지우는 명령어
            memo_list.pop()
        else:
            memo_list.append(player_say)


def memo_print():  # 메모 출력하는 함수
    for memos in memo_list:
        print("%s" % memos)


def quiz():  # 깜짝 퀴즈를 내는 함수
    if random.randint(1, 6) == 1 and mouth is True:  # 1/6 확률로 깜짝 퀴즈를 진행
        q_n = random.randint(0, len(q_list) - 1)  # q_num개 중 하나를 무작위로 선택
        eq_print()
        print("깜짝 퀴즈 타임!\n%s \n yes 아니면 no로 대답해보세요." % q_list[q_n])

        eq_print()
        str3 = input()

        eq_print()
        if str3 == a_list[q_n]:  # T. 변수명에 축약어를 너무 줄이지 마세요.
            print("정답! 생명 +3")  # 맞춘다면 생명을 3 추가함
            return 3
        else:
            print('틀렸습니다! 나중에 다시 도전...')
    return 0


def count(list_temp):  # 아웃, 스트라이크, 볼을 세는 코드
    O, S, B = 0, 0, 0  # python 에서 대문자 변수명은 '상수' 를 의미합니다.
    if not can_double:
        for i in range(0, game_num):
            hit_flag = 0
            for j in range(0, game_num):
                if ans_list[j] == list_temp[i]:
                    hit_flag = 1
                    if i == j:
                        S += 1
                    else:
                        B += 1
            if hit_flag == 0:
                O += 1
    else:  # 수를 중복하여 생각할 수 있을 때
        for i in range(0, game_num):
            hit_flag, strike_flag = 0, 0
            for j in range(0, game_num):
                if ans_list[j] == list_temp[i]:
                    hit_flag = 1
                    if i == j:
                        strike_flag = 1
            if strike_flag == 1:
                S += 1
            elif hit_flag == 1:
                B += 1
            else:
                O += 1
    return O, S, B


def eq_print():  # 글들을 구분해주는 선을 만들어주는 함수
    print('=' * 60)


def life_print(x):  # 남은 목숨을 출력함
    print("목숨이 %d개 남았습니다." % x)
    if mouth:
        if x == 7:
            print("제 생일은 7월이에요!")
        if x == 20:
            print("제 생일은 20일이에요!")


def make_ans(n):  # 수를 하나 생각함
    tmp_list = []  # 수를 생각하는 리스트
    chk = [0] * 10  # 체크 배열
    for i in range(0, n):
        x = random.randint(0, 9)
        while chk[x] and can_double == 0:
            x = random.randint(0, 9)
        tmp_list.append(x)
        chk[x] = True
    return tmp_list


def retry():  # 재도전 여부를 묻는 함수
    print("다시 하실래요? 다시 하시려면 yes를, 아니면 no를 입력해주세요.")
    player_ans = input()
    eq_print()
    # if player_ans == 'yes' or player_ans == 'ㅛㄷㄴ':
    if player_ans in 'yes ㅛㄷㄴ'.split():
        print("그러면 숫자 하나를 다시 선택해볼게요...")
        return True  # 재도전
    # elif player_ans == 'no' or player_ans == 'ㅜㅐ':
    elif player_ans in 'no ㅜㅐ'.split():
        print("아쉽네... 재밌었어요!")
    else:
        # if mouth == True:
        if mouth:
            print("끝까지 말을 안듣네;;")
    return False  # 재도전 X


def score_save(n):  # 점수를 저장 - 이름을 물어봄
    print("이름이 뭐에요?")
    player_name = input().strip('')
    eq_print()
    if mouth:
        reply_flag = False
        for set_reply in name_reply:
            if set_reply[0] == player_name or set_reply[0][1:3] == player_name:
                reply_flag = True
                print("%s" % set_reply[1])  # set_reply 리스트에 이름이 있으면 특별한 대답
        if reply_flag:
            print("재밌었어요, %s님!" % player_name)
    else:
        print("저장되었습니다.")
    scoreboard.append([player_name, n])
    scoreboard.sort(key=lambda x: x[1])  # 점수가 낮은 순으로 배열


def score_print():  # 점수판 출력
    cnt = 1
    if len(scoreboard) == 0:
        print("아직 아무것도 없네요.")
        return
    eq_print()
    print("등수      이름       시도 횟수")
    for i in scoreboard:
        print("%d      %s       %d" % (cnt, i[0], i[1]))
        cnt += 1
    eq_print()


def select_gamenum():  # 생각할 숫자 개수를 정함
    gamenum_temp = game_num
    if mouth:
        if again == 1:
            print(
                "이번에는 좀 더 재밌게 해보려고 하는데, %s 자리가 아니라 다른 숫자 개수로 해보고 싶어요!\n하고 싶으시면 yes, 아니면 no를 입력해주세요." % number_list[
                    gamenum_temp])
        if again > 1:
            print("다른 숫자 개수로 해보고 싶나요? yes 또는 no로 대답해주세요.")
    else:
        print("다른 자리수로 할까요? (yes/no)")
    # 몇 자리수로 할 것인지를 입력받음
    str1_flag = 1
    while str1_flag:  # flag값이 1이면 계속 입력받게 하였음
        str1_flag = False
        str1 = input()
        eq_print()
        if str1 == 'yes':  # yes일 때 - 1~9 중 하나를 입력받음
            print("몇 자리 수로 하고 싶으세요? (1~9 중 하나만 입력해주세요)")
            print("랜덤을 원하시면 random을 입력해주셔도 됩니다.")
            str2_flag = True
            while str2_flag:
                str2 = input()
                str2_flag = False
                eq_print()
                if len(str2) == 1 and '0' <= str2[0] <= '9':
                    gamenum_temp = int(str2)  # 1~9 중 하나로 game_num을 바꿈, 입력받는 자릿수가 달라짐
                    print("앞으로는 %s 자리 수로 게임할 거에요!" % number_list[gamenum_temp])
                elif str2 == 'random':
                    gamenum_temp = random.randint(1, 9)
                    print("%s자리 수로 게임할 거에요!" % number_list[gamenum_temp])
                else:
                    print("다시 입력하세요")
                    str2_flag = True

        elif str1 == 'no':  # no일 때 - 그대로 계속 함
            print("그럼 계속 %s개로 하죠 뭐" % number_list[gamenum_temp])

        else:
            print("? yes나 no중 하나 입력하라고요")
            str1_flag = 1  # 틀린 값을 입력했을 때 다시 입력받도록 함

    return gamenum_temp


def input_life():  # 목숨을 입력받음, 특별한 목숨 숫자는 선택하여 이스터에그로 만듦
    global game_num, ans_list, mouth, can_double
    if mouth:
        print("목숨은... 얼마로 드릴까요? 양심적으로 숫자를 입력해주세요...")
    else:
        print("목숨을 입력해주세요.")
    life_temp = None
    # while life_temp == None:  # 목숨에 정상적인 입력이 들어올 때까지
    while life_temp is None:  # 목숨에 정상적인 입력이 들어올 때까지
        try:
            print("목숨 : ", end='')
            life_temp = int(input())
        except ValueError:  # 숫자가 아닌 입력을 했을 때 발생하는 오류를 except 함
            eq_print()
            print("숫자만 똑바로 입력하세요 ^^")
        eq_print()

    if life_temp <= 0:  # 목숨을 0 이하로 입력했을 때 - 게임 종료
        print('그냥 죽어라')
        return 0

    elif life_temp == 720:  # 이스터에그 - 생각한 숫자를 무작위 순서로 알려준 후, 순서만 맞추게 함
        print("7월 20일은 제 생일이에요! 감사합니다!\n제가 생각하는 숫자 %s 개는" % number_list[game_num], end='')
        rand_num = list(range(game_num))
        random.shuffle(rand_num)
        for i in rand_num:
            print(" %d" % ans_list[i], end='')  # 무작위 순서로 ans_list에 있던 숫자들을 출력
        print("입니다.\n목숨이 %s 개로 설정되었습니다." % number_list[game_num])  # 목숨 개수를 새로 설정함
        life_temp = game_num

    elif life_temp == 210:  # 이스터에그 - 난이도 조절
        print("동혁이 하고 싶은 거 다 해")
        print("자리수가 7로 변경됩니다. 목숨이 99999999999로 조정됩니다.")
        life_temp = 99999999999
        game_num = 7
        ans_list = make_ans(game_num)

    elif life_temp == 207:  # 이스터에그 - 난이도 조정
        print("엥... 안녕 친구야. 너라면 이 정도는 풀어야지")
        print("자리수가 5로 변경됩니다.")
        game_num = 5
        ans_list = make_ans(game_num)

    elif life_temp == 529:  # 이스터에그 - 난이도 조져
        print("너는 내가 진짜 짜증나게 할거야")
        print("자리수가 5로 변경됩니다. 숫자 중복이 가능해집니다.")
        game_num = 5
        can_double = 1
        ans_list = make_ans(game_num)

    elif life_temp == 203:  # 이스터에그 - 난이도 조오져
        print("죽어라, 유사 정보충!")
        print("자리수가 7로 변경됩니다. 숫자 중복이 가능해집니다.")
        game_num = 7
        can_double = 1
        ans_list = make_ans(game_num)
        sub, sum = 1, 0
        for i in ans_list:
            if i != 0:
                sub *= i
            sum += i
        print("0을 제외한 숫자들 전체의 곱은 %d입니다!" % sub)
        print("아, 그리고 합은 %d!" % sum)

    elif life_temp == 777:  # 이스터에그 - 생각한 숫자 중 하나를 알려줌
        print("행운이 당신을 찾아왔어요!\n제가 생각한 수의 숫자 하나를 알려드릴게요.\n제가 생각한 숫자엔 '%d'이(가) 들어있어요" % ans_list[
            random.randint(0, game_num - 1)])

    elif life_temp > 100:  # 100 이상으로 설정할 시 목숨을 10으로
        print('양심 어디?\n목숨이 10으로 설정되었습니다.')
        life_temp = 10

    elif life_temp <= 3:  # 이스터에그 - 목숨이 3 이하일 때는 마지막 숫자 하나를 맞추게 함
        print('괜찮으시겠어요? 이 정도로는 안될텐데...\n 제가 생각한 숫자는 ', end='')
        for j in range(game_num - 1):
            print("%d" % ans_list[j], end='')
        print("? 에요.\n마지막 자리 수 하나만 맞춰보세요!")

    else:
        print("행운을 빌게요!\n다음 판에는 목숨을 %d로 설정해보시는것도 재밌을거에요" % special_life[random.randint(0, len(special_life) - 1)])

    return life_temp


def player_ans2():  # 정상적인 '시도'를 받음, 여기서 숫자를 입력하느냐, hint 나 watch 등의 명령어를 입력하느냐가 따로 나뉨
    global hint_num, re_flag, mouth, hint_flag
    # 수 입력 과정
    flag = 1  # 정상적으로 입력이 들어오지 않았거나 / watch, hint가 입력되었거나 / 처음 입력받을 때 flag=1
    while flag:  # 숫자 입력이 아닐 때 계속 입력받는 것을 반복함
        flag = False
        eq_print()
        if mouth:
            print("수를 입력하세요. help 를 입력하시면 도움말이 출력됩니다.")
            if if_prankster and random.randint(1, 2) == 1:  # 만약 입력을 이상하게 넣은 적이 있다면, 1/2 확률로 경고함
                print("%s 자리로 입력하세요 괜히 딴거 입력하지 마시고" % number_list[game_num], end='')
                print("!" * random.randint(1, 5))
        else:
            print("%s 자리 수 " % number_list[game_num], end='')
        print("입력 : ", end='')

        # 입력을 받음
        str_temp = input().strip(' ')
        if str_temp == 'watch':  # watch 라면, 지금까지의 기록을 모두 출력함(play_list 에 저장되어 있음)
            if len(play_list) == 0:  # play_list 에 아무것도 없다면 출력하지 않음
                print("아직 아무것도 없습니다.")
            else:
                eq_print()
                cnt = 1
                for one_list in play_list:  # 지금까지의 기록 하나하나 다시 계산을 실행함
                    o, s, b = count(one_list)
                    # 출력 함수
                    print("%d - " % cnt, end='')
                    for j in range(game_num):
                        print("%d" % one_list[j], end='')
                    print(' %dS %dB %dO' % (s, b, o))
                    cnt += 1
            flag = True
        if str_temp == 'help':  # 도움말 출력
            eq_print()
            print("""watch 를 입력하면 지금까지 입력한 시도들이 출력됩니다.
hint 를 입력하면 무언가 나오긴 합니다.
RE를 입력하시면 처음부터 다시 하실 수 있습니다.
memo 를 입력하시면 메모장이 켜집니다.""")
            flag = True
        if str_temp == 'hint' and mouth:  # 힌트를 줍니다. 이 때 입력한 횟수에 따라 다릅니다.
            if hint_flag == 0:
                print("%d 번째 숫자는 0과 9 사이에 있어요." % (hint_num + 1))

            elif 2 > hint_flag > 0:
                print("%d 번째 숫자는 %d ~ %d 사이에 있어요." % (
                    hint_num + 1, max(0, ans_list[hint_num] - random.randint(0, 2)),
                    min(ans_list[hint_num] + random.randint(0, 2), 9)))

            elif hint_flag == 2:
                print("끈질기네... %d 번째 숫자는 %d입니다." % (hint_num + 1, ans_list[hint_num]))

            else:
                print("힌트 이제 없어 저리가")
                hint_flag = -1
                hint_num = (hint_num + 1) % game_num

            hint_flag += 1
            flag = True

        if str_temp == 'Red Silver Plate':
            print("이건 코드를 뜯어봤어야 알 수 있는 건데... 굳이?")
            print("제가 생각하는 숫자 %s개는" % number_list[game_num], end='')
            rand_num = list(range(game_num))
            random.shuffle(rand_num)

            for i in rand_num:
                print(" %d" % ans_list[i], end='')  # 무작위 순서로 ans_list에 있던 숫자들을 출력
            print("입니다. 만족하셨어요?")  # 목숨 개수를 새로 설정함
            flag = True

        if str_temp == '참':
            if mouth:
                print("'참'을 하실 정도로 오오오오오래 생각하셨군요!")
                print("정답 공개!\n정답 : ", end='')

            rand_num = list(range(game_num))

            for i in rand_num:
                print("%d" % ans_list[i], end='')  # 무작위 순서로 ans_list에 있던 숫자들을 출력

            if mouth:
                print("입니다.")  # 목숨 개수를 새로 설정함
            else:
                print()
            flag = True

        if str_temp == 'RE':  # 다시 시작
            if mouth:
                print("뭘 하셨길래? 뭐 첨부터 다시 해드릴게요")
            else:
                print("처음부터 다시 시작합니다.")
            re_flag = 1

        if str_temp == 'Shut Up':  # 조용해집니다. 꼭 해보세요!
            mouth = not mouth
            print('넹', end='')
            print('!' * mouth)
            flag = True

        if str_temp == 'memo':  # 메모를 기록합니다.
            print("메모를 끄시려면 !!!를 입력해주세요. 메모를 하나 삭제하려면 clear를 입력해주세요.")
            eq_print()
            memo_print()
            memo_write()
            flag = True

    return str_temp


def check():
    # 수가 올바르게 들어왔는지 확인하는 코드
    # 만약 다른 문자가 들어와도, 숫자 개수가 올바르게 들어왔다면 넘어감
    # 1v2cd3을 123이 들어왔다고 인식하게 만듦
    num_cntt = 0
    num_listt = []
    num_chkt = [0] * 10
    num_ifdoublet = 0

    for c in str:
        if '0' <= c <= '9':  # 입력받은 str 에 숫자가 있다면 cnt 를 세줌
            num_cntt += 1
            if num_chkt[int(c)] == 1:  # 만약 입력한 숫자들 중 중복되는 숫자가 있다면 if double 을 체크함
                num_ifdoublet = 1
            else:
                num_chkt[int(c)] = 1
            num_listt.append(int(c))
    return num_cntt, num_listt, num_chkt, num_ifdoublet


def response(cnt, ifdouble):
    global if_pranster, life, try_n, if_double
    if cnt != game_num:  # 원하는 자릿수와 cnt 가 다르다면, 잘못된 입력임
        if mouth:
            print("내가 장난치지 말랬지? 목숨 날라감")
        else:
            print("잘못 입력하셨습니다. 숫자 %s개를 입력해주세요.\n 생명의 절반이 차감됩니다." % number_list[game_num])
        if_prankster = True  # 잘못 입력한 기록이 남음 (171줄 참조)
        life -= (life - try_n) // 2  # 생명 절반이 날아가고, 다시 입력을 받음
        return 1

    # if num_ifdouble == True and can_double == False:  # 중복되는 숫자가 있을 때
    if num_ifdouble and can_double is False:  # 중복되는 숫자가 있을 때
        print("같은 숫자를 중복해서 입력하시면 안돼요. ", end='')  # 경고
        if mouth:
            if ifdouble == 1:  # 두 번째 반복했을 때
                print("제가 아까 한 번 말씀드렸지 않나요?")
            elif ifdouble % 5 == 1:  # 다섯번마다 한 번씩
                print("전 이제 포기했습니다.")
            elif ifdouble > 3 and random.randint(1, 3) == 1:  # 네 번 넘게 말했을 때
                print("솔직히 개도 세 번 말하면 알아듣는데...")
            elif ifdouble > 1:  # 세네번 말했을 때
                print("제가 아까 말씀드렸지 않나요? 한 %d번 정도?" % (ifdouble))
            else:  # 이번이 처음이라면 봐줌(생명이 줄지 않는다)
                print("이번만 봐드립니다.")
                try_n -= 1
        else:
            print()
        if_double += 1
        return 1
    return 0


def prior_print(try_n, life):
    if if_prankster and mouth:  # 만약 장난을 쳤다면(입력을 이상하게 넣었다면) 경고함
        print("%d번째 몸부림" % try_n)
    else:
        print("%d번째 시도" % try_n)
    if life == try_n:  # 생명이 하나 남았으면 경고함
        print("마지막 기회입니다. 신중을 기하세요")
    else:  # 남은 생명을 출력함
        life_print(life - try_n + 1)


def hit(out_num, strike, ball):  # 들어온 아웃, 스트라이크, 볼 점수를 가지고 평가함
    global great_s, great_o, great_b
    # 신기록 저장(스트라이크를 많이 할수록 좋은 점수라고 가정)
    if great_s < strike:
        great_s, great_b, great_o = strike, ball, out_num

    if mouth:
        print(">>> %d STRIKE %d BALL %d OUT <<<" % (strike, ball, out_num))  # 결과 출력
    else:
        print("%dS %dB %dO" % (strike, ball, out_num))  # 결과 출력
    if strike + ball == game_num and strike != game_num and can_double == False and mouth == True:  # 아웃이 없을 때
        print('오 이제 자리만 맞추시면 되겠네요')
    if out_num == game_num and mouth == True:  # 맞춘 숫자가 없을 때
        print("ㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋ\n%d아웃ㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋ\n실력 "
              "실화야? ㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋ""" % game_num)
    if strike == game_num:
        return 1
    return 0


def game_end_lose():  # 게임을 졌을 때
    global again
    eq_print()
    again += 1
    print("게임이 끝났습니다.")
    print("답 : ", end='')
    for j in range(game_num):  # 답 출력
        print("%d" % ans_list[j], end='')
    print()
    if great_b or great_s:  # 신기록 출력
        print("아쉽네요! 당신의 최고점수는 %dS %dB %dO입니다." % (great_s, great_b, great_o))
    else:  # 만약 볼 또는 스트라이크가 없을 때
        if mouth:
            print("아쉽네요! 그래도 하나는 맞출 줄 알았는데.")
    eq_print()


def game_end_win():  # 게임을 이겼을 때
    global win_flag, again
    win_flag = True  # 승패 여부를 표시
    again += 1  # 몇 판 했는지
    print("%d번째에 답을 맞추셨어요! 답 : " % try_n, end='')
    for j in range(game_num):  # 답 출력
        print("%d" % ans_list[j], end='')
    print()


# 야구 게임 시작
# ============================================================================
eq_print()
print("야구게임")
eq_print()
print("""제가 정한 %s 자리 숫자를 맞추는 게임이에요!
%s 자리 숫자를 입력하시면
숫자와 자리가 모두 맞으면 스트라이크(S)
숫자만 맞고 자리가 틀리면 볼(B)
숫자가 틀리면 아웃(O) 
을 출력해 드릴거에요""" % (number_list[game_num], number_list[game_num]))

while True:
    if again:  # 만약 게임을 처음 하는게 아니라면 생각하는 숫자의 개수를 다르게 할 수 있음
        print("%d번째 게임, 다시 시작합니다!" % (again + 1))
        eq_print()
        game_num = select_gamenum()
    can_double = 0
    ans_list = make_ans(game_num)
    play_list = []  # 지금까지 입력한 시도들을 저장함
    # 목숨 입력
    eq_print()
    life = input_life()
    if life == 0:
        continue
    hint_flag, hint_num, try_n, if_prankster, if_double, great_o, great_s, great_b, win_flag, re_flag = 0, 0, 0, 0, 0, 0, 0, 0, 0, 0  # 값들 설정, 초기화
    # T. python PEP8 에 의하면 한줄에 한개의 변수만 초기화하는것을 권장합니다.

    eq_print()
    print("!!!!!!!!!%s 자리 수를 입력하시면 됩니다.!!!!!!!!!" % number_list[game_num])
    while life - try_n >= 1:  # 목숨이 남았을 때
        life += quiz()
        eq_print()
        try_n += 1
        prior_print(try_n, life)

        str = player_ans2()  # T. str 이나 int 와 같이 의미가 통용되는 변수명은 사용하지 않는것이 좋습니다.
        if re_flag == 1:
            break
        eq_print()

        # 수가 올바르게 들어왔는지 확인하는 코드
        # 만약 다른 문자가 들어와도, 숫자 개수가 올바르게 들어왔다면 넘어감
        num_cnt, num_list, num_chk, num_ifdouble = check()
        may_go_home_flag = response(num_cnt, if_double)

        if may_go_home_flag:
            continue

        play_list.append(num_list)
        out_num, strike, ball = count(num_list)

        win = hit(out_num, strike, ball)

        if win:  # 모두 맞췄을 때(정답)
            game_end_win()
            eq_print()
            score_save(try_n)  # 점수판에 점수 저장
            eq_print()
            player_retry = retry()  # 재도전 여부를 물어봄
            if player_retry:
                break
            else:
                sys.exit(0)

    if re_flag:  # RE를 입력했을 때
        continue

    # 숫자를 맞추지 못했을 때
    if not win_flag:
        game_end_lose()
        player_retry = retry()
        if player_retry:
            continue
        else:
            sys.exit(0)

    # 점수판 출력
    eq_print()
    print("혹시 점수판 보고 싶으시면 show라고 입력해주세요. 싫다면 아무 글자나 입력해주세요.")
    player_ans = input()
    if player_ans == 'show':
        score_print()
