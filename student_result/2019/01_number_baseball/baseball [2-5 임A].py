"""
Title   숫자야구 게임
Author  25** 임**
Date    2019.09.20
2019학년도 2학기 객체지향프로그래밍
"""
import random  # 랜덤으로 맞출 숫자를 만들기 위해 random 모듈을 가져온다.


def ran_num():  # 랜덤으로 세 원소의, 중복 없는, 0~9의 정수로 이루어진 리스트를 리턴하는 함수이다.
    tmp = list(range(0, 10))  # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]의 리스트를 만든다.
    random.shuffle(tmp)  # 위 리스트를 무작위 순서로 배열한다.
    return tmp[0:3]  # 무작위로 배열된 리스트에서 앞의 3개 값만을 가진 리스트를 리턴한다.


# T. list, dict, set 등과 같은 용어들은 변수명의 사용하지 않는 것을 권장함.
def input_check(list):  # 사용자의 입력값을 리스트로 받아서 조건에 충족하는지 확인하는 함수이다. 에러가 없으면 1을, 있으면 0을 리턴.
    err_set = set()  # 오류가 날 때마다 값을 추가하는데, 같은 오류에 대해서는 하나의 원소만이 들어가도록 set 자료형을 사용했다.
    cnt = 0  # 사용자의 입력값의 길이이다.
    err_cnt = 0  # 몇 개의 에러가 발생했는지 저장하는 값이다.

    for i in list:  # 매개변수로 받은 리스트 내의 문자열을 모두 체크한다.
        # cnt += 1  # 리스트 원소 개수를 센다.
        for j in list[cnt:]:  # 리스트의 현재 위치 이후의 값들 중
            if i == j:  # 현재 값과 같은 것이 있다면
                err_set.add('rept')  # err_set 에 '중복 오류'가 발생했다고 저장한다.

    cnt = len(list)

    # if cnt is 0:  # 만약 사용자가 아무 입력도 하지 않았다면
    if cnt == 0:  # 만약 사용자가 아무 입력도 하지 않았다면  # T. is 는 객체의 identity 가 같은지 구분. 변수 값을 비교할 때는 적절하지 않음.
        err_set.add('null')  # err_set 에 '공백 오류'가 발생했다고 저장한다.
    elif cnt is not 3:  # 만약 사용자 입력값의 길이가 3이 아니라면
        err_set.add('size')  # err_set 에 '길이 오류'가 발생했다고 저장한다.

    for i in list:
        if i < '0' or '9' < i:  # 만약 사용자 입력값 내에 정수가 아닌 다른 모든 문자가 들어있다면
            err_set = set()  # '숫자 아님 오류'가 발생할 시에는 '중복 오류', '길이 오류' 알림을 띄우지 않는다.
            err_set.add('numb')  # err_set 에 '숫자 아님 오류'가 발생했다고 저장한다.

    # T. 조금더 줄일 수 있는 구문이지 않을까 싶습니다.
    if cnt == 5:  # 숫자 사이에 공백을 넣은 사용자들을 위한 에러이다. 공백을 포함해 총 5개의 원소가 있을 것이다.
        if '0' <= list[0] <= '9' and '0' <= list[2] <= '9' and '0' <= list[4] <= '9':  # 1, 3, 5번째의 원소는 0~9의 정수라면
            if list[1] == list[3] == ' ':  # 만약 2, 4번째의 원소가 공백이라면
                err_set = set()  # 지금까지 에러를 지우고
                err_set.add('spac')  # err_srt 에 '공백 오류'가 발생했다고 저장한다.
            if list[0] == list[2] or list[2] == list[4] or list[4] == list[0]:  # 만약 값의 중복도 있다면
                err_set.add('rept')  # err_set 에 '중복 오류'가 발생했다고 저장한다.

    end_chr = ', '  # 기본적으로 에러 출력의 end 값은 콤마로 설정된다.
    end_cnt = len(err_set)  # end_cnt 는 현재 사용자의 입력값 중에서 에러가 몇 종류나 있는지를 저장한다.
    if len(err_set):  # 만약 에러가 하나라도 있다면
        print('입력 오류:', end=' ')  # 입력에서 오류가 있다고 출력한 뒤

    for i in err_set:  # 발생한 에러의 종류들이 하나씩만 저장된 err_set 의 원소들마다
        end_cnt -= 1  # err_cnt를 아직 탐색하지 않은 err_set 의 원소의 수로 정하고
        if end_cnt == 0:  # 만약 이를 제외하고 에러가 더 있지 않다면
            end_chr = ' 입력하세요.\n' + '=' * 80 + '\n'  # 에러 출력을 마무리한다.
        print('%s' % (err_dict[i]), end=end_chr)  # 딕셔너리 err_dict 에서 각각 에러명에 해당하는 에러 알림을 출력한다.

    err_cnt = len(err_set)  # 발생한 에러 종류의 수를 err_set 의 원소 개수로 정한다.
    return not bool(err_cnt)  # 에러가 발생했다면 0을, 에러가 발생하지 않았다면 1을 리턴한다.


def correct_chk(attemp, ans):  # 시도 횟수와 사용자 입력값을 전해받아 S, B, O를 출력하고 정답 여부를 1, 0으로 리턴한다.
    chk = 0  # 사용자 입력값이 입력조건을 만족하면 1, 아니면 0이 된다.
    strike = 0  # 사용자가 입력한 세 개의 수 중 숫자와 위치가 모두 일치하는 것의 개수.
    ball = 0  # 사용자가 입력한 세 개의 수 중 숫자만 일치하는 것의 개수.
    out = 0  # 사용자가 입력한 세 개의 수 중 숫자가 일치하지 않는 것의 개수.

    while not chk:  # 사용자 값이 입력조건을 만족하지 않는 동안
        print('추측 %d:' % attemp, end=' ')
        guess = list(input())  # 사용자의 입력값을 받아 리스트 형식으로 바꾼 뒤
        chk = input_check(guess)  # input_check 함수를 통해 입력조건을 만족하는지 확인한다. 여기서 조건을 만족하면 chk 값이 1이 되어 while 문을 빠져나간다.

    for i in range(3):  # 입력조건을 만족하는 입력값의 원소는 3개이므로 3번동안
        if ans[i] == guess[i]:  # 만약 위치와 값이 모두 같은 것이 있다면
            strike += 1  # 스트라이크 수를 하나 늘린다.
        for j in range(3):
            if ans[i] == guess[j] and i != j:  # 사용자 입력값과 정답 중 숫자가 같으면서 위치는 다른 수가 있다면
                ball += 1  # 볼 수를 하나 늘린다.

    out = 3 - strike - ball  # 아웃의 수는 스트라이크도, 볼도 아닌 수의 개수이다.

    print("┌─────┬─────┬─────┐")
    print("│ %d S │ %d B │ %d O │" % (strike, ball, out))  # 직사각형의 창 안에 스트라이크, 볼, 아웃의 개수를 출력한다.
    print("└─────┴─────┴─────┘")
    print('=' * 80)

    if strike == 3:  # 만약 이번 추측이 정답이라면
        return 1  # 1을 리턴하고
    else:  # 정답이 아니면
        return 0  # 0을 리턴한다.


special_ans2 = ['0', '1', '3', '6', '7', '8']  # 정답은 ~~~(이)였습니다 출력 판단을 위한 리스트... 받침이 있는 마지막 수들.
yes_list = ['yes', 'Yes', 'YES', 'Y', 'y', '네', '응', 'ㅇ', 'ㅇㅇ', '좋아', '웅']  # 이 리스트 속의 원소가 입력될 경우 yes로 간주
no_list = ['no', 'No', 'NO', 'N', 'n', '아니요', '아니', 'ㄴ', 'ㄴㄴ', '싫어', '아닝']  # 이 리스트 속의 원소가 입력될 경우 no로 간주
err_dict = {'size': '세 자리로', 'rept': '중복 없이', 'numb': '숫자만', 'null': '값을', 'spac': '공백 없이'}  # 각 입력 오류에 대해 출력해주기 위한 딕셔너리
score_list = []  # 순위표를 위해 만든 리스트. 각 원소는 [정답시까지 시도 횟수, 이름]으로 이루어진다.

script = """
제가 0부터 9까지의 서로 다른 정수로 이루어진 세 자리의 숫자를 생각 할 거예요.(맨 앞자리는 0이 될 수 있습니다.)
당신은 숫자를 10번 추측할 수 있어요. 그러면 그 추측이 제가 생각한 숫자와 얼마나 일치하는지 다음과 같이 알려드릴게요.
┌─────┬─────┬─────┐ 숫자와 위치가 일치할 때는 스트라이크(S),
│ 1 S │ 2 B │ 0 O │ 숫자는 맞지만 위치는 일치하지 않을 때는 볼(B),
└─────┴─────┴─────┘ 숫자와 위치가 모두 일치하지 않을 때는 아웃(O) 으로요.
위 예시는 1 스트라이크 2볼 0아웃이라는 뜻이에요.
10번 안에 숫자를 맞히시면 당신의 승리예요!
추측할 때는 721과 같이 띄어쓰기 없이 입력해야 해요.

그럼 지금부터 시작할게요.
"""  # 숫자야구의 규칙

playtime = 1  # 현재까지 프로그램을 종료하지 않고 실행한 횟수를 뜻한다.
replay = 1  # 다시 플레이 할지 여부를 1(다시 한다), 0(다시 안한다)으로 저장한다.

while replay:
    ans = list(map(str, ran_num()))  # ans는 0~9의 정수 중 3개가 중복 없이 저장된 리스트이다.
    correct = 0  # 정답 맞힌 여부를 1(맞힘), 0(못맞힘)으로 저장한다.
    attemp = 1  # 이번 게임에서 시도한 횟수이다.

    print('=' * 80)
    if playtime % 10 == 0:
        print('축하드려요 벌써 %d번째 게임이예요.' % (playtime))  # 10의 배수번째 게임을 플레이할 때마다 축하 메시지를 띄운다.
    elif playtime >= 25:
        print('안 힘드세요..? %d번째 게임이예요...' % (playtime))  # 게임을 25게임 이상 할 시의 메시지이다.
    elif playtime > 1:
        print('또 오셨네요, 오늘의 %d번째 게임이예요.' % (playtime))  # 첫 게임이 아닐 때의 메시지이다.
    else:
        print('어서 오세요! 숫자야구 규칙에 대해서 설명 드릴게요.')  # 첫 게임일 때의 시작 메시지이다.
        print('%s' % (script))  # 첫 게임일 경우, 숫자야구의 규칙을 알려준다.

    print('지금 3자리 숫자를 생각했어요. 10번 안에 숫자를 맞혀보세요.')
    print('=' * 80)

    while not correct:  # 정답이 맞지 않는 동안
        if correct_chk(attemp, ans):  # 만약 이번 추측 값이 정답이라면
            correct = 1  # 정답 여부를 1로 바꾸고
            print('축하합니다. %d번만에 맞았어요.' % attemp)  # 몇 번째만에 맞았는지 출력한다.
            print('순위에 등록할 이름을 적어주세요', end=': ')
            score_list.append([attemp, input()])  # 순위 등록을 위해서 이름을 입력받고, 시도 횟수와 함께 score_list 에 저장한다.
            break  # 이번 게임을 끝낸다.

        if attemp == 10:  # 만약 10번의 시도동안 맞히지 못한 경우
            print('10번의 기회를 모두 사용했지만 정답을 맞히지 못했어요...')
            end_str = '였습니다...'
            if ans[2] in special_ans2:  # 세자리 수의 마지막 자리수의 받침에 따른 (이)였습니다... 구분
                end_str = '이였습니다...'
            print('정답은 %s' % (ans[0] + ans[1] + ans[2]), end=end_str)
            break  # 이번 게임을 끝낸다.

        attemp += 1  # 시도 횟수를 1증가시킨다.

    print('다시 플레이 할래요?')
    print('yes / no', end=': ')
    replay_input = 0  # 다시 플레이할지 물어본 뒤 입력받은 문자열이다.
    while True:
        replay_input = input()
        if replay_input in yes_list:  # 만약 다시 플레이할지 물어봤을 때 입력값이 yes_list 에 있다면
            if replay_input != 'yes':  # 만약 yes 는 아니라면
                print("'%s'도 좋지만 다음부터는 시키는대로 입력하세요..." % replay_input)  # 특별 메시지를 출력한다.

            replay = 1  # 다시 플레이할지 여부를 1로 남겨두고
            playtime += 1  # 몇 번째 게임인지를 1 증가시킨다.

            break  # 다시 플레이 할지의 여부 입력 과정을 나간다.

        elif replay_input in no_list:  # 만약 다시 플레이할지 물어봤을 때 입력값이 no_list 에 있다면
            if replay_input != 'no':  # 만약 no는 아니라면
                print("'%s'도 좋지만 다음부터는 시키는대로 입력하세요..." % replay_input)  # 특별 메시지를 출력한다.
            replay = 0  # 다시 플레이할지의 여부를 0으로 설정한다.

            break  # 다시 플레이 할지의 여부 입력 과정을 나간다.
        else:
            print('yes 또는 no로 입력해주세요.', end=': ')  # 다시 플레이할지 물어봤을 때 입력값이 yes_list 나 no_list 에 없다면 다시 입력받는다.

# sorted(score_list, key=lambda x: x[1], reverse = 1)  # 사용자가 다시 플레이하지 않는다면 score_list 의를 각 원소의 attemp 횟수의 오름차순으로 정렬한다.
sorted(score_list, key=lambda x: x[1], reverse=True)  # 사용자가 다시 플레이하지 않는다면 score_list 의를 각 원소의 attemp 횟수의 오름차순으로 정렬한다.

print('=' * 80)
print('순위표')
print('순위 │ 시도 횟수 │ 이름')

if len(score_list) == 0:  # 만약 한 번도 정답을 맞히지 못했다면 아래와 같이 순위표에 출력한다.
    print('게임 내역이 없어요.')
for i in range(len(score_list)):
    print('%3d │ %8d │ %s' % (i + 1, score_list[i][0], score_list[i][1]))  # 순위, 시도 횟수, 이름으로 이루어진 순위표를 출력한다.

print('=' * 80)
