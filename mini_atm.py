from colorama import Fore, init
from datetime import datetime

init(autoreset=True)
balance = 1000
pin = "1234"  # You can choose any 4-digit number
history = []

name = input(Fore.LIGHTMAGENTA_EX + "Enter your name :").strip().title()
attempts = 0
while attempts < 3:
    entered_pin = input(Fore.LIGHTMAGENTA_EX + "Enter your PIN: ")
    if entered_pin == pin:
        print(Fore.GREEN + "PIN accepted. Access granted!")
        break
    else:
        attempts += 1
        print(Fore.RED + f"Incorrect PIN! Attempts left: {3 - attempts}")

if attempts == 3:
    print(Fore.RED + "Too many incorrect attempts. Access denied!")
    exit()  

print(Fore.BLUE + f"Welcome {name} We are glad to have you here !")
while True:
    print(Fore.YELLOW + "\nChoose you next option")
    print(Fore.LIGHTBLUE_EX + "\n---MINI BANKING---")
    print(Fore.CYAN + "1) Check balance :")
    print(Fore.LIGHTYELLOW_EX + "2) Deposit :")
    print(Fore.GREEN + "3) Withdraw :")
    print(Fore.MAGENTA + "4) Transaction History :")
    print(Fore.RED + "5) Exit :")

    try:
        choice = int(input("Choose an option :"))
    except ValueError:
        print(Fore.RED + "Invalid input. Please enter a number 1-5.")
        continue

    if choice == 1:
            print(Fore.GREEN + f"Your balance is: SH {balance}")
            now = datetime.now()
            time_str = now.strftime("%Y-%m-%d %H:%M:%S")
            history.append(f"Checked balance at {time_str} | Balance: SH {balance}")

    elif choice == 2:
        try:
            amount = int(input("Enter an amount to deposit :"))
            if amount <= 0:
                print(Fore.RED + "Enter a positive amount :")
                continue
        except ValueError:
            print(Fore.RED + "Invalid amount.")
            continue
        balance += amount
        now = datetime.now()
        time_str = now.strftime("%Y-%m-%d %H:%M:%S")
        history.append(f"Deposited: SH {amount} at {time_str} | Balance: {balance}")
        print(Fore.GREEN + "Deposit successful! New balance is :", balance)
    elif choice == 3:
        try:
            withdraw = int(input("Enter an amount to withdraw :"))
            if withdraw <= 0:
                print(Fore.RED + "Enter a positive number :")
                continue
            if withdraw > balance:
                print(Fore.RED + "Insufficient balance to withdraw ")
                continue
        except ValueError:
            print(Fore.RED + "Invalid amount.")
            continue
        balance -= withdraw
        now = datetime.now()
        time_str = now.strftime("%Y-%m-%d %H:%M:%S")
        history.append(f"Withdrew: SH {withdraw} at {time_str} | Balance: {balance}")
        print(
            Fore.GREEN
            + f"Withdrawal of SH {withdraw} was successful!")
        print(Fore.GREEN + "New balance is :", balance)
    elif choice == 4:
        print(Fore.MAGENTA + "\n--- TRANSACTION HISTORY ---")
        if len(history) == 0:
            print(Fore.YELLOW + "No transactions yet.")
        else:
            for item in history:
                print(Fore.WHITE + "- " + item)
    elif choice == 5:
        print(Fore.RED + "Exiting :")
        break
    else:
        print(Fore.YELLOW + "Invalid choice. Try again")
        continue
