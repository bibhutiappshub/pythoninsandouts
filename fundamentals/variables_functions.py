import random


def get_choices():
    player_choice = input("Enter player choices (rock, paper, scissors :)")
    computer_choice_list = ["rock", "paper", "scissors"]
    computer_choice = random.choice(computer_choice_list)
    choices = {"player": player_choice, "computer": computer_choice}
    return choices


def check_win(player, computer):
    if player == computer:
        print("Player Wins")
    else:
        print("Player Looses")


given_choices = get_choices()
check_win(given_choices.get("player"), given_choices.get("computer"))
