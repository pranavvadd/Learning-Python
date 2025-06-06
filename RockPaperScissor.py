#A simple Rock, Paper, Scissors game in Python using basic control structures and data types.
import random

options = ("rock", "paper", "scissors")
player = None
computer = random.choice(options)

while player not in options:
    player = input("Enter rock, paper, or scissors: ").lower()

print(f"Player: {player}")
print(f"Computer: {computer}")

if player == computer:
    print("It's a tie!")
elif (player == "rock" and computer == "scissors") or\
     (player == "paper" and computer == "rock") or \
     (player == "scissors" and computer == "paper"):
    print("Player wins!")
else:
    print("Computer wins!")
# Example usage:
# Enter rock, paper, or scissors: rock
# Player: rock
# Computer: paper
# It's a tie!
# Enter rock, paper, or scissors: paper
# Player: paper
# Computer: scissors
# Player wins!
