import random

print("WELCOME TO HANGMAN")
print("YOU WILL HAVE 7 TRIES TO GUESS A SECRET WORD")

wordLength = int(input("How many letters do you want the word to be? (5-10 letters): "))


#word list
fiveLetters = [
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

sixLetters = [
    "banana", "castle", "donkey", "eleven", "frozen", "guitar", "hammer", "island", "jacket",
    "laptop", "museum", "noodle", "orange", "pencil", "quartz", "rabbit", "sunset", "turtle",
    "velvet", "window", "yellow", "zigzag", "anchor", "breeze", "carpet", "dancer", "engine", "floral",
    "garden", "hustle", "impact", "jigsaw", "knight", "lizard", "magnet", "nephew", "output", "pebble",
    "quiver", "rocket", "spirit", "temple", "unique", "violet", "wizard", "xyloph", "yonder"
]

sevenLetters = [
    "accused", "battery", "cabbage", "dancing", "explode", "giraffe", "hydrate", "journey", "kitchen", "lettuce",
    "monster", "novelty", "package", "quarter", "rainbow", "silence", "traffic", "undergo", "vaccine", "wealthy",
    "bicycle", "comfort", "diamond", "element", "freedom", "gravity", "harness", "jackpot", "keyword", "liberty",
    "monster", "nothing", "outline", "provoke", "quality", "release", "storage", "trouble", "upgrade", "victory",
    "weather", "yankees", "zephyrs", "breathe", "channel", "default", "explore", "gravity", "husband"
]

eightLetters = [
    "absolute", "birthday", "calendar", "daughter", "elephant", "favorite", "gardener", "hospital", "infinity", "jeweller",
    "keyboard", "language", "mountain", "operator", "platform", "question", "spectrum", "tropical",
    "umbrella", "vacation", "yearbook", "zeppelin"
]

nineLetters = [
    "abundance", "challenge", "delicious", "efficient", "fireplace", "hilarious", "important", "juxtapose",
    "knowledge", "landscape", "necessary", "operation", "portfolio", "quintuple", "symphonic", "tigerlily",
    "underwear", "waterfall", "xylophone", "yellowish", "beautiful", "chocolate", "direction", "education",
    "fireworks", "gentleman", "happiness", "jubilance", "kilometer", "marvelous",
    "quadratic", "radiation", "signature", "telephone", "universal", "warehouse", "xylophagy", "yesterday", "zoologist"
]

tenLetters = [
    "aberration", "blackboard", "decoration", "efficiency", 
    "federation", "generation", "holography", "innovation", "juxtaposed",
    "laboratory", "perfection", "quintuplet", 
    "vocabulary", "watermelon", "zoological", "chronology",
    "indiscreet", "jubilation", "kilometers", "nomination", "xenophobic"
]



#select word
if wordLength == 5:
    secretWord = random.choice(fiveLetters)
elif wordLength == 6:
    secretWord = random.choice(sixLetters)
elif wordLength == 7:
    secretWord = random.choice(sevenLetters)
elif wordLength == 8:
    secretWord = random.choice(eightLetters)
elif wordLength == 9:
    secretWord = random.choice(nineLetters)
elif wordLength == 10:
    secretWord = random.choice(tenLetters)

#secretWord = random.choice()


hangman = ['''
  +---+
  |   |
      |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========''']

board = []

for x in range(0, wordLength):
    board.append("_")


j=0
checkedLetters = ""


for word in range(0, 100):
    #print hangman
    print(board)
    guessWord = ""

    while True:
        guessLetter = input("GUESS LETTER: ").lower()
        
        
        if guessLetter in checkedLetters:
            print("YOU ALREADY GUESSED THIS LETTER. TRY AGAIN")

        else:
            break


    checkedLetters+=guessLetter


    for guessNum in range(0, wordLength):
            #change board

            #compare words

            if guessLetter == secretWord[guessNum]:
                board[guessNum] = guessLetter 



    if guessLetter not in secretWord:
         print(hangman[j])
         j+=1



    for i in range(0, wordLength):
         guessWord+=board[i]      

    if guessWord == secretWord:
        print("YOU WIN! THE WORD WAS: ", secretWord)
        break

    if j==7:
         print("YOU LOST. THE WORD WAS: ", secretWord)
         break