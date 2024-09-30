
import random

print("================== ROCK PAPER SCISSORS ==================")

print("\nWelcome to Rock Paper Scissors!")

print("\nRules:")

print("Scissors beats paper, paper beats rock, rock beats scissors.")

   
def main(): 
    pPointTotal = 0
    
    cPointTotal = 0
    
    mainLoop = True 
    
    roundNum = int(input("\nHow many rounds must a player win to win the match? "))

    while mainLoop == True:

        if roundNum > 1:
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
                            
                                print("Not sure what you mean. Try again...")
                                
                    
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
                            
                                print("Not sure what you mean. Try again...")
                        
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
                            
                                print("Not sure what you mean. Try again...")
                

        if roundNum < 1:

                print("\n================== Please enter a whole number equal to or greater than 1 ==================")
                
                roundNum = int(input("\nHow many rounds must a player win to win the match? "))

                if roundNum > 1:
                    
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
                            
                                print("Not sure what you mean. Try again...")
                                
                    
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
                            
                                print("Not sure what you mean. Try again...")
                        
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
                            
                                print("Not sure what you mean. Try again...")

        if pPointTotal == roundNum:

                contGame = input("\nYou win the match! Do you want to play another match? (y/n): ")
                
                if contGame == "y":

                    print("\nNew game!\n")

                    pPointTotal = 0
    
                    cPointTotal = 0

                else:
                    
                    print("\nThank you for playing!")

                    break
                
        if cPointTotal == roundNum:

                contGame = input("\nYou lost the match! Do you want to play another match? (y/n): ")

                if contGame == "y":

                    print("\nNew game!\n")

                    pPointTotal = 0
    
                    cPointTotal = 0

                else:
                    
                    print("\nThank you for playing!")
                    
                    break

if __name__ == "__main__":
    main()              