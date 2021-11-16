'''
Created on Oct 21, 2021
@author: BGross23
Discription: plays rock, paper, scissors
'''
import random
user_action = input("enter a choice (rock, paper, scissors): ")
possible_actions = ["rock", "paper", "scissors"]
computer_action = random.choice(possible_actions)
print(f"\nYou chose {user_action}, computer chose {computer_action}.\n")
if user_action == computer_action:
    print(f"both players selected {user_action}. Tie")
elif user_action == "rock":
    if computer_action == "scissors":
        print("You win")
    else:
        print("You lose")
elif user_action == "paper":
    if computer_action == "rock":
        print("You win")
    else:
        print("You lose")
elif user_action == "scissors":
    if computer_action == "paper":
        print("You win")
    else:
        print("You lose")