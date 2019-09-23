import random

# chance = 10
# 밑에서 받을거라서 없어도..
print("how many chance you want?")
chance = input()
chance = int(chance)

print("how many number you want?")
number = input()
number = int(number)

print("Try, you have %d chance. Should get three exact %d with correct place." % (chance, number))
print("input should be like '"'int int int'"' ")
print("Pls, pls input exact amount of number")

f = random.sample(range(1, 10), number)

while chance >= 1:
    s = 0
    o = 0
    ball = 0
    r = input().split()
    i = list(range(1, 15))
    for q in range(0, number):
        i[q] = int(r[q])

    for k in range(0, number):
        for j in range(0, number):
            if i[k] == f[j]:
                if k == j:
                    s = s + 1
                else:
                    ball = ball + 1

    o = number - ball - s

    if s == number:
        print("Great you got it!!!")
        break
    else:
        print("Strike %d Ball %d Out %d" % (s, ball, o))

    chance = chance - 1
    print("Chance left = %d" % chance)

if chance == 0:
    print("You didn't got it it was...")
    print(f)
