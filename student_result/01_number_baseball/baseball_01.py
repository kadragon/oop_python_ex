# number baseball game
import random

NUMBER_LENGTH=4 # 1<N<=10
GUESS_CHANCE=10 # 1<M

# Check duplicate. (Parameter: int, Return: Boolean)
def duplicate(x):
    numbers=[0,1,2,3,4,5,6,7,8,9]
    for i in range(NUMBER_LENGTH):
        if x%10 in numbers:
            numbers.remove(x%10)
            x=x//10
        else:
            return True
    return False


# Make answer. (Parameter: X, Return: answer(3 digit int))
def make_answer():
    ans_list=[0,1,2,3,4,5,6,7,8,9]
    random.shuffle(ans_list)
    ans_list=ans_list[:NUMBER_LENGTH]
    return ans_list

# Get number from user. (Parameter: X, return: answer list)
def get_number():
    while True:
        try:
            a=input("Guess a number. ").replace(" ","")
            if(len(a)!=NUMBER_LENGTH):
                print("Check the length of your input. (Length)")
                continue
            a=int(a)
            if duplicate(a):
                print("Choose another number. (Duplicate)")
                continue
        except ValueError:
            print("Please input an integer. (String)")
            continue
        x=[]
        for i in range(NUMBER_LENGTH):
            x.append(a%10)
            a=a//10
        x.reverse()
        return x

# Compare user's guessing and answer. (Parameter: answer and guessing(list), return: Boolean)
def compare(ans_list,guess):
    strike=0
    ball=0
    out=0
    for i in range(NUMBER_LENGTH):
        k=guess[i]
        if k not in ans_list:
            out+=1
        else:
            if k==ans_list[i]:
                strike+=1
                continue
            else:
                ball+=1
    print("%dS %dB %dO" %(strike,ball,out))
    return (strike==NUMBER_LENGTH)

# Ask user of playing again. (Parameter: X, Return: Boolean)
def ask_play_again():
    return input("Do you want to play again? (Y/N) ").lower().startswith("y")

# Explain Rules. (Parameter: X, Return: X)
def tutorial():
    print("Welcome to number baseball game!")
    print("You should guess %d digit number with the clues." %NUMBER_LENGTH)
    print("You have %d opportunities to guess." %GUESS_CHANCE)
    print("[Strike]: The number of correct digits")
    print("[Ball]: The number of misplaced digits")
    print("[Out]: The number of wrong digits")
    print("-"*30)

tutorial()
play_game=True
while play_game:
    game_clear=False
    ans_list=make_answer()
    for i in range(GUESS_CHANCE):
        print("%d:" %(i+1), end=" ")
        game_clear=compare(ans_list,get_number())
        if game_clear:
            break
    if game_clear:
        print("Congratulations! You've got the answer.")
    else:
        print("The answer was", ans_list)
    play_game=ask_play_again()
