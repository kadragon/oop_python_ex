import random

how_win = [[1, 2, 3], [4, 5, 6], [7, 8, 9], [1, 4, 7], [2, 5, 8], [3, 6, 9], [1, 5, 9], [3, 5, 7]]  # 이기는 경우의 수


def show_board(board):  # 게임보드 출력
    print("%s %s %s" % (board[1], board[2], board[3]))
    print("%s %s %s" % (board[4], board[5], board[6]))
    print("%s %s %s" % (board[7], board[8], board[9]))


def game_end(board):  # 이겼는지, 졌는지, 비겼는지, 끝나지 않았는지 확인
    for i in how_win:
        # O와 X의 개수 저장
        sum1 = 0
        sum2 = 0
        sum3 = 0
        for j in i:
            if board[j] == 'O':
                sum1 += 1
                if sum1 == 3:  # 한 줄이 모두 O일 때
                    return 1
            if board[j] == 'X':
                sum2 += 1
                if sum2 == 3:  # 한 줄이 모두 X일 때
                    return 2
        for i in range(1, 10):
            if board[i] != '-':
                sum3 += 1
                if sum3 == 9:  # 더 이상 둘 곳이 없을 때 == 비겼을 때
                    return 0
    return -1  # 게임이 끝나지 않음


def computer_turn(board):
    for i in range(1, 10):  # 놓으면 computer가 이길 수 있는 곳이 있다면 그 자리에 말을 놓는다.
        if board[i] == '-':
            board[i] = 'X'  # i칸에 말을 놓는다 가정
            if game_end(board) == 2:  # i칸에 말을 놓았을 때 이길 수 있으면 그 자리에 놓는다.
                return
            else:
                board[i] = '-'  # 한 번에 이길 수 있는 수가 없다면 일단 원상복귀

    for i in range(1, 10):  # 막지 않으면 player가 이길 수 있는 곳이 있다면 그 자리에 말을 놓는다.
        if board[i] == '-':
            board[i] = 'O'  # 다음 차례에 player가 i칸에 말을 놓았을 때
            if game_end(board) == 1:  # player가 이긴다면 그 자리를 막는다.
                board[i] = 'X'
                return
            else:
                board[i] = '-'  # 어떤 경우에도 player가 다음 턴에 승리할 수 없다면 일단 원상복귀

    if board[5] == '-':  # 중앙이 비어있다면 중앙 선점
        board[5] = 'X'
        return

    select = [1, 3, 7, 9]  # 꼭짓점이 비어있다면 랜덤으로 모서리 선점
    random.shuffle(select)
    for i in select:
        if board[i] == '-':
            board[i] = 'X'
            return

    select = [2, 4, 6, 8]  # 남는 자리 중 하나 선점
    random.shuffle(select)
    for i in select:
        if board[i] == '-':
            board[i] = 'X'
            return


def player_turn(board):
    show_board(board)
    print("말을 놓을 위치를 선택해주세요.")
    while True:
        put = input()
        if put not in ['1', '2', '3', '4', '5', '6', '7', '8', '9']:  # 잘못 입력한 경우 재입력 요청
            print("1 ~ 9의 정수 중 하나를 입력해주세요")
        else:
            put = int(put)
            if board[put] == '-':  # player가 원하는 곳에 말 놓기
                board[put] = 'O'
                break
            else:  # 이미 말이 있는 곳에 말을 놓고자 할 때
                print("이미 채워진 칸에는 말을 놓을 수 없습니다.")


def play_again():  # 게임을 지속할 지 묻기
    print("게임을 다시 플레이하시겠습니까?")
    print("다시 플레이하시려면 Y를, 그만하시려면 N를 입력해주세요")

    while True:
        again = input()
        if again == 'Y':
            return True
        elif again == 'N':
            return False
        else:  # 에러 체크
            print("Y와 N 둘 중에 하나만을 선택해주세요.")


def record(win, lose, tie):  # 승률 출력
    print("현재 승률은 %d %% 입니다." % (win * 100 / (win + lose + tie)))
    print("%d승 %d패 %d무" % (win, lose, tie))
    return


win = 0  # 이긴 횟수
lose = 0  # 진 횟수
tie = 0  # 비긴 횟수

while True:
    print("지금부터 TicTacToe 게임을 시작하겠습니다!")
    board = ['-'] * 10  # 게임보드 생성
    get_turn = True

    while get_turn == True:
        get_turn = False
        print("원하는 순서에 해당하는 번호를 입력해주세요")  # 선 플레이어 결정하기
        print("1: 선 플레이어  | 2: 후 플레이어")
        order = input()

        if order == '1':
            turn = 'player'
        elif order == '2':
            turn = 'computer'
        else:  # 에러 체크
            get_turn = True
            print("반드시 1, 2중에 하나를 선택하셔야 합니다.")

    print("지금부터 TicTacToe 게임을 시작합니다.")
    print("유저분의 말은 O, 컴퓨터의 말은 X, 빈 공간은 - 입니다.")

    while True:
        if turn == 'player':  # 플레이어의 차례
            player_turn(board)
            if game_end(board) == 1:  # 이겼을 때
                show_board(board)
                print("축하합니다! 유저분이 승리하셨습니다.")
                win += 1
                record(win, lose, tie)
                if play_again():  # player가 게임의 지속을 원할 때
                    print("게임을 다시 시작합니다.")
                    break
                else:  # player가 게임을 끝내고 싶어할 때
                    print("TicTacToe 게임을 이용해 주셔서 감사합니다.")
                    exit()

            if game_end(board) == 0:  # 비겼을 때
                show_board(board)
                print("안타깝지만 비겼습니다.")
                tie += 1
                record(win, lose, tie)
                if play_again():  # player가 게임의 지속을 원할 때
                    print("게임을 다시 시작합니다.")
                    break
                else:  # player가 게임을 끝내고 싶어할 때
                    print("TicTacToe 게임을 이용해 주셔서 감사합니다.")
                    exit()

            if game_end(board) == -1:  # 게임이 끝나지 않았을 때
                turn = 'computer'

        else:  # 컴퓨터의 차례
            computer_turn(board)
            if game_end(board) == 2:  # 이겼을 때
                show_board(board)
                print("이런, 패배하셨습니다.")
                lose += 1
                record(win, lose, tie)
                if play_again():  # player가 게임의 지속을 원할 때
                    print("게임을 다시 시작합니다.")
                    break
                else:  # player가 게임을 끝내고 싶어할 때
                    print("TicTacToe 게임을 이용해 주셔서 감사합니다.")
                    play = False
                    exit()

            if game_end(board) == 0:  # 비겼을 때
                show_board(board)
                print("안타깝지만 비겼습니다.")
                tie += 1
                record(win, lose, tie)
                if play_again():  # player가 게임의 지속을 원할 때
                    print("게임을 다시 시작합니다.")
                    break
                else:  # player가 게임을 끝내고 싶어할 때
                    print("TicTacToe 게임을 이용해 주셔서 감사합니다.")
                    play = False
                    exit()

            if game_end(board) == -1:  # 게임이 끝나지 않았을 때
                turn = 'player'
