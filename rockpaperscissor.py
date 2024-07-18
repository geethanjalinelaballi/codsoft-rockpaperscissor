import random

def get_user_choice():
   
    user_choice = input("Enter 'rock', 'paper', or 'scissors': ").lower()
    while user_choice not in ['rock', 'paper', 'scissors']:
        print("Invalid choice. Please enter 'rock', 'paper', or 'scissors'.")
        user_choice = input("Enter 'rock', 'paper', or 'scissors': ").lower()
    return user_choice

def get_computer_choice():
   
    return random.choice(['rock', 'paper', 'scissors'])

def determine_winner(user_choice, computer_choice):
    
    if user_choice == computer_choice:
        return 'tie', 0
    elif (
        (user_choice == 'rock' and computer_choice == 'scissors') or
        (user_choice == 'scissors' and computer_choice == 'paper') or
        (user_choice == 'paper' and computer_choice == 'rock')
    ):
        return 'User won', 1
    else:
        return 'Computer won', -1

def play_game():
   
    user_score = 0
    computer_score = 0

    while True:
        print(f"Score - Player: {user_score}, Computer: {computer_score}")
        
        user_choice = get_user_choice()
        computer_choice = get_computer_choice()
        
        print(f"You chose: {user_choice}")
        print(f"Computer chose: {computer_choice}")
        
        result, score = determine_winner(user_choice, computer_choice)
        print(result)
        
        if score == 1:
            user_score += 1
        elif score == -1:
            computer_score += 1
        
        play_again = input("Do you want to play again? (yes/no): ").lower()
        if play_again != 'yes':
            break
    
    print(f"Final Score - Player: {user_score}, Computer: {computer_score}")

if __name__ == "__main__":
    play_game()
