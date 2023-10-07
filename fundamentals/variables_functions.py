import random


def get_choices():
    player_choice = input("Enter player choices (rock, paper, scissors :)")
    computer_choice_list = ["rock", "paper", "scissors"]
    computer_choice = random.choice(computer_choice_list)
    choices = {"player": player_choice, "computer": computer_choice}
    return choices


def check_win(player, computer):
    print(f"You choose {player} and the computer choose {computer}")
    if player == computer:
        print("It's a tie")
    elif player == "rock":
        if computer == "paper":
            return "Paper covers rock. You Loose!!!"
        else:
            return "Rock smashes scissors. You Win!!!"
    elif player == "paper":
        if computer == "rock":
            return "Paper covers rock. You Win!!!"
        else:
            return "Scissors cut paper. You Loose!!!"
    elif player == "scissors":
        if computer == "rock":
            return "Rock smashes Scissors. You Loose!!!"
        else:
            return "Scissors cut papers. You Win!!!"


given_choices = get_choices()
result = check_win(given_choices["player"], given_choices["computer"])
print(result)
