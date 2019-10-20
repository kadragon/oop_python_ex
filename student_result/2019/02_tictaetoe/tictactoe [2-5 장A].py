from time import sleep
import random

connected_lines = (((0, 3, 6), (0, 4), (0, 5, 7)),
                   ((1, 3), (1, 4, 6, 7), (1, 5)),
                   ((2, 3, 7), (2, 4), (2, 5, 6)))  # 보드판의 각 좌표에 연결된 줄(행/열/대각선)에 정보

connected_dots = ((1, 2, 3), (4, 5, 6), (7, 8, 9), (1, 4, 7),
                  (2, 5, 8), (3, 6, 9), (1, 5, 9), (3, 5, 7))  # 보드판의 각 줄에 연결된 칸(1~9)에 대한 정보

line_length = 48  # 출력 line 길이

"""
보드판의 각 칸의 번호는 다음과 같다:
1 2 3
4 5 6
7 8 9
x를 행, y를 열이라고 하면 줄(행/열/대각선) 8개(0~7)는 각각
x = 1, x = 2, x = 3, y = 1, y = 2, y = 3, y = x, y = 3 - x 에 해당한다
"""


def check_input(func):
    """
    입력 오류가 없을 때까지 반복하도록 하는 데코레이터
    :param func: 입력 받는 함수
    :return: 데코레이터가 적용된 함수
    """

    def wrapper(*args, **kwargs):
        while True:
            try:
                return func(*args, **kwargs)
            except Exception as e:
                print("잘못된 입력입니다.")
                if str(e).split(':')[0] == "invalid literal for int() with base 10":
                    print("정수 값을 입력해주세요.")
                else:
                    print(e)
                print()

    return wrapper


@check_input
def get_command(string, cmd_list):
    """
    명령을 입력 받는 함수
    :param string: 입력 안내 문구
    :param cmd_list: 입력 받을 수 있는 명령어 리스트
    :return: 입력 받은 명령어
    """
    user_input = input(string).upper().strip()
    if user_input in cmd_list:
        return user_input
    else:
        error_name = f"{cmd_list} 중 하나를 입력하세요."
        raise ValueError(error_name)


class Game:
    """
    게임 한 판을 진행하는데 필요한 함수들을 모아서 관리하는 클래스
    """

    def __init__(self, user_character, round_number):
        """
        게임 오브젝트를 초기화하는 함수
        :param user_character: 사용자가 사용하기로 한 캐릭터 [O/X]
        :param round_number: 이번 게임의 회차
        """
        self.board = [['-', '-', '-'], ['-', '-', '-'], ['-', '-', '-']]  # 보드판
        self.user_board_info = [0, 0, 0, 0, 0, 0, 0, 0]  # 각각의 줄(행/열/대각선)에 놓인 사용자 말의 개수
        self.com_board_info = [0, 0, 0, 0, 0, 0, 0, 0]  # 각각의 줄(행/열/대각선)에 놓인 컴퓨터 말의 개수
        self.user_character = user_character
        self.com_character = 'O' if self.user_character == 'X' else 'X'
        self.turn_count = 1
        self.winner = None
        print()
        print(f" ROUND {round_number} ".center(line_length, '#'))  # 게임 회차 출력

    def display(self):
        """
        턴에 대한 정보와 보드판을 출력하는 함수
        """
        who = self.whose_turn()
        print()
        print(f" {who} turn ".center(line_length, '-'))  # 누구 턴인지 출력
        print()
        for i in range(3):
            line = ''
            for j in range(3):
                line += f" {self.board[i][j]} "
            print(line.center(line_length))  # 보드판을 각 행별로 출력
        print()

    def take_turn(self):
        """
        게임의 한 턴을 진행하는 함수
        """
        x, y = None, None
        if self.whose_turn() == self.user_character:  # 지금이 사용자 턴이라면
            x, y = self.get_turn()  # 사람이 말을 놓을 위치를 입력 받음
            for i in connected_lines[x][y]:  # 그 위치에 연결된 모든 줄(행/열/대각선)에 대해
                self.user_board_info[i] += 1  # 줄에 놓인 말의 개수 1 증가
            for i in self.user_board_info:  # 모든 줄 검사
                if i == 3:  # 3개가 놓이는 줄이 발생한다면
                    self.winner = self.user_character  # 사용자가 이긴 것!

        elif self.whose_turn() == self.com_character:  # 컴퓨터 턴에 대해서도 같은 방식으로 진행
            x, y = self.think_turn()
            for i in connected_lines[x][y]:
                self.com_board_info[i] += 1
            for i in self.com_board_info:
                if i == 3:
                    self.winner = self.com_character

        self.board[x][y] = self.whose_turn()  # 가져온 행, 열 위치에 말 놓기
        self.turn_count += 1

    @check_input  # 데코레이터 적용
    def get_turn(self):
        """
        사용자가 둘 수를 입력받는 함수
        :return: 사용자 수의 좌표
        """
        user_input = int(input("type to place character [1~9]: "))
        if not 1 <= user_input <= 9:
            raise ValueError("1부터 9 사이의 정수를 입력하세요.")
        x = (user_input - 1) // 3
        y = (user_input - 1) % 3  # 행, 열 위치 결정
        if self.board[x][y] == '-':
            return x, y  # 위치가 비었다면 순서쌍 반환
        else:
            raise ValueError(f"{user_input}번 자리가 비어있지 않습니다. 다른 자리를 입력하세요.")

    def think_turn(self):
        """
        컴퓨터가 둘 수를 생각하는 함수
        :return: 컴퓨터 수의 좌표
        """
        print("Thinking...".center(line_length))
        sleep(0.5)

        u_info = self.user_board_info
        c_info = self.com_board_info
        result = []
        # 놓으면 바로 이기는 수
        for i in range(8):  # 모든 줄(행/열/대각선) 검사
            if c_info[i] == 2:
                result.extend(self.find_blank(i))  # 컴퓨터의 말이 2개 놓여 있는 줄의 blank 좌표들을 result 에 저장
        if len(result) > 0:
            return result[random.randrange(len(result))]  # 만약 있다면 그 중에서 하나를 골라 반환
        # 가장 방어를 잘 할 수 있는 수
        sorted_info = sorted(list(set(u_info)), reverse=True)  # 줄 별로 놓여 있는 사용자의 말의 개수를 내림차순 정렬
        for m in sorted_info:
            for i in range(8):  # m이 가장 큰 값부터 내려오면서 모든 줄(행/열/대각선) 검사
                if u_info[i] == m:
                    result.extend(self.find_blank(i))  # 놓인 말의 수가 m인 줄의 빈 공간의 blank 좌표들을 result 에 저장
            if len(result) > 0:
                return result[random.randrange(len(result))]  # 만약 있다면 그 중에서 하나를 골라 반환

    def find_blank(self, i):
        """
        i번 줄에 연결된 비어있는 점의 좌표를 반환하는 함수
        :param i: 줄 번호
        :return: result
        """
        result = []
        for dot in connected_dots[i]:  # i번 줄에 연결된 모든 점(1~9)에 대해
            x = (dot - 1) // 3
            y = (dot - 1) % 3
            if self.board[x][y] == '-':
                result.append((x, y))  # 빈 공간이라면 리스트에 저장
        return result

    def whose_turn(self):
        """
        :return: 지금 턴에 해당하는 캐릭터
        """
        if self.turn_count % 2 == 0:
            return 'O'
        else:
            return 'X'  # 짝수면 'O', 홀수면 'X'

    def show_results(self, win, lose, round_tot):
        """
        게임 한 라운드의 최종 결과를 보여주는 함수
        :param win: 지금까지 이긴 횟수
        :param lose: 지금까지 진 횟수
        :param round_tot: 총 게임 횟수
        """
        if self.winner is None:
            print("We're tied!".center(line_length))  # 이긴 사람이 없다면 비겼다고 출력
        else:
            print(f"{self.winner} is the winner!".center(line_length))  # 이긴 사람이 있다면 누구인지 출력
            if self.winner == self.user_character:
                print("Congratulations! You win!".center(line_length))  # 사용자가 이겼으면 축하 메세지
            else:
                print("Oh, no! Maybe next time...".center(line_length))  # 컴퓨터가 이겼으면 패배 메시지
        print(f"win: {win} | lose: {lose} | tie: {round_tot - win - lose}".center(line_length))  # 지금까지의 stats
        print("winning percentage: %.2f".center(line_length) % (win / round_tot))  # winning rate 출력
        print()


print("""
Welcome to Tic Tac Toe.
You'll be matching the computer.
You can choose between two characters, O and X.
Choose X to start first.
each space is numbered as follows:
1 2 3
4 5 6
7 8 9
""")

round_count = 0
win_count = 0
lose_count = 0

while True:
    round_count += 1
    chosen_character = get_command("Choose character [O/X]: ", ['o', 'O', 'x', 'X'])  # O/X 입력
    thisGame = Game(chosen_character, round_count)  # thisGame 객체 생성
    while True:
        thisGame.display()  # 보드판 출력
        thisGame.take_turn()  # 한 턴을 진행함
        if thisGame.winner is not None or thisGame.turn_count >= 10:
            break  # 승패가 결정되었거나 보드판이 모두 찼으면 반복문 탈출
    thisGame.display()  # 최종 보드판 출력
    if thisGame.winner == thisGame.user_character:  # 사용자가 이겼다면
        win_count += 1
    if thisGame.winner == thisGame.com_character:  # 컴퓨터가 이겼다면
        lose_count += 1
    thisGame.show_results(win_count, lose_count, round_count)  # 결과 출력
    play_again = get_command("Play again? [Y/N]: ", ['y', 'Y', 'n', 'N'])  # 게임을 끝낼 지 결정
    if play_again == 'N':
        break
