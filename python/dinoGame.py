#intro/rules
print("WELCOME TO THE GAME.")
print("YOU ARE THE & SYMBOL.")
print("USE WASD TO COLLECT COINS ($) AND REACH THE EXIT (*).")
print("THE @ SYMBOLS ARE MOVABLE BLOCKS.")


print("LEVEL 1:")

#board
board = [
    ["#", "#", "#", "#", "#", "#", "#", "#", "#", "#"],
    ["&", " ", " ", "$", "#", " ", " ", " ", "$", "#"],
    ["#", " ", " ", " ", "#", " ", " ", " ", "#", "#"],
    ["#", "#", "@", "#", "#", "@", "@", "@", "#", "#"],
    ["#", " ", " ", " ", " ", " ", " ", "$", "#", "#"],
    ["#", "$", " ", "#", "#", " ", " ", " ", " ", "*"],
    ["#", "#", "#", "#", "#", "#", "#", "#", "#", "#"]
]


def printBoard(board):
    print(board[0])
    print(board[1])
    print(board[2])
    print(board[3])
    print(board[4])
    print(board[5])
    print(board[6])


#x and y for board position
x = 0
y = 1


#coin counter
c = 0

#move counter
m = 0


for i in range(0, 200):
    m += 1
    
    #print board
    printBoard(board)

    #get move
    move = input("INPUT A MOVE (WASD): ").lower()


    if move == "w":
        y -= 1
        if board[y][x] == " ":
            board[y+1][x] = " "
            board[y][x] = "&"

        elif board[y][x] == "$":
            c += 1
            board[y+1][x] = " "
            board[y][x] = "&"

        elif board[y][x] == "#":
            y += 1

        elif board[y][x] == "@":
            if board[y-1][x] == " ":
                board[y][x] = "&"
                board[y+1][x] = " "
                board[y-1][x] = "@"
            else: 
                y += 1


    elif move == "a":
        x -= 1
        if board[y][x] == " ":
            board[y][x+1] = " "
            board[y][x] = "&"

        elif board[y][x] == "$":
            c += 1
            board[y][x+1] = " "
            board[y][x] = "&"

        elif board[y][x] == "#":
            x += 1
        
        elif board[y][x] == "@":
            if board[y][x-1] == " ":
                board[y][x] = "&"
                board[y][x+1] = " "
                board[y][x-1] = "@"
            else:
                x += 1
                

    elif move == "s":
        y += 1
        if board[y][x] == " ":
            board[y-1][x] = " "
            board[y][x] = "&"

        elif board[y][x] == "$":
            c += 1
            board[y-1][x] = " "
            board[y][x] = "&"

        elif board[y][x] == "#":
            y -= 1

        elif board[y][x] == "@":
            if board[y+1][x] == " ":
                board[y][x] = "&"
                board[y-1][x] = " "
                board[y+1][x] = "@"
            else:
                y -= 1

    elif move == "d":
        x += 1
        if board[y][x] == " ":
            board[y][x-1] = " "
            board[y][x] = "&"
        elif board[y][x] == "$":
            c += 1
            board[y][x] = "&"
            board[y][x-1] = " "

        elif board[y][x] == "#":
            x -= 1

        elif board[y][x] == "@":
            if board[y][x+1] == " ":
                board[y][x] = "&"
                board[y][x-1] = " "
                board[y][x+1] = "@"
            else:
                x-=1
            
        elif board[y][x] == "*":
            print("YOU WON!")
            if c == 1:
                print("YOU COLLECTED 1 COIN")
                print("YOU TOOK", m, "MOVES.")
            else:
                print("YOU COLLECTED", c, "/ 4 COINS.")
                print("YOU TOOK", m, "MOVES.")
            break


print("LEVEL 2:")
print("THE _ SYMBOLS ARE PRESSURE PLATES. WHEN PUSHED DOWN, CERTAIN WALLS (%) WILL LIFT.")


board = [
    ["#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#"],
    ["&", " ", " ", " ", " ", "@", " ", " ", "_", "#", " ", " ", " ", " ", "#"],
    ["#", "#", "#", " ", " ", "#", "#", " ", " ", "#", " ", "#", "#", "@", "#"],
    ["#", "_", "#", " ", " ", "#", "$", " ", " ", "%", " ", "#", " ", " ", "#"],
    ["#", " ", "#", " ", " ", "#", "#", "#", "#", "#", "#", "#", " ", " ", "#"],
    ["#", " ", "#", "$", "#", "#", "$", " ", " ", "@", " ", "#", " ", "#", "#"],
    ["#", " ", "#", "#", "#", "$", " ", " ", " ", "#", " ", "#", " ", "#", "#"],
    ["#", " ", " ", " ", " ", "@", " ", "#", "#", "#", " ", "#", " ", "#", "#"],
    ["#", " ", "$", " ", " ", "#", "$", "#", "$", " ", " ", " ", " ", "%", "*"],
    ["#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#"]
]


def printBoard(board):
    print(board[0])
    print(board[1])
    print(board[2])
    print(board[3])
    print(board[4])
    print(board[5])
    print(board[6])
    print(board[7])
    print(board[8])
    print(board[9])

#x and y for board position
x = 0
y = 1


#coin counter
c = 0

#move counter
m = 0


pressurePlate1 = False

for i in range(0, 200):
    m += 1
    
    #print board
    printBoard(board)

    #get move
    move = input("INPUT A MOVE (WASD): ").lower()


    if move == "w":
        y -= 1
        if board[y][x] == " ":
            board[y+1][x] = " "
            board[y][x] = "&"

        elif board[y][x] == "$":
            c += 1
            board[y+1][x] = " "
            board[y][x] = "&"

        elif board[y][x] == "#":
            y += 1

        elif board[y][x] == "@":
            if board[y-1][x] == " ":
                board[y][x] = "&"
                board[y+1][x] = " "
                board[y-1][x] = "@"

            elif board[y-1][x] == board[1][8]:
                board[1][8] = "@"
                board[y][x] = "&"
                board[y+1][x] = " "
                board[3][9] = " "

            elif board[y-1][x] == board[3][1]:
                board[3][1] = "@"
                board[y][x] = "&"
                board[y+1][x] = " "
                board[8][13] = " "

            else: 
                y += 1


    elif move == "a":
        x -= 1
        if board[y][x] == " ":
            board[y][x+1] = " "
            board[y][x] = "&"

        elif board[y][x] == "$":
            c += 1
            board[y][x+1] = " "
            board[y][x] = "&"

        elif board[y][x] == "#":
            x += 1
        
        elif board[y][x] == "@":
            if board[y][x-1] == " ":
                board[y][x] = "&"
                board[y][x+1] = " "
                board[y][x-1] = "@"

            elif board[y][x-1] == board[1][8]:
                board[1][8] = "@"
                board[y][x] = "&"
                board[y][x+1] = " "
                board[3][9] = " "

            elif board[y][x-1] == board[3][1]:
                board[3][1] = "@"
                board[y][x] = "&"
                board[y][x-1] = " "
                board[8][13] = " "

            else:
                x += 1
                

    elif move == "s":
        y += 1
        if board[y][x] == " ":
            board[y-1][x] = " "
            board[y][x] = "&"

        elif board[y][x] == "$":
            c += 1
            board[y-1][x] = " "
            board[y][x] = "&"

        elif board[y][x] == "#":
            y -= 1

        elif board[y][x] == "@":
            if board[y+1][x] == " ":
                board[y][x] = "&"
                board[y-1][x] = " "
                board[y+1][x] = "@"

            elif board[y+1][x] == board[1][8]:
                board[1][8] = "@"
                board[y][x] = "&"
                board[y-1][x] = " "
                board[3][9] = " "

            elif board[y+1][x] == board[3][1]:
                board[3][1] = "@"
                board[y][x] = "&"
                board[y+1][x] = " "
                board[8][13] = " "
                
            else:
                y -= 1

    elif move == "d":
        x += 1
        if board[y][x] == " ":
            board[y][x-1] = " "
            board[y][x] = "&"
        elif board[y][x] == "$":
            c += 1
            board[y][x] = "&"
            board[y][x-1] = " "

        elif board[y][x] == "#":
            x -= 1
        
        elif board[y][x] == "%":
            x -= 1

        elif board[y][x] == "@":
            if board[y][x+1] == " ":
                board[y][x] = "&"
                board[y][x-1] = " "
                board[y][x+1] = "@"

            elif board[y][x+1] == board[1][8]:
                board[1][8] = "@"
                board[y][x] = "&"
                board[y][x-1] = " "
                board[3][9] = " "

            elif board[y][x+1] == board[3][1]:
                board[3][1] = "@"
                board[y][x] = "&"
                board[y][x+1] = " "
                board[8][13] = " "
                    
            else:
                x-=1
            
        elif board[y][x] == "*":
            print("YOU WON!")
            if c == 1:
                print("YOU COLLECTED 1 COIN")
                print("YOU TOOK", m, "MOVES.")
            else:
                print("YOU COLLECTED", c, "/ 7 COINS.")
                print("YOU TOOK", m, "MOVES.")
            break