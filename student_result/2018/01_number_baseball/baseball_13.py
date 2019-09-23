import random
import time


# 함수의 선언시 첫글자는 소문자로 시작하는 것을 권장한다.
# Introduction
def Intro():
    print("\n\nLet's start the Number Baseball Game!")
    print("-------------------------------------")
    digits = int(input("\nHow many digits would you like? \t"))
    print("\n\nLet me think of a number...\n")
    time.sleep(2)
    print("Okay!\n\n")
    return digits


# Get a number
# If the len of number is not 3 or input isn't number, repeat
def Input(trial):
    global digits
    while True:
        try:
            n = input("Trial {} \t n: ".format(trial)).replace(" ", "")

            while len(n) is not digits:
                print("You did not enter a valid number. Please try again.\n")
                n = input("Trial {} \t n: ".format(trial)).replace(" ", "")

            int(n)
            break

        # If n isn't a number repeat input
        except ValueError:
            print("You did not enter a number. Please try again.\n")

    return n


# Guess a number and grade
# Return whether to replay or not
def Guess(ans):
    trial = 1
    n = Input(trial)

    while n != ans and trial < 10:
        ball = 0
        strike = 0
        out = 0

        for i in str(ans):
            found = False

            for j in str(n):
                if i == j:
                    found = True
                    if str(ans).find(i) == str(n).find(j):
                        strike += 1
                    else:
                        ball += 1

            if not found:
                out += 1

        print("Strike: {} \t Ball: {} \t Out: {}\n".format(strike, ball, out))
        trial += 1

        n = Input(trial)

    if trial >= 10:
        print("\nGood luck next time!")
    else:
        print("\nGood Job!(*^-^*)")

    sel = input("Play again? (y/n)  ")
    return sel in ['Yes', 'Y', 'yes', 'y']


# Check if a number has no repeats
def Check(ans):
    for i in range(len(ans)):
        for j in range(len(ans)):
            if i != j and ans[i] == ans[j]:
                return False
    return True


retry = True

while retry:

    digits = Intro()
    ans = str(random.randint(10 ** (digits - 1), 10 ** digits))
    while not Check(ans):
        ans = str(random.randint(10 ** (digits - 1), 10 ** digits))
    retry = Guess(ans)

print("\nGoodbye!(^_-)~")
