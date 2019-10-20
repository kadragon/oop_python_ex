import copy  # copy.deepcopy 함수를 사용해 이차원 배열을 복사해 주기 위함
import random  # 컴퓨터가 말을 둘 때, 자신이 이길 수나 상대가 이길 수를 발견하지 못 하면 랜덤으로 두기 위함


def print_status(status):
    """
    현재 말판의 상황을 구분해 출력해주는 함수
    :param: status, 즉 현재 말판의 상황
    :return: 함수 자체에서 말판의 상황을 출력하고 종료하여, return값 존재하지 않음
    """
    for i in range(3):
        print()
        print("=" * 19)
        for j in range(3):
            print("|", end='')
            if status[i][j] == 0:
                print("     ", end='')
            elif status[i][j] == 1:  # status라는 이차원 배열에 들어 있는 값이 1이면, O를 뜻해 O 출력
                print("  O  ", end='')
            elif status[i][j] == 2:  # status라는 이차원 배열에 들어 있는 값이 2이면, X를 뜻해 X 출력
                print("  X  ", end='')
        print("|", end='')
    print()
    print("=" * 19)


def is_correct(x, y):
    """
    x,y 의 범위가 옳은지 확인하는 함수
    :param: 말판 위의 좌표값 x,y
    :return: 범위가 옳을 경우 True를 반환, 틀릴 경우 False를 반환
    """
    if not x - 1 in range(3):  # 배열에서의 인덱스는 0부터 시작이므로, x-1로 보정해줌
        return False
    if not y - 1 in range(3):  # 배열에서의 인덱스는 0부터 시작이므로, y-1로 보정해줌
        return False
    return True


def is_able(status, x, y):
    """
    말을 놓으려 하는 위치 빈 곳인지 확인한느 함수
    :param: 말판의 상황을 기록한 이차원 배열 status와 놓으려는 좌표값 x,y
    :return: 가능한 경우 True, 불가능한 경우 False
    """
    if status[x - 1][y - 1] == 0:  # 0으로 기록되어, 빈 곳인 경우 True 반환
        return True
    else:
        return False


def decide_userid():
    """
    사용자가 O 말을 사용할지 X 말을 사용할 지 파악하는 함수
    :return: O일 경우 1, X일 경우 2 반환해 사용자의 userid(사용자 말의 고유번호, 1혹은 2)를 지정해 줌
    """
    while True:
        user = input()  # 사용자로부터 입력을 받음
        if user == 'O':  # O인 경우 1 반환
            return 1
        elif user == 'X':  # X인 경우 2 반환
            return 2
        else:  # 다른 값이 입력된 경우 재입력 요구
            print("아니 제대로 입력해요! 게임하기 싫어요??")


def win_check(status, id):
    """
    사용자 혹은 컴퓨터가 이겼는지 확인하는 함수
    :param: status 즉, 현재 말판의 상황과 승리를 확인하려 하는 대상의 id(1 혹은 2)
    :return: 승리했을 경우 True, 아닐 경우 False
    """
    for i in range(3):
        if status[i][0] == status[i][1] == status[i][2] and status[i][0] == id:  # 세로줄 중 완성된 줄을 확인
            return True
        if status[0][i] == status[1][i] == status[2][i] and status[0][i] == id:  # 가로줄 중 완성된 줄을 확인
            return True
    if status[0][0] == status[1][1] == status[2][2] and status[0][0] == id:  # 왼쪽 위에서 오른쪽 아래로 내려가는 대각선 확인
        return True
    if status[2][0] == status[1][1] == status[0][2] and status[i][0] == id:  # 오른쪽 위에서 왼쪽 아래로 내려가는 대각선 확인
        return True
    return False  # 아무 것도 해당되지 않을 경우 False 반환


def next_draw(status, comid, userid):
    """
    컴퓨터가 다음에 어느 곳에 놓아야 할지 결정하는 함수
    먼저, 컴퓨터가 이길 수 있는 위치가 있는지 체크해 만약 존재한다면 그 좌표를 반환
    컴퓨터가 이길 수 있는 위치가 없다면, 사용자가 이길 수 있는 위치를 체크, 존재하면 그 위치를 반환하는 함수
    :param:status 즉, 현재 말판의 상황과 comid, userid 각각 컴퓨터와 사용자의 고유번호(1과 2)
    :return: 컴퓨터가 이길 수 있거나, 사용자가 이길 수 있는 위치가 존재한다면 그 위치의 좌표를 반환하고, 존재하지 않으면 -1,-1을 반환
    """
    test_status = copy.deepcopy(status)  # deepcopy 함수를 통해 현재 말판의 상황인 status를 복사한 새로운 이차원 배열 생성
    for i in range(3):
        for j in range(3):
            if test_status[i][j] == 0:  # 현재 말판에서 비어 있는 위치인지 확인
                test_status[i][j] = comid  # 새로 생성한 이차원 배열 말판의 비어 있는 곳에 컴퓨터의 말을 놓음
                if win_check(test_status, comid):  # 컴퓨터가 한 줄을 만들어 이겼는지 판단, 이긴 경우에는 좌표 반환
                    return i, j
                test_status[i][j] = 0  # 이기지 못한 경우, 두었던 컴퓨터의 말을 제거함
    for i in range(3):
        for j in range(3):
            if test_status[i][j] == 0:  # 현재 말판에서 비어 있는 위치인지 확인
                test_status[i][j] = userid  # 새로 생성한 이차원 배열 말판의 비어 있는 곳에 사용자의 말을 놓음
                if win_check(test_status, userid):  # 사용자가 한 줄을 만들어 이겼는지 판단, 이긴 경우에는 좌표 반환
                    return i, j
                test_status[i][j] = 0  # 이기지 못한 경우, 두었던 사용자의 말을 제거함
    return -1, -1  # 존재하지 않는 경우, -1,-1 반환


def turn_decide():
    """
    사용자와 컴퓨터 중 누가 먼저 시작할지를 랜덤으로 결정해 주고, 관련된 문구를 출력해 주는 함수
    :return: 랜덤으로 나온 결과가 0이면 사용자의 순서로 0 반환, 1이면 컴퓨터의 순서로 1 반환
    """
    turn = list(range(2))
    random.shuffle(turn)  # 0,1 이 들어 있는 list를 생성한 후 random.shuffle 하여 임의로 섞어 줌
    if turn[0] == 0:  # 0인 경우 이용자의 순서
        print("오! 이용자분 먼저에요! 먼저 두세요")
    elif turn[0] == 1:  # 1인 경우 컴퓨터의 순서
        print("하하하! 제가 먼저네요 먼저 두죠")
    return turn[0]


def replay():
    """
    게임이 종료되었을 경우 다시 게임을 플레이 할지 판단하는 함수
    :return: '네'가 입력되었을 경우 True, '아니요'가 입력되었을 경우 False
    """
    print("다시 한 번 플레이하시겠어요?, '네' 혹은 '아니요'로 대답해주세요!")
    while True:
        replay = input()  # 다시 플레이할지 여부를 입력
        if replay == '아니요':  # '아니요'인 경우 False 반환
            return False
        elif replay == '네':  # '네'인 경우 재시작을 위해 "="로 구분해 준 후 True 반환
            print("=" * 80)
            return True
        else:  # 다른 값이 입력된 경우 재입력을 위해 문장 출력
            print("아니 말좀 들어요... '네' 혹은 '아니요'로 대답해달랬잖아요...")


def have_more_space(status):
    """
    말판에 더 남은 공간이 남았는지를 체크하는 함수, 공간이 더 이상 남지 않은 경우 무승부로 처리해 줌
    :param: status 즉, 현재 말판의 상황
    :return: 공간이 남았으면, True 남지 않았으면, False를 출력함
    """
    global draw
    for i in range(3):
        for j in range(3):
            if status[i][j] == 0:
                return True
    print("무승부입니다")
    draw += 1  # 무승부로 처리하기 위해 문구를 출력해 준 후 draw라는 무승부 수를 기록하기 위한 전역변수에 1을 더해 줌
    return False


def random_cord(status):
    """
    next_draw 함수에서 모든 조건에 해당하는 값이 존재하지 않아서 -1,-1가 반환된 경우, 랜덤으로 말을 놓을 곳을 지정해 주기 위한 함수
    :param: status 즉, 현재 말판의 상황
    :return: 말판 빈 곳 중 한 곳을 랜덤으로 선택해 좌표를 반환해 줌
    """
    x = list(range(3))
    y = list(range(3))  # x,y 좌표에 해당하는 list를 생성
    while True:
        random.shuffle(x)
        random.shuffle(y)  # random.shuffle 함수를 통해서 임의로 list를 섞어 줌
        if status[x[0]][y[0]] == 0:  # 섞은 list의 값에 해당하는 좌표가 비어 있다면, 그 좌표를 반환해 줌
            return x[0], y[0]


def win_rate(win, lose):
    """
    승률을 기록해 주는 함수
    :param: win: 승리 횟수, lose: 패배 횟수
    :return: 함수 자체에서 전적과 승률을 출력해 주기 때문에 반환값 존재하지 않음
    """
    global draw
    print("전적은 %d승 %d패 %d무 입니다" % (win, lose, draw))
    rate = (win * 100) / (win + lose + draw)  # 승률 계산
    print("승률은 %.2f퍼센트 입니다" % rate)  # 승률 출력


if __name__ == '__main__':
    print("=" * 80)
    print("Tic-Tac-Toe 게임에 오신 것을 환영합니다!!!")
    print("오목이랑 되게 비슷한 게임인데요! 제가 룰을 설명해 드릴게요!")
    print("저(컴퓨터)랑 이용자분께서 O 랑 X 중 하나를 선택해서 번갈아 놓는거에요")
    print("이렇게 3X3 판에 놓아서 먼저 3개의 표시로 된 한 줄을 만들면 이기는겁니다!")
    print("이용자분의 차례에는 ex) 3,3 등의 형식으로 구분해서 놓을 자리를 입력해주세요")
    print("준비되셨으면 시작해봐요!")
    print("=" * 80)

    lose = 0
    win = 0
    draw = 0  # lose, win, draw 변수를 통해 승,패,무 횟수 기록
    while True:
        print("시작하기 전 할게 있어요! O 랑 X 중에 뭐 쓰실래요?")
        userid = decide_userid()  # 사용자가 O,X 말중 무엇을 사용할지에 따라 userid라는 고유번호 지정(O:1 X:2)
        comid = 0
        if userid == 1:  # comid를 userid가 1이면 2, 2면 1로 지정
            comid = 2
        elif userid == 2:
            comid = 1
        print("그러면 순서를 정할게요! 제가 랜덤으로 정정당당하게 정할거니깐 걱정하지 마시구요")
        status = []
        for i in range(3):
            status.append([0] * 3)  # 말판의 상황을 기록할 status라는 이차원 배열 생성
        turn = turn_decide()  # turn이라는 변수에 컴퓨터와 이용자의 순서 기록(turn==0:이용자 차례 turn==1:컴퓨터 차례)
        while have_more_space(status):  # 말판이 비어있는 동안 계속해서 while 문 실행
            if turn == 0:  # 이용자의 차례인 경우
                print("이용자분 차례에요! 어디다 놓으실래요?")
                while True:
                    while True:
                        try:
                            x, y = map(int, input().split(","))  # 이용자에게서 말을 놓을 위치를 입력받을 때 ','로 나누어 입력받음(ex)2,2)
                            break
                        except ValueError:  # 숫자가 아닌 문자가 입력된 경우의 오류를 방지해 줌
                            print("형식에 맞게 제대로 입력좀요...")
                    if is_correct(x, y):  # 입력된 x,y 값이 1~3 범위의 수인지 확인
                        if is_able(status, x, y):  # 말판이 비어 말을 놓는 것이 가능한지 확인
                            status[x - 1][y - 1] = userid  # 모두 가능한 경우 사용자의 말을 놓음
                            break
                        else:  # 말판이 비어 있지 않은 경우
                            print("빈 곳에 놓아야죠... 후우우...다시 하세요")
                    else:  # 옳지 못한 범위의 수인 경우
                        print("1~3 의 숫자만 입력할 수 있어요.. 판이 3X3 이잖아요")
                if win_check(status, userid):  # 사용자가 말을 놓아 승리하게 된 경우 파악
                    print_status(status)
                    print("승리하셨습니다!!")
                    win += 1  # win 변수에 승리 기록
                    break  # 게임 종료
                turn = 1  # 컴퓨터의 차례로 바꾸어 줌
            elif turn == 1:  # 컴퓨터의 차례인 경우
                x, y = next_draw(status, comid, userid)  # 컴퓨터가 다음에 놓아야 할 위치 파악
                if x in range(3):  # next_draw 함수를 통해 얻은 값이 옳은 값인지 파악
                    status[x][y] = comid  # 컴퓨터의 말을 놓아 줌
                else:  # 컴퓨터가 이기는 경우나 이용자가 이기는 경우가 없어 조건을 모두 통과한 경우 랜덤으로 위치 지정
                    x, y = random_cord(status)  # random_cord 함수를 통해 랜덤으로 위치 지정
                    status[x][y] = comid  # 컴퓨터의 말을 놓아 줌
                if win_check(status, comid):  # 컴퓨터가 말을 놓아 패배하게 된 경우를 파악하고 문구 출력
                    print_status(status)
                    print("패배하셨습니다...")
                    lose += 1  # lose 변수에 패배 기록해 줌
                    break  # 게임 종료
                turn = 0  # 이용자의 차례로 바꾸어 줌
            print_status(status)
        win_rate(win, lose)
        if not replay():  # 게임 재시작 여부 파악
            break  # 프로그램 종료
