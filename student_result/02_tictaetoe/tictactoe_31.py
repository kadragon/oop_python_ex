import random
import time

wait_time = 1

print("Welcome to Tic Tac Toe World~")  # 게임 소개

def play():

    menu = ('X', 'O')  # 원하는 입력값


    def choice():
        choose = input('\n무엇을 원하시나요? (X/O) >>> ')  # X 혹은 O 입력받기
        choose = choose.upper()  # 소문자 입력 가능
        while not choose in menu:  # 잘못 입력시 제대로 입력할 때까지 반복
            choose = input('잘못 입력하셨습니다. 다시입력하세요. (X/O) >>> ')
            choose = choose.upper()
        return choose  # 사용자가 선택한 모양을 반환
        # print(choose)


    def computer_choice():  # 사용자가 선택하지 않은 모양을 컴퓨터가 선택
        if menu[0] == choose:
            return menu[1]
        else:
            return menu[0]


    place = [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']  # board 초기값


    def board():  # board 출력
        print(''' %c|%c|%c
ㅡㅡㅡㅡ
 %c|%c|%c
ㅡㅡㅡㅡ
 %c|%c|%c
''' % (place[1], place[2], place[3], place[4], place[5], place[6], place[7], place[8], place[9]))


    def who_is_win(win):  # 누가 이겼는지를 입력받아 각 상황에 맞는 축하글을 출력
        if win == choose:
            print('You are win! Congratulation~')
        else:
            print('Computer is win! You are looser..')


    def check_bingo():  # 가로, 세로, 대각선을 각각 확인하며 bingo인지를 확인
        if place[1] == place[2] == place[3] and place[1] != ' ': return 'bingo'
        if place[4] == place[5] == place[6] and place[4] != ' ': return 'bingo'
        if place[7] == place[8] == place[9] and place[7] != ' ': return 'bingo'
        if place[1] == place[4] == place[7] and place[1] != ' ': return 'bingo'
        if place[2] == place[5] == place[8] and place[2] != ' ': return 'bingo'
        if place[3] == place[6] == place[9] and place[3] != ' ': return 'bingo'
        if place[1] == place[5] == place[9] and place[1] != ' ': return 'bingo'
        if place[3] == place[5] == place[7] and place[3] != ' ': return 'bingo'

    def game_over() :  # 무승부로 끝났을 경우 더이상 채울 곳이 없음을 확인
        for i in range(1,10):
            if place[i] == ' ' :
                return 'conti'
        print('game over ;;')   # 채울 곳이 없으니 게임이 끝났음을 출력!
        return 'End'

    def checking_bingo(shape):  # 위 두 함수를 이용하여 bingo인지를 확인하는 함수
        if check_bingo() == 'bingo':
            who_is_win(shape)
            return 'finish'

    place_menu=('1','2','3','4','5','6','7','8','9')    # 1~9 중에 입력된 값이 있는지 확인을 위함

    def do_user():  # 사용자에게 어디에 놓을지를 입력받아 그 자리에 놓는 함수

        which = input('''   
어디에 놓으시겠습니까?
1 2 3
4 5 6
7 8 9
>>> ''')        # 1~9 중 원하는 값 입력

        while not which in place_menu :
            which = input('''
다시 말씀해 주시죠...
1 2 3
4 5 6
7 8 9
>>> ''')    # 보기에 없는 값이 입력되었을 경우 다시 물어봄

        which=int(which)

        while place[which] != ' ' :
            which = int(input('''
다시 말씀해 주시죠...
1 2 3
4 5 6
7 8 9
>>> '''))   # 이미 채워진 공간을 입력하였을 경우 다시 물어봄
        place[which] = choose   # 입력 받은 장소에 고른 모양을 집어 넣고..
        return which    # 입력 받은 값을 return

    def possibility():  # 컴퓨터가 놓을 자리를 보는 함수 중 하나로, 컴퓨터가 놓았을 때 바로 이기는 자리를 탐색
        for i in range(1, 10):
            if place[i] == ' ' :
                place[i] = c_choose
                if check_bingo() == 'bingo':
                    place[i] = ' '
                    return i
                place[i] = ' '
        return 10


    def danger():  # 컴퓨터가 놓을 자리를 보는 함수 중 하나로, 컴퓨터가 막아야 할 자리를 탐색
        for i in range(1, 10):
            if place[i] == ' ' :
                place[i] = choose
                if check_bingo() == 'bingo':
                    place[i] = ' '
                    return i
                place[i] = ' '
        return 10

    def rand_number():
        randy = random.randint(1, 9)    # 1~9 중 숫자를 랜덤으로 하나 뽑는데..
        while randy % 2 == 0 or randy == 5: # 짝수나 5를 제외한 1,3,7,9 중 랜덤을 고름
            randy = random.randint(1, 9)
        return randy    # 결국 1,3,7,9 중 랜덤하게 값이 반환됨

    def do_genius(user_did):  # 반드시 놓아야 할 자리가 없을 경우, 컴퓨터가 유리하도록 하는 자리를 탐색 후 놓기
        if user_did == 1 or 3 or 7 or 9 :   # 바로 이전에 사용자가 가장 자리에 놓았을 경우
            if place[5] == ' ' :    # 가운데 위치에 둘 수 있는 지 확인 => 구글 고급 모드에서 그렇게 하던데...;;
                place[5] = c_choose
                return
            if place[2] == ' ' and 5-user_did > 0 :     # 사용자가 1이나 3에 두었다면 2에 두어 미리 차단
                place[2] = c_choose
                return
            if place[8] == ' ' and 5-user_did < 0 :     # 사용자가 7이나 9에 두었다면 8에 두어 미리 차단
                place[8] = c_choose
                return
            if place[4] == ' ' and (user_did == 1 or 7) : # 사용자가 1이나 7에 두었는데 2나 8에 둘 수 없는 경우
                place[4] = c_choose
                return
            if place[6] == ' ' and (user_did == 3 or 9) : # 사용자가 3이나 9에 두었는데 2나 8에 둘 수 없는 경우
                place[6] = c_choose
                return

        if user_did == 2 or 4 or 6 or 8 :   # 바로 이전에 사용자가 모서리에 놓았을 경우

            if place[10-user_did] == ' ' :  # 맞은 편에 두어 경로를 차단 => 구글 고급모드에서 그렇게 하던데.. ;;
                place[10-user_did] = c_choose
                return

            elif place[5] == ' ' :    # 5에 두어 미리 경로를 차단
                place[5] = c_choose
                return

            else :      # 모두 아닐 경우 1,3,7,9 중 랜덤으로 고른다.
                rand_here = rand_number()
                while place[rand_here] != ' ' : # 랜덤 값이 비어있는지 확인
                    rand_here = rand_number()
                place[rand_here] = c_choose

        if user_did == 5 :  # 사용자가 가운데 놓았을 경우
            rand_here = rand_number()   # 1,3,7,9 중 랜덤으로 고른다.
            while place[rand_here] != ' ':
                rand_here = rand_number()   # 랜덤 값이 비어있는지 확인
            place[rand_here] = c_choose



    def do_computer(user_did):  # 컴퓨터가 생각하는 과정을 담은 함수
        here = possibility()  # 컴퓨터가 놓으면 이기는 경우 먼저 생각
        if here < 10:
            place[here] = c_choose
            #print('posible')
            return

        here = danger() # 컴퓨터가 막지 않으면 안되는 자리를 다음으로 생각
        if here < 10:
            place[here] = c_choose
            #print('danger')
            return

        do_genius(user_did)  # 유리하게 놓아봅시다. / 바로 전에 사용자가 어디에 두었는지를 입력(?)받음


    for i in range(1,10):   # 시작 전 판 초기화
        place[i] = ' '

    choose = choice()   # 사용자 모양 선정
    c_choose = computer_choice()    # 컴퓨터 모양 설정

    random_choose = random.randint(1,2)     # 랜덤으로 시작!
    if random_choose == 2:  # 컴퓨터 먼저 시작일 경우, while문 들어가기 전에 컴퓨터에게 먼저 기회를 준다.
        print("\ncomputer first\n")     # 컴퓨터가 먼저 하는 것을 알림!
        place[rand_number()] = c_choose   # 컴퓨터가 처음에 놓을 자리 탐색
        time.sleep(wait_time)           # 컴퓨터가 생각하고 있는 척하기
    else : print("\nyou first\n")       # 사용자가 먼저임을 알림!
    board()                             # 판을 출력하고
    ending = checking_bingo(c_choose)   # 게임이 끝났는지 확인

    while ending != 'finish' :  # 게임이 끝날 때까지 사용자와 컴퓨터의 순서를 돌린다.
        what_did = do_user()                # 사용자의 입력을 받고
        board()                             # 판을 출력하고
        ending = checking_bingo(choose)     # 게임이 끝났는지 확인한다.

        if ending == 'finish': break        # 게임이 끝났다면 while문 종료
        if game_over() == 'End' : break     # board가 꽉 찼다면 while문 종료

        do_computer(what_did)               # 컴퓨터가 놓을 자리 탐색
        time.sleep(wait_time)               # wait_time 동안 생각...하는 척...
        board()                             # 판 출력
        ending = checking_bingo(c_choose)   # 게임이 끝났는지 확인

        if game_over() == 'End' : break     # board가 꽉 찼는지 확인

def replay():   # 재시작 여부 확인 함수
    replay_menu = ('Y','N')     # 재시작 여부 입력 예시
    replay = input('다시 하시겠습니까?? (Y/N) >>> ').upper()    # 재시작 여부 입력

    while not replay in replay_menu :   # 입력 받은 값이 제대로 되었는지 확인
        replay = input('다시 하시겠냐구요... (Y/N) >>> ').upper()

    return replay


play()
re = replay()

while re == 'Y' :   # 재시작을 원하면 계속 게임 실행
    play()
    re = replay()