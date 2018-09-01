import random

# 사용자는 제대로 입력하지 않을 때가 있습니다..!
while True:
    a = list(range(10))
    random.shuffle(a)

    while True:
        b = int(input("guess the number : "))

        b1 = b // 100
        b2 = (b - b1 * 100) // 10
        b3 = b % 10
        sc = 0
        bc = 0

        if b1 == a[0]:
            sc += 1

        elif b1 == a[1] or b1 == a[2]:
            bc += 1

        if b2 == a[1]:
            sc += 1

        elif b2 == a[0] or b2 == a[2]:
            bc += 1

        if b3 == a[2]:
            sc += 1

        elif b3 == a[0] or b3 == a[1]:
            bc += 1

        if sc == 3:
            break

        if sc + bc == 0:
            print("OUT!!")
            continue

        print("%d S %d B" % (sc, bc))

    print("STRIKE!!")

    again = input("Do you want to play again? (Y/N)")

    if again == 'Y':
        continue

    elif 1:
        break
