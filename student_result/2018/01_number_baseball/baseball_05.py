import random

explain = '''
             <숫자야구게임>

사용되는 숫자는 0에서 9까지 서로 다른 숫자이다.

숫자는 맞지만 위치가 틀렸을 때는 볼.

숫자와 위치가 전부 맞으면 스트라이크.

숫자와 위치가 전부 틀리면 아웃. 

물론 무엇이 볼이고 스트라이크인지는 알려주지 않는다.

중복 숫자는 없다.
'''

print(explain)

inputLength = int(input("Length of Number: "))


def get_num() -> str:
    while True:
        numList = list(map(str, range(10)))
        random.shuffle(numList)
        newNumber = numList[:inputLength]
        if newNumber[0] == '0':
            continue
        else:
            break
    ret = ''.join(newNumber)
    return ret


def compare(secretNumber, inputNumber) -> dict:
    ret = {'S': 0, 'B': 0, 'O': 0}
    length = len(inputNumber)
    for i in range(length):
        a = inputNumber[i]
        if a in secretNumber:
            if inputNumber[i] == secretNumber[i]:
                ret['S'] += 1
            else:
                ret['B'] += 1
        else:
            ret['O'] += 1

    return ret


while True:
    secretNumber = get_num()
    i = 0
    flag = False

    for i in range(10):
        while True:
            inputNumber = input("Guess a number: ")
            if len(inputNumber) != inputLength:
                print("Error, type again")
                continue
            check = int(inputNumber)
            try:
                break
            except ValueError:
                print("Error, type again")
                continue

        info = compare(secretNumber, inputNumber)
        if info['S'] == inputLength:
            print("You got it!", end='\n')
            flag = True
            break

        else:
            print("%d Strike, %d Ball, %d Out" % (info['S'], info['B'], info['O']))

    if flag is False:
        print("Fail, the answer was %d." % (int(secretNumber)), end='\n')  # end='\n' 기본값이기 때문에 안해도 된다.

    tryAgain = input("Try again?(Yes/No)")
    if tryAgain == 'Yes':
        continue
    elif tryAgain == 'No':
        break
    else:
        exit()
