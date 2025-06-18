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