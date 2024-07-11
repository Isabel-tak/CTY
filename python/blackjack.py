import random
import time

print("WELCOME TO BLACKJACK.")
gameRunning = True

userBalance = 1000



#user and computer each get 2 random cards
cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]


def showCards():
    print("COMPUTER CARDS:", computerCards)
    print("\n")
    print("USER CARDS: ", userCards)
    print("\n")


def USum():
    userSum = sum(userCards)
    return(userSum)

def CSum():
    computerSum = sum(computerCards)
    return(computerSum)





while gameRunning == True:

    userCards = []
    computerCards = []

    userCards.append(random.choice(cards))
    userCards.append(random.choice(cards))
    computerCards.append(random.choice(cards))
    computerCards.append(random.choice(cards))

    print("YOU HAVE", userBalance)

    while True:
        bet = int(input("HOW MUCH DO YOU WANT TO BET? "))

        if bet <= 0:
            print("PUT A VALID INPUT. TRY AGAIN!")
        else:
            break

    showCards()

    userBalance -= bet

    while True:
        choice=input("Hit or Stand: ").lower()

        if choice == "hit":
            userCards.append(random.choice(cards))
            showCards()
            print(USum())


            if USum() > 21:
                if 11 in userCards:
                    for i in range(len(userCards)):
                        if userCards[i] == '11':
                            userCards[i] = '1'
                    USum()
                            
                    if USum() > 21:
                        print("YOU LOST!")
                        print("\n")
                        break
                else:
                    print("YOU LOST!")
                    print("\n")
                    break


        elif choice == "stand":
            while CSum() <= 17:
                time.sleep(3)
                computerCards.append(random.choice(cards))
                showCards()
                print("COMPUTER SUM: ", CSum())
                
            if USum() > 21:
                if 11 in userCards:
                    for i in range(len(userCards)):
                        if userCards[i] == '11':
                            userCards[i] = '1'
                    USum()
                            
                    if USum() > 21:
                        print("YOU LOST!")
                        print("\n")
                        break
                else:
                    print("YOU LOST!")
                    print("\n")
                    break

            if CSum() > 21:
                if 11 in computerCards:
                    for i in range(len(computerCards)):
                        if computerCards[i] == '11':
                            computerCards[i] = '1'
                    CSum()

                    if CSum() > 21:
                        print("DEALER LOST!")
                        print("\n")
                        userBalance += 2*bet
                        break
                else:
                    print("DEALER LOST!")
                    print("\n")
                    userBalance += 2*bet
                    break

            elif USum() < CSum():
                print("DEALER WON!")
                print("\n")
                break

            elif USum() > CSum():
                print("YOU WON!")
                print("\n")
                userBalance += 2*bet
                break

            elif USum() == CSum():
                print("THERE WAS A TIE!")
                print("\n")
                userBalance += bet
                break

        else: 
            print("PUT A VALID INPUT. TRY AGAIN!")



    print("------------------------------------------")

    if userBalance <= 0:
        print("YOU ARE BROKE!")
        break
            
        

        




