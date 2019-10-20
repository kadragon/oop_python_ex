import random

winningcase = ((0, 1, 2), (3, 4, 5), (6, 7, 8), (0, 3, 6), (1, 4, 7), (2, 5, 8), (0, 4, 8), (2, 4, 6))
# winningcase : 틱택토 판에서 모든 가로, 세로, 대각선
board = [1, 2, 3, 4, 5, 6, 7, 8, 9]  # 틱택토 판. 디폴트값은 1~9가 넣어져 있는 것으로 설정
yourmal = ''  # 플레이어의 말
mymal = ''  # 컴퓨터의 말


def prt():  # 판을 출력하는 함수
    global board
    for i in range(9):
        print(str(board[i]) + " |", end=' ')  # 판은 매 턴 3*3 형태이며 칸막이가 있는 형태로 출력됨
        if (i + 1) % 3 == 0:  # 가로에 3개가 출력될 때마다 줄바꿈
            print()
            print("===========")
            print()


def filter(number):  # 사용자가 입력한 것을 조건에 맞는지 확인하여 맞지 않으면 걸러주는 함수
    global board
    if number.isdigit() is False:  # 사용자가 입력한 것이 숫자 문자가 아닐 때 거른다
        return True
    elif number == '0':  # 숫자 문자이긴 하지만 여기서 입력할 수 있는 위치는 1부터 9까지이므로 0도 거른다
        return True
    elif board[int(number) - 1] == 'X' or board[int(number) - 1] == 'O':  # 이미 말이 그 칸에 채워져 있으면 거른다
        return True
    return False  # 조건을 통과한 것들은 False를 리턴하는데, main의 조건문에서 not filter(number)이므로 메인에서는 참이 된다


def win(pan, mal):  # pan은 리스트형의 틱택토 판이며, mal은 이길 수 있을지 보려는 플레이어 또는 컴퓨터의 말이다
    cnt = 0  # 한 줄에 똑같은 말이 몇 개 있는지 세는 변수
    for line in winningcase:  # winningcase의 8개 줄을 차례로 탐색
        for a in line:
            if pan[a] == mal:  # 줄에 들어있는 한 원소가 말과 같으면 카운트 1 증가
                cnt += 1
        if cnt == 2:  # 줄에 똑같은 말이 2개 들어있는지 확인
            for b in line:
                if pan[b] != 'X' and pan[
                    b] != 'O':  # OXO와 같이 cnt가 2여도 나머지 하나가 상대의 말인 경우는 우선 필터링. 또한 X2X와 같은 경우 2에 X가 들어가면 되므로 조건으로 빈 곳을 확인함
                    return b  # 비어있는 곳의 인덱스를 반환
            cnt = 0  # cnt가 2지만 비어있는 곳이 없다면 다른 줄에서 가능한지 계속 알아보기 위해 초기화
        else:
            cnt = 0  # 줄이 X32와 같이 cnt=1일 때도 초기화하고 계속 진행
            continue
    return 10  # 승리가 가능한 줄이 없다면 10을 반환


def gameisend(pan, mal):  # 한 줄에 3개의 연속된 표시가 있는지 확인
    cnt = 0  # 한 줄에 똑같은 말이 몇 개 있는지 세는 변수
    for line in winningcase:  # winningcase의 8개 줄을 차례로 탐색
        for a in line:
            if pan[a] == mal:  # 줄에 들어있는 한 원소가 말과 같으면 카운트 1 증가
                cnt += 1
        if cnt == 3:  # 줄에 똑같은 말이 3개 들어있는지 확인
            return True
        else:
            cnt = 0  # 그렇지 않다면 초기화하고 계속
            continue
    return False  # 연속된 부분이 하나도 없다면 False 반환


def rand():  # 사용자가 이길 수 있는 수나 내가 이길 수 있는 수가 없을 때, 컴퓨터가 빈 곳 중 아무 곳이나 랜덤으로 말을 넣는 함수
    global board
    ran = random.randrange(0, 9)  # 0부터 8까지 중의 숫자 하나 뽑음
    while board[ran] == 'X' or board[ran] == 'O':  # 뽑은 숫자가 리스트의 인덱스일 때 그곳에 이미 말이 있는지 확인
        ran = random.randrange(0, 9)
    return ran


def myturn():  # 컴퓨터가 다음으로 둘 곳을 판단하는 함수
    print("제 차례입니다.")
    global board, mymal, yourmal
    towin = win(board, mymal)  # towin은 우리가 이길 수 있는 자리의 인덱스 값임. 없다면 10임
    toblock = win(board, yourmal)  # toblock은 사용자가 이기는 자리, 즉 막아야 할 자리의 인덱스 값. 없다면 역시 10임
    if towin != 10:
        board[towin] = mymal  # 이길 수 있는 자리가 있으면 그곳에 말 놓음
    elif toblock != 10:
        board[toblock] = mymal  # 그 밖의 경우 중 막아야 하는 자리가 있으면 그곳에 말 놓음
    else:
        board[rand()] = mymal  # 둘 다 해당하지 않으면 랜덤으로 놓음
    prt()  # 컴퓨터가 놓고 난 후 판의 상황을 출력
    return


def playerturn():  # 사용자가 다음으로 둘 곳을 입력받는 함수
    print("당신 차례입니다.")
    global board, yourmal
    place = input()  # place는 사용자가 놓을 자리를 나타냄
    while len(place) != 1 or filter(place) is True:  # 조건에 맞을 때까지 다시 입력하게끔 함
        print("다시 입력해주세요 ㅠㅠ")
        place = input()
    p = int(place)  # place는 아직 문자열이므로 정수로 변환
    board[p - 1] = yourmal  # 써있는 자리는 1~9이지만 실제로는 0~8이므로 p-1의 자리에 사용자의 말을 놓음
    prt()  # 사용자가 놓고 난 후 판의 상황을 출력
    return


def again():  # 다시 할 것인지를 물어보는 함수
    print("한판 더 하고 싶으시나요? 그렇다면 전부 소문자로 yes 라고 말해주세요.")
    x = input()
    if x == "yes":  # yes를 입력하면 True를 반환하여 반복하여 진행할 수 있게 함
        return True
    else:  # 이외에는 False를 반환하여 게임을 끝내도록 함
        return False


def percent():  # 승률을 출력하는 함수
    global turn, playerwin
    if turn != 0:
        print("당신의 승률은 " + str(int(playerwin * 100 / turn)) + "%")  # (사용자가 이긴 판 수)를 전체 판 수로 나누어 승률 구함. 이때 일의 자리까지만 나타냄.
        return
    else:
        return


if __name__ == "__main__":
    playerwin = 0  # playerwin은 사용자가 이긴 판 수. 처음에는 0으로 설정
    turn = 0  # turn은 전체 판 수. 처음에는 0으로 설정
    while True:
        print("O와 X 중 무엇을 선택하시겠습니까?")
        yourmal = input()  # 사용자가 자신의 말을 입력
        while yourmal.upper() != 'O' and yourmal.upper() != 'X':  # 입력한 문자열이 'O'나 'X'가 아니면 다시 입력. 이때 소문자까지는 허용
            print("다시 입력해주세요 ㅠㅠ")
            yourmal = input()
        yourmal = yourmal.upper()  # 소문자가 입력되었으면 대문자로 바꿈
        if yourmal == 'X':  # 사용자의 말에 따라 둘 중 나머지 말을 컴퓨터 말로 설정
            mymal = 'O'
        else:
            mymal = 'X'
        print("당신의 말은 " + yourmal, "제 말은 " + mymal + "입니다.")
        print()
        print("먼저 시작하실 건가요? 선공을 원하시면 1, 후공을 원하시면 0를 입력해주세요")
        order = input()  # 후공을 할 거면 0, 선공을 할 거면 1을 입력
        while order != '0' and order != '1':  # 조건에 맞지 않으면 다시 입력
            print("다시 입력해주세요 ㅠㅠ")
            order = input()
        print(''' 판은 다음과 같습니다.
    1 | 2 | 3 |
    ===========
    4 | 5 | 6 |
    ===========
    7 | 8 | 9 |
    ===========
    여기서 당신과 제가 놓은 자리에는 각자의 말이 표시되고, 아직 놓지 않은 자리에만 이 자리가 몇 번째 자리인지 표시됩니다.
    또한 시작할 때를 제외하고 매 턴마다 당신이 얼마나 이겼는지에 대한 승률 일의 자리까지 표시됩니다. 그럼 화이팅''')
        count = 1
        while count <= 9:  # 최대 9번 돌아가면 판이 꽉차므로 9번까지 돌아가게 함
            if count % 2 == int(order):  # 선공이면 order이 1이므로 이 수식에 따르면 홀수 번째에 플레이하게 되어 맞는 순서가 됨. 후공일 때도 마찬가지임.
                playerturn()
            else:
                myturn()

            if gameisend(board, yourmal) is True:  # 사용자가 이겼는지 확인
                playerwin += 1  # 이겼으면 사용자가 이긴 판 수를 1 추가
                print("당신이 이겼네요. ㅂㄷㅂㄷ")
                break

            elif gameisend(board, mymal) is True:  # 컴퓨터가 이겼는지 확인
                print("제가 이겼네요. ㅉㅉ")
                break

            print(count)
            if count == 9:
                print("무승부! 좀 하시네요~")  # 승패를 가리지 못하고 모든 판이 채워지면 무승부로 종료
            count += 1

        turn += 1  # 한 턴이 끝났으므로 턴 수에 1 추가
        percent()  # 승률 출력
        if again() is False:  # 사용자가 다시 할 것인지 확인하여 그렇지 않다면 게임종료
            break
        else:
            board = [1, 2, 3, 4, 5, 6, 7, 8, 9]  # 판을 처음 상태로 되돌림
