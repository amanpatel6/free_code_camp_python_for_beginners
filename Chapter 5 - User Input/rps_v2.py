import random

while True:

# Welcome message
    print("Hi, let's play Rock, Paper, Scissors!")
    print("")
    print("Choose rock, paper or scissors")

    # Prompt player to pick rock, paper or scissors
    player_choice = input().lower()

    print(f"Player chose {player_choice}")

    # Computer then chooses rock, paper or scissors
    options = ["rock", "paper", "scissors"]

    computer_choice = random.choice(options)

    print(f"Computer chose {computer_choice}")


    # Create rules to determine a winner and then display the winner
    if player_choice == computer_choice:
        print("It's a draw!")
    elif player_choice == "rock" and computer_choice == "scissors":
        print("You win!")
    elif player_choice == "scissors" and computer_choice == "paper":
        print("You win!")
    elif player_choice == "paper" and computer_choice == "rock":
        print("You win!")
    else:
        print("You lose")

    # Ask if the player wants to play again
    play_again = input("Do you want to play again? (yes/no): ").lower()

    if play_again != "yes":
        print("Thanks for playing! Goodbye!")
        break  # Exit the loop and end the game