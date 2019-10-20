import random
import time


def giveinf():  # 틱택토를 아는지 여부 묻고 소개
    print("""안녕 친구, 너는 지금부터 Tic-Tac-Toe 게임을 하게 될거야.
게임을 하기 전!
Tic-Tac-Toe의 규칙은 알고 있니?(y/n) :""", end=' ')
    know = getyn()
    if know == 'y':
        print("알고 있구나! 그럼 시작해볼까?")
    else:
        print("""그럼 지금부터 설명을 시작하지
3X3 타일이 있어.
너와 cpu는 한번씩 번갈아가며 수를 놓을거야
이때 먼저 자신의 수가 3개 줄로 존재하면 이긴거야
설명 끝! 그럼 시작해볼까?""")


def choose():  # 내 말을 고르고 내 말과 상대의 말을 차례대로 리턴
    print("X or O, 하나를 선택하시오(x/o) : ", end='')
    mycharacter = input()
    if mycharacter not in "XxOo":
        print("다시 입력하시오")
        return choose()
    else:
        if mycharacter is 'X' or mycharacter is 'x':
            return 'X', 'O'
        elif mycharacter is 'O' or mycharacter is 'o':
            return 'O', 'X'
        else:
            print("다시 입력하시오")
            return choose()


def getyn():  # y/n 입력 받아 리턴
    yours = input()
    if yours is "y" or yours is "n":
        return yours
    else:
        print("다시 입력하시오 : ", end='')
        return getyn()


def getmychoice():  # 내가 말을 어디에 둘지 입력받고 위치 리턴
    try:
        print("Yours : ", end='')
        mine = int(input())
        if check(mine - 1):
            return mine - 1
        else:
            print("다시 입력하시오")
            return getmychoice()
    except:
        print("다시 입력하시오")
        return getmychoice()


def getrandomplace():  # cpu가 말을 어디에 둘지 결정(내가 이길 수 있는 경우에는 랜덤으로 하지 않고 방해하는 곳에 둠)하고 위치 리턴
    losing, lineinfo = cpu_losing()
    if losing:
        if lineinfo[0] == "row":
            for j in range(3):
                if tile[lineinfo[1]][j] == ' ':
                    return lineinfo[1] * 3 + j
        elif lineinfo[0] == "line":
            for i in range(3):
                if tile[i][lineinfo[1]] == ' ':
                    return i * 3 + lineinfo[1]
        elif lineinfo[0] == "crossup":
            for i in range(3):
                if tile[i][2 - i] == ' ':
                    return 2 + 2 * i
        else:
            for i in range(3):
                if tile[i][i] == ' ':
                    return 4 * i
    else:
        place = random.randrange(9)
        if check(place):
            return place
        else:
            return getrandomplace()


def cpu_losing():  # 내가 이기고 있는지(내 말이 연속으로 두개 있을 때) 여부와 이기고 있을 시 장소에 대한 정보를 리턴
    for i in range(3):
        if line[i][mychar] == 2 and line[i][cpuchar] == 0:
            return True, ["line", i]
        if row[i][mychar] == 2 and row[i][cpuchar] == 0:
            return True, ["row", i]
    if cross_up[mychar] == 2 and cross_up[cpuchar] == 0:
        return True, ["crossup"]
    if cross_down[mychar] == 2 and cross_down[cpuchar] == 0:
        return True, ["cross_down"]
    return False, 0


def check(mynum):  # 내가 놓는 자리가 놓을 수 있는 자리인지 여부를 리턴
    return mynum >= 0 and tile[mynum // 3][mynum % 3] == ' '


def update(mynum, char):  # 각 행과 열, 대각선에서 말들의 상태를 갱신
    tile[mynum // 3][mynum % 3] = char
    row[mynum // 3][char] += 1
    line[mynum % 3][char] += 1
    if mynum in [0, 4, 8]:
        cross_down[char] += 1
    if mynum in [2, 4, 6]:
        cross_up[char] += 1


def isitright(character):  # character의 문자를 말로 둔 사람이 이겼는지 아닌지 리턴
    right = False
    for i in range(3):
        if row[i][character] == 3 or line[i][character] == 3:
            right = True
    if cross_down[character] == 3 or cross_up[character] == 3:
        right = True
    return right


def endgame(character):  # 게임이 끝났을 때 그에 따라 축하말이나 위로말, 그리고 승률 출력, 다시 할지 여부 묻고 리턴
    global wins
    global loses
    if character is mychar:
        print("You WON!!!!!!!!!!!!")
        wins += 1
    elif character is cpuchar:
        print("you lose_________")
        loses += 1
    else:
        print("Tie!")
    print_winningrate()
    print("wanna try again?(y/n) : ", end='')
    return getyn() == 'y'


def print_winningrate():  # 승률 출력
    if wins + loses == 0:
        print("0:0")
    else:
        print("승률 :", (wins) / (wins + loses))


def printtile():  # 타일 상태를 그림으로 출력
    print('-' * 15)
    for i in range(3):
        print(' | ', end='')
        for j in range(3):
            if tile[i][j] == ' ':
                print(i * 3 + j + 1, end=' | ')
            else:
                print(tile[i][j], end=' | ')
        print()
        print('-' * 15)


# -----------------------------------------main

play = 1
giveinf()  ## Tic-Tac-Toe 규칙 아는지 물음

mychar, cpuchar = choose()
charlist = ['X', 'O']
loses = 0
wins = 0
while play:  ##플레이어가 플레이하고 싶은 동안(play==True) 게임을 함
    tile = [[' ' for i in range(3)] for j in range(3)]  # 타일 상태 초기화
    line = [{'X': 0, 'O': 0} for j in range(3)]  # 열의 정보 초기화
    row = [{'X': 0, 'O': 0} for j in range(3)]  # 열의 정보 초기화
    cross_down = {'X': 0, 'O': 0}  # 오른쪽 아래 대각선 정보 초기화
    cross_up = {'X': 0, 'O': 0}  # 오른쪽 위 대각선 정보 초기화
    cnt = 0

    print("START!!")
    myturn = random.randrange(2)  # 먼저 말 놓는 사람 정하기
    printtile()
    while True:
        if mychar is charlist[myturn]:  # 내 턴일 때
            myplace = getmychoice()
            update(myplace, charlist[myturn])
            bingo = isitright(charlist[myturn])
            if bingo:  # 내가 이겼다면
                printtile()
                play = endgame(charlist[myturn])
                break
            myturn = 1 - myturn
        else:  # 상대(cpu) 턴일 때
            print("Computer thinking.....")  # 컴퓨터 생각 시간으로 2초 줌
            time.sleep(2)
            myplace = getrandomplace()
            print("computer : ", myplace + 1)
            update(myplace, charlist[myturn])
            bingo = isitright(charlist[myturn])
            if bingo:  # cpu가 이겼다면
                printtile()
                play = endgame(charlist[myturn])
                break
            myturn = 1 - myturn
        cnt += 1
        printtile()
        if cnt == 9:  # 무승부(칸이 꽉 찰 때)
            play = endgame(' ')
            break

print("그럼 GOOD BYE~")
