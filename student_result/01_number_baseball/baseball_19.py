# making a baseball game!
# 20180829 Object-Oriented Programming class

import random

life = 10
a = b = c = 0
t1 = t2 = t3 = 0


def inputcheck(t):
    global t1, t2, t3

    # 0 으로 시작하는 3자리는 만들어 지지 않음
    if t < 100 or t >= 1000:
        print("Please type a three-digit number")
        return 0

    t1 = t // 100
    t2 = (t % 100) // 10
    t3 = t % 10

    if (t1 == t2) or (t2 == t3) or (t3 == t1):
        print("Please type non-overlapped numbers")
        return 0


def compare(t1, t2, t3):
    global a, b, c

    scnt = 0
    bcnt = 0
    ocnt = 0

    test_list = [t1, t2, t3]
    ans_list = [a, b, c]

    for i in range(3):
        if test_list[i] == ans_list[i]:
            scnt += 1
        elif test_list[i] in ans_list:
            bcnt += 1
        else:
            ocnt += 1

    return scnt * 100 + bcnt * 10 + ocnt


def make_quest():
    global a, b, c

    quest = list(range(1, 10))  # default 가 1이라서 빼 먹어도 됨
    random.shuffle(quest)

    a = quest[0]
    b = quest[1]
    c = quest[2]


make_quest()

while 1:
    print("Guess a non-overlapped, three-digit number:")
    tlist = int(input())
    result = inputcheck(tlist)
    if result == 0:
        continue

    result = compare(t1, t2, t3)
    if result // 300 == 1:
        print("Congratulations! You made three strikes!")
        print("Do you want to play again?[Y/N]")
        replay = input()
        if replay.lower() == 'y':
            make_quest()
            life = 10
            continue
        else:
            break
    elif life == 1:
        print("Sorry! You've used all of your chances. Game over.")
        print("The answer was :", a, b, c)
        print("Do you want to play again?[Y/N]")
        replay = input()
        if replay.lower() == 'y':
            make_quest()
            life = 10
            continue
        else:
            break
    else:
        print(result // 100, " S  | ", (result // 10) % 10, " B  | ", result % 10, " O")
        life -= 1
        print("life : ", life)
        continue
