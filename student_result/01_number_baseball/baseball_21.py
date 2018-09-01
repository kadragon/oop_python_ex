import random


#generate random number
def generateAns():
    buf = list(range(10))
    random.shuffle(buf)
    return buf[0:NUMBERS]


def check_input(buf):
    if len(buf)!=NUMBERS:
        return True

    cnt = 0
    for i in "0 1 2 3 4 5 6 7 8 9".split():
        if i in buf:
            cnt+=1

    #print(cnt)
            
    if cnt!=NUMBERS:
        return True

    return False


def user_in():
    buf = input().split()
    while check_input(buf):
        print("Input Error: Try it again")
        buf = input().split()
    return buf

def judge(user,answer):

    strike = 0
    ball=0;
    for i in range(NUMBERS):
        if int(user[i])==answer[i]:
            strike+=1
        if int(user[i]) in answer:
            ball+=1

    if strike==NUMBERS:
        print("%d Strikes. Congrats" % NUMBERS)
        return True
    if ball==0:
        print("Out")
    else:
        print("%dS %dB" %(strike,ball-strike))
    


#main

TRY_OUT = 100
NUMBERS = 9

answer = generateAns()
#print(answer)

print("""Number BaseBall Game\n\n
You have %d Chances to guess
Input Example:"""% TRY_OUT, end="" )
for i in range(NUMBERS):
    print("%d" % i,end=" ")
print("")

flag = 0
for i in range(TRY_OUT):
    print("\nGuess #%d" % int(i+1))
    user = user_in()
    if judge(user, answer):
        flag = 1
        break
    
if flag == 0: print("\nWrong\nAnswer was "+str(answer))

print("\nEnd of Game")
    

