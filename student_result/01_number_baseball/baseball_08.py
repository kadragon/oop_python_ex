import random

# 변수명이 너무 짧아서 다른 사람이 추측하기 어려운것은 비추천
L = 3


def make_number():
    index = list(range(10))
    random.shuffle(index)
    n = ""
    for i in range(L):
        n = n + str(index[i])  # 임의의 변수 설정
    return n


def intro():
    print("=" * 50)
    print("""
    Welcome to the baseball game!
    The number that you have to guess is maked with three diffrent number like "256" "023"
    If you input the number, I can return answer you with S,B,O
    S means same position and smae number, B means same number is in the computer number but the position is wrong
    O is worng everything
    So Let's start!
    """)
    print("=" * 50)


def scan():  # 사용자에게 정수를 받아서 되돌려주는 함수
    Form = 'F'
    while Form == 'F':
        scan_number = input("input the number:")
        number = ""
        check_list = "0 1 2 3 4 5 6 7 8 9".split()

        for i in range(len(scan_number)):
            if scan_number[i] in check_list:
                number = number + scan_number[i]
                del (check_list[check_list.index(scan_number[i])])

        if len(number) == L:  # 개수가 맞는지 확인
            Form = 'T'

        else:
            print("It is not right form, input again")

    return number


# game_end 인수가 들어오긴 하지만, 내부 판단에 사용되지 않아 삭제해도 됨.
def judgement(scan_number, num):  # 판정하는 함수
    if scan_number == num:  # 숫자가 맞았을 때
        print("The number is Correct!!")
        return True

    S = 0
    B = 0
    O = L

    for i in range(3):
        if num[i] in scan_number:
            B += 1
            O -= 1

    for i in range(3):
        if num[i] == scan_number[i]:
            S += 1
            B -= 1
    print("|| S:%d  B:%d  O:%d ||" % (S, B, O))
    return False


play_again = 'yes'

while play_again.startswith('y'):
    num = make_number()
    intro()

    L = int(input("choose a cipher: "))
    game_end = False

    while not game_end:
        scan_number = scan()
        game_end = judgement(scan_number, num)

    play_again = input("Do you want to play again? (yes or no): ")
