import random # random 함수를 쓰기 위해 import 한다.
 
def shuffle(): # 정답이 되는 랜덤의 세 자리 수를 생성하는 함수 이다.
  ten = list(range(10)) # 0~9의 배열을 생성한다.
  random.shuffle(ten) # 0~9가 들어있는 배열을 섞는다.
  target = ten[0] * 100 + ten[1] * 10 + ten[2] # 타겟을 세자리 정수로 만든다
  return target # 그래서 랜덤한 세자리 수가 된 타깃을 반환
 
def play_game(guess, target): # 스트라이크, 볼, 아웃 수를 알려주는 함수이다.
  if guess == target:
    return '정답입니다!' # 만약 정답이면 '정답입니다!'를 외친다.
  strike = 0 # 값을 0으로 초기화 한다.
  ball = 0 # 값을 0으로 초기화 한다.
 
  guess_list = list(range(3)) # 플레이어가 예측한 수 또한 세자리의 형태로 만들기 위해 배열을 생성한다.
  guess_list[0] = int(guess / 100) # 예측한 값의 100의 자리를 넣는다.
  guess_list[1] = int((guess - guess_list[0] * 100) / 10) # 예측한 값의 10의 자리를 넣는다.
  guess_list[2] = int(guess % 10) # 예측한 값의 1의 자리를 넣는다.
 
  target_list = list(range(3)) # 세자리 정수인 타겟을 예측한 수와 하나하나 대응하기 위해 배열을 생성산다.
  target_list[0] = int(target / 100) # 타겟의 100의 자리를 넣는다.
  target_list[1] = int((target - target_list[0] * 100) / 10) # 타겟의 10의 자리를 넣는다.
  target_list[2] = int(target % 10) # 타겟의 1의 자리를 넣는다.
 
  for i in range(3):
    for j in range(3): # 예측값과 타겟의 각 자리수를 대응하기 위해 for문을 두개 돌린다.
      if guess_list[i] == target_list[j] and i == j:
        strike += 1 # 만약 자리수와 숫자 모두 동일하면 스트라이크 처리한다.
      elif guess_list[i] == target_list[j]:
        ball += 1 # 만약 자리수는 같이 않으나 동일한 숫자가 존재할 경우 볼로 처리한다.
  out = 3 - strike - ball # 아웃은 항상 3에서 스트라이크와 볼을 뺀 값일 것이다.
 
  return str(strike) + 'S | ' + str(ball) + 'B | ' + str(out) + '0\n' # 스트라이크, 볼, 아웃의 수를 문자열로써 리턴한다.
 
def alphabet(): # 정수 이외의 값이 입력 될 때 받아치는 함수를 만든다. 쌤거 따라했는데 제 코드랑은 맞지 않나봐요..ㅠ
  for i in range(3): # for문을 세 번 돌린다.
    if int(i) not in list(range(0, 10)): # 0부터 9사이의 값인지 확인한다.
      return False # 아니면 False를 리턴하여 실행을 못하게 한다.
 
  return True # 이상없으면 True를 리턴한다.
 
def retry(): # 다시 플레이 할 것인지를 물어보는 함수를 만든다.
  return input('다시 플레이 하시겠습니까? (진심 붙이세요)').lower().startswith('진심') # 진심을 붙이면 다시 플레이하게 해준다.
 
limit = 10 # 한계 도전횟수를 10번으로 한다.
 
print("=" * 50)
print(" \n 숫자 야구 게임을 시작합니다 \n 첫 번째 숫자는 1부터 9까지 입력가능합니다.(쉬운 난이도) \n 제발 숫자 이외의 것을 입력하지 마세요. 경고합니다\n") # 시작하는 말
print("=" * 50)
 
while True: # while문을 돌린다.
  go = shuffle() # 타겟이 되는 랜덤한 수를 따로 저장한다.
  print('%s 번의 기회가 남았습니다' % limit) # 몇 번의 기회가 남았는지 알려준다.
 
  chance = 1 # 1로 초기화한 정수를 하나 만든다.
  while chance <= limit: # 조금씩 커지다가 10번 이상이 되면 그만하도록 설정한다.
    guess = ' ' # 플레이어의 예측값을 받는곳을 만든다.
    while len(str(guess)) != 3 or not alphabet(): # 세자리 받으면 while을 돌린다.
      print('세자리 숫자를 입력하세요') # 친철하게 알려준다.
      guess = int(input()) # 플레이어의 예측값을 입력받는다.
    print(play_game(guess, go)) # 예측값을 받았을 때 결과를 알려준다.
    chance += 1 # 찬스 1번을 날린다.
 
    if guess / 100 == go / 100 and (guess - (guess / 100) * 100) / 10 == (go - (go / 100) * 100) / 10 and guess % 10 == go % 10:
      break # 만약 정답이면 while을 탈출한다.
    if chance > limit:
      print('아쉽네요. 정답은 %s 입니다.' % go) # 답이 틀렸으면 끝내고 정답을 알려준다.
  
  if not retry():
    break # 재도전을 신청하지 않으면 게임을 끝낸다.
 
 
 
 

