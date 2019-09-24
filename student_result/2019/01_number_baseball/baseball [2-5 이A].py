
"""
Title       야구 게임
Reference   baseball.py by Kadragon
Author      4기 이승민
Date        2019.09.23
"""

import random

def get_ans(digit):
    """
    digit 길이만큼의 랜덤한 숫자로 이루어진 문자열을 반환한다.
    param digit: 원하는 문자열의 길이
    return: digit 길이의 랜덤 문자열
    """
    numz = list(range(10)) #0~9까지의 수로 이루어진 리스트 생성
    random.shuffle(numz) #리스트를 랜덤하게 섞음
    answer = ''
    for i in range(digit):
        answer += str(numz[i]) #섞인 리스트를 digit만큼 꺼내옴
    return answer #정답 문자열 반환

def get_clues_or_success(guess,answer):
    """
    guess와 answer가 일치하면 정답 메시지 반환
    일치하지 않을 경우 S|B|O로 이루어진 힌트 반환
    param guess: 사용자가 입력한 값
    param answer: 정답
    return: 성공 or 힌트
    """
    if guess == answer:
        return "정답을 맞추셨습니다!"

    ans_s = 0 #스트라이크인 경우의 수
    ans_b = 0 #볼인 경우의 수
    ans_o = 0 #아웃인 경우의 수

    for i in range(len(guess)):
        if guess[i] == answer[i]: #숫자와 위치가 모두 맞음
            ans_s += 1
        elif guess[i] in answer: #숫자는 맞으나 위치가 틀림
            ans_b += 1
        else: #숫자가 틀림
            ans_o += 1

    return str(ans_s)+' S | ' + str(ans_b) + ' B | ' + str(ans_o) + ' 0\n' #SBO 정보 반환

def only_integer(guess):
    """
    guess가 숫자로 이루어져 있으면 True, 아니면 False
    param guess: 사용자가 입력한 값
    return: True or False
    """
    for i in guess: #guess 문자열 안의 문자 i에 대해
        if i not in str(list(range(10))): #i의 정수형이 0~9까지의 정수가 아니라면
            return False #숫자가 제대로 입력되지 않았음.

    return True

def play_again():
    """
    다시 플레이할지 물어봄.
    return: True or False
    """
    print("다시 플레이하시겠습니까? [y/n]")
    again = input()
    while again != 'y' and again != 'n': #입력한 값이 y나 n이 아니면
        print("y나 n을 입력하십시오.")
        again = input() #다시 입력받음
    if again == 'y': #y가 입력되면 다시 플레이
        return True
    else:
        return False
    
     

DIGIT = 3 #문자열의 길이는 3
CHANCE = 10 #기회는 총 10회

while True:

    Answer = get_ans(DIGIT) #랜덤하게 DIGIT 길이의 숫자로 이루어진 문자열생성
    print("=" * 50)
    print("숫자를 맞춰라! %s 번의 기회가 주어집니다." % CHANCE)
    print("숫자의 자릿수는 %s 자리 입니다." % DIGIT)
    print("=" * 50)
    print("* 숫자를 입력할 때마다 힌트를 얻을 수 있습니다.")
    print("스트라이크(S) 는 입력한 숫자와 위치가 모두 맞음을 의미합니다.")
    print("볼(B)         은 숫자는 맞으나 위치가 틀렸음을 의미합니다.")
    print("아웃(O)       는 숫자가 틀렸음을 의미합니다.")
    print("열심히 해보세요!")
    print("=" * 50)
    Try = 1 #시도 횟수를 저장

    while Try <= CHANCE: #시도 횟수가 주어진 기회보다 작거나 같을 때
        
        print("Guess #%s:" % Try,end='')
        Guess = input() #입력 받음
        if Guess == '':
            print("입력이 들어오지 않았습니다.") #입력이 들어오지 않았으면 출력
            continue
        if not only_integer(Guess):
            print("0~9까지의 숫자를 입력하세요.") #들어온 입력이 숫자가 아니면 출력
            continue
        if len(Guess) != DIGIT:
            print("%s 자릿수의 숫자를 입력하세요." % DIGIT) #입력의 크기가 자릿수와 다르면 출력
            continue
        
        Try += 1 #시도 1 증가
        clues_or_success = get_clues_or_success(Guess,Answer) #힌트 or 성공메시지 받아오기
        print(clues_or_success) #힌트 or 성공메시지 출력

        if Guess == Answer: #정답이었다면 성공메시지를 출력했으므로 break
            break
        if Try > CHANCE:
            print("게임 오버.... 정답은 %s 이었습니다." % Answer) #기회를 전부 소모했을 경우 답 알려줌

    if not play_again(): #다시 플레이하지 않을 경우 종료
        break

