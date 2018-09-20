import sys
import random


# A three by three board (index starts from 1)
board = [[0 for i in range(0, 4)] for j in range(0, 4)]


# Initalize the board with everything empty
for i in range(0, 4):
    for j in range(0, 4):
        board[i][j] = ' '


# Given a coordinate,
# Check if given coordinate is valid
def check(a, b):
    global board
    numbers = [1, 2, 3]
    # If both a and b are smaller than 3 and that spot is empty
    if a in numbers and b in numbers and board[a][b] == ' ':
        # you can place there
        return True
    else:
        return False


# Given a flag, check whther there is a line of flag
def checkBoard(flag):
    global board
    # First check horizontal & vertical line
    for i in range(1, 4):
        if board[i][1] == flag and board[i][2] == flag and board[i][3] == flag:
            return True
        if board[1][i] == flag and board[2][i] == flag and board[3][i] == flag:
            return True
    # Second check right - down line
    if board[1][1] == flag and board[2][2] == flag and board[3][3] == flag:
        return True
    # Finally check left - down line
    if board[1][3] == flag and board[2][2] == flag and board[3][1] == flag:
        return True
    
    # If none returns, there is no line
    return False


# Finds if there is a spot that player can win
# Player's mark is given
def findspot(player):
    global board
    for i in range(1, 4):
        for j in range(1, 4):
            # Try placing one mark in an empty spot
            if board[i][j] == ' ':
                board[i][j] = player
                # If then a line is created
                if checkBoard(player):
                    # Decheck the mark and
                    board[i][j] = ' '
                    # Return that pos
                    return i, j
                board[i][j] = ' '

    # If there's no such spot, return (0, 0)
    return 0, 0


# If there's spot where the ai would win place mark there
# If there's spot where the player would win place mark there
# Else, place anywher
# AI's mark is given
def aiTurn(mark):
    global board

    # Determine the mark of player and ai
    if mark == 'X':
        player = 'O'
    else:
        player = 'X'
    
    # Search for place where ai can win
    a, b = findspot(mark)
    # If there is such spot, place at that spot and win
    if a + b != 0:
        board[a][b] = mark
        printBoard()
        endGame(2)
        return

    # Search for place where player can win
    a, b = findspot(player)
    # If there is such spot, block that spot
    if a + b != 0:
        board[a][b] = mark
        return

    # Else, place randomly where there is no mark
    a, b = random.randint(1, 3), random.randint(1, 3)
    while board[a][b] != ' ':
        a, b = random.randint(1, 3), random.randint(1, 3)
    
    board[a][b] = mark


# Get input of a coordinate, put player's mark there
# Player's mark is given
def playerTurn(mark):
    global board

    while True:
        try:
            a, b = map(int, input("x y: ").split())

            while not check(a, b):
                a, b = map(int, input("Enter validate x y: ").split())
            
            break

        except ValueError:
            print("Enter validate ", end='')

    # Put player's mark
    board[a][b] = mark

    # If the player made a line
    if(checkBoard(mark)):
        printBoard()
        # Player wins
        endGame(1)


# Print current board
def printBoard():
    print('\n-------------')
    for i in range(1, 4):
        print("|", end = ' ')
        for j in range(1, 4):
            print(board[i][j], end = ' | ')
        print('\b\b\n-------------')
    print('\n')


# A game where ai goes first, i.e. ai is X
# Player's mark is given
def aiFirst(mark):
    if mark == 'O':
        aimark = 'X'
    else:
        aimark = 'O'

    aiTurn(aimark)
    printBoard()
    cnt = 1

    # Play until the board is full
    while cnt < 9:
        playerTurn(mark)
        printBoard()
        cnt += 1
        aiTurn(aimark)
        printBoard()
        cnt += 1
    
    # If the board is full then it's tie    
    endGame(0)


# A game where player goes first
# Player's mark is given
def playerFirst(mark):
    if mark == 'O':
        aimark = 'X'
    else:
        aimark = 'O'

    playerTurn(mark)
    printBoard()
    cnt = 1

    # Play until the board is full
    while cnt < 9:
        aiTurn(aimark)
        printBoard()
        cnt += 1

        playerTurn(mark)
        printBoard()
        cnt += 1

    # If the board is full then it's tie
    endGame(0)


# End the game
# The result of game is given
# Inputs whether the player would play again
def endGame(flag):
    if flag == 1:
        print("You won!")
    elif flag == 2:
        print("You lost...")
    else:
        print("It's a draw")

    sel = input("Would you like to play again? (Y/N):  ")

    sel = sel.upper()
    li = ['Y', 'N']
    while not (sel in li):
        sel = input("Enter validate choice:  ")
        sel = sel.upper()

    # Play again
    if sel == 'Y':
        # Reset the board
        for i in range(0, 4):
            for j in range(0, 4):
                board[i][j] = ' '
        startGame()

    # Finish the code
    else:
        sys.exit()


# Decide between O and X
def startGame():
    sel = input("Would you like to play O or X?  ")
    sel = sel.upper()

    while sel != 'O' and sel != 'X':
        sel = input("Enter a valid option:  ")
        sel = sel.upper()

    if random.randint(0, 1) == 0:
        playerFirst(sel)
    else:
        aiFirst(sel)


print("Welcome to tic-tac-toe game!\n")
print("---------------------------------\n")
startGame()