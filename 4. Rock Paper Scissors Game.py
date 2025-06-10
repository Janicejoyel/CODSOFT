# Rock, Paper, Scissors Game 

import random

# Possible choices
choices = ['rock', 'paper', 'scissors']

# Scores
user_score = 0
computer_score = 0

def determine_winner(user, computer):
    if user == computer:
        return "Tie"
    elif (user == 'rock' and computer == 'scissors') or \
         (user == 'scissors' and computer == 'paper') or \
         (user == 'paper' and computer == 'rock'):
        return "User"
    else:
        return "Computer"

print("Welcome to Rock, Paper, Scissors Game!")

while True:
    print("\nOptions: rock, paper, scissors")
    user_choice = input("Enter your choice: ").lower()

    if user_choice not in choices:
        print("Invalid choice. Please select rock, paper, or scissors.")
        continue

    computer_choice = random.choice(choices)
    print(f"Computer chose: {computer_choice}")

    result = determine_winner(user_choice, computer_choice)

    if result == "Tie":
        print("It's a tie!")
    elif result == "User":
        print("You win this round!")
        user_score += 1
    else:
        print("Computer wins this round!")
        computer_score += 1

    print(f"Score -> You: {user_score} | Computer: {computer_score}")

    play_again = input("Do you want to play again? (yes/no): ").lower()
    if play_again != 'yes':
        print("Thanks for playing! Final Score:")
        print(f"You: {user_score} | Computer: {computer_score}")
        break
