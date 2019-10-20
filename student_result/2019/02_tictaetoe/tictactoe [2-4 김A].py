import random

game_board_or = [1, 2, 3, 4, 5, 6, 7, 8, 9]  # game_board 를 초기화 하기 위한 리스트 입니다
winner_board = ((1, 2, 3), (4, 5, 6), (7, 8, 9), (1, 4, 7), (2, 5, 8), (3, 6, 9), (1, 5, 9), (3, 5, 7))
# 이길 수 있는 조합을 모아놓은 튜플입니다
can_move_or = [0, 1, 2, 3, 4, 5, 6, 7, 8]  # can_move 를 초기화 하기 위한 리스트 입니다
user_char = ""  # user 가 사용할 문자입니다
com_char = ""  # computer 가 사용할 문자입니다
game = True  # game 을 할지말지 결정하는 변수입니다.
user_win = 0  # user 의 승리 횟수를 저장하는 변수입니다.
com_win = 0  # computer 의 승리 횟수를 저장하는 변수입니다.


def explain() -> None:
    """
    user 에게 틱택토의 규칙을 설명해주는 함수입니다
    :return: None
    """
    print("3*3형태의 판에서 하는 오목이라고 생각하시면 편해요!")
    print("대각선, 가로, 세로 어떤 방향이던 세 개를 연속해서 두게 되면 승리합니다!")
    print("아무리 못해도 랜덤하게 두는 컴퓨터는 이겨야겠죠?")
    print()


def chose_ch() -> None:
    """
    user 가 어떤 문자를 사용할지 선택하도록 하는 함수입니다
    :return: None
    """
    print("O나 X 중 어떤 문자를 사용할지 고르세요")
    ch = input().upper()  # 소문자가 들어오면 대문자로 수정해줌

    while ch != 'O' and ch != 'X':  # O나 X가 아닌 경우 계속해서 다시 입력을 받음
        print("제대로 입력해주세요ㅜㅜ")
        ch = input().upper()

    print("좋아요 그럼 %s로 진행하도록 하죠!" % ch)  # user 가 선택한 문자를 출력함
    print()

    global user_char, com_char
    user_char = ch
    if ch == 'O':
        com_char = 'X'
    else:
        com_char = 'O'  # user 의 선택에 따라 user_char 와 com_char 를 결정함


def chose_turn():
    """
    user 가  자신이 먼저할지 computer 가 먼저 할지 선택하는 함수입니다.
    :return: user 가 선택한 숫자 1 or 2 를 return 합니다.
    """
    print("먼저할지 늦게할지를 결정해주세요")
    print("먼저하려면 1, 늦게하려면 2를 눌러주세요")

    whose_turn = input()

    while whose_turn != '1' and whose_turn != '2':
        print("제대로 입력해주세요ㅜㅠ")
        whose_turn = input()

    if whose_turn == '1':
        print()
        print("좋아요 그럼 먼저 시작하세요")
        return 1

    elif whose_turn == '2':
        print()
        print("자신 넘치시는군요! 그럼 저부터 시작할게요!")
        return 2


def is_right(pl):
    """
    user 가 선택한 숫자(위치)가 규칙에 맞는 숫자인지 알려주는 함수입니다.
    :param pl: 선택한 숫자
    :return: 제대로 된 숫자가 아닐 경우 False, 제대로 된 숫자의 경우 True
    """
    if '1' > pl or pl > '9':
        print("제대로 입력해주세요ㅜㅠ")
        return False

    pl = int(pl)

    if pl - 1 not in can_move:
        print("제대로 입력해주세요ㅜㅠ")
        return False

    return True


def show_board():
    """
    game_board 를 보여주는 함수입니다.
    :return: None
    """
    for i in range(9):
        print(game_board[i], end=" | ")
        if (i + 1) % 3 == 0:
            print()
            print("===========")
    print()


def player_turn():
    """
    player 에게 숫자를 입력받아 game_board 에 배치하는 함수입니다
    :return: None
    """
    print("어디에 놓을지 골라주세요 당연히 1~9까지 중에 골라야겠죠?")
    player_sel = input()  # player 에게 입력을 받습니다

    while is_right(player_sel) is False:
        player_sel = input()  # 만일 숫자가 규칙에 맞지 않는다면 계속해서 다시 입력을 받습니다

    player_sel = int(player_sel)  # 입력한 숫자가 규칙에 맞는다면 str 을 int 형으로 전환합니다

    game_board[player_sel - 1] = user_char  # game_board 에 user_char 를 표시합니다
    can_move.remove(player_sel - 1)  # 움직일 수 있는 수에서 선택된 위치를 제거합니다.


def can_win(char, brd, move):
    """
    자신이 이길 수 있는지, 혹은 상대방이 이길 수 있는지 예측하는 함수입니다.
    :param char: user 혹은 computer 의 문자입니다
    :param brd: game_board 를 copy 한 다른 보드입니다
    :param move: 선택했을 때 결과를 예측하고 싶은 위치입니다.
    :return: ch_win(char, brd)의 결과 (만약 char 문자를 가진 쪽이 승리할 수 있다면 True 를 그렇지 않다면 False 를 return)
    """
    if move not in can_move:
        return False  # move 가 이동할 수 없는 곳이면 False return

    brd[move] = char  # copy 된 판에 move 대로 char 배치
    win = ch_win(char, brd)  # ch_win 으로부터 결과를 받아옴

    return win


def com_turn():
    """
    computer 가 선택하도록 하는 함수입니다.
    1. 자신이 이기는 수가 있다면 그곳에 둡니다.
    2. 1의 경우가 존재하지 않고, 상대가 이길 수가 있다면 그곳에 둡니다.
    3. 1, 2의 경우가 모두 존재하지 않을 경우 빈 칸 중 랜덤하게 한 곳을 선택합니다.
    :return: None
    """
    print("제가 고르도독 하죠!")

    for i in range(9):
        if can_win(com_char, game_board.copy(), i):
            game_board[i] = com_char
            can_move.remove(i)
            return  # can_win 함수를 이용하여 자신이 이길 곳이 있는지 탐색하고 있다면 그곳에 둡니다

    for i in range(9):
        if can_win(user_char, game_board.copy(), i):
            can_move.remove(i)
            game_board[i] = com_char
            return  # can_win 함수를 이용하여 상대방이 이길 곳이 있는지 탐색하고 있다면 그곳에 둡니다

    move = random.sample(can_move, 1)[0]  # 1, 2 경우가 존재하지 않으면 랜덤으로 행동을 선택합니다.
    game_board[move] = com_char
    can_move.remove(move)  # 움직일 수 있는 수에서 선택된 위치를 제거합니다.


def ch_win(char: str, brd: list) -> bool:
    """
    brd 에서 char 의 문자를 가진 쪽이 승리했는지 판단해주는 함수입니다.
    :param char: 승리했는지 알고 싶은 문자입니다.
    :param brd: 승리했는지 알고 싶은 board 입니다. ex) game_board or game_board.copy()
    :return: char 문자 쪽이 승리했다면 True, 아니면 False 를 return 합니다
    """
    for tu in winner_board:  # 이길 수 있는 조합이 담긴 튜플에서 조합을 꺼냅니다
        win = True  # win 변수 초기화
        for ix in tu:  # 이길 수 잇는 조합에서 숫자 하나씩을 꺼내 그 위치가 모두 char 로 채워져있는지 확인합니다.
            if brd[ix - 1] != char:
                win = False
                break  # 하나라도 char 로 채워져있지 않으면 win 은 False 가 되고 다른 조합으로 넘어갑니다
        if win:  # 만약 win 이 True 라면(승리하는 조합을 만족했다면), 탐색을 종료합니다.
            break

    return win


def ask_re_game():
    """
    user 에게 game 을 다시 할지 물어보는 함수입니다.
    :return: user 가 다시 하고자 할 경우 True 를, 그렇지 않거나 잘못 입력했을 경우 False 를 return 합니다.
    """
    print("게임을 다시 하시겠습니까? 다시하려면 Yes, 그렇지 않으면 No를 입력해주세요")
    rep = input()

    if rep == "Yes":
        print("좋아요 다시하죠!")
        return True  # user 가 다시 하고자 할 때 True return
    elif rep == "No":
        if user_win + com_win == 0:
            print("비기기만 했군요! 비긴건 승률에 안 넣어요ㅎㅎ")
        else:
            print("좋아요 승률은 %.2f이네요!" % (user_win / (user_win + com_win)))
        print("잘가요!!")
        return False  # user 가 게임을 끝내고자 할 때 승률을 출력하고 False return
    else:
        print("이것도 답을 똑바로 못하네;; 걍 가세요")
        return False  # user 가 답을 제대로 하지 못했을 때 False return


def start_game(cnt: int):
    """
    게임의 초기 파트를 모아놓은 함수입니다.
    :param cnt: 게임을 몇 판 진행했는지를 담고 있습니다.
    :return: 게임 진행에 필요한 게임 횟수, 게임 순서, 움직일 수 있는 위치들, 게임 보드를 return 합니다
    """
    if cnt == 1:
        explain()  # 첫 판이라면 틱택토에 대한 설명을 보여줍니다.
    cnt += 1  # 게임 판수를 증가시킵니다

    chose_ch()  # user 가 O나 X 중 문자를 선택합니다.
    turn_tmp = chose_turn()  # user 가 순서를 선택합니다.
    can_move_tmp = can_move_or.copy()  # can_move 리스트를 초기화 하기 위한 작업입니다.
    game_board_tmp = game_board_or.copy()  # game_board 를 초기화 하기 위한 작업입니다.

    return cnt, turn_tmp, can_move_tmp, game_board_tmp


def game_play(turn_tmp, turn_cnt_tmp):
    """
    게임을 플레이하는 함수입니다. user 와 computer 가 번갈아가며 틱택토를 진행합니다.
    :param turn_tmp: 누가 선공일지 알려주는 변수입니다
    :param turn_cnt_tmp: 현재 몇턴이지 알려주는 변수입니다.
    :return: None
    """
    if turn_tmp == 1:
        if turn_cnt_tmp % 2 == 1:
            player_turn()
        else:
            com_turn()  # user 가 선공을 택한 경우입니다.
    else:
        if turn_cnt_tmp % 2 == 1:
            com_turn()
        else:
            player_turn()  # user 가 후공을 택한 경우입니다.

    show_board()  # game_board 를 보여줍니다.


if __name__ == '__main__':
    game_cnt = 1  # 게임 횟수를 초기화합니다
    while game:
        game_cnt, turn, can_move, game_board = start_game(game_cnt)  # 초기 조건들을 설정해주는 함수입니다.
        turn_cnt = 1  # 턴 횟수를 초기화합니다
        show_board()  # game_board 를 보여줍니다
        print("자, 이게 보드에요^^")

        while turn_cnt < 10:  # 최대 9칸이 다 채워질 동안 게임을 진행합니다
            game_play(turn, turn_cnt)  # computer 와 user 가 번갈아가며 게임을 진행하는 함수입니다

            if ch_win(user_char, game_board):
                user_win += 1
                print("축하합니다! 승리하셨네요!")
                break  # user 가 이긴 경우, user_win 을 1 증가시키고, 이번 게임을 종료합니다
            elif ch_win(com_char, game_board):
                com_win += 1
                print("이걸 컴퓨터한테 지냐;;")
                break  # computer 가 이긴 경우, computer_win 을 1 증가시키고, 이번 게임을 종료합니다

            turn_cnt += 1  # 이긴 사람이 없을 경우 턴 횟수를 증가시킵니다

        if turn_cnt > 9:
            print("컴퓨터랑 비겨요? 장난합니까?")  # 결판이 나지 않고 끝난 경우 질책합니다

        game = ask_re_game()  # user 에게 새로운 게임을 진행할 것인지 물어봅니다
