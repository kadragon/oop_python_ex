"""
Title Number Baseball
Date 2018.08.29
"""

import random

num = list(range(10))


def intro():
    print("=" * 80)
    print("Welcome to the number baseball game!")
    print("A strike means that you've gotten your number and it's position right.")
    print("A ball means that you've only gotten your number right.")
    print("An out means that your guess is wrong")
    print("=" * 80)


def num_generate():
    random.shuffle(num)  # num 을 여기서만 사용한다면, 바로 list(range(10)) 을 넣는 것이


def get_num():
    global chk  # global 을 사용할 것이라면, 함수 최상단에 명시해주자.

    while True:
        check = 0
        tmp = input("Guess the Numbers I'm thinking of ").split()
        for i in range(0, len(tmp)):
            if tmp[i] < '0' or tmp[i] > '9':
                print("Please type the answer again")
                check = 1
                break

        if check == 1:
            continue

        get = list(map(int, tmp))

        chk = list(get)
        if len(get) != 3:
            print("Please type the answer again")
            check = 1

        for i in get:
            if i >= 10 or i < 0:
                print("Please type the answer again")
                check = 1
                break

        if check == 0:
            break


def play_again():
    return input('Do you want to play again? (Press Y to play again) ').lower().startswith('y')


intro()

cnt = 0
num_generate()

while True:
    st = 0
    ba = 0
    ou = 0
    get_num()
    for i in range(0, 3):
        if chk[i] == num[i]:
            st += 1
            chk[i] = 10

    for i in range(0, 3):
        for j in range(0, 3):
            if chk[i] == num[j]:
                ba += 1
    ou = 3 - (st + ba)
    cnt += 1

    if st == 3:
        print("You Successfully Guessed the Number! It was %d %d %d" % (num[0], num[1], num[2]))
        if play_again():
            st = 0
            ba = 0
            ou = 0
            cnt = 0
            num_generate()
            get_num()
        else:
            break

    if cnt > 10:
        print("You failed to get the right number It was %d %d %d" % (num[0], num[1], num[2]))
        if play_again():
            st = 0
            ba = 0
            ou = 0
            cnt = 0
            num_generate()
            get_num()
        # st, ba, ou, cnt, num_generate(), get_num() 을 초기화 하는 것은 한번에 묶어서 처리하자.

    print("%d Strikes || %d Balls || %d Outs" % (st, ba, ou))
