import random



def random_play():
    possibleMoves=["Rock","Paper","Scissors"]
    rndMove=random.choice(possibleMoves)
    return rndMove

Player1Score=0
Player2Score=0

print("ROCK PAPER SCISSORS GAME: Best 3 out of 5\n====================================\nPress enter to begin play")
input()
while Player1Score!=3 or Player2Score!=3:
    Player1Move=(random_play())
    Player2Move=(random_play())
    print("Player 1: "+Player1Move)
    print("Player 2: "+Player2Move)
    if Player1Move=="Rock" and Player2Move=="Paper":
        print("Paper beats Rock, Player 2 Wins!")
        Player2Score+=1
        print("Player 1 Score: "+str(Player1Score),", Player 2 Score: "+str(Player2Score))
        
    elif Player1Move=="Rock" and Player2Move=="Rock":
        print("Two Rocks makes a tie, no points awarded!")
        print("Player 1 Score: "+str(Player1Score),", Player 2 Score: "+str(Player2Score))
        
    elif Player1Move=="Rock" and Player2Move=="Scissors":
        print("Rock beats scissors, Player 1 Wins!")
        Player1Score+=1
        print("Player 1 Score: "+str(Player1Score),", Player 2 Score: "+str(Player2Score))
        
    elif Player1Move=="Paper" and Player2Move=="Rock":
        print("Paper beats Rock, Player 1 Wins!")
        Player1Score+=1
        print("Player 1 Score: "+str(Player1Score),", Player 2 Score: "+str(Player2Score))
        
    elif Player1Move=="Paper" and Player2Move=="Paper":
        print("Two Papers makes a tie, no points awarded!")
        print("Player 1 Score: "+str(Player1Score),", Player 2 Score: "+str(Player2Score))
        
    elif Player1Move=="Paper" and Player2Move=="Scissors":
        print("Scissors beats Paper, Player 2 Wins!")
        Player2Score+=1
        print("Player 1 Score: "+str(Player1Score),", Player 2 Score: "+str(Player2Score))
        
    elif Player1Move=="Scissors" and Player2Move=="Paper":
        print("Scissors beats Paper, Player 1 Wins!")
        Player1Score+=1
        print("Player 1 Score: "+str(Player1Score),", Player 2 Score: "+str(Player2Score))
        
    elif Player1Move=="Scissors" and Player2Move=="Scissors":
        print("Two Scissors makes a tie, no points awarded!")
        print("Player 1 Score: "+str(Player1Score),", Player 2 Score: "+str(Player2Score))
        
    else:
        print("Rock beats Scissors, Player 2 Wins!")
        Player2Score+=1
        print("Player 1 Score: "+str(Player1Score),", Player 2 Score: "+str(Player2Score))
        
    if Player1Score==3 or Player2Score==3:
        print(" \n \nGame is over")
        if Player1Score==3:
            print("Player 1 Wins "+str(Player1Score), "to "+str(Player2Score))
            break
        else:
            print("Player 2 Wins "+str(Player2Score), "to "+str(Player1Score))
            break

    input()
