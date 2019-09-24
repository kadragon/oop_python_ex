import random

def makenumber():
  numlist = list(range(10))
  random.shuffle(numlist)
  a = 100*numlist[0] + 10*numlist[1] + numlist[2]

  if a < 100 :
    a = a + numlist[3] * 100
  
  return a
#랜덤 숫자 생성하기. 0~9의 숫자 배열 만들고 랜덤으로 섞은 다음
#세 자리 숫자를 만들어서 리턴


def sbobigyo(num,keynum):
  baknum = num//100
  sibnum = (num - baknum*100)//10
  ilnum = num - baknum*100 - sibnum*10

  keybaknum = keynum//100
  keysibnum = (keynum-keybaknum*100)//10
  keyilnum = keynum - keybaknum*100 - keysibnum*10
  
  returnum = 0
  #변수 설정

  if baknum == sibnum or baknum == ilnum or sibnum == ilnum or baknum >= 10:
    raise Exception

  if baknum == keybaknum:
    returnum = returnum + 100
  elif baknum == keysibnum or baknum == keyilnum:
    returnum = returnum +10
  else:
    returnum = returnum + 1
  #첫번째 자리 비교

  if sibnum == keysibnum:
    returnum = returnum + 100
  elif sibnum == keybaknum or sibnum == keyilnum:
    returnum = returnum +10
  else:
    returnum = returnum +1
  #두번째 자리 비교

  if ilnum == keyilnum:
    returnum = returnum + 100
  elif ilnum == keybaknum or ilnum == keysibnum:
    returnum = returnum +10
  else:
    returnum = returnum +1
  #세번째 자리 비교
  
  return returnum
  #정답과 입력 값을 비교하여 스트라이크, 볼, 아웃의 개수를 찾는 함수


def gurlgwa(keynum):
  if keynum == 300:
    print("우효 겟또다제!")
    return 1
  #넘겨 받은 keynum을 통해 s, t, o를 확인, s==3이면 성공 표시하고
  #한 판을 종료하기 위해 1을 리턴한다
  
  else:
    st = keynum//100
    ball = (keynum - st*100)//10
    out = keynum - st*100 - ball*10
    #print(keynum)
    print('S : ',st, ' B : ', ball, ' O : ', out)
    return 0
  #sbobugyo에서 나온 값으로 정답의 여부와 스트라이크, 볼, 아웃 
  #개수를 출력

def sijak():
  st = 0
  ball = 0
  out = 0
  keynum = makenumber()
  #print(keynum)

  for i in range(10):
    try:
      num = int(input())
      if gurlgwa(sbobigyo(num, keynum)) == 1:
        break
      #만약 숫자를 모두 맞추면 1이 리턴되고, 반복문이 종료된다.

    except Exception:
      print("너는 기회를 하나 잃었다 이말이야! 다시 입력해라! (남은기회 : ", 9-i, ")")

  print("다시 할꺼? (할꺼면 y / 안 할꺼면 n")
  dedap=input()

  if dedap == "y":
    sijak()
  elif dedap =="n":
    print("ㅅㄱㅂㅇ")
  else:
    print("이것도 똑바로 못 쓰네? ㅅㄱㅂㅇ")
  #게임을 다시할지 선택한다. 이상한걸 입력하면 뭐라그러고 끝내버린다.

print("빠밤! 숫자야구다 이말이야!! 세 자리 숫자를  입력해라\n")
print("숫자와 자리수가 모두 맞으면 스트라이크!\n")
print("숫자는 맞지만 자리가 다르면 볼!!\n")
print("숫자랑 자리 둘 다 틀리면 아웃!!!\n")
print("이제 세 자리 숫자를 입력해! (각 자리 숫자는 모두 달라야 됨. 기회는 10번)\n")

sijak()