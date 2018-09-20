import random

OXJudge = ['  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ']

def DefaultField():
    print("""
    --------------
     1  | 2  | 3  
    ______________
     4  | 5  | 6  
    --------------
     7  | 8  | 9  
    --------------
    """)

def PrintResult():
    global OXJudge
    print("""
    --------------
     %s | %s | %s 
    ______________
     %s | %s | %s 
    --------------
     %s | %s | %s 
    --------------
    """ %(OXJudge[0], OXJudge[1], OXJudge[2],OXJudge[3],OXJudge[4],OXJudge[5],OXJudge[6], OXJudge[7], OXJudge[8]))


print('피치 못할 사정이 있어 완성하지 못했습니다')
