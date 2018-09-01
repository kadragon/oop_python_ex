import random
from time import sleep

# getNumber(): returns a 3-digit number in the form of list.

DIGITS = 4


def getNumber():
    # makes a list containing 0 to 9(It's a string!).
    numList = list(map(str, range(0, 10)))
    while numList[0] == '0':  # avoid the first digit being 0!
        random.shuffle(numList)  # shuffles the list.
    # returns the first "DIGITS" elements of the list.
    return numList[:DIGITS]

# ItoL(): converts string to list.
# Params:
# guess: The number to be converted.


def ItoL(guess):
    # returns a list with each digits seperated.
    list = []
    for i in range(0, DIGITS):
        list.append(guess[i])
    return list

# Intro(): Shows player intro


def Intro():
    showList = ['='*40+'\nWelcome to the Number baseball game!\n'+'='*40,
                '<How to play>',
                'You must guess a %d-digit number.' % DIGITS,
                'Every time when you guess, you get a hint',
                '\"Out\" Means that your guess has no common number with the answer',
                '\"Ball(B)\" Means the number of digits in your guess that is contained in the answer, but with different place.',
                '\"Strike(S)\" Means the number of digits in your guess that is contained in the answer with same place',
                'Now let the game begin!']
    # ShowList: list of strings to be shown to the player.
    for lines in showList:
        print(lines)
        sleep(1.5)
        # Prints each element in ShowList with 2-seconds delay.

# getInput(): gets Input from the player and returns in int form.


def getInput():
    guess = input('Guess the number!: ')
    if guess.isdigit():  # if guess is numeric:
        if len(guess) != DIGITS:  # if is not a "DIGITS"-digit number
            print('Enter a %d-digit number.' % DIGITS)
            return ''  # returns a blank string if input failed
        else:
            return guess  # returns guess
    else:
        print('Enter a number.')
        return ''


# Intro()

while True:
    ans = getNumber()
    guess = ''

    print(ans)

    while guess == '':
        guess = getInput()  # get correct input from the player.

    while ans != ItoL(guess):  # while the input and the answer is not same:
        strike = 0
        ball = 0
        guessList = ItoL(guess)  # convert input to list.
        for i in range(0, DIGITS):
            if guessList[i] == ans[i]:  # if has same digit and same position:
                strike += 1  # It's a strike!
            elif guessList[i] in ans:  # else if It's just contained:
                ball += 1  # It's a ball!
        if strike == 0 and ball == 0:
            print('Out!')  # It's out if there's neither strike or ball
        else:
            # prints srtike and ball, if there's any.
            print("%dS " % strike if strike > 0 else '', end='')
            print("%dB " % ball if ball > 0 else '')
        guess = getInput()  # get more Inputs!
    print("You've got it! the answer was %s!" % guess)
    re = ''
    while re == '':  # Repeat until it gets desired result.
        # Ask if the player wants to play again
        replay = input('Do you want to play it again?(Yes/No): ')
        if 'y' in replay.lower():
            re = True
        elif 'n' in replay.lower():
            re = False
        else:
            print('Please answer yes or no.')
    if not re:
        break
