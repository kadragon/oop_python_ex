"""
Project  틱택토 게임
Author   지명금
Date     2018.09.06
"""

# copy :: 컴퓨터의 수를 결정하기 위한 testBoard를 만들기 위하여
import copy
# random :: 게임 순서를 임의로 정하는 함수를 정의하기 위하여
import random

def game_Explain():
    """
    >> 틱택토 게임에 대한 설명을 화면으로 보여주는 함수
    """
    print("="*80)
    print("""
    -|---|---|---|-  >> tic-tac-toe game!
     | 1 | 2 | 3 |      저와 함께 틱택토(tic-tac-toe) 게임을 해봅시다!
    -|---|---|---|-     1) 원하는 표식을 선택해주세요! (O 혹은 X)
     | 4 | 5 | 6 |      2) 원하는 위치를 선택하며 게임을 진행!
    -|---|---|---|-     3) 가로 or 세로 or 대각선을 먼저 채우면 승!
     | 7 | 8 | 9 |
    -|---|---|---|-
    """);
    print("="*80)
    

def get_OX():
    """
    >> 사용자로부터 O 또는 X의 표식을 선택하게 하는 함수

    :param userSymbol: 사용자가 입력한 표식
    :return userSymbol: 사용자의 표식
    """
    userSymbol = input(">> 어떤 표식을 선택하시겠습니까? [O/X] : ").upper()
    
    if userSymbol == "O" or userSymbol == "X":
        return userSymbol
    else :
        print("게임 플레이를 안하실건가요? 제대로 입력해주세요")
        return get_OX()
    
def choose_playOrder(userSymbol):
    """
    >> 게임 플레이 순서를 랜덤으로 결정하는 함수

    :param userSymbol: 사용자의 표식
    :return order: 랜덤으로 결정된 게임순서 "0" "X"
    """
    order = int((random.random()*10)%2) # random.random()함수를 통해 받은 0<=x<1의 값을 binary 표현으로 변환
    order = 'O' if order==0 else 'X' # order가 0 이면 'O', order가 1이면 'X'으로 인식
    
    if order == userSymbol: # order의 결과를 나타냄
        print(">> 당신이 먼저 합니다!")
    else :
        print(">> 내가 먼저 할게요!")
        
    return order
    

def ask_Replay():
    """
    >> 사용자가 재게임을 한다면 True, 아니면 False를 반환하는 함수

    :return <'bool'>: 재게임 여부
    """
    answer = input("게임을 다시 플레이하시겠습니까? [y/n] ").upper() # 재게임 여부를 y(yes) 혹은 n(no)으로 입력
    
    if answer == 'Y' or answer == 'YES':
        return True
    elif answer == 'N' or answer == 'NO':
        return False
    
    else : # y(yes) 혹은 n(no)가 아닌 값을 입력했을 시 다시 확인 
        print("어이쿠 손가락이 미끄러지셨나보네요!")
        return ask_Replay()

def board_isFull(gameBoard):
    """
    >> gameBoard가 다 선택됬으면 True, 아니면 False를 반환하는 함수

    :param gameBoard: 게임판으로 이용되는 list
    :return <'bool'>: 9개의 칸이 다 선택됬으면 True, 아니면 False
    """
    check_full = 0 # 선택된 칸의 개수를 세기 위한 변수 객체
    
    for i in gameBoard:
        if i  == 'O' or i == 'X': # 선택된 칸은 'O' 혹은 'X'
            check_full += 1
    if check_full == 9 : # 9개의 칸이 모두 선택됬으면 True
        return True
    else :
        return False

def play_User(userSymbol,gameBoard):
    """
    >> 사용자로부터 위치 입력을 받는 함수

    :param userSymbol: 사용자의 표식
    :param gameBoard: 게임판으로 이용되는 list
    :return gameBoard: 사용자의 선택을 반영한 gameBoard
    """
    get_locate = input(">> 표식을 할 위치를 선정해주세요!(1~9): ") # 1~9사이로 위치를 입력받음
    
    if check_gameInput(get_locate,gameBoard) == False: # check_gameInput() :: 사용자가 입력을 잘했는지 판단/아니면 다시 입력받음
        print("다시 입력해주세요!")
        return play_User(userSymbol,gameBoard)
    
    else:
        get_locate = int(get_locate) # idx로 이용하기 위해 int형으로 객체의 class 변환
        gameBoard[get_locate-1] = userSymbol # 사용자의 선택 반영
        return gameBoard

def play_Computer(userSymbol, compSymbol, gameBoard):
    """
    >> 컴퓨터의 위치 입력을 받는 함수
    >> 컴퓨터의 룰
        a. 둘 수 있는 곳인가?
        b. 컴퓨터가 승리할 수 있는 곳이 있는가?
        c. 사용자가 승리할 수 있는 곳이 있는가?
        d. 이길 확률이 높은 곳에 두자
        
    :param userSymbol: 사용자의 표식
    :param compSymbol: 컴퓨터의 표식
    :param gameBoard: 게임판으로 이용되는 list
    :return testBoard: 컴퓨터의 선택을 반영한 gameBoard
    """
    testBoard = copy.deepcopy(gameBoard) # 가능한 경우의 수를 많이 시도해보기 위해 testBoard로 copy
    
    # 컴퓨터의 수는 한 번의 시도만 반영했을 때를 고려하고 있음

    # Rule(b) : 컴퓨터가 승리할 수 있는 곳이 있는가?
    for i in range(9):
        if testBoard[i] != 0: # Rule(a) : 둘 수 있는 곳인가?
            continue
        testBoard[i] = compSymbol
        
        if game_Win(testBoard)[0] == True and game_Win(testBoard)[1] == compSymbol: # 컴퓨터가 승리할 수 있는 위치가 존재하면 선택하고 반영
            return testBoard
        else :
            testBoard[i] = 0
    
    # Rule(c) : 사용자가 승리할 수 있는 곳이 있는가?
    for i in range(9):
        if testBoard[i] != 0: # Rule(a) :  둘 수 있는 곳인가?
            continue
        testBoard[i] = userSymbol
        
        if game_Win(testBoard)[0] == True and game_Win(testBoard)[1] == userSymbol: # 사용자가 승리할 수 있는 위치가 존재하면 선택하고 반영
            testBoard[i] = compSymbol
            return testBoard
        else :
            testBoard[i] = 0
    
    # Rule(d) : 이길 확률이 높은 곳에 두자
    # 이길 확률이 높은 순서는 모서리 > 중앙 > 이외 로 판단하여

    idx = [0,2,6,8] # 왼쪽위 - 오른쪽위 - 왼쪽아래 - 오른쪽아래의 인덱스를 담은 list
    random.shuffle(idx) # 랜덤으로 위치를 선택하게 된다
    while len(idx)!=0 : 
        if testBoard[idx[0]] == 0: # Rule(a) : 둘 수 있는 곳인가?
            testBoard[idx[0]] = compSymbol
            break;
        else :
            del idx[0] # 한번 뽑았지만 놓지 못하는 자리는 idx에서 제거한다
            random.shuffle(idx)
            
    if len(idx) == 0:
        if testBoard[4] == 0: # 중앙에 둘 수 있는가?
            testBoard[4] = compSymbol
        else : # 중앙에 둘 수 없으면 나머지 자리를 고려한다
            idx = [1,3,5,7] # 나머지 자리의 인덱스를 담은 list
            random.shuffle(idx) # 랜덤으로 위치를 선택하게 된다
            while len(idx)!=0 :
                if testBoard[idx[0]] == 0:
                    testBoard[idx[0]] = compSymbol
                    break;
                else :
                    del idx[0]
                    random.shuffle(idx)
                    
    return testBoard

def check_gameInput(get_locate , gameBoard) :
    """
    >> 사용자의 입력이 규칙에 위배되면 False, 아니면 True를 반환하는 함수
    >> 입력 규칙에 위배되는 경우 
        a. 입력의 길이가 1이 아닌 경우
        b. 숫자(0 제외)가 아닌 다른 것을 입력한 경우
        c. 이미 선택된 자리를 선택한 경우

    :param get_locate: 사용자가 입력한 위치
    :paran gameBoard: 게임판으로 이용되는 list
    :return <'bool'>: 규칙에 위배되면 False, 아니면 True
    """
    if get_locate.upper() == "HELP": # easteregg :: 사용자가 help를 입력하면 게임설명을 다시 한번 보여준다
        game_Explain() 
        return False
    
    if len(get_locate) != 1: # Rule(a) : 입력의 길이가 1이 아닌 경우 
        return False
    
    elif get_locate not in '123456789': # Rule(b) : 숫자(0 제외)가 아닌 다른 것을 입력한 경우
        return False
    
    elif gameBoard[int(get_locate)-1] != 0: # Rule(c) : 이미 선택된 자리를 선택한 경우
        return False
    
    return True

def game_Win(gameBoard):
    """
    >> 게임의 승리자가 있으면 True와 symbol을, 없으면 False와 default 값을 반환하는 함수

    :param gameBoard: 게임판으로 이용되는 list
    :return result: result[0] :: 게임의 승리자가 있으면 True, 없으면 False
                    result[1] :: 승리자의 표식, default 값으로 'O'
    """
    symbol,Try = 'O',0 # symbol은 'O' 혹은 'X' 표식을 담아두는 문자열 객체, Try는 시도횟수를 확인하기 위한 변수 객체
    result = [ False,'O' ]
    
    while Try<2:
        checkBoard = list(map(str,gameBoard)) # int와 str이 혼합되어 있는 gameBoard를 전부 str로 변환하여 저장해두기 위한 list

        # 가로 줄이 있는지 확인
        if ''.join(checkBoard[:3]) == symbol*3 or ''.join(checkBoard[3:6]) == symbol*3 or ''.join(checkBoard[6:]) == symbol*3: 
            result[0] = True
            result[1] = symbol
            break

        # 세로 줄이 있는지 확인
        elif ''.join(checkBoard[::3]) == symbol*3 or ''.join(checkBoard[1::3]) == symbol*3 or ''.join(checkBoard[2::3]) == symbol*3:
            result[0] = True
            result[1] = symbol
            break
        
        # 대각선 줄이 있는지 확인
        elif ''.join(checkBoard[0]+checkBoard[4]+checkBoard[8]) == symbol*3 or ''.join(checkBoard[2]+checkBoard[4]+checkBoard[6]) == symbol*3: 
            result[0] = True
            result[1] = symbol
            break
        
        Try += 1
        symbol = 'X' # 'X'로 바꾸어서 확인
        
    return result

def print_gameBoard(gameBoard):
    """
    >> gameBoard를 출력해주는 함수

    :param gameBoard: 게임판으로 이용되는 list
    """
    printBoard = [] # gameBoard를 출력하기 위한 list
    
    for i in range(9):
        if gameBoard[i] == 0:
            printBoard.append(' ') # printBoard 출력시에는 0을 ' '으로 변환해서 출력
            
        else :
            printBoard.append(gameBoard[i])
            
    print("""
    -|---|---|---|-
     | %s | %s | %s |  
    -|---|---|---|- 
     | %s | %s | %s |  
    -|---|---|---|-
     | %s | %s | %s |
    -|---|---|---|-
    """ % tuple(printBoard))

# Main 
gamePlay = True # 게임 플레이 여부를 저장하기 위한 변수 객체
game_Explain()

while gamePlay == True:
    gameBoard = [ 0 for i in range(9)] # 게임판으로 이용되는 list
    
    userSymbol = get_OX() 
    compSymbol = 'X' if userSymbol=='O' else 'O' # 사용자의 표식이 아닌 것을 컴퓨터의 표식으로 이용
    
    playOrder = choose_playOrder(userSymbol) # 게임의 진행 순서를 표기하기 위한 변수 객체
    
    while board_isFull(gameBoard) == False and game_Win(gameBoard)[0] == False : # 게임판이 다 차지 않았는지, 승리자가 있는지 확인
        print(">> 이번 순서는 %s입니다!" % playOrder) # 현재 게임의 진행 순서를 설명
        
        if playOrder == userSymbol:
            gameBoard = play_User(userSymbol,gameBoard)
        else :
            gameBoard = play_Computer(userSymbol,compSymbol,gameBoard)

        playOrder = 'X' if playOrder=='O' else 'O' # 게임의 진행 순서 바꾸기
        print_gameBoard(gameBoard)

    # 승리자가 나와서 게임이 끝난 경우
    if(game_Win(gameBoard)[0] == True): 
        winner = game_Win(gameBoard)[1] # 게임의 승리자를 출력
        if winner == userSymbol :
            print(">> 게임결과 : User Win!")
        else:
            print(">> 게임결과 : User Lose!")

    # 게임판이 다 차서 게임이 끝난 경우  
    else :
        print(">> 게임결과 : Tie!")
        
    gamePlay = ask_Replay()


