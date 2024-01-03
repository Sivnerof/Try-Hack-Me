"""Supports a round of rock, paper, scissors between a user and a computer."""
import random

def make_user_choice():
    """Returns the user's choice of rock, paper, or scissors.
    The user enters a choice by input prompt.
    """
    player_choice = ""
    while (player_choice != "rock" and player_choice != "paper" and player_choice != "scissors"):
        player_choice = input("Choose one: rock, paper, scissors? ")
   
    return player_choice

def make_computer_choice():
    """Returns the computer's choice of rock, paper, or scissors.
    The computer chooses randomly, with each choice equally likely.
    """
    random_number = random.randint(0, 2)
    if random_number == 0:
        return "scissors"
    elif random_number == 1:
        return "paper"
    else:
        return "rock"

def wins_matchup(choice, opponent_choice):
    """Returns True if the first player's choice wins over their opponent.
    Choices can be rock, paper, or scissors. Assumes the choices are different.
    """
    if choice == "rock" and opponent_choice == "scissors":
        return True
    elif choice == "paper" and opponent_choice == "rock":
        return True
    elif choice == "scissors" and opponent_choice == "paper":
        return True
    else:
        return False

def format_score(user_score, computer_score):
    """Returns a formatted version of the players's current scores."""
    user = "user (" + str(user_score) + ")"
    computer = "computer (" + str(computer_score) + ")"
    return user + " vs. " + computer

