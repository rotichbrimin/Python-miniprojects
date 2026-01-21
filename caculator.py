
while True:
    print("Select an operator")
    print("1) Add")
    print("2) Subtract")
    print("3) Multiply")
    print("4) Divide")
    print("5) Exit")

    choice = int(input("Enter a choice (1,2,3,4,5):"))
    
    if choice == 5:
        print("Goodbye :")
        break
    num1 = int(input("Enter the first number :"))
    num2 = int(input("Enter the second number :"))

    if choice == 1:
        print("Results = ", num1 + num2)
    elif choice == 2:
        print("Results = ", num1 - num2)
    elif choice == 3:
        print("Results =", num1 * num2)
    elif choice == 4:
        if num2 !=0:
            print("Results =", num1/num2)
        else:
            print("Cannot divide by zero !")
    else:
        print("Invalid input !")    