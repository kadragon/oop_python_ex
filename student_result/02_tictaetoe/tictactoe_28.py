import copy
import random


def play_again():  # 다시 게임을 할건지 질문, 사용자의 입력값을 리턴
    return input('Do you want to play again? (yes or no): ')


def prn():  # 현재 sheet의 상태를 출력
    print("-------------")
    for i in range(0, 9):
        print("| %c " % (sheet[i]), end="")
        if i % 3 == 2:  # 3줄로 나눠서 출력
            print("|")
            print("-------------")


def find(sheet, check):  # 현재 sheet의 상태와 찾을 값 전달
    if sheet[2] == check and sheet[4] == check and sheet[6] == check:  # 좌하향 길
        return 1
    elif sheet[0] == check and sheet[4] == check and sheet[8] == check:  # 우하향 길
        return 1
    elif sheet[0] == check and sheet[1] == check and sheet[2] == check:  # 1행
        return 1
    elif sheet[3] == check and sheet[4] == check and sheet[5] == check:  # 2행
        return 1
    elif sheet[8] == check and sheet[7] == check and sheet[6] == check:  # 3행
        return 1
    elif sheet[0] == check and sheet[3] == check and sheet[6] == check:  # 1열
        return 1
    elif sheet[1] == check and sheet[4] == check and sheet[7] == check:  # 2열
        return 1
    elif sheet[2] == check and sheet[5] == check and sheet[8] == check:  # 3열
        return 1


def cp():
    return copy.copy(sheet)  # 내용을 복사해서 승률이 높은 자리인지 확인


def write(plc, put):  # 전달된 위치에 사용자 또는 컴퓨터를 현재 sheet에 입력함
    sheet[plc] = put


def user_play():  # 사용자가 플레이할 경우
    print("\nWhat will you choose?")  # 각 위치의 번호를 출력
    print("-------------")
    print("| 0 | 1 | 2 |")
    print("-------------")
    print("| 3 | 4 | 5 | ")
    print("-------------")
    print("| 6 | 7 | 8 |")
    print("-------------")
    plc = 0
    while True:  # 빈위치가 입력될 때까지 입력 받기
        plc = input()
        if plc in number and sheet[int(plc)] == ' ':  # 입력된 값이 0-8사이 정수이고 빈 위치인지 확인
            break
        else:
            print("Choose another place")  # 다른 위치
    write(int(plc), riv)  # 입력받은 위치에 쓰기


def cmp_play():  # 컴퓨터가 플레이할 때
    for i in range(0, 9):  # 정답이있을경우
        plate = cp()  # 승률을 테스트하기 위해 현재 sheet를 복사
        if plate[i] == ' ':
            plate[i] = cmp
            if find(plate, cmp) == 1:  # 이기는 위치일 경우
                print("The computer chooses %d" % (i))  # 선택
                write(i, cmp)
                return
            plate[i] = ' '  # 선택되지 못할 경우 다시 원래대로 바꾸기

    # 상대방이 다음에 놓아서 이길 수 있을 경우
    for i in range(0, 9):
        plate = cp()
        if plate[i] == ' ':
            plate[i] = riv
            if find(plate, riv) == 1:
                write(i, cmp)
                print("The computer will choose %d" % (i))
                return
            plate[i] = ' '

    plate = cp()
    random.shuffle(list1)
    for i in list1:  # 나머지 모서리
        if plate[i] == ' ':
            write(i, cmp)
            print("The computer will choose %d" % i)
            return

    plate = cp()
    if plate[4] == ' ':  # 중심이 비어있을 경우
        write(4, cmp)
        print("The computer will choose 4")
        return

    for i in number:  # 서택되지 못할 경우
        if plate[int(i)] == ' ':
            write(int(i), cmp)
            print("The computer will choose %d" % int(i))
            return


def game(play_count):
    # now가 짝수일 경우 cmp, 홀수일경우 riv의 차례(처음 game을 호출할 때, riv이 먼저 시작할 경우 now를 1로,cmp가 먼저 시작할 경우 now를 0으로 만들어줌 )
    while ' ' in sheet:
        if play_count % 2 == 1:
            user_play()
        elif play_count % 2 == 0:
            cmp_play()
        play_count += 1

        prn()
        if find(sheet, riv) == 1:
            print("You Win!")
            return
        elif find(sheet, cmp) == 1:
            print("You Lose!")
            return
    print("It's a tie.")


# 게임이 시작하는 부분

print("Welcome to Tic Tac Toe:\n"
      "Do you want to be O or X?", end=" ")

number = ['0', '1', '2', '3', '4', '5', '6', '7', '8']
list1 = [1, 3, 5, 7]
while True:
    riv = input().upper()  # input
    if (" " not in riv) and (riv == 'O' or riv == 'X'):
        break
    else:
        print("Wrong.")
        print("Do you want to be O or X?", end=" ")

if riv == 'X':  # riv가 X를 선택할 경우
    cmp = 'O'  # cmp는 O를 선택
else:  # 반대의 경우도 동일
    cmp = 'X'

play_count = 0
sheet = [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']
ran = random.choice([0, 1])  # 0일 경우 X가 먼저 1일 경우 O가 먼저
if (ran == 0 and riv == 'X') or (ran == 1 and riv == 'O'):
    print("You wll go first.")
    play_count = 1
    game(1)
else:
    print("The computer will go first.")
    game(0)

# 다시 게임 시작
while True:  # 답변이 yes일 때까지 게임 진행
    an = play_again()
    if an[0] == "n" or an[0] == "N":
        break
    sheet = [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']  # 시트를 초기화 하기
    game(play_count)  # 다시 게임 시작
