#소 과제-1_숫자 야구 (2202 김윤종)

import random   #Random수를 생성하기 위해, import random!

Text = """
========================윤종's 숫자야구 ========================
-  설명
저는 임의의 세 자리 숫자를 떠올릴 거고요, 플레이어가 그 숫자를 맞추시면 돼요!
세 자리 숫자를 입력하시면, 제가 Strike, Ball, Out의 개수를 알려드릴게요!
*세 숫자는 서로 다르고, 0으로 시작할 수 있어요 ! 

Strike : 한 개의 숫자가 사용됐고, 올바른 자리에 있어요!
Ball : 한 개의 숫자가 사용됐지만, 틀린 자리에 있어요!
Out : 사용되지 않은 숫자에요!

- 조건
입력은 각각 정수로 이루어진 세 자리 숫자여야만 해요! 
숫자를 누르고, Enter 키를 누르면 입력이 됩니다. 

-예시
가정 : 제가 135라는 수를 떠올렸다고 합시다,
플레이어께서 123을 입력하셨다면, 
1은 Strike, 3은 Ball, 5는 Out이므로
S:1 | B:1 | O:1
라고 알려드릴게요!
"""

def notnum(letter):         #notnum은 입력문자열이 숫자로만 이루어져있는지 확인한다
    for i in range(len(letter)):
        if (ord(letter[i])<48 or ord(letter[i])>57):   #숫자 0~9는 ASCII 코드로 48~57임을 활용한다
            return 1

def input_valid(G):
    """
    사용자가 입력한 Guess가 적합한지 확인하는 함수이다.
    G를 변수로 받고, 자리수, 숫자여부를 확인한다.
    """

    if len(G) != 3:    #3자리가 아니면 다시 입력받는다.
        print('자리수 에러 : 3자리 정수를 입력해주세요!')
        return 0

    if notnum(G):      #숫자로 이루어지지 않았으면 다시 입력받는다.
        print('알파벳/한글/기호/띄어쓰기를 입력하셨습니다, 숫자를 입력해주세요')
        return 0
    return 1

def input_guess(num):      #숫자 (Guess)를 입력받는 함수
    while(1):
        Guess = input('Guess #%d >>' % num)
        if input_valid(Guess):
            return Guess

def check(G):
    Strike = Ball = Out = 0         #Strike, Ball, Out을 초기화한다
    """
    사용자의 추정에 대한 Strike, Ball, Out을 판단하여 출력하는 함수. 
    정답(3 Strike)이면 1을 반환한다. 
    G는 사용자의 Guess : G는 리스트로, G[0], G[1], G[2]에 각각 1, 2, 3의 자리 숫자가 담겨있다.
    Checklist에는 Random숫자가 저장되있는데, 숫자가 456이라면 
    Checklist는 [0, 0, 0, 1, 2, 3, 0, 0, 0, 0]으로 저장된다. (각 index가 사용된 자리를 의미)
    i는 0부터 2까지 순서대로, G[i] (입력 값)이 Random 수에 있는지 확인한다.
    G[0]은 첫 번째 수로, checklist[int(G[0]]이 1이면 Random에서도 첫 수이므로 Strike
    1이 아니고 2, 3 처럼 0이 아니면 사용만 된것이므로 Ball
    0이면 Out
    """
    for i in range(3):
        if checklist[int(G[i])] == i+1:
            Strike += 1
        elif checklist[int(G[i])]:
            Ball += 1
        else:
            Out += 1

    if Strike == 3: return 1
    else:
        print('S:%d | B:%d | O:%d' % (Strike, Ball, Out))
        return 0

#==============================================================================================================================
#Step 1 : 설명문 출력
print(Text)

#Step 2 : 게임 시작
Play = 1  #Play는 재시작에 대한 flag

#게임 종료 후, 재시작이 가능하도록 while(play) 설치
while(Play):
    """
    Random수를 생성하는 부분
    Num에 랜덤수를 생성하고
    Checklist는 Num의 다른 표현법, 사용된 위치를 저장한다 (이후 S,B,O를 판단할때 사용)
    """
    Q_list = list(range(10))
    random.shuffle(Q_list)
    Num = []
    checklist = [0] * 10
    for i in range(1 , 4):
        Num.append(Q_list[i])
        checklist[Q_list[i]] = i   #RANDOM수에 대한 다른 표현법. checklist에 사용된 위치를 저장
    print('='*60)

    flag_answer = 1              #flag_answer는 사용자가 정답을 맞추면 0으로 바뀌는 flag
    try_num = 1                  #시도 횟수를 담음

    while(try_num <= 10):         #10회
        guess = input_guess(try_num)    #세 자리 숫자를 입력받음, 숫자가 유효한지 검사하는 과정이 포함됨
        try_num += 1

        if(check(guess)):       #입력받은 것을 확인하여 S,B,O를 출력한다, 정답시 return 1
            print("우왕! %d번 만에 정답을 찾아내셨어요!" % (try_num-1))
            try_num = 1         #try_num =1이 없을 때, 정확히 10회에 맞추었을 때, 오답이라고 판단함
            break               #10회 이내에 정답을 맞추었을 때, 성공함.

    if(try_num == 11):          #10회 안에 정답을 맞추지 못한 경우
        print('10회면 충분할줄 알았는데... 실망입니다')
        print('정답은 %d%d%d 였습니다' % (Num[0], Num[1], Num[2]))

    again = input('다시 도전하시겠습니까? (y/n)')     #재도전 여부 입력

    while (again != 'n' and again != 'y'):          #재도전 입력이 이상한지 검사
        print('잘못 입력하셨습니다.')
        print('영글자 y 혹은 n를 입력해주세요')
        again = input('다시 도전하시겠습니까? (y/n)')

    if (again =='n'):                               #게임 종료
        print('수고하셨습니다, 다음에 또만나요')
        Play = 0           #게임 종료

    elif (again == 'y'):                            #게임 재도전
        print('새로운 숫자를 떠올렸어요! 이번엔 더 빨리 맞춰보세요')

123