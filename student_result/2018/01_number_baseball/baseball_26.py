import random

b = "0 1 2 3 4 5 6 7 8 9".split()
random.shuffle(b)
c = 0
d = ['0', '0', '0']

print('=' * 40)
print("""
GAME START
""")
print('=' * 40)

for i in b:
    if c < 3:
        d[c] = i
        c += 1
    else:
        break


def gameplay():
    inning = 0
    while True:
        if inning == 10:
            print("OVER 9 INNING. YOU LOSE")
            break
        strike = 0
        ball = 0
        out = 0
        while True:
            flag = 0
            a = input()
            if a[0] == a[1] or a[0] < '0' or a[0] > '9':
                flag = 1
            if a[0] == a[2] or a[1] < '0' or a[1] > '9':
                flag = 1
            if a[1] == a[2] or a[2] < '0' or a[2] > '9':
                flag = 1
            if len(a) > 3 or count != 0:  #
                print("INPUT EXAMPLE) 481")
            else:
                break

        inning += 1
        j = 0

        while j < 3:
            x = 0
            for k in d:
                if a[j] == k:
                    break
                else:
                    x += 1

            if x == 3:
                out += 1

            elif x == j:
                strike += 1

            elif x != j:
                ball += 1

            j += 1

        if strike == 3:
            print("GREAT")
            break
        else:
            print('%d S %d B %d O' % (strike, ball, out))


again = 'yes'

while again == 'yes' or again == 'y':
    print("")
    gameplay()
    again = input('TRY AGAIN?(yes / no): ')
