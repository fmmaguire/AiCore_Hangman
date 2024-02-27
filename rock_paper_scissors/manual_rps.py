import random

def get_computer_choice():
    choices = ["rock", "paper", "scissors"]
    computer_choice = random.choice(choices)
    return computer_choice

def get_user_choice():
    user_choice = input("Choose:" )
    return user_choice

def get_winner(computer_choice, user_choice):
    print(computer_choice)
    if computer_choice == user_choice:
        print("It's a tie")
    elif (computer_choice == "rock" and user_choice == "scissors"):
        print("You lost.")
    elif (computer_choice == "paper" and user_choice == "rock"):
        print("You lost.")
    elif (computer_choice == "scissors" and user_choice == "rock"):
        print("You lost.")
    else:
        print("You won!")

def play():
    guc = get_user_choice()
    gcc = get_computer_choice()

    get_winner(gcc, guc)