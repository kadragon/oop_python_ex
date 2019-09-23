import random


def display_intro():  # 처음 시작 화면
    print('\n' * 15)
    print('-' * 50)
    print("""
        Let's Baseball Game !!
        The chance will be given 10 times.
        Can you win? HAHAHA 
    """)
    print('-' * 50)
    print()


# 함수명의 시작은 소문자로..!
def Strike(num, ans):  # 스트라이크 개수를 판별하는 함수
    st = 0
    for i in range(0, 3):  # 각각의 자리수를 비교하여 같으면 st를 1 증가시킨다
        if ans[i] == num[i]:
            st += 1
    return st


def Ball(num, ans):  # 볼의 개수를 판별하는 함수
    ba = 0
    for i in range(0, 3):
        for j in range(0, 3):
            if num[i] == ans[j]:
                ba += 1
    return ba


def Enter():  # 입력값 판별 함수
    try:  # 정수가 입력되었을 때 100~999 사이의 수가 아닐 경우 Enter 함수를 재귀적으로 호출한다
        x = int(input())
        if x < 100 | x > 999:
            print("Hey, you should enter 3 numbers.")
            return Enter()
        else:
            return x
    # 정수형이 아닌 문자형이 입력될 때 발생하는 TypeError 메시지와 ValueError 메세지를 e에 저장하여 예외처리하고 재귀적으로 Enter 함수를 호출한다
    except TypeError as e:
        print("Hey, you should enter 3 numbers.")
        return Enter()
    except ValueError as e:
        print("Hey, you should enter 3 numbers.")
        return Enter()


def check():
    ans = random.sample(range(1, 10), 3)
    guesstaken = 1
    while guesstaken < 11:
        print('attempt : %d \nInput : ' % guesstaken)
        x = Enter()  # Enter 함수 호출
        num = [int(x / 100), int((x % 100) / 10), int(x % 10)]
        guesstaken += 1
        if num == ans:
            break
        else:
            st = Strike(num, ans)  # 스트라이크의 개수를 저장한다
            ba = Ball(num, ans) - st  # 볼의 개수를 저장한다
            ou = 3 - st - ba  # 아웃의 개수를 저장한다
        print('%d S | %d B | %d O' % (st, ba, ou))  # 스트라이크, 볼, 아웃의 개수를 차례로 출력한다
        print()

    if num == ans:
        print("Wow! you win!")
    else:
        print('HAHAHAHA!! you lose. The answer is %d%d%d.' % (ans[0], ans[1], ans[2]))


play_again = 'yes'
while play_again in ['yes', 'y']:
    display_intro()
    check()
    play_again = input('Do you want to play again? (y/n): ')
