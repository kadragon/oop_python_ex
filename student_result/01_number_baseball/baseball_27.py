"""
Title   Baseball Game
Date    2018.08.29
"""

import random

number = 0


def display_intro():
    print('-' * 68)
    print('Welcome to Baseball Game!')
    print('Guess the random number made by three different numbers from 0 to 9.')
    print('You have only 10 opportunities. Let\'s start!')
    print('-' * 68)


def get_number():
    global number

    numlist = list(range(0, 10))
    random.shuffle(numlist)
    number = numlist[:3]


def play():
    global number

    S = B = O = 0

    guessesTaken = 0
    while S != 3 and guessesTaken <= 10:
        S = B = 0
        guess = []
        # 사용자는 친절하지 않습니다ㅠ
        inp = input('Guess the random number: ')
        for i in inp:
            guess.append(int(i))
        guessesTaken += 1
        for i in range(0, 3):
            for j in range(0, 3):
                if number[i] == guess[j]:
                    if i == j:
                        S += 1
                    else:
                        B += 1
        if S == 0 and B == 0:
            print("OUT")
        else:
            print("%d S | %d B" % (S, B))
    if S == 3:
        print("Great! You did a job for %d times." % guessesTaken)
    else:
        print("Oh no! You failed for 10 times. Try again!")


play_again = True

while play_again:
    display_intro()
    get_number()
    play()
    play_again = input('Do you want to play again? (yes or no): ').lower().startswith('y')
