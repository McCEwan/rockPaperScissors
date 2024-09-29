
import random

n = 0

print("================== ROCK PAPER SCISSORS ==================")

print("\nWelcome to Rock Paper Scissors!")

print("\nRules:")

print("Scissors beats paper, paper beats rock, rock beats scissors.")

roundNum = int(input("\nHow many rounds must a player win to win the match? "))

print("Sounds great! Lets play...")

while n < roundNum:
    compChoice = random.randrange(1,4)
    playerChoice = str(input("\nChoose Rock (R), Paper (P), or Scissors (S): "))
    if compChoice == 1:
        
        print("Computer: Rock ")
        
        if playerChoice == "r":
        
            print("Tie!... Try again")
        
        elif playerChoice == "p":
        
            print("You win! Score:")

        elif playerChoice == "s":
        
            print("I win! Score:")

        else:
        
            print("invalid input")
            break
   
    elif compChoice == 2:
       
        print("Computer: Paper ")       
       
        if playerChoice == "r":
        
           print("I win! Score:")

        elif playerChoice == "p":
        
            print("Tie!... Try again")
        
        elif playerChoice == "s":

            print("You win! Score:")

        else:
        
            print("invalid input")
            break
    
    else:

        print("Computer: Scissors ") 

        if playerChoice == "r":
           
            print("You win! Score:")
        
        elif playerChoice == "p":
       
            print("I win! Score:")
       
        elif playerChoice == "s":
        
            print("Tie!... Try again")

        else:
        
            print("invalid input")
            break

    

    
    n = n + 1

