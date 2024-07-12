import random

print("WELCOME TO BATTLESHIP!")

playerOneSelf = [
    [" ", "0", "1", "2", "3", "4", "5", "6", "7", "8", "9"],
    ["0", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-"],
    ["1", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-"],
    ["2", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-"],
    ["3", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-"],
    ["4", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-"],
    ["5", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-"],
    ["6", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-"],
    ["7", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-"],
    ["8", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-"],
    ["9", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-"]
]

playerOneOpponent = [
    [" ", "0", "1", "2", "3", "4", "5", "6", "7", "8", "9"],
    ["0", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-"],
    ["1", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-"],
    ["2", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-"],
    ["3", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-"],
    ["4", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-"],
    ["5", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-"],
    ["6", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-"],
    ["7", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-"],
    ["8", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-"],
    ["9", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-"]
]

playerTwoSelf = [
    [" ", "0", "1", "2", "3", "4", "5", "6", "7", "8", "9"],
    ["0", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-"],
    ["1", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-"],
    ["2", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-"],
    ["3", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-"],
    ["4", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-"],
    ["5", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-"],
    ["6", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-"],
    ["7", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-"],
    ["8", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-"],
    ["9", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-"]
]

playerTwoOpponent = [
    [" ", "0", "1", "2", "3", "4", "5", "6", "7", "8", "9"],
    ["0", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-"],
    ["1", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-"],
    ["2", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-"],
    ["3", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-"],
    ["4", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-"],
    ["5", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-"],
    ["6", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-"],
    ["7", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-"],
    ["8", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-"],
    ["9", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-"]
]

def printBoard(matrix):
    for i in matrix:
        print(*i)


playerOneSum = 0
playerTwoSum = 0

print("PLAYER 1: CHOOSE YOUR SHIPS!")
print("YOU HAVE FOUR 3-LENGTH SHIPS!")

for x in range(4):
    print("WHERE DO YOU WANT SHIP", x + 1, "?")
    shipLength = int(input("HOW LONG DO YOU WANT THE SHIP TO BE? (2-5): "))
    shipOrientation = input("HORIZONTAL OR VERTICAL? (H OR V) ").lower()
    column = int(input("COLUMN (0-9): "))
    row = int(input("ROW (0-9): "))

    playerOneSum += shipLength

    column_number = int(column) + 1
    row_number = int(row) + 1

    if shipOrientation == "v":
        for s in range(0,shipLength):
            playerOneSelf[row_number+s][column_number] = "X"
    elif shipOrientation == "h":
        for s in range(0,shipLength):
            playerOneSelf[row_number][column_number+s] = "X"
    
    printBoard(playerOneSelf)
    print("\n")

print("\n")
print("\n")
print("\n")
print("\n")
print("\n")


print("PLAYER 2: CHOOSE YOUR SHIPS!")
print("YOU HAVE FOUR 3-LENGTH SHIPS!")

for x in range(4):
    print("WHERE DO YOU WANT SHIP", x + 1, "?")
    shipLength = int(input("HOW LONG DO YOU WANT THE SHIP TO BE? (2-5): "))
    shipOrientation = input("HORIZONTAL OR VERTICAL? (H OR V)").lower()
    column = int(input("COLUMN (0-9): "))
    row = int(input("ROW (0-9): "))

    playerTwoSum += shipLength

    column_number = int(column) + 1
    row_number = int(row) + 1

    if shipOrientation == "v":
        for s in range(0,shipLength):
            playerTwoSelf[row_number+s][column_number] = "X"
    elif shipOrientation == "h":
        for s in range(0,shipLength):
            playerTwoSelf[row_number][column_number+s] = "X"
    
    print("\n")
    printBoard(playerTwoSelf)
    print("\n")

print("\n")
print("\n")
print("\n")
print("\n")
print("\n")

gameRunning = True

while gameRunning == True:
    print("PLAYER 1: GUESS A SPACE!")

    while True:
        playerOneColumn = int(input("COLUMN (0-9): ")) + 1
        playerOneRow = int(input("ROW (0-9): ")) + 1

        if playerTwoSelf[playerOneRow][playerOneColumn] == "X":
            playerOneOpponent[playerOneRow][playerOneColumn] = "X"
            print("YOU HIT A SHIP!")
            print("PLAYER 2 BOARD: ")
            printBoard(playerOneOpponent)
        else:
            print("YOU MISSED!")
            playerOneOpponent[playerOneRow][playerOneColumn] = "*"
            print("PLAYER 2 BOARD: ")
            printBoard(playerOneOpponent)
            break

        #if hit a whole ship
            #say you sunk a ship
        
        if playerOneOpponent.count("X") == playerTwoSum:
            print("PLAYER 1 WON!")
            gameRunning = False

    print("PLAYER 2: GUESS A SPACE!")

    while True:
        playerTwoColumn = int(input("COLUMN (0-9): ")) + 1
        playerTwoRow = int(input("ROW (0-9): ")) + 1

        if playerOneSelf[playerTwoRow][playerTwoColumn] == "X":
            playerTwoOpponent[playerTwoRow][playerTwoColumn] = "X"
            print("YOU HIT A SHIP!")
            print("PLAYER 2 BOARD: ")
            printBoard(playerTwoOpponent)
        else:
            print("YOU MISSED!")
            playerTwoOpponent[playerTwoRow][playerTwoColumn] = "*"
            print("PLAYER 1 BOARD: ")
            printBoard(playerTwoOpponent)
            break

        #if hit a whole ship
            #say you sunk a ship

        if playerTwoOpponent.count("X") == playerOneSum:
            print("PLAYER 2 WON!")
            gameRunning = False