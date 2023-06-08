import random

valid_actions = ['rock', 'scissors', 'paper']
wins = 0
ties = 0
losses = 0


def get_computer_action(user_action):
    if user_action == "rock":
        return 'scissors'
    elif user_action == "scissors":
        return 'paper'
    elif user_action == "paper":
        return 'rock'
    else:
        return random.choice(valid_actions)


while True:
    user_action = input("Choose your action (Rock, Scissors, Paper): ")
    user_action = user_action.lower()

    if user_action not in valid_actions:
        print("Invalid choice. Please choose Rock, Scissors, or Paper to play.")
        continue

    computer_action = random.choice(valid_actions)
    print(f"\nYou chose {user_action} and the opponent chose {computer_action}")

    if user_action == computer_action:
        print(f"Both players chose {user_action}. It's a tie!")
        ties += 1
    elif user_action == "rock":
        if computer_action == "scissors":
            print("You win!")
            wins += 1
        else:
            print("You lose!")
            losses += 1
    elif user_action == "paper":
        if computer_action == "rock":
            print("You win!")
            wins += 1
        else:
            print("You lose!")
            losses += 1
    elif user_action == "scissors":
        if computer_action == "paper":
            print("You win!")
            wins += 1
        else:
            print("You lose!")
            losses += 1

    play_again = input("Play again? (Y/N): ")
    if play_again.lower() != "y":
        print(f"Wins: {wins}, Ties: {ties}, Losses: {losses}")
        print("Thanks for playing. See you next time!")
        break
    else:
        print(f"Wins: {wins}, Ties: {ties}, Losses: {losses}")
