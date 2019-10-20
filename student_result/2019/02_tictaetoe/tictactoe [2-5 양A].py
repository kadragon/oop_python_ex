import random  # 무작위로 번호를 고를 때 사용하기 위해 random import
from time import sleep  # 컴퓨터가 생각하는 시간을 연출하기 위해 sleep import

instruction = "*" * 40 + '''
>> <틱택토 게임 규칙>
>> 칸마다 번호가 쓰여진 정사각형 보드가 있습니다.
>> 게임의 목표는 컴퓨터보다 빠르게 한 줄을 자신의 것으로 만드는 것입니다.
>> 당신이 어떤 빈 칸의 번호를 입력하면, 그 칸은 당신의 것이 됩니다.
>> 컴퓨터 또한 마찬가지의 방식으로 게임을 진행하며, 각자의 턴은 번갈아 찾아옵니다.
>> 당신의 칸은 O, 컴퓨터의 칸은 X로 표시됩니다.
>> 컴퓨터보다 빠르게 가로, 세로, 대각선 중 무엇이든 한 줄을 당신의 것으로 만들면 승리입니다.
>> 
>> 번호를 입력할 때, 번호 대신 키워드를 입력할 수 있습니다.
>> 키워드를 입력하면 각 키워드에 해당하는 결과를 출력합니다. 턴은 소모되지 않습니다.
>> 
>> 키워드 종류
>> help: 도움말
>> back: 무르기
>> quit: 중도 포기
>>
>> 무르기를 선택하면 컴퓨터와 사용자 모두 한 수씩 전으로 돌아갑니다.
>> 전략적인 플레이로 컴퓨터를 이겨보세요.
''' + "*" * 40  # 게임 설명문


class RangeError(Exception):  # 입력 범위를 벗어났을 때 발생하는 오류
    def __init__(self):
        super().__init__(">> 입력 범위를 벗어났습니다. 입력 범위를 확인해주세요.")


class SelectionError(Exception):  # 이미 선택된 번호를 입력했을 때 발생하는 오류
    def __init__(self):
        super().__init__(">> 이미 선택된 번호입니다.")


class DummyError(Exception):  # 데코레이터 안에서 continue 를 호출하기 위해 만들어진 오류
    def __init__(self):
        super().__init__(">> 데코레이터 안에서 반복하기 위해 만들어진 오류입니다.")


class BackError(Exception):  # 더 이상 무를 수 없을 때 발생하는 오류
    def __init__(self):
        super().__init__(">> 더 이상 무를 수 없습니다.")


def input_check(func):  # 사용자의 입력이 올바른지 확인하는 데코레이터
    def wrapper():
        while True:  # 사용자가 올바른 입력을 줄 때까지
            try:
                return func()
            except ValueError:  # 원하는 입력이 아니라면 잘못된 입력임을 출력
                print(">> 잘못된 입력입니다.")
            except DummyError:  # raise DummyError -> while, continue (데코레이터를 사용한 함수는 while 밖이므로 정상적으로 continue 호출 불가)
                continue
            except Exception as e:  # 다른 오류가 생기면 오류 메세지 출력
                print(e)

    return wrapper


class Board:  # 보드판 클래스
    def __init__(self, s):  # 크기 전달 받고 초기화
        self.size = s  # 크기 저장
        self.board = list(range(1, s ** 2 + 1))  # 크기^2 만큼 리스트 생성, 게임에서 쓰일 실제 보드

    def is_not_full(self):  # 보드판이 전부 채워졌는지 판단하는 메써드
        for element in self.board:  # 보드에서 요소를 꺼내온 다음
            if type(element) == int:  # 만약 하나라도 아직 정수 상태이면
                return True  # True 반환
        return False  # 전부 정수가 아니면 False 반환

    def is_not_selected(self, number):  # 번호를 입력 받아 그 번호가 이미 선택됐는지 판단하는 메써드
        if number in self.board:  # 만약 번호가 보드판에 남아있다면
            return True  # True 반환
        return False  # 아니라면 False 반환

    def select(self, number, turn):  # 번호와 표식을 입력받아 해당하는 칸을 표식으로 채워주는 메써드
        if self.is_not_selected(number):  # 만약 해당하는 칸이 선택된 적 없다면
            self.board[number - 1] = turn  # 해당하는 칸을 표식으로 바꿔줌
            if turn == " O":  # 선택자가 사용자라면
                global player_history
                player_history.append(number)  # 사용자 선택 기록에 번호를 남김
            else:  # 선택자가 컴퓨터라면
                global computer_history
                computer_history.append(number)  # 컴퓨터 선택 기록에 번호를 남김
        else:  # 해당하는 칸이 이미 선택됐다면
            raise SelectionError  # 오류 발생

    def row_check(self, row, value):  # 행 번호와 표식을 입력받아 해당하는 행에 그 표식이 얼마나 있는지 반환하는 메써드
        global must_check  # 인공지능이 반드시 선택해야 하는 번호, 0으로 초기화
        same = 0  # 표식과 같은 칸의 개수
        for idx in range(self.size):  # 행의 각 칸에 대해
            if self.board[row * self.size + idx] == value:  # 칸의 값이 표식과 같다면
                same += 1  # same 1 증가
        if same == self.size - 1:  # 같은 표식이 하나만 더 채워지면 승부가 날 때
            for idx in range(self.size):  # 행의 각 칸에 대해
                if self.is_not_selected(row * self.size + idx + 1):  # 그 칸이 아직 선택된 적 없다면
                    must_check = row * self.size + idx + 1  # must_check 에 그 칸의 번호 저장
                    break  # for 탈출
        return same  # 표식과 같은 칸의 개수 반환

    def column_check(self, column, value):  # 열 번호와 표식을 입력받아 해당하는 열에 그 표식이 얼마나 있는지 반환하는 메써드
        global must_check  # 인공지능이 반드시 선택해야 하는 번호, 0으로 초기화
        same = 0
        for idx in range(self.size):  # 열의 각 칸에 대해
            if self.board[idx * self.size + column] == value:  # 칸의 값이 표식과 같다면
                same += 1  # same 1 증가
        if same == self.size - 1:  # 같은 표식이 하나만 더 채워지면 승부가 날 때
            for idx in range(self.size):  # 열의 각 칸에 대해
                if self.is_not_selected(idx * self.size + column + 1):  # 그 칸이 아직 선택된 적 없다면
                    must_check = idx * self.size + column + 1  # must_check 에 그 칸의 번호 저장
                    break  # for 탈출
        return same  # 표식과 같은 칸의 개수 반환

    def diagonal_check(self, value):  # 표식을 입력받아 우하향/우상향 대각선에 그 표식이 얼마나 있는지 리스트로 반환하는 메써드
        global must_check  # 인공지능이 반드시 선택해야 하는 번호, 0으로 초기화
        same1 = 0
        same2 = 0
        for idx in range(self.size):  # 우하향 대각선의 각 칸에 대해
            if self.board[idx * (self.size + 1)] == value:  # 칸의 값이 표식과 같다면
                same1 += 1  # same1 1 증가
        if same1 == self.size - 1:  # 같은 표식이 하나만 더 채워지면 승부가 날 때
            for idx in range(self.size):  # 우하향 대각선의 각 칸에 대해
                if self.is_not_selected(idx * (self.size + 1) + 1):  # 그 칸이 아직 선택된 적 없다면
                    must_check = idx * (self.size + 1) + 1  # must_check 에 그 칸의 번호 저장
                    break
        for idx in range(1, self.size + 1):  # 우상향 대각선의 각 칸에 대해
            if self.board[idx * self.size - idx] == value:  # 칸의 값이 표식과 같다면
                same2 += 1  # same2 1 증가
        if same2 == self.size - 1:  # 같은 표식이 하나만 더 채워지면 승부가 날 때
            for idx in range(1, self.size + 1):  # 우상향 대각선의 각 칸에 대해
                if self.is_not_selected(idx * self.size - idx + 1):  # 그 칸이 아직 선택된 적 없다면
                    must_check = idx * self.size - idx + 1  # must_check 에 그 칸의 번호 저장
                    break  # for 탈출
        return [same1, same2]  # 우하향/우상향 대각선에서 표식과 같은 칸의 개수를 순서대로 리스트로 만들어 반환

    def print_board(self):  # 보드판의 상황을 출력하는 메써드
        cnt = 1  # 지금까지 출력한 요소의 개수, 1로 초기화
        print_str = ""  # 출력용 문자열
        print("<Game Board>".center(80))
        for num in self.board:
            if type(num) == int:  # 이 칸이 선택된 적 없다면, 즉 숫자라면
                print_str += f"{num:2d} "  # 두 자리 숫자로 문자열에 집어넣음
            else:  # 이 칸이 선택된 적 있다면, 즉 문자라면
                print_str += num + " "  # 문자 상태로 문자열에 집어넣음
            if cnt % self.size == 0:  # 행의 마지막 칸이라면
                print(print_str.center(80))  # 출력
                print_str = ""  # 문자열 비우기
            cnt += 1  # 출력한 칸의 개수 1 증가


@input_check
def change_setting():  # 사용자에게 설정 변경 여부를 물어보는 함수
    choice = input(">> 설정을 변경하시겠습니까? '예'라면 y, '아니오'라면 n을 입력해주세요 [y/n]: ").strip()  # 사용자에게 설정을 변경할 지 물어봄
    if choice == 'y':  # 그렇다고 답하면 True 반환
        return True
    elif choice == 'n':  # 아니라고 답하면 False 반환
        return False
    else:  # 원하는 입력이 아니면 오류 발생
        raise ValueError


@input_check
def scan_size():  # 보드판 크기를 입력 받아 그대로 반환하는 함수
    s = int(input(">> 보드의 크기를 입력해주세요 [3 ~ 7]: ").strip())  # 보드판 크기를 입력 받음, s = size
    if not 3 <= s <= 7:  # 입력값이 3 이상 7 이하가 아니거나 문자, 띄어쓰기를 포함하면 오류 발생
        raise RangeError
    return s  # 보드판 크기 반환


@input_check
def scan_level():  # 난이도를 입력 받아 그대로 반환하는 함수
    lvl = input(">> 게임의 난이도를 설정해주세요 [easy/medium/hard]: ").strip()  # 난이도를 입력 받음, lvl = level
    if lvl not in ["easy", "medium", "hard"]:  # 입력값이 3개의 난이도 중 하나가 아니라면 오류 발생
        raise ValueError
    return lvl  # 난이도 반환


@input_check
def scan_back():  # 최대 무르기 횟수를 입력 받아 그대로 반환하는 함수
    b = int(input(">> 최대 무르기 횟수를 입력해주세요 [0 ~ 7]: ").strip())  # 최대 무르기 횟수를 입력 받음, b = back
    if not 0 <= b <= 7:  # 입력값이 0 이상 7 이하가 아니거나 문자, 띄어쓰기를 포함하면 오류 발생
        raise RangeError
    return b  # 최대 무르기 횟수 반환


@input_check
def want_first():  # 사용자에게 선공 여부를 물어보는 함수
    choice = input(">> 선공하시겠습니까? '예'라면 y, '아니오'라면 n을 입력해주세요 [y/n]: ").strip()  # 사용자에게 다시 선공할 지 물어봄
    if choice == 'y':  # 그렇다고 답하면 True 반환
        return True
    elif choice == 'n':  # 아니라고 답하면 False 반환
        return False
    else:  # 원하는 입력이 아니면 오류 발생
        raise ValueError


@input_check
def player_turn():  # 사용자의 차례에 입력에 대응하는 함수
    num = input(">> 선택할 번호를 입력해주세요: ").strip()  # 사용자에게 선택할 번호를 입력받음
    if num == 'quit':  # 중도 포기를 원한다면
        return give_up()  # give_up 함수 결과값 반환
    elif num == 'help':  # 도움말을 원한다면
        print(instruction)  # 게임 설명문 출력
        raise DummyError  # 데코레이터 때문에 while, continue -> raise DummyError
    elif num == 'back':  # 무르기를 원한다면
        go_back()  # go_back 함수 호출
    num = int(num)  # 입력값을 정수로 변환
    if not 1 <= num <= game.size ** 2:  # 보드판 위에 없는 번호라면 오류 발생
        raise RangeError
    game.select(num, " O")  # 사용자가 번호를 선택했음을 보드판 game 에게 알림
    game.print_board()  # 현재 상황 출력
    return judge((num - 1) // game.size, (num - 1) % game.size, " O")  # 선택한 뒤 결과가 나왔는지 판별 후 반환


def give_up():  # 중도 포기를 원할 때 사용자의 입력에 대응하는 함수
    global lose  # 진 게임 수
    print(">> 게임을 그만 두면 패배로 기록됩니다.")  # 패배로 기록되는 사실을 사용자에게 고지
    choice = input(">> 정말로 그만두시겠습니까? '예'라면 y, '아니오'라면 n을 입력해주세요 [y/n]: ").strip()  # 사용자에게 마지막 확인
    if choice == 'y':  # 정말 중도 포기를 원하면
        print(">> 게임을 종료합니다.")
        lose += 1  # 진 게임 수 1 증가
        return True  # 결과가 나왔음을 main 함수에 알림
    elif choice == 'n':  # 중도 포기를 원하지 않는다면
        raise DummyError  # player_turn 함수에 DummyError 발생, 데코레이터 때문에 while, continue -> raise DummyError
    else:  # 원하는 입력이 아니라면 오류 발생
        raise ValueError


def go_back():  # 무르기를 원할 때 사용자의 입력에 대응하는 함수
    global computer_history  # 컴퓨터 선택 기록
    global player_history  # 사용자 선택 기록
    global left_back  # 남은 무르기 횟수
    if left_back > 0 and player_history and computer_history:  # 무르기가 아직 남아있고 사용자와 컴퓨터 모두 한번씩은 선택을 한 상황이면
        left_back -= 1  # 무르기 횟수 1 감소
        game.board[player_history.pop() - 1] = player_history[-1]  # 사용자가 가장 마지막에 선택한 값을 보드판에 복원, 기록에서 삭제
        game.board[computer_history.pop() - 1] = computer_history[-1]  # 컴퓨터가 가장 마지막에 선택한 값을 보드판에 복원, 기록에서 삭제
        game.print_board()  # 현재 상황 출력
        print(f">> 남은 무르기 횟수: {left_back:d}")  # 남은 무르기 횟수 출력
        raise DummyError  # player_turn 함수에 DummyError 발생, 데코레이터 때문에 while, continue -> raise DummyError
    else:  # 무르기가 남아있지 않거나 사용자나 컴퓨터 중 무를 선택이 남아있지 않은 경우(가장 초기의 상태) 오류 발생
        raise BackError


def computer_turn():  # 컴퓨터의 차례에 컴퓨터의 행동을 결정하는 함수
    choice = 0  # 선택할 번호, 0으로 초기화
    print(">> 컴퓨터의 차례입니다.")
    print(">> 계산 중...")
    should_be_chosen()  # 승부에 직결된 칸이 있는지 탐색
    if must_check != 0:  # 승부에 직결된 칸이 있다면
        choice = must_check  # 승부에 직결된 칸을 선택할 번호로 저장
    elif level == "easy":  # 난이도가 쉬움으로 설정되어 있다면
        choice = easy_ai()  # easy_ai 함수 결과값을 선택할 번호로 저장
    elif level == "medium":  # 난이도가 중간으로 설정되어 있다면
        choice = medium_ai()  # medium_ai 함수 결과값을 선택할 번호로 저장
    elif level == "hard":  # 난이도가 어려움으로 설정되어 있다면
        choice = hard_ai()  # hard_ai 함수 결과값을 선택할 번호로 저장
    game.select(choice, " X")  # 컴퓨터가 번호를 선택했음을 보드판 game 에 알림
    sleep(1)  # 컴퓨터가 계산에 시간이 걸리는 연출을 위한 sleep 함수, 1초간 프로그램 정지
    game.print_board()  # 현재 상황 출력
    print(f">> {choice:d}번 선택")  # 컴퓨터가 선택한 번호 출력
    return judge((choice - 1) // game.size, (choice - 1) % game.size, " X")  # 선택한 뒤 결과가 나왔는지 판별 후 반환


def should_be_chosen():  # 승부에 직결된 칸이 있는지 탐색하는 함수 (우선순위: 컴퓨터 승리 > 사용자 승리 저지)
    global must_check  # 인공지능이 반드시 선택해야 하는 번호
    must_check = 0  # 0으로 초기화, 순서대로 탐색 도중 must_check 가 바뀌면 탐색을 그만두기 위함이므로 중요
    for i in range(game.size):  # 모든 행과 열에 대해 컴퓨터가 한 칸만 더 둬서 승리한다면 must_check 에 그 칸 번호 저장
        if must_check == 0:  # 아직 must_check 가 초기화 값 그대로라면
            game.row_check(i, " X")
        if must_check == 0:  # 아직 must_check 가 초기화 값 그대로라면
            game.column_check(i, " X")
    if must_check == 0:  # 아직 must_check 가 초기화 값 그대로라면
        game.diagonal_check(" X")  # 두 대각선에 대해 컴퓨터가 한 칸만 더 둬서 승리한다면 must_check 에 그 칸 번호 저장
    for i in range(game.size):  # 모든 행과 열에 대해 사용자가 한 칸만 더 둬서 승리한다면 must_check 에 그 칸 번호 저장
        if must_check == 0:  # 아직 must_check 가 초기화 값 그대로라면
            game.row_check(i, " O")
        if must_check == 0:  # 아직 must_check 가 초기화 값 그대로라면
            game.column_check(i, " O")
    if must_check == 0:  # 아직 must_check 가 초기화 값 그대로라면
        game.diagonal_check(" O")  # 두 대각선에 대해 사용자가 한 칸만 더 둬서 승리한다면 must_check 에 그 칸 번호 저장


def easy_ai():  # 쉬움 난이도에서 컴퓨터가 선택할 번호를 결정하는 함수
    while True:  # 번호가 이미 선택된 번호일 동안
        num = random.randint(1, game.size ** 2)  # 범위 내의 번호를 무작위 선택
        if game.is_not_selected(num):  # 아직 선택되지 않은 번호라면
            break  # while 탈출
    return num  # 번호 반환


def medium_ai():  # 중간 난이도에서 컴퓨터가 선택할 번호를 결정하는 함수
    lines = [0] * game.size * game.size  # 각 칸마다 가중치를 저장하는 리스트, 모두 0으로 초기화
    for i in range(game.size):  # 각 행, 열마다 컴퓨터 표식 * 2 + 사용자 표식 * 1 + 기본값 1의 가중치 부여
        row = 2 * game.row_check(i, " X") + game.row_check(i, " O") + 1
        column = 2 * game.column_check(i, " X") + game.column_check(i, " O") + 1
        for j in range(game.size):
            lines[i * game.size + j] += row
        for j in range(game.size):
            lines[i + j * game.size] += column
    down1, up1 = game.diagonal_check(" O")  # down1 = 우하향 대각선 상의 사용자 표식 개수, up1 = 우상향 대각선 상의 사용자 표식 개수
    down2, up2 = game.diagonal_check(" X")  # down2 = 우하향 대각선 상의 컴퓨터 표식 개수, up2 = 우상향 대각선 상의 컴퓨터 표식 개수
    for i in range(game.size):  # 우하향 대각선에 컴퓨터 표식 * 2 + 사용자 표식 * 1 + 기본값 1의 가중치 부여
        lines[i * (game.size + 1)] += 2 * down2 + down1 + 1
    for i in range(1, game.size + 1):  # 우상향 대각선에 컴퓨터 표식 * 2 + 사용자 표식 * 1 + 기본값 1의 가중치 부여
        lines[i * game.size - i] += 2 * up2 + up1 + 1
    point = 0  # 선택하고자 하는 번호, 0으로 초기화
    while point == 0 or not game.is_not_selected(point):  # 맨 처음이거나 point 가 선택되지 않은 번호일 때까지
        maximum = max(lines)  # 각 칸의 가중치 중 최대 가중치를 구함
        maximum_list = []  # 최대 가중치를 가진 번호들을 저장할 리스트
        while max(lines) == maximum:  # 최대 가중치가 변하지 않는 때까지 가중치가 최대인 번호들을 저장하고 그 번호 가중치를 -1로 바꾸어 체크
            maximum_list.append(lines.index(maximum))
            lines[lines.index(maximum)] = -1
        random.shuffle(maximum_list)  # maximum_list 를 무작위로 섞음
        point = maximum_list.pop() + 1  # point 에 maximum_list 의 가장 마지막 번호를 저장
        for i in maximum_list:  # maximum_list 에 남아있는 번호들의 가중치를 원래대로 돌려놓음
            lines[i] = maximum
    return point  # 번호 반환


def hard_ai():  # 어려움 난이도에서 컴퓨터가 선택할 번호를 결정하는 함수 (medium_ai 함수에 승리할 가능성 존재 여부 판별 기능 추가)
    lines = [0] * game.size * game.size  # 각 칸마다 가중치를 저장하는 리스트, 모두 0으로 초기화
    for i in range(game.size):  # 각 행, 열마다
        computer = game.row_check(i, " X")  # i 번째 행의 컴퓨터 표식 개수
        player = game.row_check(i, " O")  # i 번째 행의 사용자 표식 개수
        if computer > 0 and player > 0:  # 이 행에 컴퓨터와 사용자 둘 다 표식이 존재한다면 승리할 가능성이 없으므로
            for j in range(game.size):  # 이 행에 가중치를 기본값 1만 부여
                lines[i * game.size + j] += 1
        else:  # 이 행에 컴퓨터와 사용자 한 쪽만 존재하거나 둘 다 존재하지 않을 경우
            for j in range(game.size):  # 이 행에 컴퓨터 표식 * 2 + 사용자 표식 * 1 + 기본값 1의 가중치 부여
                lines[i * game.size + j] += 2 * computer + player + 1
        computer = game.column_check(i, " X")  # i 번째 열의 컴퓨터 표식 개수
        player = game.column_check(i, " O")  # i 번째 열의 사용자 표식 개수
        if computer > 0 and player > 0:  # 이 열에 컴퓨터와 사용자 둘 다 표식이 존재한다면 승리할 가능성이 없으므로
            for j in range(game.size):  # 이 열에 가중치를 기본값 1만 부여
                lines[i + j * game.size] += 1
        else:  # 이 열에 컴퓨터와 사용자 한 쪽만 존재하거나 둘 다 존재하지 않을 경우
            for j in range(game.size):  # 이 열에 컴퓨터 표식 * 2 + 사용자 표식 * 1 + 기본값 1의 가중치 부여
                lines[i + j * game.size] += 2 * computer + player + 1
    down1, up1 = game.diagonal_check(" O")  # down1 = 우하향 대각선 상의 사용자 표식 개수, up1 = 우상향 대각선 상의 사용자 표식 개수
    down2, up2 = game.diagonal_check(" X")  # down2 = 우하향 대각선 상의 컴퓨터 표식 개수, up2 = 우상향 대각선 상의 컴퓨터 표식 개수
    if down1 > 0 and down2 > 0:  # 우하향 대각선에 컴퓨터와 사용주 둘 다 표식이 존재한다면 승리할 가능성이 없으므로
        for i in range(game.size):  # 우하향 대각선에 가중치를 기본값 1만 부여
            lines[i * (game.size + 1)] += 1
    else:  # 우하향 대각선에 컴퓨터와 사용자 한 쪽만 존재하거나 둘 다 존재하지 않을 경우
        for i in range(game.size):  # 우하향 대각선에 컴퓨터 표식 * 2 + 사용자 표식 * 1 + 기본값 1의 가중치 부여
            lines[i * (game.size + 1)] += 2 * down2 + down1 + 1
    if up1 > 0 and up2 > 0:  # 우상향 대각선에 컴퓨터와 사용주 둘 다 표식이 존재한다면 승리할 가능성이 없으므로
        for i in range(1, game.size + 1):  # 우상향 대각선에 가중치를 기본값 1만 부여
            lines[i * game.size - i] += 1
    else:  # 우상향 대각선에 컴퓨터와 사용자 한 쪽만 존재하거나 둘 다 존재하지 않을 경우
        for i in range(1, game.size + 1):  # 우상향 대각선에 컴퓨터 표식 * 2 + 사용자 표식 * 1 + 기본값 1의 가중치 부여
            lines[i * game.size - i] += 2 * up2 + up1 + 1
    point = 0  # 선택하고자 하는 번호, 0으로 초기화
    while point == 0 or not game.is_not_selected(point):  # 맨 처음이거나 point 가 선택되지 않은 번호일 때까지
        maximum = max(lines)  # 각 칸의 가중치 중 최대 가중치를 구함
        maximum_list = []  # 최대 가중치를 가진 번호들을 저장할 리스트
        while max(lines) == maximum:  # 최대 가중치가 변하지 않는 때까지 가중치가 최대인 번호들을 저장하고 그 번호 가중치를 -1로 바꾸어 체크
            maximum_list.append(lines.index(maximum))
            lines[lines.index(maximum)] = -1
        random.shuffle(maximum_list)  # maximum_list 를 무작위로 섞음
        point = maximum_list.pop() + 1  # point 에 maximum_list 의 가장 마지막 번호를 저장
        for i in maximum_list:  # maximum_list 에 남아있는 번호들의 가중치를 원래대로 돌려놓음
            lines[i] = maximum
    return point  # 번호 반환


def judge(r, c, turn):  # 선택한 칸의 행, 열, 선택한 참가자의 표식을 전달받아 결과를 판단하는 함수
    global win  # 이긴 게임 수
    global draw  # 비긴 게임 수
    global lose  # 진 게임 수
    chk = [game.row_check(r, turn), game.column_check(c, turn)]  # 각 열, 행, 대각선에 선택자의 표식과 같은 칸이 몇 개인지 체크
    chk.extend(game.diagonal_check(turn))
    tie = True  # 무승부 여부, True 로 초기화
    for i in range(game.size):  # 각 행, 열에 대하여
        if game.row_check(i, ' O') * game.row_check(i, ' X') == 0:  # 해당하는 행에 컴퓨터와 사용자 중 하나라도 표식을 놓지 않았다면
            tie = False
        if game.column_check(i, ' O') * game.column_check(i, ' X') == 0:  # 해당하는 열에 컴퓨터와 사용자 중 하나라도 표식을 놓지 않았다면
            tie = False
    if 0 in game.diagonal_check(' O') or 0 in game.diagonal_check(' X'):  # 대각선에 컴퓨터와 사용자 중 하나라도 표식을 놓지 않았다면
        tie = False
    if game.size in chk:  # 열, 행, 대각선 중 하나라도 선택자의 표식으로 가득 찼다면
        if turn == " O":  # 선택자가 사용자라면
            win += 1  # 이긴 게임 수 1 증가
            print(">> 축하합니다. 승리하셨습니다.")  # 승리 메세지 출력
        else:  # 선택자가 컴퓨터라면
            lose += 1  # 진 게임 수 1 증가
            print(">> 안타깝지만 패배했습니다.")  # 패배 메세지 출력
    elif tie:  # 어떤 줄에도 사용자와 컴퓨터의 표식이 둘 다 존재한다면
        draw += 1  # 비긴 게임 수 1 증가
        print(">> 승부가 날 수 없습니다. 비겼습니다.")  # 무승부 메세지 출력
    else:  # 게임이 아직 끝나지 않았다면
        return False  # 상위 함수에 결과가 나오지 않았음을 False 전달로 알림
    return True  # 상위 함수에 결과가 나왔음을 True 전달로 알림


def print_rate():  # 승률을 출력하는 함수
    print("-" * 20)
    print(">> 전체 게임 수:", play)  # 전체 게임 수 출력
    print(">> 이긴 게임 수:", win)  # 이긴 게임 수 출력
    print(">> 비긴 게임 수:", draw)  # 비긴 게임 수 출력
    print(">> 진 게임 수:", lose)  # 진 게임 수 출력
    print(f">> 승률: {win / play * 100:.2f}%")  # 승률 출력, 승률 = 이긴 게임 수 / 전체 게임 수 * 100 (%)
    print("-" * 20)


@input_check
def replay():  # 사용자에게 다시 플레이할 지 여부를 물어보는 함수
    choice = input(">> 다시 플레이하시겠습니까? '예'라면 y, '아니오'라면 n을 입력해주세요 [y/n]: ").strip()  # 사용자에게 다시 플레이할 지 물어봄
    if choice == 'y':  # 그렇다고 답하면 True 반환
        return True
    elif choice == 'n':  # 아니라고 답하면 False 반환
        return False
    else:  # 원하는 입력이 아니면 오류 발생
        raise ValueError


# main 함수
win = 0  # 이긴 게임 수, 0으로 초기화
draw = 0  # 비긴 게임 수, 0으로 초기화
lose = 0  # 진 게임 수, 0으로 초기화
play = 0  # 전체 게임 수, 0으로 초기화
size = 0  # 보드판 크기, 0으로 초기화
max_back = 0  # 최대 무르기 횟수, 0으로 초기화
while True:  # 사용자가 원할 때까지
    play += 1  # 전체 게임 수 1 증가
    print(instruction)  # 게임 설명문 출력
    if play == 1 or change_setting():  # 첫 판이거나 설정 변경을 원하면
        size = scan_size()  # 보드판 크기 설정
        level = scan_level()  # 난이도 설정
        max_back = scan_back()  # 최대 무르기 횟수 설정
    left_back = max_back  # 남은 무르기 횟수, 최대 무르기 횟수로 초기화
    player_history = []  # 무르기 때 되돌아가기 위한 사용자 선택 기록, 빈 리스트로 초기화
    computer_history = []  # 무르기 때 되돌아가기 위한 컴퓨터 선택 기록, 빈 리스트로 초기화
    must_check = 0  # 인공지능이 반드시 선택해야 하는 번호, 0으로 초기화
    game = Board(size)  # 보드판 생성
    if want_first():  # 플레이어가 선공이라면
        print(">> 게임이 시작됩니다.")
        game.print_board()  # 초기 상황 출력
        while True:  # 결과가 나올 때까지
            if player_turn() or computer_turn():  # 사용자 먼저, 그 다음 컴퓨터 차례, 둘 중 결과가 나왔다면
                break  # while 탈출
    else:  # 플레이어가 후공이라면
        print(">> 게임이 시작됩니다.")
        while True:  # 결과가 나올 때까지, 컴퓨터가 선택한 후 상황 출력하므로 print_board 필요 없음
            if computer_turn() or player_turn():  # 컴퓨터 먼저, 그 다음 사용자 차례, 둘 중 결과가 나왔다면
                break  # while 탈출
    print_rate()  # 승률 출력
    if not replay():  # 사용자가 다시 플레이하고 싶어하지 않는다면
        print(">> 수고하셨습니다.")
        break  # 게임 종료
