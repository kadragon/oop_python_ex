import random
import sys

# 플레이어가 입력한 수를 한자리씩 삽입하는 리스트
User_list = []
# 컴퓨터가 랜덤으로 생성한 수를 한자리씩 삽입하는 리스트
Com_list = []

# strike, ball, out 선언
strike = 0
ball = 0
out = 0


# 컴퓨터가 생성한 난수와 내가 입력한 수에 반복되는 수가 있는지 판별하는 함수, k에는 내가 확인하고 싶은 리스트나 문자열을 넣어준다.
def same_number(k):
    for x in range(len(k)):
        for y in range(len(k)):
            if x != y and k[x] == k[y]:  # 자릿수가 서로 다른데 숫자가 같은 경우
                return True  # 참을 반환
    return False  # 그 외에는 거짓을 반환


# 사용자가 입력을 잘못해서 게임을 종료할 때 사용하는 함수
def print_game_over():
    print("제대로 입력하지 않았으므로 게임을 종료합니다! 다음부터는 입력을 제대로 해주세요!!!")
    print("Game over!!")
    sys.exit()  # 시스템 종료


# strike, ball, out 을 0으로 초기화해주는 함수
def make_zero():
    global strike, ball, out
    strike = 0
    ball = 0
    out = 0


# strike, ball, out 을 구해주는 함수
def return_strike_ball_out():
    global strike, ball, out  # 전역변수 사용
    for i in range(3):
        for j in range(3):
            if Com_list[i] == User_list[i]:  # 같은 자리에 대해서 확인
                strike += 1  # 같으면 strike 추가
                break
            if Com_list[i] == User_list[j]:  # 서로 다른 자리에 대해서 확인
                ball += 1
                break
    out = 3 - strike - ball  # out 구하기


# 사용자가 게임을 제대로 플레이 하지 않을 경우에 대비해서 만든 함수이다.
def get_game_over(k):
    if len(k) != 3:  # 길이가 3이 아니면
        print_game_over()  # 게임 종료

    for i in range(len(k)):
        if '0' <= k[i] <= '9':  # 받은 문자가 0에서 9사이이면
            User_list.append(k[i])  # User_list 에 추가해준다
        else:  # 아니면
            print_game_over()  # 게임 종료

    if same_number(User_list):  # 숫자가 반복되면
        print_game_over()  # 게임 종료


# 컴퓨터가 난수 생성하는 함수
def make_com_number():
    same = True
    while same:
        random_number = random.randrange(100, 1000)  # 100에서 999 사이의 수를 생성
        # print(random_number)
        random_number = str(random_number)  # 문자열로 만들어준다
        same = same_number(random_number)  # 반복되는 수가 있는지 확인

    for i in range(len(random_number)):
        Com_list.append(random_number[i])  # Com_list 에 추가해준다


# list 의 원소들을 전부 삭제해준다
def delete_list(k):
    for i in range(len(k)):
        del (k[0])


# 시도 횟수
trial_number = 1

print("========================================================================================")
print("숫자 야구 게임을 해주셔서 감사합니다.")
print("간단하게 규칙을 설명드리겠습니다.")
print("숫자 야구 게임은 3자리의 임의의 숫자를 플레이어가 맞추는 게임이고 사용되는 숫자는 0 ~ 9 까지 서로 다른 숫자입니다.")
print("숫자와 위치가 모두 맞으면 Strike, 숫자는 맞지만 위치가 틀리면 Ball, 숫자와 위치가 모두 틀리면 Out입니다.")
print("단, 무엇이 볼이고 스트라이크인지 알려주지는 않습니다.")
print("참고로 입력을 형식에 맞춰 꼭 해주세요~!! 그렇게 하지 않는다면 불이익이 있습니다ㅠㅠ")
print("자, 그러면 게임을 시작하겠습니다!")
print("========================================================================================")

while trial_number <= 10:  # 10번의 기회
    if trial_number == 1:  # 처음 할 때
        print("제 머리 속에는  현재 중복되지 않은 숫자로 이루어진 3자리의 임의의 정수가 있습니다. 한번 맞춰보세요!!")
        print("10번의 시도 제한이 있습니다!!!!!!!!!!!!!!!!!!!!!!!!!! ")
        make_com_number()  # 난수 생성

    print("========================================================================================")
    print("%d개 목숨이 남았습니다" % (10 - trial_number + 1))
    a = input("숫자를 입력해주세요: ")
    get_game_over(a)  # 입력이 조건에 맞는지 확인

    make_zero()  # 초기화

    return_strike_ball_out()  # strike, ball, out을 구해준다

    # if strike == 3: # 숫자를 맞췄을 때
    #     print("정말 똑똑하군요!! 당신이 승리하였습니다!!!")
    if strike != 3:
        print("%d번째 시도: %dStrike %dBall %dOut" % (trial_number, strike, ball, out))

    delete_list(User_list)  # 사용자 리스트 초기화

    trial_number += 1  # 시도 횟수 1 증가

    if trial_number == 11 or strike == 3:
        if strike == 3:
            print("정말 똑똑하군요!! 당신이 승리하였습니다!!!")
        elif trial_number == 11:
            print("목숨을 전부 사용하셨습니다......")
        print("다시 플레이하고 싶으신가요?? YES 또는 NO를 입력해주세요! 정확하게 입력하세요!!!")
        b = input()  # YES 또는 NO를 입력 받는다.
        if b == "YES":
            trial_number = 1  # 시도 횟수를 1로 초기화해주고
            delete_list(Com_list)  # 컴퓨터 숫자가 들어있는 리스트를 초기화
        else:  # 아니면
            break  # while 문을 빠져나온다

print("========================================================================================")
print("Game over!!")
