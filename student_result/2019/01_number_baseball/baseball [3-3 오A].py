import random

# 비밀 숫자 생성 함수
def generating_Secret_Number():
    randstr = list(range(10))               # 0~9까지의 수를 리스트타입으로 생성
    random.shuffle(randstr)                 # random 모듈의 shuffle 함수를 이용해 무작위로 배열
    secret_number = ''
    for i in range(3):
        secret_number += str(randstr[i])    # 무작위로 섞인 리스트에서 첫 3개의 수를 선택해 길이 3인 문자열로 합성

    return secret_number                # 비밀 숫자를 덱스트타입(str)으로 반환한다.


# s, b, o 판정 함수
def sbo(secret_number, assume_number):
    strike = 0
    ball = 0
    out = 0
    for i in range(3):
        for j in range(3):
            if assume_number[i] == secret_number[j]:
                if i == j:
                    strike += 1
                else:
                    ball += 1
    out = 3 - strike - ball
    if strike == 3:
        return 999, print("Congratulation!")        # 숫자 999를 while 문을 빠져나오기 위한 flag로 둠
    print("strike : {}\nball : {}\nout : {}".format(strike, ball, out))

    return


def game_start():
    # 비밀 숫자를 생성
    secret_number = generating_Secret_Number()
    print(secret_number)

    # 10번의 기회를 제공
    trial=10
    while(trial > 0):
        # 사용자가 추측한 숫자 입력
        # exception : 입력 오류시 재입력 요구
        try :
            a, b, c = list(map(str, input().split()))           # 3개 미만, 초과 입력시 오류 발생
            assume_number = a + b + c

            # 사용자 입력 오류시 오류를 유도하는 구문
            # 0~9 이내의 정수가 아닌 수(소수점, 한자, 영문, 음수)를 입력하면 raise exception으로 강제 오류 발생
            errordict = {'1':1, '2':2, '3':3, '4':4, '5':5, '6':6, '7':7, '8':8, '9':9, '0':0}
            if errordict[a] != int(a) or errordict[b] != int(b) or errordict[c] != int(c):
                raise Exception
            # 중복되는 값이 있으면 오류 발생
            errorset = {a, b, c}
            if len(list(errorset)) != 3:
                raise Exception

            # 사용자가 추측한 숫자와 비밀 숫자를 비교하여 s, b, o를 출력
            r = sbo(secret_number, assume_number)
            if r != None:                       # 비밀 숫자를 맞췄을 때 sbo의 반환값이 None이 아니게 됨.
                break
            trial -= 1
            print("남은 시도 횟수 : %d" % trial)
            
        except :
            print ("다시 입력하세요")

    # 게임이 끝난 후, 사용자의 의사를 묻는다.
    # n을 입력 -> 프로그램 종료 y를 입력 -> 다시 플레이
    print("\n다시 플레이 할까요?(y : 다시 플레이 n : 게임종료)")
    respond = input()
    if respond == 'n':
        print("끝~")
        return
    elif respond == 'y':
        print("===============새로운 게임================")
        game_start()


game_start()
