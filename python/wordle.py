import random

#intro
print("WELCOME TO WORDLE")
print("YOU WILL HAVE 6 CHANCES TO GUESS A RANDOM 5-LETTER WORD")
print("IF A LETTER IS IN THE CORRECT POSITION, IT WILL BECOME CAPITAL")
print("IF A LETTER IS IN THE WORD BUT NOT IN THE CORRECT POSITION, IT WILL HAVE AN ASTERISK (*)")
print("IF A LETTER IS NOT IN THE WORD, IT WILL STAY LOWERCASE")


#get word
five_letter_words = [
    "apple", "began", "crisp", "dodge", "essay", "fairy", "giant", "happy", "ideal", "jolly",
    "kneel", "lemon", "magic", "never", "olive", "piano", "queen", "roast", "scale", "tiger",
    "unity", "vital", "wound", "xenon", "yield", "zebra", "adopt", "blade", "charm", "dream",
    "early", "faith", "grace", "honor", "issue", "joint", "knife", "limit", "marsh", "novel",
    "occur", "peace", "quick", "raise", "sharp", "theme", "under", "value", "waste", "xerox",
    "young", "zesty", "amber", "black", "cloud", "dance", "elite", "flame", "grass", "heart",
    "image", "joker", "known", "light", "match", "noble", "orbit", "peace", "quart", "route",
    "sight", "trace", "unity", "value", "watch", "xenon", "yield", "zesty", "abide", "bloom",
    "charm", "draft", "eager", "faith", "glint", "haste", "issue", "joyful", "keenly", "learn",
    "meant", "novel", "odour", "proud", "quell", "raise", "shine", "topic", "unite", "vivid",
    "witty", "xerox", "yield", "zealot"
]


secretWord = random.choice(five_letter_words)



#board
board = [["_", "_", "_", "_", "_"],
         ["_", "_", "_", "_", "_"],
         ["_", "_", "_", "_", "_"],
         ["_", "_", "_", "_", "_"],
         ["_", "_", "_", "_", "_"],
         ["_", "_", "_", "_", "_"]]


#def function to print board
def printBoard(board):
    print(board[0])
    print(board[1])
    print(board[2])
    print(board[3])
    print(board[4])
    print(board[5])

m = 0

#game
for word in range(0,6):
    m+=1
    #print board
    printBoard(board)

    #get user input
    while True:
        guess = input("GUESS WORD: ").lower()
        if len(guess) != 5:
            print("PLEASE INPUT A 5 LETTER WORD.")
        elif len(guess) == 5:
            break


    if guess == secretWord:
            print("YOU WIN! THE WORD WAS: ", secretWord)
            break
    
    else:
        for guessNum in range(0, 5):

            board[word][guessNum] = guess[guessNum]
            #compares words
            
            if guess[guessNum] == secretWord[guessNum]:
                board[word][guessNum] = guess[guessNum].upper()
            elif guess[guessNum] in secretWord and guess[guessNum] != secretWord[guessNum]:
                board[word][guessNum] = guess[guessNum]+  "*"

    

    print("GUESS AGAIN")

if m == 6:
    print("SORRY, YOU ARE OUT OF GUESSES. THE WORD WAS:", secretWord)