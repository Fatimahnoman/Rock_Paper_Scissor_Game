#   Project: 04
# "ROCK , PAPER , SCISSOR GAME"

import random

# Game's Instructions
print("0 for Rock, 1 for Paper, 2 for Scissor")

# User's Choice
user_choice = int(input("Enter Your Choice: "))

# Computer's Random Choice
computer_choice = random.randint(0, 2)

# Show Computer's Choice
if computer_choice == 0:
    print("Computer chose: Rock")
elif computer_choice == 1:
    print("Computer chose: Paper")
else:
    print("Computer chose: Scissor")

# Determine the Winner!
if computer_choice == user_choice:
    print("It's a Draw!")  # If same choices, it's a draw

elif user_choice == 0 and computer_choice == 2:
    print("You Win!")  # User wins, Rock beats Scissors
    
elif user_choice == 2 and computer_choice == 1:
    print("You Win!")  # User wins, Scissors beats Paper
    
elif user_choice == 1 and computer_choice == 0:
    print("You Win!")  # User wins, Paper beats Rock

else:
    print("You Lose This Time!")  # If user doesn't win, they lose
