from colorama import Fore, init

init(autoreset=True)
balance = 1000
history = []

name = input(Fore.LIGHTMAGENTA_EX + "Enter your name :").strip().lower()
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
        print(Fore.GREEN + "Your balance is :", balance)
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
        history.append(f"Deposited: SH {amount}")
        print(Fore.CYAN + "Deposit successful! New balance is :", balance)
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
        history.append(f"Withdrew: SH {withdraw}")
        print(
            Fore.GREEN
            + f"Withdrawal of SH {withdraw} was successfull !New balance is :",
            balance,
        )
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
