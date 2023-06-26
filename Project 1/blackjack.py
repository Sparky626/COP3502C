# Geovanny G. Ortiz
# Blackjack P1

from p1_random import P1Random

#Main Game Function
def main():
    rng = P1Random()
    playerHand = 0    
    dealerHand = 0
    gameActive = True
    gameNumber = 0
    playerWins = 0
    dealerWins = 0
    tieGames = 0
    #Loop for overall game
    while gameActive == True:
        hold = False
        playerCard = rng.next_int(13) + 1
        beginningHand = startGame(playerCard, playerHand, gameNumber)
        playerHand = beginningHand
        #Loop for the individual rounds in the game
        while hold == False:
            print("")
            menu()
            print(" ")
            menuChoice = int(input("Choose an option: "))
            print(" ")
            # Takes menu input and randomly generates a card to be used in the drawCard function
            if menuChoice == 1:
                playerCard = rng.next_int(13) + 1
                playerHand = drawCard(playerHand, playerCard)
                # Ends the game if the card drawn causes the hand to exceed 21
                if playerHand > 21:
                    hold = True
                    print("")
                    print("You exceeded 21! You lose.")
                    print("")
                    dealerWins += 1
                    gameNumber += 1
                    playerHand = 0
                # Ends the game if the card drawn causes the hand to equal 21
                elif playerHand == 21:
                    hold = True
                    print("")
                    print("BLACKJACK! You win!")
                    print("")
                    playerWins += 1
                    gameNumber += 1
                    playerHand = 0
            # Takes menu input and randomly generates the dealers hand to be used in the holdHand function
            elif menuChoice == 2:
                dealerHand = rng.next_int(11) + 16
                results = holdHand(playerHand, dealerHand, playerWins, dealerWins, tieGames, gameNumber)
                playerWins = results[0]
                dealerWins = results[1]
                tieGames = results[2]
                gameNumber = results[3]
                playerHand = 0
                dealerHand = 0
                hold = True
            # Takes menu imput and allows for the game stats to be printed
            elif menuChoice == 3:
                printStatistics(gameNumber, playerWins, dealerWins, tieGames)
            # Ends the game runtime/loops
            elif menuChoice == 4:
                gameActive = False
                hold = True
            # Does not allow for invalid input.
            else:
                print("Invalid input!")
                print("Please enter an integer value between 1 and 4.")

#Function begins the game and draws a card to add to the players hand
def startGame(playerCard, playerHand, gameNumber):
    print("START GAME #" + str(gameNumber + 1))
    print(" ")
    if playerCard == 1:
        print("Your card is a ACE!")
    elif playerCard == 11:
        print("Your card is a JACK!")
    elif playerCard == 12:
        print("Your card is a QUEEN!")
    elif playerCard == 13:
        print("Your card is a KING!")
        playerHand -= 3
    else:
        print("Your card is a " + str(playerCard) + "!")
    playerHand = playerHand + playerCard
    print("Your hand is: " + str(playerHand))
    return playerHand

#Function draws a card to add to the players hand and displays its value aswell as the value of the hand
def drawCard(playerHand, playerCard):
    playerHand = playerHand + playerCard
    if playerCard == 1:
        print("Your card is a ACE!")
    elif playerCard == 11:
        print("Your card is a JACK!")
    elif playerCard == 12:
        print("Your card is a QUEEN!")
    elif playerCard == 13:
        print("Your card is a KING!")
        playerHand -= 3
    else:
        print("Your card is a " + str(playerCard) + "!")
    print("Your hand is: " + str(playerHand))
    return playerHand

# Function ends the round and decides the winner of the game
def holdHand(playerHand, dealerHand, playerWins, dealerWins, tieGames, gameNumber):
    print("Dealer's hand: " + str(dealerHand))
    print("Your hand is: " + str(playerHand))
    # Win condition
    if playerHand > dealerHand:
        print("")
        print("You win!")
        playerWins += 1
    elif playerHand < dealerHand:
        if dealerHand > 21:
            print("")
            print("You win!")
            playerWins += 1 
        # Lose condition
        else:
            print("")
            print("Dealer wins!")
            dealerWins += 1
    # Tie condition
    else:
        print("")
        print("It's a tie! No one wins!")
        tieGames += 1
    # Adds to the amount of games played
    gameNumber += 1
    print(" ")
    return playerWins,dealerWins,tieGames,gameNumber   
# Function prints the amount  of games played as well as the wins for both player and dealer and the amount of tie games.
# It also calculates the win percentage
def printStatistics(gameNumber, playerWins, dealerWins, tieGames):
    percentWin = float((playerWins/gameNumber)*100)
    print("Number of Player wins: " + str(playerWins))
    print("Number of Dealer wins: " + str(dealerWins))
    print("Number of tie games: " + str(tieGames))
    print("Total # of games played is: " +  str(gameNumber))
    print("Percentage of Player wins: " + str(percentWin) + "%")

#Displays menu for input
def menu():
    print("1. Get another card")
    print("2. Hold hand")
    print("3. Print statistics")
    print("4. Exit")

main()