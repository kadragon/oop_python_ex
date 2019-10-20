import random

print("답을 입력할 때 공백 없이 숫자를 적어주세요")
print("Ex] 123")
print("S = 숫자와 위치가 모두 맞은 개수")
print("B = 숫자는 맞지만 위치가 틀린 개수")
print("O = 숫자와 위치가 모두 틀린 개수")
print("=" * 100)


def fun():
    a = list(range(10))  # a=[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    random.shuffle(a)  # a가 랜덤하게 배열

    ans = []
    ans.extend(a[0:3])  # 중복 없는 random한 세자리 수 : 답

    def game():
        try:
            expect = list(map(int, list(input())))  # 사용자의 답을 리스트 형태로 저장

            S = 0  # 스트라이크 초기화
            B = 0  # 볼 초기화
            O = 0  # 아웃 초기화

            if ans == expect:  # 정답일때
                print("Answer!")
                print("One more try? yes/no")  # 다시 하는 지 묻기
                p = input()
                if p == "yes":
                    fun()  # 게임 실행
                else:
                    exit()  # 나가기
            try:
                for i in range(0, 3):
                    if ans[i] == expect[i]:  # 스트라이크 개수
                        S += 1
                    elif ans[0] == expect[i]:  # 볼 개수
                        B += 1
                    elif ans[1] == expect[i]:
                        B += 1
                    elif ans[2] == expect[i]:
                        B += 1
                    else:  # 아웃 개수
                        O += 1
                print(" %dS || %dB || %dO " % (S, B, O))  # 결과 출력

            except IndexError:
                print("Try again")  # 숫자를 적게 넣었을 때 에러 방지
        except ValueError:
            print("Try again")  # 띄어쓰기 포함했을 때 에러 방지

    i = 1
    while i < 11:
        print("Guess #%d" % i)
        game()
        i += 1  # 기회 10번

    print("Game over!")  # 10번 안에 못 맞추었을 경우
    print("Answer is", end=' ')
    for j in range(0, 3):
        print(ans[j], end='')  # 답 출력
    print()
    print("One more try? yes/no")  # 다시하는지 묻기
    y = input()
    if y == "yes":
        fun()  # 게임 실행
    else:
        exit()  # 나가기


fun()  # 게임 실행
