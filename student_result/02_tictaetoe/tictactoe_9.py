import random # 시작 순서에 대한 랜덤이 필요하다
import copy # 리스트를 변경하지 않고 사용하기 위해 deepcopy가 필요하다

#t와 c는 각각 자신과 컴퓨터의 기호
t=''
c=''

def init(): # 사용할 기호와 순서에 대한 내용이 포함됨
    start=input('자신이 사용할 기호를 입력하세요(O, X) ').upper() # O, X 중 선택이 가능하게 만든다
    global t
    global c

    # O나 X가 아닌 입력에 대한 각종 처리
    while start != 'O' and start != 'X' :
        print("잘못된 입력입니다.")
        start=input('자신이 사용할 기호를 입력하세요(O, X) ').upper()
        #print(start)

    # 컴퓨터 기호 지정
    t=start
    if t=='O' : c='X'
    else : c='O'

    # 시작 순서는 랜덤이다.
    a=random.randrange(2)
    if a==0 :
        print("\n제가 먼저 시작하겠습니다.")
    else:
        print("\n먼저 시작하세요.")

    return a

# 리스트를 맵 형태로 출력해주는 과정이다
def print_map(getmap):
    for i in range(3) :
        print(getmap[i])

standard_map=[]

# 착수 한 후, 그 점이 지는 위치이거나 이기는 위치여서 꼭 놓아야 하면 1을 반환해준다.
# deepcopy를 이용하였기 때문에 메인리스트인 standard_map[]의 값은 변화하지 않는다.
def computer_AI(defuse, checkchar):
    for i in range(3) :
        if defuse[i][0]==defuse[i][1]==defuse[i][2]==checkchar : return 1 # 가로가 일정한 문자
        if defuse[0][i]==defuse[1][i]==defuse[2][i]==checkchar : return 1 # 세로가 일정한 문자
    if defuse[0][0]==defuse[1][1]==checkchar==defuse[2][2] : return 1 # 우하향 대각선이 일정한 문자
    if defuse[0][2]==defuse[1][1]==checkchar==defuse[2][0] : return 1 # 우상향 대각선이 일정한 문자

# HARD 모드에서 지거나 이기는 위치가 없을 때, 실행되는 함수이다.
# HARD 모드가 아닐 때는, 가장 마지막에 비어있는 곳에 착수한다. 한마디로 랜덤.
# 상대가 귀에 두면 중심에 놓고, 상대가 중심에 놓으면 귀에 놓는 것을 중심으로 한다.
def dropComputer(pos, lastdrop, defuse) :
    if lastdrop==1 or lastdrop==3 or lastdrop==7 or lastdrop==9 : # 상대가 귀에 착수하였다
        if defuse[1][1] == ' ' : return 5
    elif lastdrop==5 : # 상대가 중심에 착수하였다
        if defuse[0][0] == ' ' : return 1
        elif defuse[2][0] == ' ' : return 7
        elif defuse[0][2] == ' ' : return 3
        elif defuse[2][2] == ' ' : return 9
    else : return pos

# 게임을 실행하는 중심 부분이다.
# check 인자는 누가 먼저 시작하는가에 대한 정보를 지닌다.
def play_game(check):
    a=0
    while True :
        if check==1 :
            while True : #사람의 입력 차례
                try :
                    a=int(input("돌을 놓을 위치를 입력해주세요(1-9) ")) # 사람이 착수할 곳이다. 관계식은 standard_map( (a-1)//3, (a-1)%3 ) 이다.
                except ValueError :
                    print("잘못된 입력입니다. 숫자를 입력해주세요.\n")
                    continue

                if (a>=1 and a<=9) :
                    if standard_map[(a-1)//3][(a-1)%3]!=' ' :
                        print("잘못된 입력입니다. 이미 그 위치에는 점을 놓았습니다.\n") # 이미 착수한 지점에 대한 오류이다. 다시 입력받는다.
                    else : break
                else :
                    print("잘못된 입력입니다. 숫자의 범위는 1~9입니다.\n") # 숫자 범위에 대한 오류이다. 다시 입력받는다.

            standard_map[(a-1)//3][(a-1)%3]=t # 문제가 없으면 착수한다. 다시 한번 말하지만 t는 사람이 선택한 기호이다.
            if computer_AI(standard_map, t) : # computer_AI를 통해 만약 이기는 위치가 존재하면 상대의 승리를 인정하고 끝낸다.
                print("당신이 이겼어요! 대단하십니다!")
                return

            flag=0
            for i in range(9) :
                if standard_map[(i-1)//3][(i-1)%3]== ' ': # 아직 안 놓은 곳이 있다면 플래그를 1로 바꾸어준다.
                    flag=1

            if flag==0 :
                print("모든 곳에 놓으셨네요\n무승부입니다.") # 빈 곳이 없는데 앞의 if문에 따라 이긴 곳도 없으므로 비긴 것이다.
                return

            print_map(standard_map) # 현재 상황을 출력해 준다.

        else : #컴퓨터의 입력 차례
            position=-1
            newflag=0
            for i in range(1,10) :
                use=copy.deepcopy(standard_map) # deepcopy를 해주어서 standard_map의 모든 값을 use에 복사해준다.

                if use[(i-1)//3][(i-1)%3]==' ' : # 다음턴 그곳에 상대가 돌을 놓으면 지는 위치를 파악한다.
                    position=i
                    use[(i-1)//3][(i-1)%3]=t # copy해놓은 use에 사람의 돌을 놓아보고 지는지 안지는지 아래줄을 통해 확인한다.
                    afterAI = computer_AI(use, t)
                    if afterAI==1 :
                        newflag=1 # newflag가 1이면 필수적으로 놓아야 합니다.
                        break # 만약 지는 것을 알면 position을 이미 저장했으므로 break해준다.

            # 우선순위가 내가 이김 > 상대가 이김 이라서 내가 이기는 경우의 코드가 뒤쪽에 있다.
            # 만약 특정 점에 자신이 착수했을 때, 이긴다면 안놓을 이유가 없다.
            for i in range(1,10) :
                use2=copy.deepcopy(standard_map) # 똑같이 deepcopy를 해준다.
                if use2[(i-1)//3][(i-1)%3]==' ': # 비어있고 만약 놓았을 때 이기면 놓을 곳을 저장한 position을 업데이트 해주고 끝낸다.
                    use2[(i-1)//3][(i-1)%3]=c
                    pick=computer_AI(use2, c) # 1이면 놓았을 때 이김
                    if pick==1 :
                        newflag=1 # newflag가 1이면 필수적으로 놓아야 합니다.
                        position=i # 업데이트
                        break # 종료

            if mode==1 : # EASY 모드이다. 저장된 position을 그대로 넣어준다.
                if position!=-1 :
                    standard_map[(position-1)//3][(position-1)%3]=c # 오랜 실험을 통해 얻어낸 가장 좋은 position에 드디어 착수한다.

                    if computer_AI(standard_map,c) : # 함수의 반환 결과가 1이면 컴퓨터가 이겼다!
                        print("다음 기회에 또 도전하세요!")
                        return
            else : # HARD 모드이다. dropComputer에 있는 알고리즘을 활용하여 착수를 다시 한 번 고민한다.
               if position!=-1 :
                    if newflag==1 :
                        standard_map[(position-1)//3][(position-1)%3]=c # flag가 0인 것은 어디든 꼭 놓아야 하는 점이 있다는 것이다. 공격이든 방어든 말이다.
                    else :
                        position = dropComputer(position, a, standard_map)  # flag가 1이면 꼭 놓아야 하는 점은 없다. 그러므로 dropComputer에 포함된 전략으로 착수한다.
                        standard_map[(position-1)//3][(position-1)%3]=c # 마지막 고려가 끝났다. 착수하자.

                    if computer_AI(standard_map,c) : # 함수의 반환 결과가 1이면 컴퓨터가 이겼다.
                        print("다음 기회에 또 도전하세요!")
                        return

            print_map(standard_map)
            flag=0
            for i in range(9) :
                if standard_map[(i-1)//3][(i-1)%3]== ' ': # 아직 안 놓은 곳이 있다면 플래그를 1로 바꾸어준다.
                    flag=1

            if flag==0 : # 끝까지 돌고(flag==1) 놓을 position이 아무래도 없을 때는 무승부를 출력한다.
                print("모든 곳에 놓으셨네요\n무승부입니다.")
                return

        check=1-check # 턴을 전환한다.
        print("===================")

# 리스트의 초기화이다. 3x3 리스트를 제작하고 빈 것으로 채워준다.

while True:
    for i in range(3) :
        standard_map.append([' ',' ',' '])

    # HARD 모드는 상대가 중앙에 놓나 귀에 놓나 판단하고 그것에 맞춰서 착수한다.
    # HARD 모드는 아마도 못이기는 것 같은데, 내가 틱택토 필승 전략을 잘 몰라서 못이길 수도 있다.
    # 어쨌든 강하다.
    # EASY 모드는 내가 이길 위치, 상대가 질 위치는 판단하지만 그런 상황이 아닐 때는 임의로 랜덤 착수이다.
    mode=input("모드를 선택해주세요.\n숫자 0 : HARD\n0이 아닌 다른 글자 : EASY\n")
    if mode!='0' :
        print("EASY 모드입니다.")
        mode=1
    else : print("HARD 모드입니다.")

    play_game(init()) # init()의 반환값은 시작 순서이다.
    print("==== 마지막 MAP ====")
    print_map(standard_map) # 마지막으로 리스트를 맵 형태로 출력해주자.
    print("===================")

    i = input("다시 시작하시겠습니까?\n숫자 0을 누르면 종료합니다. 다른 글자면 계속합니다.")
    if i=='0' : break
    # standard_map의 초기화 과정
    del standard_map[0]
    del standard_map[0]
    del standard_map[0]
