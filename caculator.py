from colorama import Fore, init

init(autoreset=True)

history = []
while True:
    print("Select an operator")
    print("1) Add")
    print("2) Subtract")
    print("3) Multiply")
    print("4) Divide")
    print("5) Exit")
    print("6) History")

    choice = int(input("Enter a choice (1,2,3,4,5,6):"))

    if choice == 5:
        print(Fore.GREEN + "Goodbye :")
        break
    if choice == 6:
        if len(history) == 0:
            print(Fore.RED + "No history available !")
        else:
            print(Fore.GREEN + "Calculation History:")
            for record in history:
                print(record)
        continue
    num1 = int(input("Enter the first number :"))
    num2 = int(input("Enter the second number :"))

    if choice == 1:
        print(Fore.GREEN + "Results = ", num1 + num2)
        history.append(f"{num1} + {num2} = {num1 + num2}")
    elif choice == 2:
        print(Fore.GREEN + "Results = ", num1 - num2)
        history.append(f"{num1} - {num2} = {num1 - num2}")
    elif choice == 3:
        print(Fore.GREEN + "Results =", num1 * num2)
        history.append(f"{num1} * {num2} = {num1 * num2}")
    elif choice == 4:
        if num2 != 0:
            print(Fore.GREEN + "Results =", num1 / num2)
            history.append(f"{num1} / {num2} = {num1 / num2}")
        else:
            print(Fore.RED + "Cannot divide by zero !")
    else:
        print(Fore.RED + "Invalid input !")
    again = input("Do you want to perform another calculation? (yes/no):").lower()
    if again != "yes":
        print(Fore.GREEN + "Goodbye :")
        break
