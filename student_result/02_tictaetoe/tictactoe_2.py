import random
#초기 세팅
user = 'O'
com = 'X'
map = [['-', '-', '-'], ['-', '-', '-'], ['-', '-', '-']]       #맵의 상황을 저장하는 배열
possible = [1, 2, 3, 4, 5, 6, 7, 8, 9]              #놓을 수 있는 위치
chk = 0         #이때까지 놓은 말의 개수를 세는 변수
def printmap ():        #맵의 상황을 출력하는 함수
    for i in range(3):
        print("|   ", end = '')
        for j in range(3):
            print(map[i][j], end = '   ')
        print("|")
        print("")
def retry ():       #게임을 재시작할지 종료할지 입력받는 함수
    print("다시 하시겠습니까? (O, X)")
    print("X 이외의 입력을 하실 경우 재시작됩니다.")
    replay = input()
    if len(replay) == 1:
        if replay[0] == 'X':
            return False
    else:
        return True
def is_win ():  #게임이 끝났는지 확인하는 함수
    if map[0][1] == map[0][0] and map[0][0] == map[0][2]:
        if map[0][0] == user:
            printmap()
            print("축하합니다. 사용자 님께서 이기셨어요.")
            return True
        elif map[0][0] == com:
            printmap()
            print("제가 이겼네요. ㅋ")
            return True
        return False
    elif map[1][0] == map[1][1] and map[1][0] == map[1][2]:
        if map[1][0] == user:
            printmap()
            print("축하합니다. 사용자 님께서 이기셨어요.")
            return True
        elif map[1][0] == com:
            printmap()
            print("제가 이겼네요. ㅋ")
            return True
        return False
    elif map[2][0] == map[2][1] and map[2][0] == map[2][2]:
        if map[2][0] == user:
            printmap()
            print("축하합니다. 사용자 님께서 이기셨어요.")
            return True
        elif map[2][0] == com:
            printmap()
            print("제가 이겼네요. ㅋ")
            return True
        return False
    elif map[0][0] == map[1][0] and map[0][0] == map[2][0]:
        if map[0][0] == user:
            printmap()
            print("축하합니다. 사용자 님께서 이기셨어요.")
            return True
        elif map[0][0] == com:
            printmap()
            print("제가 이겼네요. ㅋ")
            return True
        return False
    elif map[0][1] == map[1][1] and map[0][1] == map[2][1]:
        if map[0][1] == user:
            printmap()
            print("축하합니다. 사용자 님께서 이기셨어요.")
            return True
        elif map[0][1] == com:
            printmap()
            print("제가 이겼네요. ㅋ")
            return True
        return False
    elif map[0][2] == map[1][2] and map[0][2] == map[2][2]:
        if map[0][2] == user:
            printmap()
            print("축하합니다. 사용자 님께서 이기셨어요.")
            return True
        elif map[0][2] == com:
            printmap()
            print("제가 이겼네요. ㅋ")
            return True
        return False
    elif map[0][0] == map[1][1] and map[0][0] == map[2][2]:
        if map[0][0] == user:
            printmap()
            print("축하합니다. 사용자 님께서 이기셨어요.")
            return True
        elif map[0][0] == com:
            printmap()
            print("제가 이겼네요. ㅋ")
            return True
        return False
    elif map[0][2] == map[1][1] and map[0][2] == map[2][0]:
        if map[0][2] == user:
            printmap()
            print("축하합니다. 사용자 님께서 이기셨어요.")
            return True
        elif map[0][2] == com:
            printmap()
            print("제가 이겼네요. ㅋ")
            return True
        return False
    elif chk == 9:
        printmap()
        print("비겼습니다.")
        return True
    else:
        return False
def findput (): #컴퓨터가 놓을 곳을 고르는 함수
    #컴퓨터가 이기는 위치 우선적으로 탐색
    if (map[0][0] == map[0][1] == com or map[1][1] == map[2][0] == com or map[1][2] == map[2][2] == com) and possible.count(3) == 1:
        return 3
    elif (map[0][0] == map[0][2] == com or map[1][1] == map[2][1] == com) and possible.count(2) == 1:
        return 2
    elif (map[0][1] == map[0][2] == com or map[1][1] == map[2][2] == com or map[1][0] == map[2][0] == com) and possible.count(1) == 1:
        return 1
    elif (map[1][0] == map[1][1] == com or map[0][2] == map[2][2] == com) and possible.count(6) == 1:
        return 6
    elif (map[0][0] == map[2][2] == com or map[1][0] == map[1][2] == com or map[0][1] == map[2][1] == com or map[0][2] == map[2][0] == com) and possible.count(5) == 1:
        return 5
    elif (map[1][1] == map[1][2] == com or map[0][0] == map[2][0] == com) and possible.count(4) == 1:
        return 4
    elif (map[2][0] == map[2][1] == com or map[0][0] == map[1][1] == com or map[0][2] == map[1][2] == com) and possible.count(9) == 1:
        return 9
    elif (map[2][0] == map[2][2] == com or map[0][1] == map[1][1] == com) and possible.count(8) == 1:
        return 8
    elif (map[2][1] == map[2][2] == com or map[0][2] == map[1][1] == com or map[0][0] == map[1][0] == com) and possible.count(7) == 1:
        return 7
    #사용자가 이기는 위치 탐색
    elif (map[0][0] == map[0][1] == user or map[1][1] == map[2][0] == user or map[1][2] == map[2][2] == user) and possible.count(3) == 1:
        return 3
    elif (map[0][0] == map[0][2] == user or map[1][1] == map[2][1] == user) and possible.count(2) == 1:
        return 2
    elif (map[0][1] == map[0][2] == user or map[1][1] == map[2][2] == user or map[1][0] == map[2][0] == user) and possible.count(1) == 1:
        return 1
    elif (map[1][0] == map[1][1] == user or map[0][2] == map[2][2] == user) and possible.count(6) == 1:
        return 6
    elif (map[0][0] == map[2][2] == user or map[1][0] == map[1][2] == user or map[0][1] == map[2][1] == user or map[0][2] == map[2][0] == user) and possible.count(5) == 1:
        return 5
    elif (map[1][1] == map[1][2] == user or map[0][0] == map[2[0] == user) and possible.count(4) == 1:
        return 4
    elif (map[2][0] == map[2][1] == user or map[0][0] == map[1][1] == user or map[0][2] == map[1][2] == user) and possible.count(9) == 1:
        return 9
    elif (map[2][0] == map[2][2] == user or map[0][1] == map[1][1] == user) and possible.count(8) == 1:
        return 8
    elif (map[2][1] == map[2][2] == user or map[0][2] == map[1][1] == user or map[0][0] == map[1][0] == user) and possible.count(7) == 1:
        return 7
    #이기거나 지는 경우가 없으면 랜덤
    else:
        random.shuffle(possible)
        return possible[0]
def put (k, who):  #사용자나 컴퓨터가 놓을 말의 위치를 입력받아 판에 놓는 함수
    #코드 상 k는 1~9의 값만을 가질 수 있음
    if k == 1:
        map[0][0] = who
    elif k == 2:
        map[0][1] = who
    elif k == 3:
        map[0][2] = who
    elif k == 4:
        map[1][0] = who
    elif k == 5:
        map[1][1] = who
    elif k == 6:
        map[1][2] = who
    elif k == 7:
        map[2][0] = who
    elif k == 8:
        map[2][1] = who
    elif k == 9:
        map[2][2] = who

while True:
    print("틱택토 게임을 시작합니다.")
    print("당신의 말을 골라주세요 (O 또는 X)")
    a=input()
    if len(a) != 1 or (a != 'O' and a != 'X'):           #입력이 정상적이지 않은 경우 처리
        while len(a) != 1 or (a != 'O' and a != 'X'):
            print("잘못된 입력입니다. 다시 골라주세요 (O 또는 X)")
            a = input()
    if a == 'X':        #말을 고른 것이 초기 세팅과 다른 경우
        user = 'X'
        com ='O'
    for i in range(3):      # 1~9의 숫자가 나타내는 맵의 위치
        print("|   ", end='')
        for j in range(3):
            print("%d" % (i * 3 + j + 1), end='   ')
        print("|")
        print("")
    first = random.randint(1, 2)        #선후공 결정
    first = 2
    if first == 1:          #컴퓨터가 후공인 경우
        print("먼저 시작하세요.")
        while is_win() == False:        #게임이 끝나지 않은 동안
            print("당신의 말을 놓을 위치를 골라주세요.", end=' ')
            print(possible)
            loc = input()
            #입력이 정상적이지 않은 경우
            if loc != '1' and loc != '2' and loc != '3' and loc != '4' and loc != '5' and loc != '6' and loc != '7' and loc != '8' and loc != '9':
                print("잘못된 입력입니다.", end=' ')
            else:
                loc = int(loc)
                if possible.count(loc) != 1:
                    print("잘못된 입력입니다.", end=' ') #이미 놓은 곳을 골랐을 경우
                    continue
                possible.remove(loc)        #놓을 수 있는 위치에서 놓은 위치 제거
                put(loc, user)
                chk += 1
                if is_win() == True:        #게임이 끝난 경우 while문 탈출
                    printmap()
                    break
                comput = findput()          #컴퓨터가 놓을 곳 탐색
                possible.remove(comput)     #컴퓨터가 놓을 곳 놓을 수 있는 위치에서 제거
                possible.sort()             #컴퓨터가 놓을 곳 고를 때 섞였던 배열 다시 정렬
                put(comput, com)
                chk += 1
                if is_win() == True:
                    break
                else:
                    printmap()
    else:           #컴퓨터가 선공인 경우
        print("제가 먼저 시작할게요.")
        while is_win() == False:       #게임이 끝나지 않은 동안
            comput = findput()          #컴퓨터 착수
            possible.remove(comput)
            possible.sort()
            put(comput, com)
            chk += 1
            printmap()
            if is_win() == True:           #사용자 착수
                break
            loc = 10
            #입력이 정상적이지 않은 경우 제거
            while True:
                print("당신의 말을 놓을 위치를 골라주세요.", end=' ')
                print(possible)
                loc = input()
                #1~9 의 입력만을 골라냄
                if loc != '1' and loc != '2' and loc != '3' and loc != '4' and loc != '5' and loc != '6' and loc != '7' and loc != '8' and loc != '9':
                    print("잘못된 입력입니다.",end=' ')
                    continue
                else:
                    loc = int(loc)
                    if possible.count(loc) != 1:
                        print("잘못된 입력입니다.", end=' ')  # 이미 놓은 곳을 골랐을 경우
                    else:       #올바른 입력일 경우 while문 탈출
                        break
            possible.remove(loc)  # 놓을 수 있는 위치에서 놓은 위치 제거
            put(loc, user)
            chk += 1
            if is_win() == True:  # 게임이 끝난 경우 while문 탈출
                printmap()
                break
    if retry() == False:        #재시작하지 않을 경우 프로그램 종료
        print("이용해 주셔서 감사합니다.", end='')
        break
    else:
         #초기 세팅으로 복귀
        chk = 0
        del possible[0:len(possible)]
        possible.extend([1, 2, 3, 4, 5, 6, 7, 8, 9])
        user = 'O'
        com = 'X'
        del map[0:3]
        map.append(['-', '-', '-'])
        map.append(['-', '-', '-'])
        map.append(['-', '-', '-'])