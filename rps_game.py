import random

print("Welcome to Rock, Paper, Scissors!")

options = ["rock", "paper", "scissors"]

while True:
    user_choice = input("Enter rock, paper, scissors (or 'quit' to exit): ").lower()

    if user_choice == "quit":
        print("Thanks for playing!")
        break

    if user_choice not in options:
        print("Invalid choice, try again. ")
        continue

    computer_choice = random.choice(options)

    print("Computer choice :", computer_choice)

    if user_choice == computer_choice:
        print("It is a tie!")

    elif (
        (user_choice == "rock" and computer_choice == "scissors")
        or (user_choice == "scissors" and computer_choice == "paper")
        or (user_choice == "paper" and computer_choice == "rock")
    ):
        print("You win !")

    else:
        print("You lose !")
