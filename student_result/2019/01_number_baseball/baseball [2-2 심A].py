import random  # 랜덤한 수 생성을 위함


def makenum():  # 0~9의 수 중 랜덤한 수 세개를 만들어, 그 수들을 리스트로 만들어 리턴한다.
    sourcelist = []  # 0~9까지 숫자를 넣은 다음 shuffle할 리스트
    for i in range(10):
        sourcelist.append(i)
    random.shuffle(sourcelist)
    anslist = []  # 숫자를 넣고 return할 리스트
    for i in range(3):
        anslist.append(sourcelist[i])
    return anslist


def init():  # 게임 시작 후 실행됨, 문장을 출력
    print("야구-게임!")
    print("컴퓨터가 0~9까지의 정수 중 세개의 수를 생각했습니다!")
    print("숫자의 위치가 맞으면 S")
    print("숫자는 맞지만 위치가 틀리면 B")
    print("숫자와 위치가 모두 틀리면 O 입니다")
    print("세개의 숫자를 공백으로 구분하여 입력하세요. 기회는 오직 10번만")


def trygame(makelist: list,uselist: list, flag1: int):  # 사용자가 입력한 숫자 3개를 입력받아, 결과를 출력하고, 다음으로 실행될 횟수를 리턴
    # makelist: 컴퓨터가 생각한 숫자들의 리스트
    # uselist: 유저가 입력한 숫자들의 리스트
    # flag1: 게임이 실행되는 횟수(현재 실행되는 것까지 포함)
    strike = 0  # 숫자의 위치가 맞는 수의 개수
    ball = 0  # 숫자는 맞지만 위치가 틀린 수의 개수
    out = 0  # 숫자와 위치가 틀린 수의 개수
    for i in range(3):
        tmpflag = 0  # strike나 ball를 증가시킨다면 1, 아니면 0
        for j in range(3):
            if uselist[i] == makelist[j]:  # 사용자가 입력한 숫자와, 컴퓨터가 정한 숫자가 맞는지 비교
                tmpflag = 1
                if i == j:  # 위치가 맞는지 비교
                    strike += 1
                else:
                    ball += 1
        if tmpflag == 0:  # strike나 ball이 증가되지 않았음: 숫자와 위치가 틀림
            out += 1
    if strike == 3:  # 사용자가 게임을 이김
        print("우와 정말 데단해!")
        return 11  # 게임이 실행되는 횟수를 11로 만듬- 게임을 종료하기 위함
    else:
        print("S: %d, B: %d, O: %d" % (strike, ball, out))  # S,B,O의 개수를 출력
        return flag1+1  # 실행되는 횟수 1 중가


def game():  # 숫자 야구 게임을 실행함
    maklist = makenum()  # 컴퓨터가 생각한 3개의 수를 list에 저장
    init()
    flag = 1  # 게임이 실행되는 횟수(곧 실행될 것까지 포함하여 1을 더함)
    while flag <= 10:  # 횟수 제한 10
        try:
            userlist = list(map(int, input("%d번째 입력: " % flag).split()))  # 3개의 숫자를 입력받아 userlist에 저장
            if userlist[0] == userlist[1] or userlist[1] == userlist[2] or userlist[0] == userlist[2]:  # 숫자가 같은 것이 있다면
                print("숫자가 중복됨, 다시 입력")
            elif len(userlist) > 3:  # 숫자가 3개를 초과한다면
                print("숫자 개수가 너무 많음, 다시 입력")
            else:  # 오류가 없을 경우
                flag = trygame(maklist, userlist, flag)  # 입력받은 숫자를 이용해 결과를 출력, 실행되는 횟수를 flag에 저장
        except (IndexError, ValueError) as e:  # 숫자를 적게 입력해 에러났을 경우
            if isinstance(e, IndexError):
                print("숫자 개수가 너무 적거나 입력이 유효하지 않음, 다시 입력")
            elif isinstance(e, ValueError):  # 숫자가 아닌 다른 문자를 입력했을 경우
                print("숫자만 입력해주세요, 다시 입력")


isgame=1  # 게임을 시작하는지의 여부를 결정: 초기값 1
while 1:
    if isgame == 1:  # 플레그가 1이라면
        game()  # 게임 실행
    print("다시 시도할거에요? Y/N")
    tmp = input()  # Y 또는 N을 입력받음
    if tmp == 'N':
        break  # 프로그램 종료
    elif tmp != 'Y':
        print("Y 아님 N으로 답해주세요")  # 사용자가 Y,N이 아닌 문자나 문장 입력
        isgame = 0  # while문이 돌 때 다시 게임을 실행하지 않게 함
    else:
        isgame = 1  # 다시 게임을 실행함