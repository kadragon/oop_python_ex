# tic-tac-toe function part =================================
import random

"""
functions
- make a board
- get inputs and find errors to get the correct input
- make the computer try to win the player
- get player's input on the board (name it 1~9)
- ask if the player wants to continue
- print the player's percentage of victories
"""
BLANK = ' '


def player_sel_side():  # lets the player select side
    select = ''
    while not (select == 'O' or select == 'X'):
        print("Select your side, it should be ONLY O or X !\n  Your side >", end=' ')
        select = input().upper()
    return select


def print_board(board):
    print(' ' + board[0] + ' | ' + board[1] + ' | ' + board[2])
    print('-----------')
    print(' ' + board[3] + ' | ' + board[4] + ' | ' + board[5])
    print('-----------')
    print(' ' + board[6] + ' | ' + board[7] + ' | ' + board[8] + '\n')


def player_input(bd):  # get the player's input
    '''
    while True:
        j = int(str(input("\nPick between 1~9 that is blank.\n>")))
        if j >= 10 or j <= 0:
            print("Please try again :(\n")
        elif bd[j-1] != BLANK:
            print("Please try again :(\n")
        else:
            break
    return j
    '''
    ans = input('\nPick between 1~9 that is blank.\n>')
    if not ans.isdecimal():
        return player_input(bd)
    ans = int(ans)
    if ans > 9 or ans < 1:
        return player_input(bd)
    if bd[ans - 1] != BLANK:
        print("Please try again :(\n")
        return player_input(bd)
    return ans


def game_able(select, board, other):  # check if all squares are full
    return is_win(select, board, other) == -1 and board.count(' ') > 0


def winnings(win, tot):  # print how much the player won
    print("Your percentage of victories : %.2f percent" % ((win / tot) * 100))


def cont():  # if the player wants continue the game
    return input('CONTINUE GAME? (type "y" to continue)').lower().startswith('y')


def duplicate_board(boa):
    dupe_board = []
    for p in boa:
        dupe_board.append(p)

    return dupe_board


def is_win(select, game, other):
    lanes = [[0, 1, 2], [3, 4, 5], [6, 7, 8], [0, 3, 6],
             [1, 4, 7], [2, 5, 8], [0, 4, 8], [2, 4, 6]]

    for q in lanes:
        count = 0
        for w in q:
            if game[w] == select:
                count += 1
            elif game[w] == other:
                count -= 1
        if count == 3:
            return 1  # player wins
        elif count == -3:
            return 0  # computer wins

    return -1  # no one wins


def com_play(computer, game_now, play):
    dupe = duplicate_board(game_now)  # copy of board

    for i in range(9):
        if dupe[i] == BLANK:
            dupe[i] = play
            if is_win(play, dupe, computer) == 0:  # computer win check
                game_now[i] = computer
                return
            if is_win(play, dupe, computer) == 1:  # player win check
                game_now[i] = computer
                return
            dupe[i] = BLANK

    while True:
        randint = random.randrange(0, 9)
        if game_now[randint] != BLANK:
            continue
        else:
            game_now[randint] = computer
            return


# game part ===================================================


print("=" * 20)
print("Welcome to Tic-Tac-Toe game!")
print("**HOW TO PLAY / Read carefully!**")
print("1. You should make a line first with O or X to win the computer.")
print("2. O starts first.")
print("3. You can pick places with numbers 1~9 at your turn.\n*The board looks like this.")
print(' ' + '1' + ' | ' + '2' + ' | ' + '3')
print('-----------')
print(' ' + '4' + ' | ' + '5' + ' | ' + '6')
print('-----------')
print(' ' + '7' + ' | ' + '8' + ' | ' + '9')
print("=" * 20)

total_win = 0
total_play = 0  # indicates the total play
while True:
    selected_side = player_sel_side()
    board = list(' ' for i in range(9))
    game_end = False  # indicates whether this game ended
    t = -1  # turn

    if selected_side == 'O':  # make the computer's letter
        com_let = 'X'
        t = 0  # if turn = 0, player is the first
    else:
        com_let = 'O'
        t = 1  # if turn = 1, computer is the first

    while not game_end:
        # player selects an letter, computer gets the other one

        if t == 0:  # player turn
            if not game_able(selected_side, board, com_let):  # if game is over
                game_end = True
                if is_win(selected_side, board, com_let) == 1:  # player win
                    total_win += 1
                    total_play += 1
                    print("CONGRATULATIONS! You won!\n\n")
                    # print player's percentage of victories
                elif is_win(selected_side, board, com_let) == -1:  # tie
                    total_play += 1
                    print("This game is a tie.\n\n")
                else:  # computer win
                    total_play += 1
                    print("You lost the game :(\n\n")
                    # print player's percentage of victories
                winnings(total_win, total_play)
            else:
                board[player_input(board) - 1] = selected_side
                print_board(board)
                t += 1

        else:  # computer turn
            if not game_able(selected_side, board, com_let):  # if game is over
                game_end = True
                if is_win(selected_side, board, com_let) == 1:  # player win
                    total_win += 1
                    total_play += 1
                    print("CONGRATULATIONS! You won!\n\n")
                    # print player's percentage of victories
                elif is_win(selected_side, board, com_let) == -1:  # tie
                    total_play += 1
                    print("This game is a tie.\n\n")
                else:  # computer win
                    total_play += 1
                    print("You lost the game :(\n\n")
                    # print player's percentage of victories
                winnings(total_win, total_play)
            else:
                com_play(com_let, board, selected_side)
                print_board(board)
                t -= 1

    if not cont():  # ask if the player wants to continue and if not, end the game
        break
