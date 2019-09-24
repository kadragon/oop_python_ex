import random
answer = ''
def makenumber():       # 각각의 자리가 0~9 중 하나로 이루어져 있는 임의의 3자리 수를 생성하는 함수
    global answer       # 전역변수 answer의 값을 함수 안에서 수정할 수 있게 함
    elements = list(range(10))      # 0부터 9까지의 값을 요소로 가지는 리스트를 생성
    random.shuffle(elements)        # 리스트의 원소를 랜덤으로 섞음
    for i in range(3):
        answer += str(elements[i])      # 길이가 3인 문자열 생성. 리스트의 요소들은 중복되지 않으므로 정답은 숫자가 2번 이상 중복되지 않음

def filtering(number):      # number은 사용자가 입력한 값으로, 이 값이 조건을 만족하는지 확인
    for j in number:        # j는 number 문자열에서 뽑아낸 하나의 값
        if number.count(j) > 1:     # number 문자열 안에 j가 몇 번 들어있는지를 알려주는 count를 통해 그 값이 2 이상이면 같은 숫자가 중복되는 값이므로 제외
            return False

    if not number.isdigit():        # 문자열이 숫자 문자로 이루어져 있는지를 확인해주는 isdigit 함수를 통해 입력값이 숫자로만 이루어져 있는지 확인
        return False

    return True         # 조건을 만족하면 True 반환

def refree(guess, ans):         # guess는 사용자가 입력한 값, ans는 정답
    strike = 0          # 스트라이크인 경우에 해당하는 개수 카운트
    ball = 0            # 볼인 경우에 해당하는 개수 카운트
    out = 0             # 아웃인 경우에 해당하는 개수 카운트
    if guess == ans:        # 사용자가 입력한 값과 정답이 일치하면 정확하다는 문장을 반환
        return("Correct")

    else:
        for i in range(3):
            if guess[i] == ans[i]:          # 해당 숫자가 정답에 있고 위치도 일치하면 스트라이크를 1 증가
                strike += 1
            elif ans.count(guess[i]):       # 위치는 일치하지 않더라도 해당 숫자가 정답에 존재하는지를 확인하여 있다면 볼을 1 증가
                ball += 1
            else:                           # 숫자가 정답에 존재하지도 않으므로 아웃을 1 증가
                out += 1
        return("S : " + str(strike) + " B : " + str(ball) + " O : " + str(out))     # S와 B, O가 각각 몇 번인지를 반환

def again():        # 다시 할 것인지를 물어보는 함수
    print("한판 더 하고 싶으시나요? 그렇다면 전부 소문자로 yes 라고 말해주세요.")
    x = input()
    if x == "yes":      # yes를 입력하면 True를 반환하여 반복하여 진행할 수 있게 함
        return True
    else :              # 이외에는 False를 반환하여 게임을 끝내도록 함
        return False

cnt = 0  #사용자가 시도한 횟수를 값으로 가지는 변수 객체
while True:
    makenumber()  # 정답을 생성함.
    print('''
    제가 생각하는 3자리 수를 10번 안에 맞혀보세요!
    단, 062와 같이 0으로 시작하는 3자리 수는 포함되는 반면
    224나 333과 같이 같은 숫자가 두 번 이상 반복되는 경우는 없고 세 자리 모두 다른 숫자입니다.
    또한 매번 힌트가 주어질 텐데요. 
    숫자가 맞지만 위치가 틀렸을 때는 B(볼),
    숫자와 위치가 모두 맞으면 S(스트라이크),
    숫자와 위치가 모두 틀리면 O(아웃)으로 주어집니다.
    예를 들면 정답이 235일 때 213을 말하면 2는 정확한 위치에 있고, 3은 위치는 틀려도 정답에 있긴 하므로 1S 1B 1O입니다.
    그러면 게임을 즐겨주세요!
    ''')
    while cnt <= 10:                    # 사용자가 10번 이상 시도하지는 않았는지를 확인
        playerans = ''                  # 사용자가 입력한 값을 저장하는 변수 객체
        playerans = input()
        while len(playerans) != 3 or not filtering(playerans):      # 입력된 값의 길이가 3이고 모두 숫자인지 확인하여, 그렇지 않다면 조건에 맞게 입력될 때까지 반복
            print("다시 입력해주세요 ㅠㅠ")
            playerans = input()

        print(refree(playerans, answer))        # 볼과 스트라이크, 아웃을 확인
        cnt+=1                                  # 한 번 시도했으므로 시도 횟수 1 증가

        if playerans == answer :                # 정답을 맞추었으므로 이번 판 종료
            break
        elif cnt >= 10:         # 정답을 맞추지 못하고 10번 시도했으므로 정답을 알려주고 이번 판 종료
            print("정답은 " + str(answer))
            print("아쉽네요ㅠㅠ 다음에는 꼭 맞추시길 바랄게요")
            break

    if again() is False:        # 사용자가 다시 할 것인지 확인하여 그렇지 않다면 게임종료
        break
    else:
        cnt = 0     # 다시 한다면 시도 횟수 초기화하고 반복
        answer = '' # 정답을 출력하는 문자열도 초기화







