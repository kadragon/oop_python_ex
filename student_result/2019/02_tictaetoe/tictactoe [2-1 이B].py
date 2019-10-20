import random  # 무작위 착수를 위한 randomint 함수 사용
import copy  # 0으로만 채워진 보드를 가져오기 위해 deepcopy 함수 사용

# 게임 기본 설계를 위한 정보 부분
Ainum = 0
playernum = 0
playcount = 0  # 플레이한 횟수
win = 0  # 이긴 횟수

PureBoard = [[0, 0, 0, 0, 0],
             [0, 0, 0, 0],
             [0, 0, 0, 0],
             [0, 0, 0, 0]]  # 0으로만 채워진, 순수하고 깨-끗한 보드

Board = copy.deepcopy(PureBoard)  # 0으로만 채워진, 순수한 보드를 가져온다.

addlist = ['p', [3, 1], [3, 2], [3, 3], [2, 1], [2, 2], [2, 3], [1, 1], [1, 2], [1, 3]]


# 입력되는 숫자에따라 주소를 반환한다. 1이 입력되면 addresslist[1] 에 있는 [3][1]이 좌표가 되는것과 같다.

# 4*4 크기를 기준으로 하되, 0이 원소로 포함된 위치는 각 행/열/대각선에 몇개의 문자가 있는지 확인하는 용도이다.
# 따라서 본 게임판은 (1, 1)부터 (3, 3)까지의 정사각형 게임판이다.


class AiBase:
    startai = False

    def __init__(self, gameboard):  # Ai에게 필요한 기본정보를 입력해준다 (어떤 문양을 가졌는가, 현재 보드상황은 어떠한가?)
        self.Board = gameboard
        self.mark = Ainum
        pass

    def update(self, gameboard):  # Ai 내에 입력되어있는 보드 현황을 현재 보드 현황으로 업데이트한다.
        self.Board = gameboard

    def put(self, x, y):  # Ai가 수를 둘 차례엔 put 함수를 통해 Ai내부의 보드상황을 업데이트한다.
        self.Board[x][y] = Ainum  # 해당 장소에 돌을 놓는다면
        self.Board[x][0] += Ainum
        self.Board[0][y] += Ainum  # 해당 장소를 포함하는 열에 해당하는 원소의 값 또한 Ainum의 영향을 받는다.
        if x == y:
            self.Board[0][0] += Ainum  # 이 2개의 if문은 대각선에 원소가 있는지를 검사한다.
        if x == 4 - y:
            self.Board[0][4] += Ainum

    def returningboard(self):  # put 함수로 돌을 두고나선 게임진행상황 표시를 위해 현재 입력되어있는 보드를 반환한다.
        return self.Board

    def avoidlose(self):  # 승리할 수 있는 조건이 있다면 무조건 그 경우를 피하는 알고리즘.
        # 한 줄위에 상대방의 돌만 2개가 있다면, 그에 해당하는 리스트의 원소는 상대방의 돌에 해당하는 수 * 2 가 될것이다.
        # 이 때 AI의 돌에 해당하는 수 = 플레이어의 돌에 해당하는 수 * -1 이므로, AI의 돌에 해당하는 수로 나누어주면
        # 플레이어의 돌만 2개 있다면 -2의 값이 도출된다. 이를 통해 플레이어의 돌만 2개 있는지 확인하며,
        # 그것이 참일경우 착수하고 False 를 반환하며 착수하지 않은경우 True를 반환한다.
        for p in range(1, 4):
            if Board[0][p] != 0 and Board[0][p] / Ainum == -2:
                for q in range(1, 4):
                    if Board[q][p] == 0:
                        self.put(q, p)
                        return False
            if Board[p][0] != 0 and Board[p][0] / Ainum == -2:
                q = Board[p].index(0)
                self.put(p, q)
                return False
        if Board[0][0] != 0 and Board[0][0] / Ainum == -2:
            for p in range(1, 4):
                if Board[p][p] == 0:
                    self.put(p, p)
                    return False
        if Board[0][4] != 0 and Board[0][4] / Ainum == -2:
            for p in range(1, 4):
                if Board[p][4 - p] == 0:
                    self.put(p, 4 - p)
                    return False
        self.startai = True

    def pursuaidwin(self):  # 승리할 수 있는 조건이 있다면 무조건 그 경우를 사용한다.
        # 상대가 승리할 수 있는 조건이 있더라도 AI가 이길 수 있다면 무조건 이기는 수를 사용한다.
        # 본 알고리즘의 작동구조는 avoidlose와 거의 같으며, 돌을 착수하면 False를 리턴한다.
        for p in range(1, 4):
            if Board[0][p] != 0 and Board[0][p] / Ainum == 2:
                for q in range(1, 4):
                    if Board[q][p] == 0:
                        self.put(q, p)
                        return False
            if Board[p][0] != 0 and Board[p][0] / Ainum == 2:
                q = Board[p].index(0)
                self.put(p, q)
                return False
        if Board[0][0] != 0 and Board[0][0] / Ainum == 2:
            for p in range(1, 4):
                if Board[p][p] == 0:
                    self.put(p, p)
                    return False
        if Board[0][4] != 0 and Board[0][4] / Ainum == 2:
            for p in range(1, 4):
                if Board[p][4 - p] == 0:
                    self.put(p, 4 - p)
                    return False
        self.startai = True

    def gamejudge(self):  # 패배조건 피하는것, 승리확정시키는것을 제외하면 착수위치는 랜덤으로 정한다.
        while True:
            randnum = random.randint(1, 9)
            if self.Board[addlist[randnum][0]][addlist[randnum][1]] == 0:  # 결정한 착수위치엔 돌이 없어야 한다.
                return addlist[randnum]

    def gameplay(self):  # 인공지능의 한 턴을 진행시킨다.
        if self.pursuaidwin() is False:  # 승리를 확정하기위한 포석을 하지않은경우 True 반환
            return
        if self.avoidlose() is False:  # 패배조건을 피하기 위한 포석을 하지 않은경우 True 반환
            return  # 패배조건을 피하기 위한 포석을 한경우 False를 반환하며, 그 외의 포석을 진행하지 않으므로 함수를 종료한다.
        address = self.gamejudge()  # 인공지능이 판단하여
        self.put(address[0], address[1])  # 포석한다


# 유저 인터페이스 부문


def randomin(lists):  # 리스트를 받아 섞은뒤 첫 원소를 반환하는 함수
    random.shuffle(lists)
    return lists[0]


def select_replay():  # 입력으로 재시작 여부를 고르는 함수
    print("게임을 다시 플레이하시겠습니까? Y/N")
    ifreplay = False  # 디폴트는 False
    yes_or_no = input()  # Y나 N중에서 하나를 받아 재시작 여부를 정한다.
    YN = 'YN'
    if yes_or_no is '' or yes_or_no not in YN:
        print("올바르지 않은 값을 입력하셨습니다. 게임을 종료합니다.")
    elif yes_or_no is 'Y':  # Y를 받으면 True를 반환해야하므로 bool타입인 ifreplay가 True가 된다
        print("게임을 다시 시작합니다. ")
        ifreplay = True
    else:
        print("게임을 종료합니다.  ")

    return ifreplay  # False가 반환되면 종료, True가 반환되면 재시작


def select_mark():  # 입력으로 표시를 고르는 함수 ('X' 나 'O' 중 하나), 그리고 표시에 따라 선공여부 고르는 함수(선공여부를 반환한다)
    global playernum
    global Ainum  # 결과는 playernum과 Ainum의 변화로 나타난다. 이 두개의 변수는 전역에서 사용된다.
    print("문양을 선택합니다. O 나 X 중 하나를 입력해주세요. 입력을 잘못했다면 자동으로 문양이 선택됩니다.")
    markstr = 'X0O'  # X는 0번 O는 2번 자리이다 여기서 1을 빼면 O는 1과, X는 -1과 대응된다.
    # 못찾았다고 터지지 않는 find 함수의 사용을 위해 리스트가 아니라 문자열로 객체를 생성한다.
    mark = input()
    print(mark)
    if mark == '' or mark == '0' or markstr.find(mark) == -1:
        print("입력이 잘못되었습니다. 자동으로 문양을 선택합니다. ")
        selectresult = randomin([1, -1])  # 랜덤으로 1과 -1중 하나를 반환한다.
    else:
        selectresult = markstr.find(mark) - 1
    if selectresult == 1:  # 1이라면 플레이어 번호 1 인공지능 번호 -1 부여. 후공이된다
        playernum = 1
        Ainum = -1
        print("O가 선택되었습니다. 후공으로 시작합니다.")
        return 'second'

    if selectresult == -1:  # -1이라면 플레이어 번호 -1 인공지능 번호 1 부여. 선공이된다
        playernum = -1
        Ainum = 1
        print("X가 선택되었습니다. 선공으로 시작합니다.")
        return 'first'


def select_display_winrate():  # O와 X중 하나를 받아 O를 받으면 승률은 보여주고, 그 외를 받으면 해당 승률단계를 생략하는 함수
    print("현재까지의 승률을 보시겠습니까? O/X ")
    choice = input()
    res = 'OX'
    if choice == '' or res.find(choice) == -1:
        print("잘못입력하셨습니다. 해당단계는 생략합니다")
    if choice == 'O':
        display_winrate()
    else:
        print("해당단계는 생략합니다.")
        return


def display_winrate():  # 실행되면 전역변수를 이용하여출력한다.
    print("승률을 출력합니다. ")
    print("플레이 횟수 : %d, 승리 횟수 : %d, 승률: %dpercent" % (playcount, win, int(float(win / playcount) * 100)))


def display():  # 현상황을 O X가 입력된 보드로 나타내주는 함수
    Chesslist = [None]  # 배열이 1부터 시작하므로 empty 하나를 넣어준다
    for i in range(1, 10):  # 1부터 9까지 뽑는다. 이 역시 보드의 위치가 텐키와 관련이 있다.
        if Board[addlist[i][0]][addlist[i][1]] == 0:
            Chesslist.append(' ')
        elif Board[addlist[i][0]][addlist[i][1]] == 1:
            Chesslist.append('O')
        else:
            Chesslist.append('X')
    # 각자 칸에 O를 출력할건지 X를 출력할건지 출력 안하건지 정해주는 리스트를 만드는 과정
    print("\n\n  %c  |  %c  |  %c  " % (Chesslist[7], Chesslist[8], Chesslist[9]))
    print("-" * 18)
    print("  %c  |  %c  |  %c  " % (Chesslist[4], Chesslist[5], Chesslist[6]))
    print("-" * 18)
    print("  %c  |  %c  |  %c  \n\n" % (Chesslist[1], Chesslist[2], Chesslist[3]))  # 한줄 띄워주기위해 \n을 사용한다.
    # 화면상의 좌표의 위치는 키보드의 '텐키'의 배치와 같다. 리스트에도 이를 고려하여 작성한다.


def inputting(turn):  # 숫자를 입력받아 보드에 정보를 입력해주는 함수 (플레이어가 착수하기 위한 함수)
    print("좌표를 입력해주세요. : 1~9")
    numstr = '123456789'
    while 1:
        num = input()
        if num == '' or numstr.find(num) == -1:  # 잘못된 값을 입력했다면 기회를 한번 더 준다. 앞의 조건문은 그냥 엔터를 친 경우이다.
            print('잘못입력하셨습니다. 다시입력해주세요')
            continue
        else:
            num = int(num)
            # [addlist[num][0]][addlist[num][1]]은 리스트 좌표를 나타낸다
            if Board[addlist[num][0]][addlist[num][1]] != 0:
                print('이미 표시가 있는곳을 선택하셨습니다. 다시 입력해주세요')
                continue
            else:
                Board[addlist[num][0]][addlist[num][1]] = turn
                Board[0][addlist[num][1]] += turn
                Board[addlist[num][0]][0] += turn
                if addlist[num][0] == addlist[num][1]:
                    # 오른쪽 하방으로 향하는 대각선 위에 좌표가 있는경우 연장선인 [0][0]에 더한다
                    Board[0][0] += turn
                if addlist[num][0] == 4 - addlist[num][1]:
                    # 오른쪽 상방으로 향하는 대각선 위에 좌표가 위치할경우 연장선인 [0][5]에 더한다
                    Board[0][4] += turn
                break


# O는 1과, X는 -1과 대응된다. 좌표 위치에 0이 포함된 경우 이는 그 좌표에 해당하는
# 행이나 열에 있는 O와 X 의 개수에 1과 -1의곱하고 그 값들의 합을 통해 나타내며,
# 그중 하나라도 절대값이 3이되면 한 줄 전체에 같은 기호가 있는것으로 판단하고 게임이 한쪽의 승리로 끝난다.


# 승패 무승부 판정부분
def winjudge():  # 승리여부 판정 프로그램, 패배했다고 판정되면 True를 출력한다.
    for p in range(5):
        if Board[0][p] / playernum == 3:
            return True
    for p in range(4):
        if Board[p][0] / playernum == 3:
            return True
    else:
        return False


def losejudge():  # 패배여부 판정 프로그램, 패배했다고 판정되면 True를 출력한다.
    for p in range(5):
        if Board[0][p] / playernum == -3:
            return True
    for p in range(4):
        if Board[p][0] / playernum == -3:
            return True
    else:
        return False


def playerturn(ai):
    inputting(playernum)  # 플레이어에게 입력을 시키고
    ai.update(Board)  # 플레이어가 입력한 것을 AI에게 업데이트시켜주고
    display()  # 그리고 그 결과를 보여준다.


def aiturn(ai):
    global Board  # 전역변수를 수정시켜주어야 한다.
    ai.gameplay()  # AI가 돌을 놓고
    Board = versus.returningboard()  # AI가 돌을 넣은 정보를 업데이트 시켜주고
    display()  # 결과를 보여주고


"""
/ 일단
/ 빈공간을 만들어서 구분쉽게 해두었고요
/ 여기부턴 게임진행을 위한 코드입니다.
"""

print("틱택토 게임을 시작합니다")
print("틱택토 게임이란 본인의 문양을 선택하여 3X3 크기의 판에 본인의 문양을 3개를 직선으로 연속하게 두면 승리합니다.")
print("틱택토 판의 위치는 텐키의 위치와 동일합니다. 이를 참고해주세요\n\n")
print('=' * 30 + '\n')

first_or_second = select_mark()  # 마크를 고른다는것은 곧 먼저하냐 나중에하냐
versus = AiBase(Board)  # 상대는 자동으로 생성해준다
while True:
    flag = 0  # 끝까지 플래그가 0이라면 비긴것이다. 승패가 결정된다면 flag는 1이된다.
    playcount += 1  # 게임 한번당 playcount 가 1씩 올라간다.
    print("게임을 시작합니다.")
    print('=' * 30 + '\n')  # 여기서 부터 게임이 시작된다

    if playernum == -1:  # 만약 플레이어의 문양이 -1(선공) 이라면
        display()  # 일단 비어있는 판을 보여주고

        playerturn(versus)  # 플레이어턴

        for i in range(4):  # AI->플레이어 순으로 4번 반복하여 8번의 턴이 지나가는 반복문
            aiturn(versus)

            if losejudge():  # 인공지능이 이겼는가 확인
                print("패배하셨습니다.")  # 인공지능이 이겼다면 패배했다는 메세지를 출력하며
                flag = 1  # 아까 주석처럼 flag는 1이되고
                break  # 반복문은 중단한다.

            playerturn(versus)  # 플레이어턴

            if winjudge():  # 플레이어가 이겼는가 확인
                print("승리하셨습니다.")  # 플레이어가 이겼다면 승리했다는 메세지 출력
                flag = 1  # 이전 주석처럼 flag는 1이 됨
                win += 1  # 이긴 횟수를 +1.
                break  # 반복문을 중단한다

        if flag == 0:  # 모든 공간에 놓였을때까지 승패가 나지 않았다면
            print("비기셨습니다.")  # 비긴것이다.

    else:  # 플레이어가 후공일때. 플레이어의 선공/후공 여부만 다르고 다른 내용들은 모두 플레이어가 선공일때와 같다.
        aiturn(versus)

        for i in range(4):
            playerturn(versus)  # 플레이어턴
            if winjudge():
                flag = 1
                print("승리하셨습니다.")
                win += 1

            aiturn(versus)
            if losejudge():
                print("패배하셨습니다.")
                flag = 1
                break

        if flag == 0:
            print("비기셨습니다.")

    if select_replay() is False:  # 게임을 그만하는것을 선택하면
        display_winrate()  # 승률을 출력해주고
        break  # 전체반복문을 빠져나가 프로그램을 종료한다.

    # 그만하는것을 입력하지 않았다면 아래의 6줄이 실행된 뒤 다시 반복문의 처음으로 돌아간다.
    select_display_winrate()  # 승률을 출력할것인지 선택한다.
    first_or_second = select_mark()  # 마크를 고른다는것은 곧 먼저하냐 나중에하냐를 이야기한다
    Board = copy.deepcopy(PureBoard)  # 0으로만 채워진, 순수한 보드를 가져온다.
    versus = AiBase(Board)  # 상대를 다시 초기화시켜 불러온다
