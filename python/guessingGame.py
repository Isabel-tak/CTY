import random

print("HELLO! WELCOME TO THE GUESSING GAME!")
print("GUESS A NUMBER 1-100 AND THE PROGRAM WILL TELL YOU HIGHER OR LOWER.")

difLevel = input("CHOOSE A DIFFICULTY LEVEL (EASY OR HARD): ").lower()

secretNum = random.randint(1, 100)

if difLevel == "easy":
    guessNum = 10
elif difLevel == "hard":
    guessNum = 5

g = 0

print("YOU WILL GET ", guessNum, "GUESSES.")

for i in range(0, guessNum):
    guess = int(input("Guess a number: "))
    
    if guess > secretNum:
        print("YOUR NUMBER WAS GREATER THAN THE NUMBER.")
        g+=1

    elif guess < secretNum:
        print("YOUR NUMBER WAS LESS THAN THE NUMBER")
        g+=1

    elif guess == secretNum:
        print("YOU GOT THE NUMBER! IT WAS", secretNum)
        break

if g >= guessNum:
    print("YOU LOST! THE NUMBER WAS", secretNum)
