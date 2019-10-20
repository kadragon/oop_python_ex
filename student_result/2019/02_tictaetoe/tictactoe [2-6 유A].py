import random


def First_Player():  # 처음 시작하는 쪽을 정하는 함수
    if random.randint(0, 1) == 0:  # 0과 1 중 랜덤으로 하나를 택해 0이면 False 리턴
        return False
    else:
        return True


def Gameboard(board):  # 게임보드를 출력하는 함수
    print(" " * 4 + "1" + " " * 3 + "2" + " " * 3 + "3")
    print(" " * 2 + "=" * 13)
    print("1 " + "|" + " " + board[0] + " " + "|" + " " + board[1] + " " + "|" + " " + board[2] + " " + "|")
    print(" " * 2 + "=" * 13)
    print("2 " + "|" + " " + board[3] + " " + "|" + " " + board[4] + " " + "|" + " " + board[5] + " " + "|")
    print(" " * 2 + "=" * 13)
    print("3 " + "|" + " " + board[6] + " " + "|" + " " + board[7] + " " + "|" + " " + board[8] + " " + "|")
    print(" " * 2 + "=" * 13)


def Board_Full(board):  # 꽉 찬 상태일 때 True, 그렇지 않을 때 False
    for i in range(9):
        if board[i] == ' ':  # 빈칸이 하나라도 있으면 False 리턴
            return False

    return True


def Winning_Rate(computer, user):  # 승률 계산 함수, computer 와 user 는 승리 회수 기록
    return 100 * user / (computer + user)


def Player_check(board, hang, yeol):  # 플레이어의 움직임을 보드에 기록하는 함수, 입력 받은 행과 열을 int 형으로 바꾼후 board 에 플레이어의 표식 기록
    hang = int(hang)
    yeol = int(yeol)
    board[(hang - 1) * 3 + (yeol - 1)] = char_player


def ComMove(board):  # 컴퓨터의 표식을 정하는 함수
    if Player_Chance(board) != 0:  # 플레이어가 찬스를 잡은 경우
        board[Player_Chance(board) - 1] = char_com  # 리턴 받은 값에 따라 표식을 결정

    else:  # 플레이어가 찬스를 잡지 않은 경우
        nums = list(range(9))  # 0부터 8까지 자연수 리스트 생성
        random.shuffle(nums)  # 리스트를 랜덤으로 정렬
        for i in range(9):
            if board[nums[i]] == ' ':  # 입력이 안되어 있으면 입력
                board[nums[i]] = char_com
                break


def Player_Chance(board):  # player 이 찬스를 잡았는지 판단
    B1_1 = board[0]  # 1행 1열
    B1_2 = board[1]  # 1행 2열
    B1_3 = board[2]  # 1행 3열
    B2_1 = board[3]  # 2행 1열
    B2_2 = board[4]  # 2행 2열
    B2_3 = board[5]  # 2행 3열
    B3_1 = board[6]  # 3행 1열
    B3_2 = board[7]  # 3행 2열
    B3_3 = board[8]  # 3행 3열

    # 가로방향 체크
    if ThreeCheck(B1_1, B1_2, B1_3) != 0 and board[ThreeCheck(B1_1, B1_2, B1_3) - 1] == ' ':
        return ThreeCheck(B1_1, B1_2, B1_3)
    if ThreeCheck(B2_1, B2_2, B2_3) != 0 and board[ThreeCheck(B1_1, B1_2, B1_3) + 3 - 1] == ' ':
        return ThreeCheck(B2_1, B2_2, B2_3) + 3
    if ThreeCheck(B3_1, B3_2, B3_3) != 0 and board[ThreeCheck(B3_1, B3_2, B3_3) + 6 - 1] == ' ':
        return ThreeCheck(B3_1, B3_2, B3_3) + 6

    # 세로방향 체크
    if ThreeCheck(B1_1, B2_1, B3_1) != 0 and board[(ThreeCheck(B1_1, B2_1, B3_1) - 1) * 3 + 1 - 1] == ' ':
        return (ThreeCheck(B1_1, B2_1, B3_1) - 1) * 3 + 1
    if ThreeCheck(B1_2, B2_2, B3_2) != 0 and board[(ThreeCheck(B1_2, B2_2, B3_2) - 1) * 3 + 2 - 1] == ' ':
        return (ThreeCheck(B1_2, B2_2, B3_2) - 1) * 3 + 2
    if ThreeCheck(B1_3, B2_3, B3_3) != 0 and board[(ThreeCheck(B1_3, B2_3, B3_3) - 1) * 3 + 3 - 1] == ' ':
        return (ThreeCheck(B1_3, B2_3, B3_3) - 1) * 3 + 3

    # 대각선방향 체크
    if ThreeCheck(B1_1, B2_2, B3_3) != 0 and board[1 + (ThreeCheck(B1_1, B2_2, B3_3) - 1) * 4 - 1] == ' ':
        return 1 + (ThreeCheck(B1_1, B2_2, B3_3) - 1) * 4
    if ThreeCheck(B1_3, B2_2, B3_1) != 0 and board[3 + (ThreeCheck(B1_3, B2_2, B3_1) - 1) * 2 - 1] == ' ':
        return 3 + (ThreeCheck(B1_3, B2_2, B3_1) - 1) * 2

    return 0


def ThreeCheck(k1, k2, k3):  # 세 개중 어느 두 개가 같은 경우 1,2,3을 리턴, 그렇지 않으면 0 리턴

    if k2 == char_player and k3 == char_player and k1 == ' ':
        return 1
    if k3 == char_player and k1 == char_player and k2 == ' ':
        return 2
    if k1 == char_player and k2 == char_player and k3 == ' ':
        return 3

    return 0


def Player_input_check(input):  # input 이 올바르면 True, 그렇지 않으면 False
    if input == '1' or input == '2' or input == '3':
        return True

    else:
        return False


def Character_Check(ch):  # 표식 입력이 올바르면 True, 그렇지 않으면 False
    if ch == 'O' or ch == 'X':
        return True

    else:
        return False


def Who_Win(board, winner):  # 승리한 경우 True, 그렇지 않으면 False
    B1_1 = board[0]  # 1행 1열
    B1_2 = board[1]  # 1행 2열
    B1_3 = board[2]  # 1행 3열
    B2_1 = board[3]  # 2행 1열
    B2_2 = board[4]  # 2행 2열
    B2_3 = board[5]  # 2행 3열
    B3_1 = board[6]  # 3행 1열
    B3_2 = board[7]  # 3행 2열
    B3_3 = board[8]  # 3행 3열

    if winner == True:
        if B1_1 == char_player and B1_2 == char_player and B1_3 == char_player:
            return True
        if B2_1 == char_player and B2_2 == char_player and B2_3 == char_player:
            return True
        if B3_1 == char_player and B3_2 == char_player and B3_3 == char_player:
            return True
        if B1_1 == char_player and B2_1 == char_player and B3_1 == char_player:
            return True
        if B1_2 == char_player and B2_2 == char_player and B3_2 == char_player:
            return True
        if B1_3 == char_player and B2_3 == char_player and B3_3 == char_player:
            return True
        if B1_1 == char_player and B2_2 == char_player and B3_3 == char_player:
            return True
        if B1_3 == char_player and B2_2 == char_player and B3_1 == char_player:
            return True

        return False

    else:
        if B1_1 == char_com and B1_2 == char_com and B1_3 == char_com:
            return True
        if B2_1 == char_com and B2_2 == char_com and B2_3 == char_com:
            return True
        if B3_1 == char_com and B3_2 == char_com and B3_3 == char_com:
            return True
        if B1_1 == char_com and B2_1 == char_com and B3_1 == char_com:
            return True
        if B1_2 == char_com and B2_2 == char_com and B3_2 == char_com:
            return True
        if B1_3 == char_com and B2_3 == char_com and B3_3 == char_com:
            return True
        if B1_1 == char_com and B2_2 == char_com and B3_3 == char_com:
            return True
        if B1_3 == char_com and B2_2 == char_com and B3_1 == char_com:
            return True

        return False


def Hang_Input():  # hang 을 입력 하는 함수
    print("행 좌표 :", end=' ')
    hang = input()  # 행 좌표 입력

    while (Player_input_check(hang) == False):  # 행을 잘못 입력한 경우
        print("올바르지 못한 입력입니다. 행 좌표를 다시 입력하세요.")
        print("행 좌표 :", end=' ')
        hang = input()  # 행 좌표 입력

    return hang  # 바르게 입력된 행을 리턴


def Yeol_Input():  # yeol 을 입력하는 함수
    print("열 좌표 :", end=' ')
    yeol = input()  # 열 좌표 입력
    while (Player_input_check(yeol) == False):  # 열을 잘못 입력한 경우
        print("올바르지 못한 입력입니다. 열 좌표를 다시 입력하세요.")
        print("열 좌표 :", end=' ')
        yeol = input()

    return yeol  # 바르게 입력된 열을 리턴


# main loop

# 규칙설명
print("TicTacToe\n")
print("승리한 쪽이 승점 1점을 가져가고, 무승부일 경우 양쪽 모두 승점 1점을 획득합니다.")
print("승률은 플레이어의 승점을 전체 승점 총합으로 나눈 값입니다.\n")

score_com = 0  # 컴퓨터의 점수를 저장하는 객체
score_player = 0  # 플레이어의 점수를 저장하는 객체
char_com = ''  # 컴퓨터의 표식을 저장하는 객체
char_player = ''  # 플레이어의 표식을 저장하는 객체

print("플레이할 표식을 선택하세요! O / X")
ch = input()  # O/X중 한가지 입력

while (Character_Check(ch) == False):  # 잘못된 입력을 하면 다시 입력
    print("잘못된 입력입니다. 다시 입력하세요.")
    ch = input()

# 플레이어가 고른 표식에 따라 컴퓨터와 플레이어의 표식 저장
if ch == 'X':
    char_com = 'O'
    char_player = 'X'

else:
    char_com = 'X'
    char_player = 'O'

while True:
    board = [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']  # 게임보드 초기화
    turn = First_Player()  # 랜덤하게 시작하는 쪽 선정

    if turn == True:
        print("이번 판은 플레이어가 먼저 시작합니다!\n")

    else:
        print("이번 판은 컴퓨터가 먼저 시작합니다!\n")

    Keep_Play = True  # 게임을 계속해서 진행할지 판단

    while Keep_Play == True:
        if turn == True:  # True : 플레이어의 차례
            Gameboard(board)  # 플레이어 차례가 될 때 마다 게임보드 출력
            print("행, 열 순서대로 표시할 좌표를 입력하세요.")
            hang = Hang_Input()  # 리턴 받은 행을 저장
            yeol = Yeol_Input()  # 리턴 받은 열을 저장

            while board[(int(hang) - 1) * 3 + int(yeol) - 1] != ' ':  # 이미 값이 입력 되어 있는 칸을 선택하면 다시 입력
                print("이미 값이 입력되어 있습니다. 처음부터 다시 입력하세요.")
                hang = Hang_Input()  # 리턴 받은 행을 저장
                yeol = Yeol_Input()  # 리턴 받은 열을 저장

            Player_check(board, hang, yeol)  # player 가 입력한 표식 기록

            if Who_Win(board, turn) == True:  # player 가 승리한 경우
                Gameboard(board)
                print("승리!")
                score_player += 1  # 승률을 나타내기 위해서 player 의 승리회수 추가
                Keep_Play = False  # 끝내기

            else:  # 무승부인 경우
                if Board_Full(board) == True:  # 판이 다 찼는데 승리자가 나오지 않은 경우
                    Gameboard(board)
                    print("무승부!")
                    score_player += 1  # player 와 com 의 승리 회수 1씩 추가
                    score_com += 1
                    break

                else:
                    turn = False  # 컴퓨터의 차례로 넘어감

        else:  # False : 컴퓨터의 차례
            ComMove(board)

            if Who_Win(board, turn) == True:  # 컴퓨터가 승리한 경우
                Gameboard(board)
                print("패배!")
                score_com += 1  # 컴퓨터의 승리 회수 추가
                Keep_Play = False  # 끝내기

            else:
                if Board_Full(board) == True:  # 판이 다 찼는데 승리자가 나오지 않았을 경우
                    Gameboard(board)
                    print("무승부!")
                    score_player += 1  # player 와 com 의 승리 회수 1씩 추가
                    score_com += 1
                    break

                else:
                    turn = True  # player 의 차례로 넘어감

    rate = Winning_Rate(score_com, score_player)  # 승률을 기록하는 객체
    print("현재 승률은 %.1f퍼센트 입니다." % rate)
    print("다시 플레이하시겠습니까? Y / N")
    con = input()  # 다시 플레이 할지를 저장하는 객체

    while con != 'N' and con != 'Y':  # 잘못된 입력인 경우
        print("잘못된 입력입니다. 다시 답해주세요. Y / N")
        con = input()

    if con == 'N':  # N 이면 종료
        break
