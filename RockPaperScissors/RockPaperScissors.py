
import random

n = 0

print("================== ROCK PAPER SCISSORS ==================")

print("\nWelcome to Rock Paper Scissors!")

print("\nRules:")

print("Scissors beats paper, paper beats rock, rock beats scissors.")

roundNum = int(input("\nHow many rounds must a player win to win the match? "))

print("Sounds great! Lets play...")

while n < roundNum:
    compChoice = random.randrange(1,3)
    playerChoice = str(input("Choose Rock (R), Paper (P), or Scissors (S): "))
    print(compChoice)
    n = n + 1

