""" This app asks the user to choose one of either a rock, paper or scissor ,
the computer also chooses and plays with the user, it checks the choice of both the computer and player, 
determines and displays the winner. """


import random

def get_user_choice():
    """Get user choice for Rock, Paper, or Scissors."""
    user_choice = input("Enter Rock, Paper, or Scissors: ").lower()
    while user_choice not in ['rock', 'paper', 'scissors']:
        print("Invalid choice. Please enter Rock, Paper, or Scissors.")
        user_choice = input("Enter Rock, Paper, or Scissors: ").lower()
    return user_choice

def get_computer_choice():
    """Generate a random choice for the computer."""
    return random.choice(['rock', 'paper', 'scissors'])

def determine_winner(user_choice, computer_choice):
    """Determine the winner based on user and computer choices."""
    if user_choice == computer_choice:
        return "It's a tie!"
    elif (
        (user_choice == 'rock' and computer_choice == 'scissors') or
        (user_choice == 'paper' and computer_choice == 'rock') or
        (user_choice == 'scissors' and computer_choice == 'paper')
    ):
        return "You win!"
    else:
        return "Computer wins!"

def reset_game():
    """Reset the game."""
    print("Resetting the game...")

def exit_game():
    """Exit the application."""
    print("Exiting the game. Goodbye!")
    exit()

def play_game():
    """Main function to play the Rock, Paper, Scissors game."""
    while True:
        user_choice = get_user_choice()
        computer_choice = get_computer_choice()

        print(f"You chose {user_choice}.")
        print(f"Computer chose {computer_choice}.")

        result = determine_winner(user_choice, computer_choice)
        print(result)

        play_again = input("Do you want to play again? (yes/no): ").lower()
        if play_again != 'yes':
            break

    reset_game()
    exit_game()

# Run the game by calling the play_game() function
play_game()
