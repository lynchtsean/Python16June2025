def show_menu():
    print("\nWelcome to BMO!\n")
    print("1. Deposit")
    print("2. Withdraw")
    print("3. Check Balance")
    print("4. Exit")


def deposit(balance):
    try:
        amount = float(input("Enter amount to deposit: $"))
        if amount > 0:
            balance += amount
            print("Deposited successfully!")
        else:
            print("Amount must be positive.")
    except ValueError:
        print("Invalid input. Please enter a number.")
    return balance


def main():
    balance = 0.0
    while True:
        show_menu()
        choice = input("Enter your choice (1-4): ")

        if choice == '1':
            balance = deposit(balance)
        elif choice == '2':
            print("Withdraw function not implemented yet.") 
        elif choice == '3':
            print(f"Your current balance is: ${balance:.2f}")
        elif choice == '4':
            print("Thank you for using the BMO bank app. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 4.")

if __name__ == "__main__":
    main()

    balance = 500.0

while True:
    print("\nInvestment Options:")
    print("1. Fixed Deposit - Minimum $100")
    print("2. Stock Market Fund - Minimum $200")
    print("3. Crypto Basket - Minimum $50")
    print("4. Exit")

    choice = input("Choose an option (1-4): ")

    if choice == "1":
        if balance >= 100:
            balance -= 100
            print("You invested in Fixed Deposit. $100 deducted.")
        else:
            print("Not enough balance for Fixed Deposit.")

    elif choice == "2":
        if balance >= 200:
            balance -= 200
            print("You invested in Stock Market Fund. $200 deducted.")
        else:
            print("Not enough balance for Stock Market Fund.")

    elif choice == "3":
        if balance >= 50:
            balance -= 50
            print("You invested in Crypto Basket. $50 deducted.")
        else:
            print("Not enough balance for Crypto Basket.")

    elif choice == "4":
        print("Exiting investment options.")
        break

    else:
        print("Invalid option. Please choose 1-4.")

    print(f"Current balance: ${balance:.2f}")