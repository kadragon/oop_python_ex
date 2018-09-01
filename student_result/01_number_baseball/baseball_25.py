"""
Project    숫자야구 만들기
Author     지명금
Date       2018.08.27
"""
import random

TEXT_LINE = 70

gameTaken = 10
guessTaken = 1
numtotal = 3
num_list = []

def get_random_number():
    """
    랜덤으로 중복되지 않게 숫자 3개를 선택하여 list형태로 반환하는 함수
    return -> random number list
    """
    num_get = list(range(10))
    random.shuffle(num_get)
    return num_get[:numtotal]
    
def game_intro():
    """
    숫자야구게임에 대해서 설명해주는 함수
    """
    print("-"*TEXT_LINE)
    print("""
    Now you are going to play number-baseball
    You are going to guess %d numbers(Be careful not to overlap)
    (S) : when your number and index is correct
    (B) : when only your number is correct
    (O) : when you guess the wrong number and index
    """ % numtotal)
    print("-"*TEXT_LINE)

def get_guess():
    """
    사용자에게 숫자 3개를 입력받아서 맞게 입력됬는지 확인하는 함수
    확인사항 :
    1) 숫자끼리 서로 중복되는지 확인
    2) 숫자가 아닌 다른것을 입력했는지 확인
    """
    while True:
        user_list = []
        user_guess = input("Guess#%d: "%guessTaken)
        if len(user_guess)==0 or len(user_guess)<numtotal :
            print("Aren't you going to play a game? TRY AGAIN")
            continue
        
        for i in range(len(user_guess)):
            user_list += user_guess[i]

        user_list = [ item for item in user_list if item != ' ']
        if len(user_list)>numtotal:
            print("Aren't you going to play a game? TRY AGAIN")
            continue
        
        print(user_list)
        
        check_same = False
        for i in range(numtotal):
            for j in range(numtotal):
                if i<=j: continue
                if user_guess[i] ==  user_guess[j]:
                    check_same = True
                    break

        check_number = True
        for i in user_list:
            if not('0'<=i and i<='9'):
                check_number = False
                
        if check_same == True:
            #print("Your number have been overlap! TRY AGAIN")
            print("Aren't you going to play a game? TRY AGAIN")
        elif check_number == False:
            #print("You should give a number! TRY AGAIN")
            print("Aren't you going to play a game? TRY AGAIN")
        else:
            user_list = [ int(item) for item in user_list]
            return user_list
                    

def check_S(user_guess,number_list):
    """
    스트라이크의 수를 계산해서 반환하는 함수
    input  -> user_guess  : 사용자가 입력한 숫자 리스트
           -> number_list : 맞춰야 하는 숫자 리스트
    return -> s : 스트라이크의 수
    """
    s = 0
    for i in range(numtotal):
        if user_guess[i] == number_list[i]:
            s += 1

    return s

def check_B(user_guess,number_list):
    """
    볼의 수를 계산해서 반환하는 함수
    input  -> user_guess  : 사용자가 입력한 숫자 리스트
           -> number_list : 맞춰야 하는 숫자 리스트
    return -> b : 볼의 수 
    """
    b = 0
    for i in range(numtotal):
        for j in range(numtotal):
            if i!=j and user_guess[i] == number_list[j]:
                b+=1
    return b    
        
def check_guess(user_guess,number_list):
    """
    사용자의 입력과 맞춰야 하는 리스트를 계산해서 결과를 출력해주고 스트라이크의 수를 반환하는 함수
    input  -> user_guess  : 사용자가 입력한 숫자 리스트
           -> number_list : 맞춰야 하는 숫자 리스트
    return -> s : 스트라이크의 수 
    """
    s = check_S(user_guess,number_list)
    b = check_B(user_guess,number_list)
    o = numtotal - (s+b)
    print("%d S | %d B | %d O" % (s,b,o))
    return s

playagain = True
game_intro()
numbers = get_random_number()
while playagain == True:
    guessTaken = 1
    while guessTaken <= gameTaken:
        
        user_guess = get_guess()
        result = check_guess(user_guess,numbers)
        if result == numtotal:
            print("Wow you are correect! you have guess in %d time!" % gameTaken)
            break
        if guessTaken == gameTaken and result != numtotal:
            print("You have FAILED! the number was "+ str(numbers) +"!")
            
        guessTaken += 1
    playagain = input("Will you play AGAIN? [y/n] ")
    playagain = True if playagain == 'y' else False
    print(playagain)
    

