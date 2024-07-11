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

def printing(matrix):
    for i in matrix:
        print(*i)

print("PLAYER ONE: CHOOSE YOUR SHIPS!")
print("YOU HAVE FOUR 3-LENGTH SHIPS!")

for x in range(4):
    print("WHERE DO YOU WANT SHIP", x + 1, "?")
    shipLength = int(input("HOW LONG DO YOU WANT THE SHIP TO BE? (2-5): "))
    shipOrientation = input("HORIZONTAL OR VERTICAL? ").lower()
    column = int(input("COLUMN (0-9): "))
    row = int(input("ROW (0-9): "))

    column_number = int(column) + 1
    row_number = int(row) + 1

    if shipOrientation == "vertical":
        for s in range(0,shipLength):
            playerOneSelf[row_number+s][column_number] = "X"
    elif shipOrientation == "horizontal":
        for s in range(0,shipLength):
            playerOneSelf[row_number][column_number+s] = "X"
    
    printing(playerOneSelf)
    print("\n")

print("\n")
print("\n")
print("\n")
print("\n")
print("\n")

print("PLAYER TWO: CHOOSE YOUR SHIPS!")
print("YOU HAVE FOUR 3-LENGTH SHIPS!")

for x in range(4):
    print("WHERE DO YOU WANT SHIP", x + 1, "?")
    shipLength = int(input("HOW LONG DO YOU WANT THE SHIP TO BE? (2-5): "))
    shipOrientation = input("HORIZONTAL OR VERTICAL? ").lower()
    column = int(input("COLUMN (0-9): "))
    row = int(input("ROW (0-9): "))

    column_number = int(column) + 1
    row_number = int(row) + 1

    if shipOrientation == "vertical":
        for s in range(0,shipLength):
            playerOneSelf[row_number+s][column_number] = "X"
    elif shipOrientation == "horizontal":
        for s in range(0,shipLength):
            playerOneSelf[row_number][column_number+s] = "X"
    
    print("\n")
    printing(playerOneSelf)
    print("\n")

print("\n")
print("\n")
print("\n")
print("\n")
print("\n")

