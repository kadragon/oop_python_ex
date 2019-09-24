# the function part -----------------------
# to pick a random number for the player
import random


def ran_pick(num_digits):
    secret = ''     # a random three digit number that has no number more than once
    ran_num = str(random.randint(0, 9))  # pick a random number between 0 and 9

    for i in range(num_digits):  # to make all the numbers different
        while ran_num in secret:    # loop runs till the state is True
            ran_num = str(random.randint(0, 9))  # pick a new number that's not in 'secret' and escape the loop
        secret += str(ran_num)  # fill 'secret' with a random number from the front

    return secret


def hint(num, key_num):
    s = 0   # strike count
    b = 0   # ball count
    o = 0   # out count
    for i in range(0, 3):
        if num[i] == key_num[i]:
            s += 1
        elif num[i] in key_num:
            b += 1
        else:
            o += 1
    return 'S : ' + str(s) + ' |'+ " B : " +str(b) +' |'+ ' O : ' + str(o) + '\n'


def wrong_check(num):      # check if the player's input was blank or wrong format
    if num == ' ':
        return False
    elif num.isalpha():
        print("It should be a 3-digit 'number'!\n")
        return False
    elif num[0] == 0:
        return False
    elif len(num) != 3:
        return False
    else:
        return True


# if the player wants to continue game
def continue_game():
    return input('CONTINUE GAME? (yes or no)').lower().startswith('y')


# game part -----------------------------


NUM_DIGITS = 3
MAX_GUESS = 10
player_guess = 1

print("=" * 80)
print("** A BASEBALL NUMBER GAME **")
print("I am thinking of a %s-digit number. Try to guess what it is." % NUM_DIGITS)
print("Here are some clues:")
print("What I say = It means:")
print("Strike (S) = One digit is correct and in the right position.")
print("Ball   (B) = One digit is correct but in the wrong position.")
print("Out    (O) = No digits are correct.")
print("=" * 80)

while True:
    player_guess = 1
    secret_num = ran_pick(3)
    while player_guess <= MAX_GUESS:
        scanned = ' '
        while len(scanned) != NUM_DIGITS or not wrong_check(scanned):
            print('\nI have a 3-digit number, and you have %s guesses to get it.' % (MAX_GUESS - player_guess + 1))
            print('Guess  #%s:' % player_guess, end=' ')
            scanned = input()

        print(hint(scanned, secret_num))
        player_guess += 1

        if scanned == secret_num:
            break
        if player_guess > MAX_GUESS:   # more guesses than 10 times, game over
            print("GAME OVER \nThe answer was %s." % secret_num)

    if not continue_game():
        break
