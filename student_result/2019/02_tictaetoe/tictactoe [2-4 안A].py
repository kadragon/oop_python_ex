import random  # random.shuffle()을 사용하게 해준다.
import time  # time.sleep()을 사용하게 해준다.

winners = [[1, 2, 3], [4, 5, 6], [7, 8, 9], [1, 4, 7], [2, 5, 8], [3, 6, 9], [1, 5, 9], [3, 5, 7]]


# 게임 보드 상에서 컴퓨터나 사용자의 말이 winners 리스트의 한 원소의 숫자열처럼 board 칸에 배치되면 게임에서 승리하게 됨
# 예를 들면 board 1,2,3칸에 한 종류의 문자가 배치되면 그 문자를 두던 사람이 승리한다.

def printboard(board):
    """
    board 리스트의 원소들을 실제 틱택토 보드판 형태 위에 의도했던대로 알맞게 배치하여 출력하게 해주는 함수이다.
    :param board: 이 board 리스트는 틱택토 게임에서 9칸이 있는데 그 칸들을 왼쪽 위칸부터 오른쪽 아래칸 순서로 일렬로 배치
    한 것을 board[1]부터 board[9]까지 일차원리스트로 구현한 것이다. 게임 보드의 현재 상황을 나타낸 리스트
    예를 들면 가장 왼쪽 위칸은 board[1], 그 오른쪽칸은 board[2] 이렇게 대응된다.
    """
    print(' ' + board[1] + ' | ' + board[2] + ' | ' + board[3])
    print('-----------')
    print(' ' + board[4] + ' | ' + board[5] + ' | ' + board[6])
    print('-----------')
    print(' ' + board[7] + ' | ' + board[8] + ' | ' + board[9])


def chooseletter():
    """
    이 함수는 사용자가 게임판에 말을 둘 때 말을 O나 X 중 무엇을 할지 고르게 하는 함수이다. 사용자가 O를 입력하면 자동으로
    컴퓨터의 문자가 X가 되게 해주고 사용자가 O,X,o,x말고 다른 것을 입력하였을 때 다시 입력하게 한다.
    :return: 처음 원소는 사용자가 택한 문자, 두번째 원소는 컴퓨터의 문자인 리스트를 리턴한다.
    """
    XorO = ''
    passwhenzero = 0
    while not (XorO == 'X' or XorO == 'O'):  # 사용자가 'X'나 'O'를 안입력했을 때 계속 반복하게 한다.
        if passwhenzero >= 1:  # passwhenzero 가 1이상일때 if 조건 실행하게함. 처음엔 0이니 이 if문 그냥 통과됨
            print("제대로 입력합시다.\n")  # 이 if문이 실행된다는 것은 사용자가 한번 이상 'O'나 'X'를 입력안했을 때이다.
        XorO = input('먼저 어느 문자를 사용할 것입니까? (O or X)').upper()  # XorO 에 사용자가 입력한 값을 대입한다.
        # .upper()함수를 사용해서 사용자가 영어 소문자로 입력해도 영어 대문자로 바꿔준다. 예를들면 o 입력해도 O로 저장됨
        passwhenzero = passwhenzero + 1  # passwhenzero 가 1이 더해진다. while 조건을 안벗어난다면 다음 턴에서 if문이 실행될 것이다.
    print("=" * 80)
    if XorO == 'X':  # 사용자가 x나 X를 입력했을 때
        return ['X', 'O']  # 처음 원소는 사용자가 택한 문자, 두번째 원소는 컴퓨터의 문자인 리스트를 리턴한다.
    else:  # 사용자가 o나 O를 입력했을 때
        return ['O', 'X']  # 처음 원소는 사용자가 택한 문자, 두번째 원소는 컴퓨터의 문자인 리스트를 리턴한다.


def chooseturn():
    """
    사용자가 선공할지 컴퓨터가 선공할지를 정해주는 함수이다.
    :return: 랜덤 결과에 따라 '사용자'나 '컴퓨터'를 반환한다.
    """
    rand_0or1 = list(range(2))  # 0, 1로 이루어진 리스트인 rand_0or1을 만든다.
    random.shuffle(rand_0or1)  # rand_0or1 리스트의 원소들을 랜덤으로 섞는다.
    if rand_0or1[0] == 0:  # 랜덤으로 섞은 rand_0or1 의 첫번째 원소가 0이 된다면
        return '사용자'  # '사용자'를 반환함
    elif rand_0or1[0] == 1:
        return '컴퓨터'  # '컴퓨터'를 반환함


def playerinput():
    """
    사용자가 게임도중 몇번 칸에 말을 둘지 숫자를 입력한 player_num이 게임 조건에 맞는지 판단하고 조건에 맞으면 반환한다.
    :return: player_num을 정수형으로 바꾼 player_num_n이 게임 조건에 맞다면 반환한다.
    """
    while 1:
        player_num = input('말을 두고 싶은 칸의 번호를 쓰세요\n')  # player_num에 사용자가 칸에 자신의 말을 두기 위해 입력한 값을 string형으로 받는다.
        if player_num.isdigit():  # .isdigit() 함수를 사용하여 player_num이 숫자로만 이루어졌다면 if조건을 통과시켜준다.
            player_num_n = 0
            for k in player_num:  # 반복문을 사용하여 정수형인 player_num_n에 한자리씩 string형인 player_num의 값들을 대응시킨다. / 문자열'123'-->숫자 123, '092'-->92
                player_num_n *= 10
                player_num_n += int(k)
            empty1 = list()  # 빈 리스트인 empty1을 만든다.
            for i in range(1, 10):  # i는 1에서 9까지 증가한다.
                if board[i] == ' ':  # 만약에 board[i]에 컴퓨터와 사용자의 문자가 입력되어 있지 않고 비어있다면
                    empty1.append(
                        i)  # empty1 리스트에 i값을 추가시켜준다. 결국 for 반복문이 다 돌면 empty1 리스트엔 board 중 비어있는 칸의 숫자들만 입력되게 된다.
            if player_num_n in range(1, 10):  # player_num_n이 1~9까지의 정수에 속한다면
                if player_num_n in empty1:  # player_num_n이 empty1 리스트에 있는 숫자에 속한다면 (board에서 비어있는 칸의 숫자라면)
                    return player_num_n  # 1~9까지의 숫자고 비어있는 칸의 숫자를 사용자가 입력했으니 게임조건에 맞게 입력한 것이다. 이때 player_num_n을 반환한다.
                else:  # player_num_n이 board에서 비어있지 않은 칸의 숫자라면 (게임 조건에 맞지 않는다.)
                    print("이미 자리에 O나 X표가 쳐져있습니다.")
            if player_num_n == 0 or player_num_n >= 10:  # player_num_n이 0이거나 10이상의 정수라면 (게임 조건에 맞지 않는다.)
                print("1~9까지의 숫자만 입력해주세요")
        else:  # player_num이 숫자로 이루어지지 않았다면 (게임 조건에 맞지 않는다.)
            print("1~9까지의 숫자만 입력해주세요")


def computerai(board):
    """
    board 의 상황에 따라 컴퓨터가 어느 칸에다가 컴퓨터가 말을 둘지 고르고 그 칸에 컴퓨터의 문자를 대입해주는 합수이다.
    컴퓨터가 그 칸에 안두면 게임이 질 상황엔 그 칸에 두게 하고 컴퓨터가 그 칸에 두면 이길 상황일 때 그 칸에 두게 해준다.
    나머지 상황은 비어있는 칸 중 랜덤으로 컴퓨터의 문자를 대입한다.
    컴퓨터가 1 칸에 두면 이기고 3칸에 두면 사용자가 이기는 것을 막을 수 있을 때 1칸에 두는 것을 우선으로 두었다.
    :param board: 이 board 리스트는 틱택토 게임에서 9칸이 있는데 그 칸들을 왼쪽 위칸부터 오른쪽 아래칸 순서로 일렬로 배치
    한 것을 board[1]부터 board[9]까지 일차원리스트로 구현한 것이다. 게임 보드의 현재 상황을 나타낸 리스트
    """

    board_c = board.copy()  # .copy() 함수를 사용하여 board를 복사해서 board와 똑같은 리스트인 board_c를 만든다.
    empty = list()  # 비어있는 리스트인 empty 리스트를 만든다.
    for i in range(1, 10):  # i는 1에서 9까지 증가한다.
        if board[i] == ' ':  # 만약에 board[i]에 컴퓨터와 사용자의 문자가 입력되어 있지 않고 비어있다면
            empty.append(i)  # empty 리스트에 i값을 추가시켜준다. 결국 for 반복문이 다 돌면 empty 리스트엔 board 중 비어있는 칸의 숫자들만 입력되게 된다.

    for i in empty:  # i는 empty 리스트에 들어있는 숫자. for문이 돌아가며 empty 리스트 안에 들어있는 숫자가 i에 다 대응됨
        board_c[i] = computer_l  # board_c 에서 비어있는 칸에 컴퓨터의 문자인 computer_l를 대입한다.
        for j in winners:  # j는 winners 리스트에 있는 원소
            win = True  # win 이라는 변수에 True를 대입한다.
            for k in j:  # k는 j 리스트의 원소
                # 사실 winners 리스트의 원소도 리스트이다. 예를 들면 winners의 원소 중 하나인 [1,2,3]도 1,2,3이라는 원소를 포함한 리스트
                if board_c[k] != computer_l:  # 만약 k번째 칸에 컴퓨터의 문자가 없다면
                    win = False  # win이라는 변수에 False 대입 / 가상의 보드판인 board_c에 비어있는 칸 중 하나인 i 번째 칸에 컴퓨터의 문자를 대입했을 때 컴퓨터가 이기지 않는다.
                    # 이는 실제 보드판 board에서 컴퓨터의 문자를 i 번째 칸에 대입했을때 컴퓨터가 이기는 상황이 안일어남을 의미
                    break
            if win is True:  # win이 True라면 / board_c의 i 번째 칸에 컴퓨터 문자를 대입했을 때 컴퓨터가 승리하게 된다면
                board[i] = computer_l  # 실제 보드판인 board에 컴퓨터의 문자를 대입한다. / 컴퓨터가 실제로 승리하게 될 것이다.
                return
        board_c[i] = ' '  # board_c 의 i 번째 칸에 컴퓨터의 문자를 둘 때 시뮬레이션을 다 했으니 board_c[i]를 빈칸으로 초기화해준다.

    for i in empty:  # i는 empty 리스트에 들어있는 숫자. for 문이 돌아가며 empty 리스트 안에 들어있는 숫자가 i에 다 대응됨
        board_c[i] = player_l  # board_c 에서 비어있는 칸에 사용자의 문자인 player_l를 대입한다.
        for j in winners:  # j는 winners 리스트에 있는 원소
            win = True  # win 이라는 변수에 True를 대입한다.
            for k in j:  # k는 j 리스트의 원소
                if board_c[k] != player_l:  # 만약 k번째 칸에 사용자의 문자가 없다면
                    win = False  # win이라는 변수에 False 대입 / 가상의 보드판인 board_c에 비어있는 칸 중 하나인 i 번째 칸에 사용자의 문자를 대입했을 때 사용자가 이기지 않는다.
                    # 이는 실제 보드판 board에서 사용자의 문자를 i 번째 칸에 대입했을때 사용자가 이기는 상황이 안일어남을 의미
                    break
            if win is True:  # win이 True라면 / board_c의 i 번째 칸에 사용자 문자를 대입했을 때 사용자가 승리하게 된다면
                board[i] = computer_l  # 실제 보드판인 board에 컴퓨터의 문자를 대입한다. / 사용자가 이기는 상황을 막을 수 있을 것이다.
                return
        board_c[i] = ' '  # board_c 의 i 번째 칸에 사용자의 문자를 둘 때 시뮬레이션을 다 했으니 board_c[i]를 빈칸으로 초기화해준다.

    empty = list()  # 비어있는 리스트인 empty 리스트를 만든다.
    for i in range(1, 10):  # i는 1에서 9까지 증가한다.
        if board[i] == ' ':  # 만약에 board[i]에 컴퓨터와 사용자의 문자가 입력되어 있지 않고 비어있다면
            empty.append(i)  # empty 리스트에 i값을 추가시켜준다. 결국 for 반복문이 다 돌면 empty 리스트엔 board 중 비어있는 칸의 숫자들만 입력되게 된다.
    random.shuffle(empty)  # empty 리스트의 원소들을 랜덤으로 섞어준다.
    board[empty[0]] = computer_l  # 랜덤으로 섞은 후 empty 리스트의 원소 중 첫번째 원소에 해당되는 숫자의 board 칸에 컴퓨터의 문자를 대입한다.
    # 컴퓨터가 남은 비어있는 칸 중 랜덤으로 칸을 정하여 자신의 문자를 두는 것을 의미


def ending():
    """
    비기거나 승,패가 정해져서 게임 한판이 끝났을 때 사용자에게 게임을 재시작할건지 종료할건지 선택하게 하는
    함수
    :return: 사용자가 게임을 종료한다면 False, 게임을 다시 시작하겠다고 하면 True
    """
    while 1:  # return이 안됬다면(질문에 yes,no로 대답안했을 때) 계속 반복
        print("=" * 80)
        YorN1 = input('게임을 다시 하시겠습니까? (yes or no)')  # YorN1는 첫번째 질문에 대해 사용자가 입력한 것
        if YorN1 == 'no':  # 사용자가 게임을 다시 안하겠다고 했을 때
            while 1:  # return이 안됬다면(질문에 yes,no로 대답안했을 때) 계속 반복
                YorN2 = input('\n정말 이 게임을 종료시키겠습니까? (yes or no)')  # YorN2는 두번째 질문에 대해 사용자가 입력한 것
                if YorN2 == 'yes':  # 사용자가 정말 이 게임 종료하겠다 했을 때 False 반환
                    return False
                elif YorN2 == 'no':  # 사용자가 아까 no를 잘못눌렀거나 사실 이 게임을 종료하기 싫다고 했을 때 True 반환
                    return True
                else:  # 사용자가 질문에 yes, no로 대답 안했을 때
                    print("똑바로 대답합시다")
        elif YorN1 == 'yes':  # 사용자가 게임을 다시 하겠다고 했을 때
            return True
        else:  # 사용자가 질문에 yes, no로 대답 안했을 때
            print("똑바로 대답합시다")


def isitend(board):
    """
    컴퓨터나 사용자가 이겨서 끝나거나 무승부로 게임이 끝나거나 아니면 게임이 아직 안끝났는지를 판단해주는 함수이다.
    :param board: 이 board 리스트는 틱택토 게임에서 9칸이 있는데 그 칸들을 왼쪽 위칸부터 오른쪽 아래칸 순서로 일렬로 배치
    한 것을 board[1]부터 board[9]까지 일차원리스트로 구현한 것이다. 게임 보드의 현재 상황을 나타낸 리스트
    :return: 컴퓨터가 이겨서 게임이 끝났으면 'computer' 반환
    사용자가 이겨서 게임이 끝났으면 'player' 반환
    무승부로 게임이 끝났으면 'tie' 반환
    게임이 아직 안끝났으면 'not end' 반환
    """
    for i in winners:  # i는 winners의 리스트에 있는 원소
        win = True  # win이라는 변수에 True 대입
        for j in i:  # j는 winners의 원소 중 하나인 i라는 리스트의 원소
            if board[j] != computer_l:  # 만약 j번째 칸에 컴퓨터의 문자가 없다면
                win = False  # win에 False 대입 / 컴퓨터가 승리한 상황이 아니라는 것이다.
                break
        if win is True:  # win 이 True 라면 / 컴퓨터가 승리한 상황일 때
            return 'computer'

    for i in winners:  # i는 winners의 리스트에 있는 원소
        win = True  # win이라는 변수에 True 대입
        for j in i:  # j는 winners의 원소 중 하나인 i라는 리스트의 원소
            if board[j] != player_l:  # 만약 j번째 칸에 사용자의 문자가 없다면
                win = False  # win에 False 대입 / 사용자가 승리한 상황이 아니라는 것이다.
                break
        if win is True:  # win 이 True 라면 / 사용자가 승리한 상황일 때
            return 'player'

    for i in range(1, 10):  # 사용자나 컴퓨터가 승리한 상황이 아닐 때 i를 1부터 9까지 증가시키며 반복문을 돌린다.
        if board[i] == ' ':  # 만약 board 칸이 비어있다면
            return 'not end'  # 아직 게임이 끝나지 않았다.
    return 'tie'  # 누가 승리하지도 않았는데 board 칸이 가득 차있다면 게임이 비긴상태로 끝난 것이다.


def recording(word):
    """
    이번 판에서 누가 이기거나 비겼다는 정보를 받고 그 전판까지의 결과들을 총합하여 사용자의 승률을 출력해주는 함수
    :param word: 컴퓨터가 이겼다는 'computer', 사용자가 이겼다는 'player', 비겼다는 'tie'라는 정보를 word라고 하였다.
    """
    global computer_c, player_c, tie_c  # 전역변수인 computer_c, player_c, tie_c를 이 함수에서 사용한다.
    # 이 변수들은 한 판이 끝나도 값이 변하지 않는다.
    if word == 'player':  # 이번 판에서 사용자가 이겼다면
        player_c += 1  # player_c 변수에 1을 더한다. / 사용자가 이긴 횟수 1증가
    elif word == 'computer':  # 이번 판에서 컴퓨터가 이겼다면
        computer_c += 1  # computer_c 변수에 1을 더한다. / 컴퓨터가 이긴 횟수 1증가
    elif word == 'tie':  # 이번 판에서 컴퓨터와 사용자가 비겼다면
        tie_c += 1  # tie_c 변수에 1을 더한다. / 비긴 횟수 1증가
    sum = player_c / (player_c + computer_c + tie_c)  # sum 은 (사용자가 이긴 횟수)/(게임 플레이 한 횟수)
    print('당신의 승률은 %.2f퍼센트입니다' % (sum * 100))  # 승률에 sum에 100을 곱한값을 출력


print("=" * 80)
print("틱택토 게임에 온 것을 환영합니다")
print("이 틱택토 게임에선 왼쪽 위부터 오른쪽 아래 칸 순서대로 칸의 번호가 1,2,3,4,5,6,7,8,9 입니다.")
print(' 1 | 2 | 3')
print('-----------')
print(' 4 | 5 | 6')
print('-----------')
print(' 7 | 8 | 9')

player_c = 0
computer_c = 0
tie_c = 0
while 1:
    board = [' '] * 10  # board라는 리스트를 0~9까지 빈칸으로 초기화한다.
    player_l, computer_l = chooseletter()  # 사용자와 컴퓨터의 문자를 정하는 함수를 사용하여 player_l에 사용자의 문자, computer_l에 컴퓨터의 문자 대입
    turn = chooseturn()  # turn이라는 변수에 누가 먼저 시작할지 정하는 함수의 리턴값을 넣는다. 사용자 먼저면 '사용자', 컴퓨터 먼저면 '컴퓨터'가 된다.
    print(turn + '가 먼저 시작합니다')
    while 1:
        if turn == '사용자':  # 사용자의 차례라면
            print("\n당신 차례입니다")
            player_num_n = playerinput()  # 사용자가 입력한 값이 게임 조건에 맞는지 판단하고 맞을 때 리턴하는 함수의 리턴값을 변수에 대입함
            board[player_num_n] = player_l  # 사용자가 입력한 숫자에 해당되는 board 칸에 사용자의 문자를 넣는다.
            turn = '컴퓨터'  # 차례를 컴퓨터 차례로 돌린다.
            printboard(board)  # 사용자가 말을 두고 나서의 게임 보드판의 현황을 출력한다.
        elif turn == '컴퓨터':  # 컴퓨터의 차례라면
            print("\n제 차례이니 제가 한번 해보겠습니다\n")
            time.sleep(1)  # 컴퓨터가 바로 말을 두지 않게 1초 실행을 잠시 멈추게 하였다.
            computerai(board)  # 컴퓨터가 현재 상황에서 어디에 말을 두어야하는지 판단하고 말을 두는 함수 실행
            turn = '사용자'  # 차례를 사용자 차례로 돌린다.
            printboard(board)  # 컴퓨터가 말을 두고 나서의 게임 보드판의 현황을 출력한다.
        result = isitend(board)  # result 에다 현재 보드판이 게임이 끝났는지 끝났으면 누가 이기거나 비겼는지 판단하는 함수의 리턴값을 대입
        if result == 'not end':  # 게임이 아직 안끝났으면
            continue
        else:  # 게임이 끝났으면
            break
    if result == 'player':  # 게임이 끝났고 사용자가 이겼으면
        print("당신이 이겼습니다!!")
        recording('player')  # 승률을 출력하는 함수에 이번 판은 사용자가 이겼다는 것을 대입하여 승률을 갱신해준다.
    elif result == 'computer':  # 게임이 끝났고 컴퓨터가 이겼으면
        print("졌어요ㅜㅜ")
        recording('computer')  # 승률을 출력하는 함수에 이번 판은 컴퓨터가 이겼다는 것을 대입하여 승률을 갱신해준다.
    elif result == 'tie':  # 게임이 끝났고 비겼으면
        print("비겼습니다")
        recording('tie')  # 승률을 출력하는 함수에 이번 판은 비겼다는 것을 대입하여 승률을 갱신해준다.
    TorF = ending()  # 한 게임이 끝났으니 사용자에게 게임을 다시할 것인지 종료할 것인지 선택하게 하는 함수 실행
    if TorF:  # 사용자가 게임을 다시 한다고 하였을 때
        print("=" * 80)
        continue
    else:  # 사용자가 게임을 종료한다고 하였을 때
        break
