import random


class BALL:  # 본인이 입력한 숫자에 대한 정보를 담은 클래스를 따로 선언
    def __init__(self, numberlist, randlist):
        self.randlist = randlist  # randlist 는 랜덤하게 만든 세자리수
        self.nlist = numberlist   # nlist 는 입력한 세자리수
        self.SB = self.checking()  # 입력한 수가 S와 B에 몇개가 해당하는가?

    def checking(self):  # S가 몇개인가 B가 몇개인가 아웃인가?
        S = 0
        B = 0
        for i in range(len(self.nlist)):
            if self.nlist[i] == self.randlist[i]:  # 자리와 수가 모두 같다면
                S += 1  # S의 수는 하나 증가하게 되며
                continue  # 더 고려할 필요 없으니 컨티뉴
            for q in range(len(self.randlist)):  # 자리와 수가 모두 같지않다면
                if self.nlist[i] == self.randlist[q]:  # 일단 랜덤하게 선택된 수열과 일치하는 부분이 있다면
                    B += 1  # B의 수가 하나 증가하게된다.
        return [S, B]  # 이로써 S의 개수와 B의 개수가 나타난다.


def check(numlist):   # 리스트를 받아 입력이 조건에 맞는지 검사한다. 조건에 맞지않는다면 False 를 리턴한다.
    randnumlists = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']  # 들어갈 수 있는 수들이 모두 들어있는 리스트

    if len(numlist) != 3:  # 3개의 숫자가 입력되었는가부터 확인한다.
        return False

    for i in range(3):
        iffind = -1  # 3개가 딱 들어왔다면 이제 그 셋이 숫자인지 체크해야한다.
        for q in range(len(randnumlists)):
            if randnumlists[q] == numlist[i]:
                iffind = 1
        if iffind < 0:  # 셋중 하나라도 숫자에 해당하지 않는다면 False를 반환한다.
            return False

    if numlist[0] == numlist[1] or numlist[1] == numlist[2] or numlist[0] == numlist[2] :
        return False
    return True
    # 세번째 if는 numlist중 겹치는 항목이 있는지 검사한다 겹치는 항목이 있다면 False 를 출력한다.


def createrandlist():  # 무작위 세자리 수를 생성하는 함수
    numberlist = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']  # 중복없는 0부터 9까지의 문자열을 만든다.
    random.shuffle(numberlist)  # 이 리스트를 섞으면 랜덤수열이 될것이다
    randomlist = numberlist[0:3]  # 이중 앞 세개를 뽑아내면 중복없는 랜덤 3개의 숫자가 된다.
    return randomlist


if __name__ == '__main__':
    print("=" * 30)
    print("\n다음 프로그램은 숫자야구 게임을 위한 프로그램입니다.")
    print("규칙은 다음과 같습니다.")
    print("    1. 본 게임은 컴퓨터가 중복되지 않는 3개의 수로 만든 세자리수를 맞추는것을 목표로 하는 게임입니다.")
    print("    2. 중복하지 않은 숫자로 이루어진 3자리 숫자를 입력하며, 이후 컴퓨터가 그 숫자에 대한 정보를 알려줍니다")
    print("    3. S는 자리와 크기가 같은 수의 개수를 나타내며, B는 크기는 같으나 자리가 다른 수의 개수를 나타냅니다. 같은 수가 없다면 Out 이 출력됩니다.")
    print("    4. 총 10번의 기회가 주어지며 기회가 모두 소모될 때까지 3S를 완성하면 승리합니다.")
    print("\n첫판은 자동으로 시작됩니다.")
    yesorno = 'Y'  # Y냐 N 이냐 로 계속 플레이 여부를 나눈다.
    while yesorno is 'Y':
        print("=" * 30)
        print("\n숫자야구 게임을 시작하겠습니다. ")
        randnumlist = createrandlist()
        FS = 'Fail'
        print("무작위 세자리수가 결정되었습니다")

        trylist = list()
        while len(trylist) < 10:  # 올바른 숫자열 한번당 trylist에 원소가 하나씩 추가되므로 10번의 기회를 주는것과 같다
            print("\n숫자열을 입력해 주십시오: ", end=' ')
            tri = list(map(str, list(input())))  # 숫자열 입력부분. 문자열을 받아 리스트로 받게된다.
            if check(tri) is False:  # 체크함수를 통해 검사했을때 False가 출력된다면 잘못된 숫자가 입력된것이다.
                print("옳지못한 숫자열이 입력되었습니다. 다시 입력해주세요")
                continue

            now = BALL(tri, randnumlist)  # 이번에 시도한 문자열을 검사하기위해 BALL 클래스에 넣어준다.
            trylist.append(now)  # 이번에 시도한 문자열을 저장한다.
            if now.SB == [0, 0]:
                print("Out")
            else:
                print("S:%d, B:%d " % (now.SB[0], now.SB[1]))  # S의 수와 B 수를 출력해준다.

            if now.SB[0] == 3:  # S가 3개라면 맞춘거니 더 입력할 필요가 없다
                FS = 'Success'
                break

        if FS == 'Success':  # 성공 여부에 따라 나오는 멘트가 다르다
            print("숫자야구게임에서 승리하셨습니다")
            print("%d 회 시도만에 맞추셨습니다" % len(trylist))
        else:
            print("숫자 맞추기를 실패하셨습니다")
            print("정답은 '" + str(randnumlist[0]) + str(randnumlist[1]) + str(randnumlist[2]) + "' 이었습니다.")
            # 두번째 print 는 정답출력을 담당한다.

        q = ' '
        while q != 'Y' or q != 'N':
            print("숫자야구를 다시 진행하시겠습니까? Y/N:", end=' ')  # 재시작 여부 질문문
            q = input()
            if q == 'N':
                yesorno = 'N'  # N은 아니오
                print("\n숫자야구 시스템을 종료합니다.")
                break
            elif q == 'Y':  # Y는 예
                print("숫자야구를 다시 시작하겠습니다.")
                break
            else:  # 잘못 입력했다면 다시 입력하게 만든다
                print("잘못입력하셨습니다. 다시 입력해주십시오")