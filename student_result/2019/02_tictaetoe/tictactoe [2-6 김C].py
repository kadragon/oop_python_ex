import random


def FirstPlayer():
    """
    매 라운드마다 게임을 시작할 쪽을 정하는 함수
    매개변수 : 없음
    리턴값 : True는 플레이어, False는 컴퓨터 의미
    """
    if random.randint(0, 1) == 0:
        return False
    else:
        return True


def Print_Gameboard(board):
    """
    게임보드를 출력하는 함수
    매개변수 : 게임보드를 저장하는 행렬
    리턴값 : 없음
    """
    print(" " * 4 + "1" + " " * 3 + "2" + " " * 3 + "3")
    print(" " * 2 + "=" * 13)
    print("1 " + "|" + " " + board[0] + " " + "|" + " " + board[1] + " " + "|" + " " + board[2] + " " + "|")
    print(" " * 2 + "=" * 13)
    print("2 " + "|" + " " + board[3] + " " + "|" + " " + board[4] + " " + "|" + " " + board[5] + " " + "|")
    print(" " * 2 + "=" * 13)
    print("3 " + "|" + " " + board[6] + " " + "|" + " " + board[7] + " " + "|" + " " + board[8] + " " + "|")
    print(" " * 2 + "=" * 13)


def IsBoardFull(board):
    """
    게임보드가 꽉 찼는지 확인하는 함수
    매개변수 : 게임보드를 저장하는 리스트
    리턴값 : 보드가 꽉 차있으면 True, 그렇지 않으면 False
    """
    for i in range(9):
        if board[i] == ' ':
            return False

    return True


def Cal_WinningRate(computer, user):
    """
    승률을 계산하는 함수
    매개변수 : 컴퓨터 승점, 플레이어 승점
    리턴값 : 승률값 (실수)
    """
    return 100 * user / (computer + user)


def PlayerMove(board, x, y):
    """
    플레이어의 입력을 보드에 기록하는 함수
    매개변수 : 게임보드를 저장하는 리스트, 행좌표, 열좌표
    리턴값 : 없음
    """
    x = int(x)
    y = int(y)
    board[(x - 1) * 3 + (y - 1)] = char_player


def ComMove(board):
    """
    컴퓨터의 움직임을 기록하는 함수
    매개변수 : 게임보드를 저장하는 리스트
    리턴값 : 없음
    """
    if IsPlayerGotChance(board) != 0:  # 플레이어가 이길 수 있는 경우의 수를 가진 경우 따로 처리
        board[IsPlayerGotChance(board) - 1] = char_com

    else:  # 플레이어가 이길 수 있는 경우가 없는 경우
        nums = list(range(9))
        random.shuffle(nums)  # 랜덤하게 수를 둠
        for i in range(9):
            if board[nums[i]] == ' ':
                board[nums[i]] = char_com
                break


def IsPlayerGotChance(board):
    """
    플레이어가 이길 수 있는 경우를 체크하는 함수
    매개변수 : 게임보드를 저장하는 리스트
    리턴값 : 0 (플레이어가 찬스를 잡지 않은 경우) / 1~9 (방어해야 할 위치) (정수)
    """
    B1 = board[0]
    B2 = board[1]
    B3 = board[2]
    B4 = board[3]
    B5 = board[4]
    B6 = board[5]
    B7 = board[6]
    B8 = board[7]
    B9 = board[8]

    # 가로방향 체크
    if ThreeCheck(B1, B2, B3) != 0 and board[ThreeCheck(B1, B2, B3) - 1] == ' ':
        return ThreeCheck(B1, B2, B3)
    if ThreeCheck(B4, B5, B6) != 0 and board[ThreeCheck(B1, B2, B3) + 3 - 1] == ' ':
        return ThreeCheck(B4, B5, B6) + 3
    if ThreeCheck(B7, B8, B9) != 0 and board[ThreeCheck(B7, B8, B9) + 6 - 1] == ' ':
        return ThreeCheck(B7, B8, B9) + 6

    # 세로방향 체크
    if ThreeCheck(B1, B4, B7) != 0 and board[(ThreeCheck(B1, B4, B7) - 1) * 3 + 1 - 1] == ' ':
        return (ThreeCheck(B1, B4, B7) - 1) * 3 + 1
    if ThreeCheck(B2, B5, B8) != 0 and board[(ThreeCheck(B2, B5, B8) - 1) * 3 + 2 - 1] == ' ':
        return (ThreeCheck(B2, B5, B8) - 1) * 3 + 2
    if ThreeCheck(B3, B6, B9) != 0 and board[(ThreeCheck(B3, B6, B9) - 1) * 3 + 3 - 1] == ' ':
        return (ThreeCheck(B3, B6, B9) - 1) * 3 + 3

    # 대각선방향 체크
    if ThreeCheck(B1, B5, B9) != 0 and board[1 + (ThreeCheck(B1, B5, B9) - 1) * 4 - 1] == ' ':
        return 1 + (ThreeCheck(B1, B5, B9) - 1) * 4
    if ThreeCheck(B3, B5, B7) != 0 and board[3 + (ThreeCheck(B3, B5, B7) - 1) * 2 - 1] == ' ':
        return 3 + (ThreeCheck(B3, B5, B7) - 1) * 2

    return 0


def ThreeCheck(k1, k2, k3):
    """
    3개의 원소 중 2개가 플레이어의 표식이며 나머지 한 자리가 비어있는지를 체크하는 함수
    매개변수 : 세 원소의 값
    리턴값 : 0 (해당없음) / 1, 2, 3 (어느 두 개가 같은 경우 비어있는 자리의 번호) (정수)
    """
    if k1 == char_player and k2 == char_player and k3 == ' ':
        return 3
    if k2 == char_player and k3 == char_player and k1 == ' ':
        return 1
    if k3 == char_player and k1 == char_player and k2 == ' ':
        return 2

    return 0


def Check_Input(input):
    """
    행, 열 입력값이 올바른지 체크하는 함수
    매개변수 : 행 또는 열 좌표
    리턴값 : 올바른 입력이면 True, 아니면 False
    """
    if input == '1' or input == '2' or input == '3':
        return True

    else:
        return False


def Check_Character(ch):
    """
    표식 입력값이 올바른지 체크하는 함수
    매개변수 : 표식 입력값
    리턴값 : 올바른 입력이면 True, 아니면 False
    """
    if ch == 'O' or ch == 'X':
        return True

    else:
        return False


def IsWinner(board, winner):  # winner가 승리하면 True, 그렇지 않으면 False
    """
    해당 쪽이 승리했는지 판단하는 함수
    매개변수 : 게임보드를 저장하는 리스트, 선수 정보
    리턴값 : winner가 승리하면 True, 그렇지 않으면 False
    """
    B1 = board[0]
    B2 = board[1]
    B3 = board[2]
    B4 = board[3]
    B5 = board[4]
    B6 = board[5]
    B7 = board[6]
    B8 = board[7]
    B9 = board[8]

    if winner == True:
        if B1 == char_player and B2 == char_player and B3 == char_player:
            return True
        if B4 == char_player and B5 == char_player and B6 == char_player:
            return True
        if B7 == char_player and B8 == char_player and B9 == char_player:
            return True
        if B1 == char_player and B4 == char_player and B7 == char_player:
            return True
        if B2 == char_player and B5 == char_player and B8 == char_player:
            return True
        if B3 == char_player and B6 == char_player and B9 == char_player:
            return True
        if B1 == char_player and B5 == char_player and B9 == char_player:
            return True
        if B3 == char_player and B5 == char_player and B7 == char_player:
            return True

        return False

    else:
        if B1 == char_com and B2 == char_com and B3 == char_com:
            return True
        if B4 == char_com and B5 == char_com and B6 == char_com:
            return True
        if B7 == char_com and B8 == char_com and B9 == char_com:
            return True
        if B1 == char_com and B4 == char_com and B7 == char_com:
            return True
        if B2 == char_com and B5 == char_com and B8 == char_com:
            return True
        if B3 == char_com and B6 == char_com and B9 == char_com:
            return True
        if B1 == char_com and B5 == char_com and B9 == char_com:
            return True
        if B3 == char_com and B5 == char_com and B7 == char_com:
            return True

        return False


# main loop
print("TicTacToe\n")
print("승리한 쪽이 승점 1점을 가져가고, 무승부일 경우 양쪽 모두 승점 1점을 획득합니다.")
print("승률은 플레이어의 승점을 전체 승점 총합으로 나눈 값입니다.\n")

sc_com = 0  # 컴퓨터의 점수를 저장하는 객체
sc_player = 0  # 플레이어의 점수를 저장하는 객체
char_com = ''  # 컴퓨터의 표식을 저장하는 객체
char_player = ''  # 플레이어의 표식을 저장하는 객체

print("플레이할 표식을 선택하세요! O / X")
ch = input()  # 플레이어의 표식 스캔

while (Check_Character(ch) == False):  # 플레이어 표식 입력 검사
    print("잘못된 입력입니다. 다시 입력하세요.")
    ch = input()

if ch == 'X':
    char_com = 'O'
    char_player = 'X'

else:
    char_com = 'X'
    char_player = 'O'

while True:
    board = [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']  # 게임보드 초기화
    turn = FirstPlayer()  # 랜덤하게 시작하는 쪽 선정

    if turn == True:
        print("이번 판은 플레이어가 먼저 시작합니다!\n")

    else:
        print("이번 판은 컴퓨터가 먼저 시작합니다!\n")

    KeepPlaying = True  # 게임을 계속해서 진행할지 여부를 저장하는 객체

    while KeepPlaying == True:
        if turn == True:  # True : 플레이어의 차례
            Print_Gameboard(board)  # 플레이어 차례가 될 때 마다 게임보드 출력
            print("행, 열 순서대로 표시할 좌표를 입력하세요.")

            print("행 좌표 :", end=' ')
            px = input()
            while (Check_Input(px) == False):  # 행을 잘못 입력한 경우
                print("올바르지 못한 입력입니다. 행 좌표를 다시 입력하세요.")
                print("행 좌표 :", end=' ')
                px = input()

            print("열 좌표 :", end=' ')
            py = input()
            while (Check_Input(py) == False):  # 열을 잘못 입력한 경우
                print("올바르지 못한 입력입니다. 열 좌표를 다시 입력하세요.")
                print("열 좌표 :", end=' ')
                py = input()

            while board[(int(px) - 1) * 3 + int(py) - 1] != ' ':  # 이미 값이 입력되어있는 경우 재입력
                print("이미 값이 입력되어 있습니다. 처음부터 다시 입력하세요.")

                print("행 좌표 :", end=' ')
                px = input()
                while (Check_Input(px) == False):
                    print("올바르지 못한 입력입니다. 행 좌표를 다시 입력하세요.")
                    print("행 좌표 :", end=' ')
                    px = input()

                print("열 좌표 :", end=' ')
                py = input()
                while (Check_Input(py) == False):
                    print("올바르지 못한 입력입니다. 열 좌표를 다시 입력하세요.")
                    print("열 좌표 :", end=' ')
                    py = input()

            PlayerMove(board, px, py)  # 플레이어 움직임 기록

            if IsWinner(board, turn) == True:  # 플레이어가 승리한 경우
                Print_Gameboard(board)
                print("승리!")
                sc_player += 1
                KeepPlaying = False

            else:
                if IsBoardFull(board) == True:  # 게임보드가 꽉 찬 경우
                    Print_Gameboard(board)
                    print("무승부!")
                    sc_player += 1
                    sc_com += 1
                    break

                else:  # 게임보드가 꽉 차있지 않은 경우
                    turn = False

        else:  # False : 컴퓨터의 차례
            ComMove(board)  # 컴퓨터의 수 기록

            if IsWinner(board, turn) == True:  # 컴퓨터가 승리한 경우
                Print_Gameboard(board)
                print("패배!")
                sc_com += 1
                KeepPlaying = False

            else:
                if IsBoardFull(board) == True:  # 게임보드가 꽉 찬 경우
                    Print_Gameboard(board)
                    print("무승부!")
                    sc_player += 1
                    sc_com += 1
                    break

                else:  # 게임보드가 꽉 차있지 않은 경우
                    turn = True

    rate = Cal_WinningRate(sc_com, sc_player)  # 승률 계산
    print("현재 승률은 %.1f퍼센트 입니다." % rate)
    print("다시 플레이하시겠습니까? Y / N")  # 리플레이 여부
    res = input()

    while res != 'N' and res != 'Y':  # 리플레이 여부 입력 검사
        print("잘못된 입력입니다. 다시 답해주세요. Y / N")
        res = input()

    if res == 'N':  # 게임 종료
        break
