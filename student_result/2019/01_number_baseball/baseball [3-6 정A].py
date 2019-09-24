import random

Flag = False  # Flag 는 Strike 이 3일때 for 문을 끝내기 위해 사용한다.
print("DoYoung's BaseBall Game!!!\n"
      "Guess the unknown number in ten chances.\n"
      "unknown number is composed with three different number 0 to 9\n"
      "You can't type other than the numbers from 0 to 9.\n"
      "Also you can't type the same number over and over again.\n"
      "If you write wrong number, you will miss a chance")
print("=" * 40)


# check 함수 : 입력받은 값이 서로 다른 3개의 숫자인지 판별하는 함수
# 올바르게 숫자를 입력하면 Strike / Ball / Out 값을 알려주고
# 조건에 맞게 입력하지 않으면 잘못된 숫자를 입력했다는 문구를 띄운다.
def Check(x):
    number = list(range(10))
    tmp = 0
    try:
        for i in range(len(x)):
            if int(x[i]) in number:
                number.remove(int(x[i]))  # 같은 숫자가 입력되는 것을 막기 위해 list 에서 제거
                tmp += 1
        if tmp == 3:
            return True
        else:
            print("You write wrong number You missed a chance!")
            print("=" * 40)
            return False

    except Exception:
        print("You write wrong number You missed a chance!")
        print("=" * 40)
        return False


# Ask 함수 : 게임을 다시 할 것인지 묻는 함수. True 또는 True 를 반환한다.
def Ask(ask):
    if ask == 'Y':
        return True
    if ask == 'N':
        return False
    else:
        print("Please Type Y or N\nWant to play again?\nY/N")
        askagain = input()
        return Ask(askagain)


# 입력받은 값이 서로 다른 3개의 숫자일 때 Strike, Ball, Out 의 결과를 알려주는 함수
def result(x):
    global Flag
    Strike = 0
    Ball = 0
    Out = 0
    for i in range(3):
        for j in range(3):
            if x[i] == UnknownNumber[j]:
                if i == j:
                    Strike += 1
                # if i != j:
                else:
                    Ball += 1
            Out = 3 - Strike - Ball
    if Strike == 3:
        Flag = True

    print("Strike %d" % Strike, "Ball %d" % Ball, "Out %d" % Out)


while True:
    number = list(range(10))  # 0부터 9까지 저장된 number 라는 list 를 만든다.
    random.shuffle(number)  # 임의로 number 의 순서를 섞는다.
    Flag = False  # 게임이 다시 시작됬을 때를 고려해 Flag 를 False 로 초기화 한다.
    UnknownNumber = ""

    for i in number[:3]:
        UnknownNumber += str(i)  # 랜덤으로 섞은 number 리스트에서 앞의 값 3개를 뽑아 미지의 수를 UnknownNumber 로 저장한다.

    Chance = 10

    for i in range(Chance):
        print("Your left chance : %d" % Chance)
        print("Guess the unknown number!")
        a = input()  # 플레이어가 값을 입력한다.
        if Check(a):  # Check 함수를 호출하여 서로 다른 숫자 3개를 입력했는지 확인하고
            result(a)
            if Flag:  # Strike == 3 을 만족했을 때 for 문을 탈출한다.
                break
            print("=" * 40)
        Chance -= 1  # 서로 다른 숫자 3개를 입력한 것이 아니라면 기회를 -1 한다.

    if Flag:  # 3자리 숫자를 맞추면 축하해주는 문구와 함께 Ask 함수를 호출하여 게임을 다시 할 것인지 묻는다.
        print("You won the game! Congratulation!!!")
        print("Want to play again?\nY/N")
        winner = input()
        if Ask(winner):
            break

    if Chance == 0:  # 기회를 모두 사용하면 Ask 함수를 호출하여 게임을 다시 할 것인지 묻는다.
        print("You Used All Chances. You Lose...")
        print("Want to play again?\nY/N")
        loser = input()
        if Ask(loser) is False:
            break
