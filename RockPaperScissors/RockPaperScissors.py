
import random

pPointTotal = 0
cPointTotal = 0

print("================== ROCK PAPER SCISSORS ==================")

print("\nWelcome to Rock Paper Scissors!")

print("\nRules:")

print("Scissors beats paper, paper beats rock, rock beats scissors.")

roundNum = int(input("\nHow many rounds must a player win to win the match? "))

print("Sounds great! Lets play...")

while pPointTotal < roundNum and cPointTotal < roundNum:
    compChoice = random.randrange(1,4)
    playerChoice = str(input("\nChoose Rock (R), Paper (P), or Scissors (S): "))
    if compChoice == 1:
        
        print("Computer: Rock ")
        
        if playerChoice == "r":
        
            print("Tie!... Try again")
        
        elif playerChoice == "p":
        
           pPointTotal = pPointTotal + 1
           
           print("You win! Score:" ,pPointTotal, ":", cPointTotal)

        elif playerChoice == "s":
        
            cPointTotal = cPointTotal + 1

            print("I win! Score:", pPointTotal, ":" ,cPointTotal)

        else:
        
            print("invalid input")
            break
   
    elif compChoice == 2:
       
        print("Computer: Paper ")       
       
        if playerChoice == "r":
        
           cPointTotal = cPointTotal + 1
           
           print("I win! Score:" , pPointTotal, ":" ,cPointTotal)

        elif playerChoice == "p":
        
            print("Tie!... Try again")
        
        elif playerChoice == "s":

            pPointTotal = pPointTotal + 1
            
            print("You win! Score:" , pPointTotal, ":" ,cPointTotal)

        else:
        
            print("invalid input")
            break
    
    else:

        print("Computer: Scissors ") 

        if playerChoice == "r":
           
            pPointTotal = pPointTotal + 1
            
            print("You win! Score:"  ,pPointTotal, ":"  ,cPointTotal)

        elif playerChoice == "p":
       
            cPointTotal = cPointTotal + 1
            
            print("I win! Score:" , pPointTotal, ":"  ,cPointTotal)
            
        elif playerChoice == "s":
        
            print("Tie!... Try again")

        else:
        
            print("invalid input")
            break



