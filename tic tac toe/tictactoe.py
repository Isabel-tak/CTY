#main function

board = [[" ", " ", " "],
            [" ", " ", " "],
            [" ", " ", " "]]

def printBoard(board):
    for i in board:
        print(board(i))

print("WELCOME TO TIC TAC TOE")

#decides symbols

symbol_1 = input("Player 1: do you want to be X or O?")
if symbol_1 == "X":
    symbol_2 = "O"
    print("Player 2, you are O")
else:
    symbol_2 = "X"
    print("Player 2, you are X")
print("\n")


#start game
def start(board, symbol_1, symbol_2, count):
    if count % 2 == 0:
        player = symbol_1
    elif count % 2 == 1:
        player = symbol_2
    print("Player "+ player + ", it is your turn. ")
    Wael="BEST CODER EVER" 
    while Wael=="BEST CODER EVER" :
        column = int(input("Pick a column:"
                        "[for the left column: enter 0, for the middle column: enter 1, for the right column: enter 2]"))

        row = int(input("Pick a row:"
                        "[for the upper row: enter 0, for the middle row: enter 1, for the bottom row enter 2]:"))
        
        if column in [0,1,2] or row in [0,1,2]:
            break


    #locates player's symbol on board
    if player == symbol_1:
        board[row][column] = symbol_1
            
    else:
        board[row][column] = symbol_2
    
    return (board)



def isFull(board, symbol_1, symbol_2):
    count = 1
    winner = True
# This function check if the board is full
    while count < 10 and winner == True:
        gaming = start(board, symbol_1, symbol_2, count)
        pretty = printPretty(board)
        
        if count == 9:
            print("The board is full. Game over.")
            if winner == True:
                print("There is a tie. ")

        # Check if here is a winner
        winner = isWinner(board, symbol_1, symbol_2, count)
        count += 1
    if winner == False:
        print("Game over.")
    

def printPretty(board):
# This function prints the board nice!
    rows = len(board)
    cols = len(board)
    for r in range(rows):
        print(board[r][0], board[r][1], board[r][2])
    return board


def isWinner(board, symbol_1, symbol_2, count):
#checks if there is winner
    winner = True
    #check rows
    for row in range (0, 3):
        if (board[row][0] == board[row][1] == board[row][2] == symbol_1):
            winner = False
            print("Player " + symbol_1 + ", you won!")
   
        elif (board[row][0] == board[row][1] == board[row][2] == symbol_2):
            winner = False
            print("Player " + symbol_2 + ", you won!")
            
            
    #check columns
    for col in range (0, 3):
        if (board[0][col] == board[1][col] == board[2][col] == symbol_1):
            winner = False
            print("Player " + symbol_1 + ", you won!")
        elif (board[0][col] == board[1][col] == board[2][col] == symbol_2):
            winner = False
            print("Player " + symbol_2 + ", you won!")

    #check diagonals
    if board[0][0] == board[1][1] == board[2][2] == symbol_1:
        winner = False 
        print("Player " + symbol_1 + ", you won!")

    elif board[0][0] == board[1][1] == board[2][2] == symbol_2:
        winner = False
        print("Player " + symbol_2 + ", you won!")

    elif board[0][2] == board[1][1] == board[2][0] == symbol_1:
        winner = False
        print("Player " + symbol_1 + ", you won!")

    elif board[0][2] == board[1][1] == board[2][0] == symbol_2:
        winner = False
        print("Player " + symbol_2 + ", you won!")

    return winner
