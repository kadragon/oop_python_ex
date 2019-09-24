import random                           # random 함수 사용


def make_ans():                         # 답 만드는 함수
    numbers = list(range(10))           # 겹치지 않기 위해 0부터 9까지 숫자를 만들고
    random.shuffle(numbers)             # 무작위 배열
    mans = ''                           # 변환할 할 수 저장할 변수 만들기
    for i in range(3):                  # 랜덤 돌린 수 배열 중 첫 3자리 고르기
        mans += str(numbers[i])
    return mans                         # 랜덤하게 구한 3자리 배열


def compare(player_num, ans):               # 사용자의 답 상태 확인
    if player_num == ans:                   # 사용자가 선택한 값이 정답과 같으면 승리로 결과
        return print('삼진 스트라이크 아웃!')
    stk = 0                                 # 스트라이크 수
    out = 0                                 # 아웃 수
    ball = 0                                # 볼 수
    for i in range(len(player_num)):
        if player_num[i] == ans[i]:         # 위치 수 같으면 스트라이크
            stk += 1
        elif player_num[i] in ans:          # 위치는 다르고 수가 같으면 볼
            ball += 1
        else:                               # 나머지는 아웃
            out += 1
    print('S: '+str(stk)+' / B: '+str(ball)+' / O: '+str(out))      # 출력
    return


def play_again():                              # 재시작 여부 질문
    print('다음 이닝으로 넘어 가시겠습니까?')
    print('insert coin')
    print('Yes  No')
    re = str(input())                          # 스캔
    if re == 'yes':                            # 재시작 조건 1
        return True
    elif re == 'Yes':                          # 재시작 조건 2
        return True
    else:                                       # 나머지는
        return False


def numok(numb):                                # 재대로됭 숫자인지 확인
    if len(numb) != 3:                             # 3자리가 아닌 경우
        print('3자리요 3자리~!!')
        return False
    if not numb.isdigit():                          # 숫자가 아닌 경우
        print('숫자라고요 숫자~~!!')
        return False
    return True


while True:
    print('숫자 야구 게임!')
    print('컴퓨터가 임의 자정한 겹치지 않는 3자리 수를 맞추는 게임입니다.')
    print('오직 한 자리 숫자로만 이루어진 수 3개를 띄지 않고 써주세요.')
    print('그럼 시작합니다!')
    print('Play Ball!!')
    ans = make_ans()                    # 답 만들기
    for i in range(10):                 # 도전 기회는 10번
        print('%d번째 타자!!' % (i+1))
        able = False                    # 조건에 만족 될 때까지 입력을 받게 해줄 입력 성공 여부 확인 문자
        ctime = int(-1)                 # 밑에서 놀기 위한 변수 설정
        while not able:                 # 조건을 만족해야 탈출
            num = input()               # 사용자 입력 스캔
            able = numok(num)           # 입력이 잘되었는지 확인
            if ctime == 0:
                print('위에 설명좀 읽고오세요...')
            if ctime == 1:
                print('위에 설명좀 읽어보라고요.........')
            if ctime == 2:
                print('아니 진짜 왜 이렇게 말을 안들어?')
            if ctime == 3:
                print('학습능력이 없어?')
            if ctime == 4:
                print('너 일부러 그러는거지??')
            if ctime == 5:
                print('진짜 해보자는 거냐?!!')
            if ctime == 6:
                print('그래 갈 때까지 가보자 그래!!')
            if ctime == 7:
                print('흥!')
            if ctime == 8:
                print('진짜 적당히 좀.....;;')
            if ctime == 9:
                print('그래 니가 이겼다....')
            if ctime == 10:
                print('내가 졌다고 졌어')
            if ctime == 11:
                print('인줄 알았지? 메롱')
            if ctime == 12:
                print('이젠 진짜 귀찮아서 그만할래')
            if ctime == 13:
                print('더 이상 아무것도 없을거야')
            if ctime == 14:
                print('그럼에도 불구하고 한 번더 누르는 당신의 열정에 박수를...')
            if ctime == 15:
                print('진짜 레알 ㅅㄱ ㅂㅇ')
            ctime += 1
        compare(num, ans)                              # S B O 값 알아내기
        if num == ans:                                  # 정답을 맞추면 탈출, 초기화
            break
        if i == 9:                                             # 기회를 다 소진하면
            print('아 이번 경기는 무득점으로 마무리하게 되는군요....')
            print('구단의 미래가 어둡습니다...')
    if not play_again():                               # 더 하는지 물어보고 그만두면 탈출
        break
