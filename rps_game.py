import random

user_score = 0
computer_score = 0
tie_score = 0
print("Welcome to Rock, Paper, Scissors!")

options = ["rock", "paper", "scissors"]

while True:
    user_choice = input("Enter rock, paper, scissors (or 'quit' to exit): ").lower()

    if user_choice == "quit":
        print("Thanks for playing! We hope to see you soon 😊😍")
        print(f"Your score :{user_score}, Computer score :{computer_score} and Tie score: {tie_score}")
        break

    if user_choice not in options:
        print("Invalid choice, try again. ")
        continue

    computer_choice = random.choice(options)

    print("Computer choice :", computer_choice)

    if user_choice == computer_choice:
        print("It is a tie! 🤝")
        tie_score += 1

    elif (
        (user_choice == "rock" and computer_choice == "scissors")
        or (user_choice == "scissors" and computer_choice == "paper")
        or (user_choice == "paper" and computer_choice == "rock")
    ):
        print("You win! 😍")
        user_score += 1

    else:
        print("You lose! 😔")
        computer_score += 1

    print(
        f"Score = You : {user_score} | Computer : {computer_score} | ties :{tie_score}\n"
    )
