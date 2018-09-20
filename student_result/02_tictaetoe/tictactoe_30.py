"""
Title       tictactoe
Author      공도리  
Date        2018.09.10 
"""
# Access to random
import random
# Access to copy array
import copy
# Access to sleep()
from time import sleep

# The main board
boardstone = list(map(str, range(1, 10)))
# Turn number
turn = 0
# Player index
player = 0
# Computer index
computer = 0
# Stones to be put by player/computer
stone = ['', '']
# List of coordinates of one line.
oneline = [[0, 1, 2], [3, 4, 5], [6, 7, 8], [0, 3, 6],
           [1, 4, 7], [2, 5, 8], [0, 4, 8], [2, 4, 6]]


def printboard():
    """
    Prints tic-tac-toe board.
    """
    for i in range(3):
        # Prints horizontal line
        print('+' * 13)
        # Prints status of the stones between the vertical lines.
        for j in range(0, 3):
            print('| %s ' % boardstone[i * 3 + j], end='')
        print('|')
    # Prints the last base line
    print('+' * 13)


def checkwin(board):
    """
    :param board: Any Tic-Tac-Toe board.\n
    Returns if someone has won.
    """
    hasWon = False
    # "a" contains the coordinates of a line
    for a in oneline:
        # if the stones on a line are all same,
        if board[a[0]] == board[a[1]] == board[a[2]]:
            # someone has won!
            hasWon = True
            break
    return hasWon


def lineclean(linelist):
    """
    :param linelist: Coordinates of a line. \n
    Returns if there are no player's stones on a line
    """
    # "i" contains each coordinate in a line
    for i in linelist:
        # if there is a player's stone
        if boardstone[i] == stone[player]:
            # The line is not clean :(
            return False
    return True


def calcpoint(place):
    """
    :param place: place to calculate the point
    Returns how good it is to put a stone there, in a form of a number
    """
    # Lists need to search adjacent spaces
    dxlist = [-1, -1, -1, 0, 0, 1, 1, 1]
    dylist = [-1, 0, 1, -1, 1, -1, 0, 1]
    ret = 0
    for i in range(len(dxlist)):
        # Imagine as if list boardstone is 2-Dimentional List, than find the adjacent spaces
        # x, y each represents first and second factor of 2-D List.
        x = place % 3 + dxlist[i]
        y = place // 3 + dylist[i]
        # if x and y is a valid number between 0 and 2,
        if x in range(3) and y in range(3):
            # transfer it in to 1D List system.
            coor = y * 3 + x
            # if there is a computer's stone adjacent to another
            if boardstone[coor] == stone[computer]:
                # It would be better to put the stone in the "place"
                ret += 1
                for line in oneline:
                    # Find the line which the two stones(one in place and another found)are both in.
                    if coor in line and place in line:
                        # if there are no player's stone, it would be even better to put there!
                        ret += 1 if lineclean(line) else 0
                        break
    return ret


def playerturn():
    """
    Get input from player and update the board
    """
    while True:
        # Prints board
        printboard()
        # Asks player where to put the stone
        placenum = input('Where would you place your stone?')
        # If the input is not a number or if the place is already taken
        if not placenum in boardstone or not placenum.isdigit():
            # Asks again!
            print('Enter a correct place!')
            continue
        # if it was a correct input,
        for i in range(9):
            # find the place where the player wants to put the stone
            if boardstone[i] == placenum:
                # update the board
                boardstone[i] = stone[player]
                break
        break
    # prints the result
    printboard()


def computerturn():
    """
    A.I. for computer.\n
    Makes decision and put the stone in the correct place
    """
    # copy the testboard to test
    testboard = copy.copy(boardstone)
    # priority when putting the stone
    priority = [0, 2, 6, 8, 1, 3, 5, 7, 4]
    # Changed: Flag to check if there is a update in the board
    Changed = False

    # check for everywhere in the board
    for i in range(9):
        # if the place is not already taken
        if testboard[i].isdigit():
            # willWin: checks if the game could be over after 0 or 1 turn.
            willWin = False
            # puts both player's and computer's stone and test
            for j in range(2):
                # update the testboard
                testboard[i] = stone[j]
                # willWin will be true if someone can win
                willWin = willWin or checkwin(testboard)
                # restore the original state
                testboard[i] = boardstone[i]
            # if someone can win after 0 or 1 turn
            if willWin:
                # stop it, or finish it!
                boardstone[i] = stone[computer]
                # something has changed
                Changed = True
                break
            # restore the original state
            testboard[i] = boardstone[i]
    # if there aren't any critical places,
    if not Changed:
        # maxscore: value of calcpoint(place)
        maxscore = -1
        # put: place chosen to put the stone
        put = 0
        # start searching from where it has higher priority
        for i in priority:
            # if the place is not already taken,
            if boardstone[i].isdecimal():
                # and if the new place is better to put stone
                if maxscore < calcpoint(i):
                    # update maxscore and put
                    maxscore = calcpoint(i)
                    put = i
        # put the stone there!
        boardstone[put] = stone[computer]
    # wait for a while
    sleep(1.5)


# repeats forever until player quits
while True:
    # fill board with 1 to 9 (string)
    boardstone = list(map(str, range(1, 10)))
    # initalize turn
    turn = 0
    # randomize if player or computer is going to start first
    player = random.randint(0, 1)
    computer = 1 - player

    while True:
        # pick the stone to be put by player
        stonepick = input('which stone would you use(X/O)?: ').lower()
        # set the stone, according to the player's answer. computer takes the leftover stone.
        if 'o' == stonepick:
            stone[player], stone[computer] = 'O', 'X'
            break
        elif 'x' == stonepick:
            stone[player], stone[computer] = 'X', 'O'
            break
        # if player gave the wrong answer, keep asking
        else:
            print('Write in \'X\' or \'O\'!')

    # tells player if he or computer is going to do first
    if player == 0:
        print('The player starts first!\n')
    else:
        print('The computer starts first!\n')
    # wait a while
    sleep(2)
    # now let's start the game!
    while True:
        # if it is player's turn
        if player == turn % 2:
            # tell him and do the turn
            print('Player\'s turn!')
            playerturn()
        # if it is computer's turn
        else:
            # tell the player and do the turn
            print('Computer\'s turn!')
            computerturn()
        # if someone has won,
        if checkwin(boardstone):
            # tells the player who have won. The last player can be known with turn number.
            print('%s wins!' % ('Player' if player == turn % 2 else 'Computer'))
            break
        # if there is no place left to place the stone and nobody has won,
        if turn == 8:
            # it is a draw
            print('It\'s a draw!')
            break
        # increase turn number
        turn += 1
    # print the final board
    printboard()
    # again: if the player is going to play again or not
    again = True
    while True:
        # asks player if he is going to play again
        replay = input('would you like to play again(y/n)?: ').lower()
        # set again, acoording to player's answer
        if 'y' == replay:
            again = True
            break
        elif 'n' == replay:
            again = False
            break
            # if wrong answer, keep asking!
        else:
            print('Write in \'Y\' or \'N\'!')
    # if player does not want to play again, escape the final while loop.
    if not again:
        break
