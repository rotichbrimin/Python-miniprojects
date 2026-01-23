import random

secret = random.randint(1, 100)
guess = 0 
guess_number = 0

while guess != secret:
    guess = int(input('Guess a number between 1 and 100  :'))
    guess_number += 1
    
    if guess < secret:
        print("Too low !")
        
    elif guess > secret:
        print("Too high !")
        
    else:
        print("Correct! You won!")
        print(f"The number of guesses are {guess_number}")    