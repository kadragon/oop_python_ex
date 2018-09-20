import random
text=11
a=[' ',' ',' ',' ',' ',' ',' ',' ',' ']
check1=[1,2,3,4,5,6,7,8,9]
def print_result():
    print('-'*text)
    print(" %c | %c | %c" %(a[0],a[1],a[2]))
    print('-'*text)
    print(" %c | %c | %c" %(a[3],a[4],a[5]))
    print('-'*text)
    print(" %c | %c | %c" %(a[6],a[7],a[8]))
    print('-'*text)
def input_char(c,d):
    while True:
        c = input()
        if(c!='X' and c!='O'):
            print("다시 입력좀")
        else:
            if(c=='X'):
                d='O'
                break
            if(c=='O'):
                d='X'
                break

def user(k):
    while True:
        b=int(input())
        if(1<=b<=9): break
        else: print("다시 입력좀")
    a[b-1]=c
    del check1[b-1]
#    print(check1)
def check(win):
    win=0
    if(a[0]==a[1] and a[1]==a[2]): win+=1
    if(a[3]==a[4] and a[4]==a[5]): win+=1
    if(a[6]==a[7] and a[7]==a[8]): win+=1
    if(a[0]==a[3] and a[3]==a[6]): win+=1
    if(a[1]==a[4] and a[4]==a[7]): win+=1
    if(a[2]==a[5] and a[5]==a[8]): win+=1
    if(a[0]==a[4] and a[4]==a[8]): win+=1
    if(a[2]==a[4] and a[4]==a[6]): win+=1
def com(l):
    e=random.choice(check1)
    a[e-1]=d
    check1.remove(e)
 #   print(check1)
win=0
c=0
d=0
print_result()
input_char(c,d)
user(c)
print(c)
com(d)
print(a)
print_result()
check(win)
print(win)