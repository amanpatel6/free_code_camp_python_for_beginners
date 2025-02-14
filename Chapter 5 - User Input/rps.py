import random


print("Welcome to Rock, Paper, Scissors!")
print("")

print("Please choose rock, paper or scissors")

choices = ["rock", "paper", "scissors"]

playerchoice = input().lower()

while playerchoice not in choices:
    print("Invalid choice! Pleas choose rock, paper or scissors")
    playerchoice = input().lower()

computerchoice = random.choice(choices)

print(computerchoice)

win_conditions = {
    "rock": "scissors",
    "scissors": "paper",
    "paper": "rock"
}

if playerchoice == computerchoice:
    print("It's a draw")
elif win_conditions[playerchoice] == computerchoice:
    print("You win!")
else:
    print("You lose!")


print("Would you like to play again?")

play_again = input("Do you want to play again? (yes/no): ").lower()

